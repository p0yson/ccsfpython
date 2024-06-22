#Assume letters A, E, I, O, and U as the vowels. Write a program that prompts the user to enter a string and displays the number of vowels and consonants in the string.

def vowels_and_consonants(str):
    
    vowel_count = 0
    consonant_count = 0
    vowels = "aeiou"
    
    for i in str:
        if i in vowels:
            vowel_count += 1
        elif i.isalpha():
            consonant_count += 1
    
    return vowel_count, consonant_count


print(vowels_and_consonants("animals"))
