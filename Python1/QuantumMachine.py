import random
import pickle
random.seed()

binary = []
str_split_key = []
binaryList = []
def Replace():
    for code in str_split_key:
        code = code.replace("00000", "0")
        code = code.replace("00001", "1")
        code = code.replace("00010", "2")
        code = code.replace("00011", "3")
        code = code.replace("00100", "4")
        code = code.replace("00101", "5")
        code = code.replace("00110", "6")
        code = code.replace("00111", "7")
        code = code.replace("01000", "8")
        code = code.replace("01001", "9")
        code = code.replace("01010", "10")
        code = code.replace("01011", "11")
        code = code.replace("01100", "12")
        code = code.replace("01101", "13")
        code = code.replace("01110", "14")
        code = code.replace("01111", "15")
        code = code.replace("10000", "16")
        code = code.replace("10001", "17")
        code = code.replace("10010", "18")
        code = code.replace("10011", "19")
        code = code.replace("10100", "20")
        code = code.replace("10101", "21")
        code = code.replace("10110", "22")
        code = code.replace("10111", "23")
        code = code.replace("11000", "24")
        code = code.replace("11001", "25")
        code = code.replace("11010", "26")
        code = code.replace("11011", "27")
        code = code.replace("11100", "28")
        code = code.replace("11101", "29")
        code = code.replace("11110", "30")
        code = code.replace("11111", "31")
        global binary
        global binaryList
        binary.append(code)
        binary = [int(i) for i in binary]
        with open('binary', 'wb') as fp:
            pickle.dump(binary, fp)
        with open('binary', 'rb') as fp:
            binaryList = pickle.load(fp)    
            # print(binaryList)

mode = input("Please enter the mode : Encode(E) or Decode(D). ")
encode = False

if mode.upper() == "E":
    message = input("Please enter the message to be encoded: ")
    message_length = len(message)
    encode = True
elif mode.upper() == "D":
    message = input("Please enter the message to be decoded: ")
    message_length = len(message)
    encode = False
else:
    print("Please enter a correct mode.")
    exit()


binary_length = message_length * 20 #this is for the binary code to work later on
bit_number = "01" #only 0 and 1
bases_number = "0123"

#ALICE
alice_bits = list("".join(random.choices(bit_number,k=binary_length)))
alice_bases = list("".join(random.choices(bases_number,k=binary_length)))
encoded_bits = []
#print(alice_bases)

#This encodes the starting bits with the ran. bases, creating a random bit chain
for number in alice_bits:
    if number == number in alice_bases:
        encoded_bits += number 
    else:
        encoded_bits += random.choices(bit_number,k=1)

#BOB
bob_bases = list("".join(random.choices(bases_number,k=binary_length)))
bob_measurement = []
#print(bob_bases)

#This measures the bits with bob's ran. bases, creating a new random bit chain
for number in encoded_bits:
    if number == number in bob_bases:
        bob_measurement += number
    else:
        bob_measurement += random.choices(bit_number,k=1)

shared_secret_bases = [i for i, j in zip(alice_bases, bob_bases) if i == j]
shared_secret_key = []
for number in shared_secret_bases:
    if number == number in encoded_bits:
        shared_secret_key += number
    else:
        shared_secret_key += random.choices(bit_number,k=1) 

n = 5 #number of items in the split lists
split_key = [shared_secret_key[i:i + n] for i in range(0, len(shared_secret_key), n)] #this splits the list into 5 index lists
str_split_key = ["".join(sub_list) for sub_list in split_key] #this joins the sublists into str type
message = list(message)
Replace()

if encode == True:
    encoding_message = []
    def encodeMachine(s, n):
        return ''.join(chr(ord(char) + n) for char in s)
    for x, y in zip(message, binaryList):
        encoding = encodeMachine(x, y)
        #print(encoding)
        encoding_message.append(encoding)
    encoded_message = ''.join(encoding_message)
    print(encoded_message)
elif encode != True:
    decoding_message = []
    def decodeMachine(s,n):
        return ''.join(chr((ord(char) - 97 - n) % 26 + 97) for char in s)
    for x, y in zip(message, binaryList):
        decoding = decodeMachine(x, y)
        decoding_message.append(decoding)
    decoded_message = ''.join(decoding_message)
    print(decoded_message)
        