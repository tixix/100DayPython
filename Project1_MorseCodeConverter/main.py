from morse_code_dict import *


plain_text = input("Insert the phrase you want to translate into morde code: \n")
morse_code = ""
for word in plain_text.split(" "):
    word_in_morse_code = ""
    for letter in word.upper():
        if letter in MORSE_CODE_DICT:
            word_in_morse_code += MORSE_CODE_DICT[letter]
        else:
            word_in_morse_code = letter
            print(f'The letter {letter} is not available as morse code.')
    morse_code += word_in_morse_code
print(morse_code)


