# bobbing4roberts

`bobbing4roberts` charts a course through the digital seas, a trusty companion for those navigating the murky waters of penetration testing. More than a mere tool, it's a savvy ally that expands your arsenal of usernames from known names, uncovering hidden entries that could be the key to unlocking new territories. With `bobbing4roberts`, you're not just guessing names; you're armed with insight to probe the defenses of networks, web applications, and platforms, revealing usernames that lay concealed beneath the surface.

## 🎯 Purpose

At its core, `bobbing4roberts` aims to:
- Augment penetration testing efforts with an expanded arsenal of potential usernames.
- Provide a customizable and intelligent approach to generating usernames, leveraging common naming conventions and variations.

## 🛠 Usage

Embark on your username discovery voyage with:

```bash
python bobbing4roberts.py -i <inputfile> -o <outputfile> [-a <additionalfile> | -s <swapfile>] [-f <format numbers>]
```

### Options at your disposal:

-i, --ifile: Specify the maiden voyage list (input file).\
-o, --ofile: Designate the treasure map (output file) for your harvested usernames.\
-a, --add: Enlist an allied ship (additional name pairs file) alongside the default crew.\
-s, --swap: Commandeer a new vessel (swap the default name pairs file) for the journey.\
-f, --format: Choose your weaponry (username formats), e.g., -f 1,2 for fast and silent takedowns.\

### 🏴‍☠️ Username Formats
jsmith - A swift jab (First initial + Last name)\
john.smith - The classic broadside (First name + Last name with a dot)\
johns - The sneaky cutlass (First name + Last initial)\
john - Lone wolf approach (First name only)\
smith - The blunt force (Last name only)\
smithj - The reverse grip (Last name + First initial)\

### ⚓ Considerations
Tread carefully with names like "Pat," which could belong to "Patrick" or "Patricia." Our crew is savvy enough to handle these with the grace of seasoned pirates, ensuring no potential username walks the plank.\
When charting new territories or adding to the namePairs.txt map, remember to group common aliases and maintain separate lines for variations crossing gender lines.
