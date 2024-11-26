import os
import sys
import getopt

def load_name_pairs(namePair, additional_namePair=None):
    name_relations = {}
    files_to_load = [namePair]
    if additional_namePair:
        files_to_load.append(additional_namePair)  # Add the additional file to the list if specified
    
    for file in files_to_load:  # Iterate through the default and additional namePairs files if provided
        with open(file, 'r') as pairs:
            for line in pairs:
                names = line.strip().split(',')
                for name in names:
                    clean_name = name.strip().lower()
                    other_names = {n.strip().lower() for n in names if n.strip().lower() != clean_name}
                    if clean_name in name_relations:
                        name_relations[clean_name].update(other_names)
                    else:
                        name_relations[clean_name] = other_names
    return name_relations


def generate_usernames_by_format(first, last, formats):
    formats_mapping = {
        1: f"{first[0].lower()}{last.lower()}",     # jsmith
        2: f"{first.lower()}.{last.lower()}",      # john.smith
        3: f"{first.lower()}{last[0].lower()}",    # johns
        4: f"{first.lower()}",                     # john
        5: f"{last.lower()}",                      # smith
        6: f"{last.lower()}{first[0].lower()}",    # smithj
        7: f"{first[0].lower()}.{last.lower()}"    # j.smith
    }
    selected_formats = [formats_mapping[int(f)] for f in formats.split(',') if int(f) in formats_mapping]
    return set(selected_formats)


def process_names(inputfile, name_relations, selected_formats='1,2,3,4,5,6,7'):
    original_names = set()
    new_names = set()
    uname_list = set()
    with open(inputfile, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            if not line:
                continue
            full_names = [name.strip() for name in line.split(',') if name.strip()]
            for full_name in full_names:
                if ' ' in full_name:  # Ensure there's a space separating first and last names
                    first, last = full_name.split(maxsplit=1)
                    original_names.add(f"{first} {last}")
                    first_low = first.lower()
                    alternates = name_relations.get(first_low, set()) | {first_low}
                    
                    for alt in alternates:
                        alt_cap = alt.capitalize()
                        new_full_name = f"{alt_cap} {last}"
                        if new_full_name not in original_names:
                            new_names.add(new_full_name)
                        uname_variants = generate_usernames_by_format(alt_cap, last, selected_formats)
                        uname_list.update(uname_variants)

    orig_count = len(original_names)
    new_names_count = len(new_names)
    uname_count = len(uname_list)
    return uname_list, orig_count, new_names_count, uname_count


def print_summary(orig_count, new_names_count, uname_count):
    print("\nSummary Metrics\n" + "-"*40)
    print(f"{'Initial Names:':<30}{orig_count:>10}")
    print(f"{'New Names Added:':<30}{new_names_count:>10}")
    print(f"{'Total Usernames:':<30}{uname_count:>10}\n")


def print_help():
    print("\nThis tool generates usernames based on name variations for penetration testing.")
    print('Usage: script.py -i <inputfile> -o <outputfile> [-a <additionalfile> | -s <swapfile>] [-f <format numbers>]')
    print('\nOptions:')
    print('  -h, --help            Show this help message and exit')
    print('  -i, --ifile           Specify the input file name')
    print('  -o, --ofile           Specify the output file name')
    print('  -a, --add             Specify an additional name pairs file to add to the default')
    print('  -s, --swap            Specify a name pairs file to swap with the default')
    print('  -f, --format          Specify username formats to use, separated by commas')

    print('\nUsername Formats:')
    print('  1: jsmith             First initial + Last name')
    print('  2: john.smith         First name + Last name with a dot')
    print('  3: johns              First name + Last initial')
    print('  4: john               First name only')
    print('  5: smith              Last name only')
    print('  6: smithj             Last name + First initial')
    print('  7: j.smith            First initial + dot + Last name')
    
    print('\nExamples:')
    print('  Use default formats: script.py -i test.txt -o out.txt')
    print('  Specify single format: script.py -i test.txt -o out.txt -f 7')
    print('  Specify multiple formats: script.py -i test.txt -o out.txt -f 1,3,7')


def main(argv):
    inputfile = ''
    outputfile = ''
    additional_namePair = None
    swap_namePair = None
    format_option = '1,2,3,4,5,6,7'  # Default to all formats
    
    try:
        opts, args = getopt.getopt(argv, "hi:o:a:s:f:", ["help", "ifile=", "ofile=", "add=", "swap=", "format="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-a", "--add"):
            additional_namePair = arg
        elif opt in ("-s", "--swap"):
            swap_namePair = arg
        elif opt in ("-f", "--format"):
            format_option = arg

    if not inputfile or not outputfile:
        print_help()
        sys.exit()

    # Locate namePairs.txt relative to script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    default_namePair = os.path.join(script_dir, "namePairs.txt")
    if swap_namePair:
        name_relations = load_name_pairs(swap_namePair)
    else:
        name_relations = load_name_pairs(default_namePair, additional_namePair)

    uname_list, orig_count, new_names_count, uname_count = process_names(inputfile, name_relations, format_option)
    print_summary(orig_count, new_names_count, uname_count)

    if uname_list:
        with open(outputfile, 'w') as f:
            for uname in sorted(uname_list):
                f.write(uname + "\n")
        print(f'Usernames written to {outputfile}')
    else:
        print('No usernames generated.')

if __name__ == "__main__":
    main(sys.argv[1:])
