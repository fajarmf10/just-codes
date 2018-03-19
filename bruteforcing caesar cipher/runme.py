def tryme(message):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(ALPHABET)):
        translated = ''
        for symbol in message:
            if symbol in ALPHABET:
                number = ALPHABET.find(symbol)
                number = number - key

                if number < 0:
                    number = number + len(ALPHABET)

                translated = translated + ALPHABET[number]

            else:
                translated = translated + symbol
        print('Trying to use key #%s: %s' % (key, translated))

if __name__ == '__main__':
    message = input('Enter your ciphertext here : ')
    tryme(message)