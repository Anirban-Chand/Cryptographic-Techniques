class Caeser:
    def __init__(self, text_message, key):
        self.__message = text_message.replace(" ", "").lower()
        self.__key = key

    def encrypt_msg(self):
        if isinstance(self.__key, int):
            self.__key %= 26
            letters = list(self.__message)
            for i, letter in enumerate(letters):
                letters[i] = chr(((ord(letter)-ord('a'))+self.__key)+97)
                
            self.__message = ''.join(letters)
            print(f'Encrypted Message: {self.__message}')  

        else:
            print('PLEASE ENTER A VALID INTEGER KEY!')
            exit(0)



    def decrypt_msg(self):
        if isinstance(self.__key, int):
            self.__key %= 26
            letters = list(self.__message)
            for i, letter in enumerate(letters):
                letters[i] = chr(((ord(letter)-ord('a'))-self.__key)+97)
                
            self.__message = ''.join(letters)
            print(f'Decrypted Message: {self.__message}')

        else:
            print('PLEASE ENTER A VALID INTEGER KEY!')
            exit(0)






if __name__ == '__main__':
    message = input('Enter Mesasge: ')
    key = int(input('Enter integer key value: '))

    c = Caeser(text_message=message, key=key)
    c.encrypt_msg()
    c.decrypt_msg()
