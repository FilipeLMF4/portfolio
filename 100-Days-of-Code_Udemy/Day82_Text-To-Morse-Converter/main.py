MORSE_DICT = {"A": ".-", "B": "-...", "C": "-.-.",
              "D": "-..", "E": ".", "F": "..-.",
              "G": "--.", "H": "....", "I": "..",
              "J": ".---", "K": "-.-", "L": ".-..",
              "M": "--", "N": "-.", "O": "---",
              "P": ".--.", "Q": "--.-", "R": ".-.",
              "S": "...", "T": "-", "U": "..-",
              "V": "...-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--..", "0": "-----",
              "1": ".----", "2": "..---", "3": "...--",
              "4": "....-", "5": ".....", "6": "-....",
              "7": "--...", "8": "---..", "9": "----.",
              " ": "/"
              }

while True:
    text_input = input("Please type the message to convert (empty string to exit): \n").upper()
    converted_string = ""

    if text_input == "":
        break

    error = False
    for let in text_input:
        if let not in MORSE_DICT:
            print(f"{let} is not a valid character. Please use only the 26 basic latin letters and numbers.\n")
            error = True
            break

        converted_string += MORSE_DICT[let] + " "

    if not error:
        print(f"Converted Message: {converted_string.rstrip()}\n")
