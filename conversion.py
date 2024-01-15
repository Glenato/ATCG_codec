class Conversion:
    
    def __init__(self) -> None:
        self.cipher = {
        'A': '00',
        'C': '01',
        'G': '10',
        'T': '11',
        '00': 'A',
        '01': 'C',
        '10': 'G',
        '11': 'T'
        }

    def String_format(self, sentence):
        '''
        Returns the formatted sentence with the variations needed to avoid repeated patterns.

            Parameters:
                    sentence (String): The String sentence

            Returns:
                    encapsulated_formatted_sentence (String): The sentence with variations and encapsulated with "START" and "STOP"

            Example:
                    sentence = "hello world"
                    returns "STARThelLo wOrld STOP"
        '''
        formatted_sentence = ""
        count = {}
        for char in sentence:
            if char not in count:
                formatted_sentence += char
                count[char] = 1
            elif char == " ":
                options = ["#", "&", "§", "_", "+", "^", " "]
                pick = count[char] % 7 - 1
                char_new = options[pick]
                formatted_sentence += char_new
                count[char] += 1
            elif count[char] % 2 != 0:
                char_up = char.upper()
                formatted_sentence += char_up
                count[char] += 1
            else:
                formatted_sentence += char
                count[char] += 1
        encapsulated_formatted_sentence = "START" + formatted_sentence + "STOP"
        return encapsulated_formatted_sentence

    def String_to_Binary(self, sentence):
        '''
        Returns the Binary sequence of a Stringing.

            Parameters:
                    sentence (String): The String sentence

            Returns:
                    Binary (String): The Binary sequence of the variable sequence

            Example:
                    sentence = "hi"
                    returns "0110100001101001"
        '''
        Binary = ''
        for char in sentence:
            bin_char = format(ord(char), 'b')
            if len(bin_char) < 8:
                bin_char = ("0" * (8-len(bin_char))) + bin_char
            Binary = Binary + bin_char
        return Binary

    def Binary_to_DNA(self, Binary):
        '''
        Returns the DNA sequence of a Binary sequence.

            Parameters:
                    Binary (String): The Binary sequence

            Returns:
                    DNA (String): The DNA sequence of the variable Binary

            Example:
                    Binary = "0110100001101001"
                    returns "CGGACGGC"
        '''
        DNA = ''
        for i in range(0, len(Binary), 2):
            bits = Binary[i:i+2]
            DNA += self.cipher[bits]
        return DNA

    def DNA_to_Binary(self, DNA):
        '''
        Returns the Binary sequence of a DNA sequence.

            Parameters:
                    DNA (String): The DNA sequence

            Returns:
                    Binary (String): The Binary sequence of the variable DNA

            Example:
                    DNA = "CGGACGGC"
                    returns "0110100001101001"
        '''
        Binary = ''
        for base in DNA.upper():
            Binary += self.cipher[base]
        return Binary

    def Binary_to_String(self, Binary):
        '''
        Returns the sentence of a Binary sequence.

            Parameters:
                    Binary (String): The Binary sequence

            Returns:
                    sentence (String): The sentence of the variable Binary

            Example:
                    Binary = "0110100001101001"
                    returns "hi"
        '''
        sentence = ''
        for i in range(0, len(Binary), 8):
            sentence += chr(int(Binary[i:i+8], 2))
        return sentence

    def String_reverse(self, formatted_sentence):
        '''
        Returns the lower-cased sentence of a formatted sentence (e.g a sentence with the variations needed to avoid repeated patterns).

            Parameters:
                    formatted_sentence (String): The formatted sentence

            Returns:
                    reverse (String): The reverse of the variable formatted sentence

            Example:
                    formatted_sentence = "STARTThis IS#a&secrEt§meSsAgE!STOP"
                    returns "this is a secret message!"
        '''
        reversed_sentence = ""
        options = ["#", "&", "§", "_", "+", "^"]
        for char in formatted_sentence:
            if char in options:
                reversed_sentence += " "
            else:
                reversed_sentence += char
        reversed_lower_sentence = reversed_sentence.lower()
        return reversed_lower_sentence[5:-4]

    def String_to_DNA(self, message):
        '''
        Returns the DNA sequence of a message.

            Parameters:
                    message (String): The message

            Returns:
                    DNA (String): The DNA sequence of the variable message

            Example:
                    message = "hi"
                    returns "CCATCCCACAACCCAGCCCACGGACGGCCCATCCCACATTCCAA"
        '''
        formatted_string = self.String_format(message)
        bin = self.String_to_Binary(formatted_string)
        DNA = self.Binary_to_DNA(bin)
        return DNA

    def DNA_to_String(self, DNA):
        '''
        Returns the message contained in a DNA sequence.

            Parameters:
                    DNA (String): The DNA sequence

            Returns:
                    message (String): The message of the variable DNA

            Example:
                    DNA = "CCATCCCACAACCCAGCCCACGGACGGCCCATCCCACATTCCAA"
                    returns "hi"
        '''
        reversed_bin = self.DNA_to_Binary(DNA)
        reversed_formatted_string = self.Binary_to_String(reversed_bin)
        reversed_string = self.String_reverse(reversed_formatted_string)
        return reversed_string
