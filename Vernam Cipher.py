import random
import string

mat = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25,
}


class Vernam:
    def __init__(self, text_message, key_value):
        self.__message = text_message
        self.__key = key_value

    def encrypt_msg(self):
        msg_letters = list(self.__message)
        key_letters = list(self.__key)
        cipher_letters = []

        for i, char in enumerate(self.__message):
            msg_letters[i] = mat[char]
        
        for i, char in enumerate(self.__key):
            key_letters[i] = mat[char]
            cipher_letters.append((msg_letters[i]+key_letters[i])%26)
        
        for i in range(len(cipher_letters)):
            cipher_letters[i] = list(mat.keys())[list(mat.values()).index(cipher_letters[i])]
            

        self.__message = ''.join(cipher_letters)
        return  self.__message

    
    def decrypt_msg(self):
        cipher_letters = list(self.__message)
        key_letters = list(self.__key)
        real_msg = []

        for i, char in enumerate(cipher_letters):
            cipher_letters[i] = mat[char]

        for i, char in enumerate(key_letters):
            key_letters[i] = mat[char]
            real_msg.append(cipher_letters[i]-key_letters[i]    if cipher_letters[i]-key_letters[i]>=0 
                                                                else cipher_letters[i]-key_letters[i]+26)

        for i in range(len(key_letters)):
            real_msg[i] = list(mat.keys())[(list(mat.values())).index(real_msg[i])]

        self.__message = ''.join(real_msg)
        return  self.__message




if __name__ == '__main__':
    message = input('Enter Your Message: ')
    message = ''.join(e for e in message if e.isalnum()).lower()
    # generation of key randomly
    key = ''.join(random.choices(string.ascii_lowercase, k=len(message)))

    v = Vernam(text_message=message, key_value=key)
    enmsg = v.encrypt_msg()
    print('Encrypted Message: ', enmsg)
    print('Decrypted Message: ' + v.decrypt_msg())
    