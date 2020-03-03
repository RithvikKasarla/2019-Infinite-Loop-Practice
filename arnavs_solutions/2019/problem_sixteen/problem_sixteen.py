def decipher(cipher_hex: str, key_hex: str):
    cipher_converted = int(cipher_hex, 16)
    key_converted = int(key_hex, 16)

    return chr(cipher_converted ^ key_converted)


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        num_keys = int(input())
        cipher_text = input()

        for _ in range(num_keys):
            key_text = input()

            result = ""
            for i in range(0, 128, 2):
                result += decipher(cipher_text[i : i + 2], key_text[i : i + 2])

            print(f"[{result:<64}]")


if __name__ == "__main__":
    main()
