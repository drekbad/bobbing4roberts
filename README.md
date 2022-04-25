# bobbing4roberts
Expand [full name] list from short names to their corresponding long names, and visa versa (Chris Smith adds Christopher Smith).

Provided Python script parses user-supplied names list and does the following:
* splits names by space and retrieves a 'first' and 'last' name
* checks each 'first' against provided example "namePairs.txt" file for matches
  - if a match is found for Chris Smith, the line "Chris,Christopher" in namePairs.txt will associate new value "Christopher Smith"
* creates output file with original names and any new names

The "namePairs.txt" file must be CSV formatted (not .csv extension) as "Chris,Christopher" per line.
The script will create a Python dictionary from the namePairs list and will first check the user-supplied names list first names for any match in the dictionary *keys*, with any match providing the associated *value*. Then it will search against all *values* and return the associated *key* (there is probably a more efficient way to do this, but I do not know it).

--- TO DO ---
* Add support for multiple pairings (Bill,Will,William).

* For any "gender-neutral" names such as "Pat" which may be short for "Patricia" or "Patrick," a separate namePairs list will likely be required to appropriately append associated names. This is because Python dictionary keys must be unique, so while the values could contain more than one name, the reverse lookup (matching by a value and returning associated key) would not necessarily work, and even if the value were matched against all other values and a key, you would end up with an input name of "Patricia Smith" having an appended "Patrick Smith" despite knowing it would not be a relevant addition. In the case of 'more is better,' there's no issue. However, the script would need to be modified such that it checked for multiple values for a given key and returned all other items from a key/values association. Currently it is only set up to search against keys and values and return the opposite pairing.

* Build in username formatter which takes the name params (first, middle, last) and creates a list of possible usernames based on each item in the output list.
  - John A. Smith  ::  john, jsmith, jasmith, johns, john.smith
