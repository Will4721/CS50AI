
def main():
    menu()


def menu():
    print("MENU:\n1.enter phrase\n2.Get Phrase")
    choice = input()
    if choice == "1":
        encrypter()
    elif choice == "2":
        print("TODO")
        decrypter()
    else:
        print("choose 1 or 2")
        menu()



def encrypter():
    print("Enter phrase:")
    inp = input()
    print("key:")
    key = int(input())


    encoded_parts = [str(ord(char) * key) for char in inp]
    encoded_string = " ".join(encoded_parts)

    print("Encrypted string:", encoded_string)
    return encoded_string


def decrypter():
    print("Enter number string you were given:")
    inp = input()
    print("Enter key you chose:")
    key = int(input())

    result = ""
    # Split by space to get each character's multiplied number back
    for chunk in inp.split():
        original_ascii = int(chunk) // key
        result += chr(original_ascii)

    print("Decrypted phrase:", result)




if __name__ == "__main__":
    main()
