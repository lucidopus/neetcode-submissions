class Solution:

    encode_map = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }

    decode_map = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'i',
        10: 'j',
        11: 'k',
        12: 'l',
        13: 'm',
        14: 'n',
        15: 'o',
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z'
    }

    def encode_string(self, s: str) -> list:
        encoded_chars = []
        for character in s:
            encoded_chars.append(self.encode_map[character])
        return encoded_chars

    # def decode_array(self, encoded_array: list) -> str:
    #     string = ""
    #     for number in encoded_array:
    #         string += decode_map[number]


    def isAnagram(self, s: str, t: str) -> bool:
        
        # Step 1: Encode the strings
        s_encoded = self.encode_string(s)
        t_encoded = self.encode_string(t)

        # Step 2: Sort te encoded arrays
        s_encoded_and_sorted = sorted(s_encoded)
        t_encoded_and_sorted = sorted(t_encoded)


        return s_encoded_and_sorted == t_encoded_and_sorted
        






