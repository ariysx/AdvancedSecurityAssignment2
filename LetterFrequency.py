# D21125387 Advanced Security Assignment 2
def letter_frequency(cipher_text):
    cipher_text = cipher_text.upper()
    alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    # create a dictionary with the letters as keys and the values as 0
    letter_count = {x: 0 for x in alphabet}
    # count the number of times each letter appears in the ciphertext
    for c in cipher_text:
        if c in letter_count:
            letter_count[c] += 1

    # order by the most frequent letters
    letter_count = {k: v for k, v in sorted(letter_count.items(), key=lambda item: item[1], reverse=True)}

    # print the results
    print("Letter Frequency Analysis For: " + cipher_text)
    for c in letter_count:
        # to two decimal places
        print(c + ": " + str(round(letter_count[c] / len(cipher_text) * 100, 2)))

    return letter_count


def attemp_decryption(cipher_text):
    english_letter_frequency = {"E": 12.7,
                                "A": 8.2,
                                "T": 9.1,
                                "O": 7.5,
                                "I": 7.0,
                                "N": 6.7,
                                "S": 6.3,
                                "H": 6.1,
                                "R": 6.0,
                                "D": 4.3,
                                "L": 4.0,
                                "C": 2.8,
                                "U": 2.8,
                                "W": 2.4,
                                "M": 2.4,
                                "F": 2.2,
                                "Y": 2.0,
                                "G": 2.0,
                                "P": 1.9,
                                "B": 1.4,
                                "V": 1.0,
                                "K": 0.8,
                                "J": 0.2,
                                "X": 0.2,
                                "Q": 0.1,
                                "Z": 0.1}

    english_letter_frequency = {k: v for k, v in
                                sorted(english_letter_frequency.items(), key=lambda item: item[1], reverse=True)}
    freq = letter_frequency(cipher_text)

    plaintext = ""

    # turn cipher text into array of letters with corresponding index of english letter frequency
    cipher_arr = []
    for c in cipher_text:
        cipher_arr.append(
            [c, list(english_letter_frequency.keys()).index(c), list(freq.keys()).index(c)]
        )

    for c in cipher_arr:
        # therefore we should get the english letter frequency index at frequency index
        print("Letter: " + c[0] + " English Letter Frequency Index: " + str(
            c[1]) + " Cipher Letter Frequency Index: " + str(c[2]) + "\tTransform to: " + list(english_letter_frequency.keys())[c[2]])
        # replace the cipher letter with the english letter
        plaintext += list(english_letter_frequency.keys())[c[2]]

    print("Plaintext: " + plaintext)


def main():
    attemp_decryption(
        "UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ")


if __name__ == "__main__":
    main()
