def cryptoMachine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    value = keys[-1] + keys[0:-1]

    encryptDict = dict(zip(keys,value))
    decryptDict = dict(zip(value,keys))
   

    message = input("Please enter your secret message: ")
    mode = input("Please enter the mode : Encode(E) OR Decode(D). ")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter] for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter] for letter in message.lower()])
    else: 
        print("Please enter a correct choice")

    return newMessage

print(cryptoMachine())


binary_code = {
    1 : ["0", "0", "0", "0", "1"],
    2 : ["0", "0", "0", "1", "0"],
    3 : ["0", "0", "0", "1", "1"],
    4 : ["0", "0", "1", "0", "0"],
    5 : ["0", "0", "1", "0", "1"],
    6 : ["0", "0", "1", "1", "0"],
    7 : ["0", "0", "1", "1", "1"],
    8 : ["0", "1", "0", "0", "0"],
    9 : ["0", "1", "0", "0", "1"],
    10 : ["0", "1", "0", "1", "0"],
    11 : ["0", "1", "0", "1", "1"],
    12 : ["0", "1", "1", "0", "0"],
    13 : ["0", "1", "1", "0", "1"],
    14 : ["0", "1", "1", "1", "0"],
    15 : ["0", "1", "1", "1", "1"],
    16 : ["1", "0", "0", "0", "0"],
    17 : ["1", "0", "0", "0", "1"],
    18 : ["1", "0", "0", "1", "0"],
    19 : ["1", "0", "0", "1", "1"],
    20 : ["1", "0", "1", "0", "0"],
    21 : ["1", "0", "1", "0", "1"],
    22 : ["1", "0", "1", "1", "0"],
    23 : ["1", "0", "1", "1", "1"],
    24 : ["1", "1", "0", "0", "0"],
    25 : ["1", "1", "0", "0", "1"],
    26 : ["1", "1", "0", "1", "0"],
    27 : ["1", "1", "0", "1", "1"],
    28 : ["1", "1", "1", "0", "0"],
    29 : ["1", "1", "1", "0", "1"],
    30 : ["1", "1", "1", "1", "0"],
    31 : ["1", "1", "1", "1", "1"]
}


def convert_to_binary(code):
    code = code.replace("00001", 1)
    code = code.replace("00010", 2)
    code = code.replace("00011", 3)
    code = code.replace("00100", 4)
    code = code.replace("00101", 5)
    code = code.replace("00110", 6)
    code = code.replace("00111", 7)
    code = code.replace("01000", 8)
    code = code.replace("01001", 9)
    code = code.replace("01010", 10)
    code = code.replace("01011", 11)
    code = code.replace("01100", 12)
    code = code.replace("01101", 13)
    code = code.replace("01110", 14)
    code = code.replace("01111", 15)
    code = code.replace("10000", 16)
    code = code.replace("10001", 17)
    code = code.replace("10010", 18)
    code = code.replace("10011", 19)
    code = code.replace("10100", 20)
    code = code.replace("10101", 21)
    code = code.replace("10110", 22)
    code = code.replace("10111", 23)
    code = code.replace("11000", 24)
    code = code.replace("11001", 25)
    code = code.replace("11010", 26)
    code = code.replace("11011", 27)
    code = code.replace("11100", 28)
    code = code.replace("11101", 29)
    code = code.replace("11110", 30)
    code = code.replace("11111", 31)

    return code

 ''''''