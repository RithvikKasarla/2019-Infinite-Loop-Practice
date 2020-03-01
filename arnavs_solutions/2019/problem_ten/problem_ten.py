test_cases = int(input())

for _ in range(test_cases):
    shift = int(input())
    encrypted_text = input()

    if shift % 26 == 0:
        print(encrypted_text)
        continue

    for letter in encrypted_text:
        if letter == " ":
            new_letter = " "
        else:
            # Subtract 96 to get alphabetical position, shift using cipher, add 96 to get ascii code
            new_letter = chr((ord(letter) - 96 - shift) % 26 + 96)
            if new_letter == "`":
                # For some reason z is special
                new_letter = "z"
        print(new_letter, end="")

    print()
