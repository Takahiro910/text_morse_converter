morse_dic = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "_": "..--.-",
    "+": ".-.-.",
    "-": "-....-",
    "*": "-..-",
    "^": "......",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    '"': '.-..-.',
    "'": ".----.",
    "=": "-...-",
    " ": "|",
    "&": ".-...",
    "!": "-.-.--",
    "%": "----- -..-. -----"
}


def text_to_morse(text):
    text = text.lower()
    output = ""
    count = 1
    for char in text:
        output += morse_dic[char]
        if count < len(text):
            output += " "
            count += 1
    return output


def morse_to_text(morse):
    morse = morse.split(" ")
    output_text = ""
    for code in morse:
        char = [k for k, v in morse_dic.items() if v == code][0]
        output_text += char
    return output_text


input_text = input("Input text to translate morse code: ")
morse_code = text_to_morse(input_text)
print(morse_code)
return_text = morse_to_text(morse_code)
print(return_text)