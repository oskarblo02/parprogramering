def rem_vowel(string):
    vowels = ('a', 'e', 'o', 'å', 'i', 'y', 'ä', 'ö', 'u')
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "")
    print(string)

string = "hejsan grabbar"
rem_vowel(string)