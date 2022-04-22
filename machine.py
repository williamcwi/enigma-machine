from platform import machine
from components import Plugboard, Rotor, Reflector, alphabet
import re

class Machine():
    def __init__(self, pairs = None, rotors = ['I', 'II', 'III'], starting_position = 'AAA', reflector_model = 'UKW-B'):

        self.reflector_models = ['UKW-A', 'UKW-B', 'UKW-C']
        self.rotor_numbers = ['I', 'II', 'III', 'IV', 'V']
        
        for rotor in rotors:
            if rotor not in self.rotor_numbers:
                print("Please select a valid rotor number: 'I', 'II', 'III', 'IV', 'V'")
                return None
        if len(starting_position) != 3:
            print("Please provide the starting position in the format of 'AAA'")
            return None
        if reflector_model not in self.reflector_models:
            print("Please select a valid reflector model: 'UKW-A', 'UKW-B', 'UKW-C'")
            return None
        
        self.rotors = rotors
        self.starting_position = starting_position
        self.reflector_model = reflector_model

        self.plugboard = Plugboard(pairs)

        self.right_rotor = Rotor(self.rotors[2], self.starting_position[2])
        self.middle_rotor = Rotor(self.rotors[1], self.starting_position[1])
        self.left_rotor = Rotor(self.rotors[0], self.starting_position[0])
        self.right_rotor.next_forward = self.middle_rotor
        self.middle_rotor.next_forward = self.left_rotor
        self.left_rotor.next_backward = self.middle_rotor
        self.middle_rotor.next_backward = self.right_rotor

        self.reflector = Reflector(self.reflector_model)

    def set_rotor_order(self, rotors):

        for rotor in rotors:
            if rotor not in self.rotor_numbers:
                print("Please select a valid rotor number: 'I', 'II', 'III', 'IV', 'V'")
                return None

        self.right_rotor = Rotor(rotors[2], self.starting_position[2])
        self.middle_rotor = Rotor(rotors[1], self.starting_position[1])
        self.left_rotor = Rotor(rotors[0], self.starting_position[0])
        self.right_rotor.next_forward = self.middle_rotor
        self.middle_rotor.next_forward = self.left_rotor
        self.left_rotor.next_backward = self.middle_rotor
        self.middle_rotor.next_backward = self.right_rotor

    def set_starting_position(self, starting_position):

        if len(starting_position) != 3:
            print("Please provide the starting position in the format of 'AAA'")
            return None

        self.right_rotor.starting_position = starting_position[2]
        self.middle_rotor.starting_position = starting_position[1]
        self.left_rotor.starting_position = starting_position[0]

        self.right_rotor.position_index = alphabet.index(self.right_rotor.starting_position)
        self.middle_rotor.position_index = alphabet.index(self.middle_rotor.starting_position)
        self.left_rotor.position_index = alphabet.index(self.left_rotor.starting_position)

    def set_reflector_model(self, reflector_model):
        
        if reflector_model not in self.reflector_models:
            print("Please select a valid reflector model: 'UKW-A', 'UKW-B', 'UKW-C'")
            return None

        self.reflector = Reflector(self.reflector_model)
    
    def set_plugboard_pairs(self, pairs):
        self.plugboard = Plugboard(pairs)

    def encode(self, message):
        encoded_message = ''

        message = re.sub('[^a-zA-Z]+', '', message.upper())
        for char in message:
            encoded_message += self.encode_letter(char)

        return encoded_message

    def encode_letter(self, char):
        # plugboard
        if char in self.plugboard.pairs:
            char = self.plugboard.pairs[char]

        # step right rotor

        # rotor right -> middle -> left

        # reflector
        char = self.reflector.wiring[char]

        # rotor back left -> middle -> right

        # plugboard
        if char in self.plugboard.pairs:
            char = self.plugboard.pairs[char]
        
        return char