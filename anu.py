'''

    encrypt and decrypt using caesar cipher that i learned when i was in college by using python
    Rachmad Nur Hayat
    12:14 27/02/2022

    there is no copyright, you can do whatever you want with this (if u are student,u better tell your teacher that you didnt make all of these and just modified it a bit lol)

'''


def encrypt(sentence):
    """
    Encrypts a string using the Caesar cipher.
    """
    cipher = ""
    for char in sentence:
        if char.isalpha(): # https://www.w3schools.com/python/ref_string_isalpha.asp (is it alphabet? that's it)
            if char.isupper(): # check if this is upper case character
                cipher += chr((ord(char) + 3 - 65) % 26 + 65)
            else:
                cipher += chr((ord(char) + 3 - 97) % 26 + 97)
        else:
            cipher += char
    return cipher

def decrypt(sentence):
    """
    Decrypts a string using the Caesar cipher.
    """
    plain = ""
    for char in sentence:
        if char.isalpha():
            if char.isupper():
                plain += chr((ord(char) - 3 - 65) % 26 + 65)
            else:
                plain += chr((ord(char) - 3 - 97) % 26 + 97)
        else:
            plain += char
    return plain

def showdialogencrypt():
    input_sentence = input("Enter a sentence to encrypt: ")

    encryptedsentence = encrypt(input_sentence)

    print('Your encrypted sentence is : ' + encryptedsentence)

def showdialogdecrypt():
    input_sentence = input("Enter a sentence to decrypt: ")

    decryptedsentence = decrypt(input_sentence)

    print('Your decrpyted sentence is : ' + decryptedsentence)

def checkinputaction(action):
    if action == 'E':
        showdialogencrypt()
    elif action == 'D':
        showdialogdecrypt()
    else:
        print("Please enter E or D")
        initializationdialog()

def initializationdialog():
    anu = input("Do you want to encrypt or decrypt? (enter E or D): ")
    action = anu
    checkinputaction(action)

initializationdialog()
