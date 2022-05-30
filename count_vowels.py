def count_vowels(txt):
    count = 0
    letter = "aeiouAEIOU"
    for l in letter:
        count += txt.count(l)
    return count

count_vowels("Celebration")