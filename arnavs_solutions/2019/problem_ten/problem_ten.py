test_cases = int(input())

for _ in range(test_cases):
    shift = int(input())
    encrypted_text = input()

    for letter in encrypted_text:
        if letter == " ":
            new_letter = " "
        else:
            # Subtract 96 to get alphabetical position, shift using cipher, add 97 to get ascii code
            new_letter = chr((ord(letter) - 97 - shift) % 26 + 97)
        print(new_letter, end="")

    print()
