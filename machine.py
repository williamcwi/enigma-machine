from components import Plugboard, Rotor, Reflector

class Machine():
    def __init__(self, pairs = None, rotors = ['I', 'II', 'III'], starting_position = 'AAA', reflector_model = 'UKW-B'):

        reflector_models = ['UKW-A', 'UKW-B', 'UKW-C']
        rotor_numbers = ['I', 'II', 'III', 'IV', 'V']
        
        for rotor in rotors:
            if rotor not in rotor_numbers:
                print("Please select a valid rotor number: 'I', 'II', 'III', 'IV', 'V'")
                return None
        if len(starting_position) != 3:
            print("Please provide the starting position in the format of 'AAA'")
            return None
        if reflector_model not in reflector_models:
            print("Please select a valid reflector model: 'UKW-A', 'UKW-B', 'UKW-C'")
            return None
        
        self.pairs = pairs
        self.rotors = rotors
        self.starting_position = starting_position
        self.reflector_model = reflector_model

        self.plugboard = Plugboard(self.pairs)

        self.right_rotor = Rotor(rotors[0], starting_position[0])
        self.middle_rotor = Rotor(rotors[1], starting_position[1])
        self.left_rotor = Rotor(rotors[2], starting_position[2])
        self.right_rotor.next_forward = self.middle_rotor
        self.middle_rotor.next_forward = self.left_rotor
        self.left_rotor.next_backward = self.middle_rotor
        self.middle_rotor.next_backward = self.right_rotor

        self.reflector = Reflector(self.reflector_model)