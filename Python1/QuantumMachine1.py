import random
random.seed()

message_length = int(input("How long do you want your message to be? ")) #i.e. 100 bit
bit_number = "01" #only 0 and 1
bases_number = "0123"

alice_bits = list("".join(random.choices(bit_number,k=message_length)))
alice_bases = list("".join(random.choices(bases_number,k=message_length)))
encoded_bits = []

#This encodes the starting bits with the ran. bases, creating a random bit chain
for number in alice_bits:
    if number == number in alice_bases:
        encoded_bits += number 
    else:
        encoded_bits += random.choices(bit_number,k=1)

bob_bases = list("".join(random.choices(bases_number,k=message_length)))
bob_measurement = []

#This measures the bits with bob's ran. bases, creating a new random bit chain
for number in encoded_bits:
    if number == number in bob_bases:
        bob_measurement += number
    else:
        bob_measurement += random.choices(bit_number,k=1)

shared_secret_bases = []
shared_secret_key = []
for number in bob_bases:
    if number == number in alice_bases:
        shared_secret_bases += number

print(shared_secret_bases)

for number in bob_measurement:
    if number == number in alice_bits:
        shared_secret_key += number

print(shared_secret_key)

'''def QuantumCrypt():
    key = shared_secret_key


    message = input("Please input your secret message: ")
    mode = input("Please enter the mode : Encrypt(E) or Decrypt(D). ")
'''