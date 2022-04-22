alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

rotors = {
    'I': {
        'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
        # 'inverse': 'UWYGADFPVZBECKMTHXSLRINQOJ',
        'turnover': 'Q' # If rotor steps from Q to R, the next rotor is advanced
    }, 
    'II': {
        'wiring': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
        # 'inverse': 'AJPCZWRLFBDKOTYUQGENHXMIVS',
        'turnover': 'E' # If rotor steps from E to F, the next rotor is advanced
    }, 
    'III': {
        'wiring': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
        # 'inverse': 'TAGBPCSDQEUFVNZHYIXJWLRKOM',
        'turnover': 'V' # 	If rotor steps from V to W, the next rotor is advanced
    }, 
    'IV': {
        'wiring': 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
        # 'inverse': 'HZWVARTNLGUPXQCEJMBSKDYOIF',
        'turnover': 'J' # If rotor steps from J to K, the next rotor is advanced
    }, 
    'V': {
        'wiring': 'VZBRGITYUPSDNHLXAWMJQOFECK',
        # 'inverse': 'QCYLXWENFTZOSMVJUDKGIARPHB',
        'turnover': 'Z' # If rotor steps from Z to A, the next rotor is advanced
    }, 
    'VI': {
        'wiring': 'JPGVOUMFYQBENHZRDKASXLICTW',
        # 'inverse': '',
        'turnover': 'ZM' # 	If rotor steps from Z to A, or from M to N the next rotor is advanced
    }, 
    'VII': {
        'wiring': 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
        # 'inverse': '',
        'turnover': 'ZM' # 	If rotor steps from Z to A, or from M to N the next rotor is advanced
    }, 
    'VIII': {
        'wiring': 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
        # 'inverse': '',
        'turnover': 'ZM' # 	If rotor steps from Z to A, or from M to N the next rotor is advanced
    }
}

reflectors = {
    'UKW-A': 'EJMZALYXVBWFCRQUONTSPIKHGD', 
    'UKW-B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT', 
    'UKW-C': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'
}

class Plugboard():
    def __init__(self, pairs):
        self.pairs = {}

        if pairs != None:
            for pair in pairs:
                self.pairs[pair[0]] = pair[1]
                self.pairs[pair[1]] = pair[0]

class Rotor():
    def __init__(self, rotor_number, starting_position, next_forward = None, next_backward = None):
        self.wiring = rotors[rotor_number]['wiring']
        self.turnover = rotors[rotor_number]['turnover']
        self.starting_position = starting_position
        self.next_forward = next_forward
        self.next_backward = next_backward

        self.forward = {}
        self.backward = {}

        for start, end in zip(alphabet, self.wiring):
            self.forward[start] = end
            self.backward[end] = start

class Reflector():
    def __init__(self, reflector_model):
        self.wiring = reflectors[reflector_model]