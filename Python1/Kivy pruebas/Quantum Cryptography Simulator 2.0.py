import pickle
import pyperclip
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import random
random.seed()

encoded = False
binary = []
encoded_message = ""
decoded_message = ""
decoding_message = []
str_split_key = []
binaryList = []
message = ""


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


def BobAndAlice():
    global message
    message_length = len(message)
    binary_length = message_length * 20
    bit_number = '01'
    bases_number = '0123'
    # ALICE
    alice_bits = list("".join(random.choices(bit_number, k=binary_length)))
    alice_bases = list("".join(random.choices(bases_number, k=binary_length)))
    encoded_bits = []
    for number in alice_bits:
        if number == number in alice_bases:
            encoded_bits += number
        else:
            encoded_bits += random.choices(bit_number, k=1)
    # BOB
    bob_bases = list("".join(random.choices(bases_number, k=binary_length)))
    bob_measurement = []
    for number in encoded_bits:
        if number == number in bob_bases:
            bob_measurement += number
        else:
            bob_measurement += random.choices(bit_number, k=1)
    shared_secret_bases = [i for i, j in zip(alice_bases, bob_bases) if i == j]
    shared_secret_key = []
    for number in shared_secret_bases:
        if number == number in encoded_bits:
            shared_secret_key += number
        else:
            shared_secret_key += random.choices(bit_number, k=1)
    n = 5  # number of items in the split lists
    # this splits the list into 5 index lists
    split_key = [shared_secret_key[i:i + n]
                 for i in range(0, len(shared_secret_key), n)]
    global str_split_key
    # this joins the sublists into str type
    str_split_key = ["".join(sub_list) for sub_list in split_key]
    message = list(message)
    Replace()


def encodeMessage(self):
    BobAndAlice()
    encoding_message = []

    def encodeMachine(s, n):
        return ''.join(chr(ord(char) + n) for char in s)
    for x, y in zip(message, binaryList):
        global encoded_message
        encoding = encodeMachine(x, y)
        encoding_message.append(encoding)
        global encoded
        encoded = True
    encoded_message = ''.join(encoding_message)


def decodeMessage(self):
    global binary
    global decoded_message
    global message
    if encoded != True:
        BobAndAlice()

        def decodeMachine(s, n):
            return ''.join(chr(ord(char) - n) for char in s)
        for x, y in zip(message, binaryList):
            decoding = decodeMachine(x, y)
            decoding_message.append(decoding)
        decoded_message = ''.join(decoding_message)
    elif encoded == True:
        message = list(message)

        def decode_encodedMessage(s, n):
            return ''.join(chr(ord(char) - n) for char in s)
        for x, y in zip(message, binaryList):
            decoding = decode_encodedMessage(x, y)
            decoding_message.append(decoding)
        decoded_message = ''.join(decoding_message)


class Languages(Screen):
    pass


class MainWindow(Screen):
    pass


class PantallaPrincipalEsp(Screen):
    pass


class PantallaPrincipalCat(Screen):
    pass


class EncodeWindow(Screen):
    def EncodeEn(self):
        global message
        message = self.ids.emessage.text
        encodeMessage(message)
        # self.ids.elabel.text = "Your cyphered message is:"
        self.ids.emessage.text = encoded_message
    
    def Copy(self):
        pyperclip.copy(encoded_message)


class DecodeWindow(Screen):
    def DecodeEn(self):
        global message
        message = self.ids.dmessage.text
        decodeMessage(message)
        self.ids.dlabel.text = "Your dechypered message is:"
        self.ids.dmessage.text = decoded_message


class Encodificador(Screen):
    def EncodeEs(self):
        global message
        message = self.ids.emessage.text
        encodeMessage(message)
        self.ids.elabel.text = "Tu mensaje cifrado es:"
        self.ids.emessage.text = encoded_message

    def Copy(self):
        pyperclip.copy(encoded_message)

class Decodificador(Screen):
    def DecodeEs(self):
        global message
        message = self.ids.dmessage.text
        decodeMessage(message)
        self.ids.dlabel.text = "Tu mensaje descifrado es:"
        self.ids.dmessage.text = decoded_message


class EncodificadorCat(Screen):
    def EncodeCa(self):
        global message
        message = self.ids.emessage.text
        encodeMessage(message)
        self.ids.elabel.text = "El teu missatge xifrat és:"
        self.ids.emessage.text = encoded_message
    
    def Copy(self):
        pyperclip.copy(encoded_message)


class DecodificadorCat(Screen):
    def DecodeCa(self):
        global message
        message = self.ids.dmessage.text
        decodeMessage(message)
        self.ids.dlabel.text = "El teu missatge desxifrat és:"
        self.ids.dmessage.text = decoded_message


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('quantumcryptographysimulator.kv')


class QuantumCryptographySimulator(App):
    def build(self):
        Window.clearcolor = (.84, .88, .86, 1)
        return kv


if __name__ == "__main__":
    QuantumCryptographySimulator().run()
