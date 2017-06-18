

class LetterValueMap:
    """Contains a map of all Letters and their respective values, as well as the globally used BLANK constant"""
    BLANK = " "
    # TODO: Because __set__ or __del__ are NOT called when accessing attribute via class, all attempts at making
    # TODO: a const class attribute have fail. Find a way, and write Unit Test!

    def __init__(self, letter_value_dict):
        if not isinstance(letter_value_dict, dict):
            raise TypeError("letter_value_dict must be of type dict")
        for key, value in letter_value_dict.items():
            if not isinstance(key, str) or len(key) is not 1:
                raise TypeError("letter '" + str(key) + "' must be str type and one character long")
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("value must be a numeric value - int, float")
        if self.BLANK not in letter_value_dict:
            raise ValueError("BLANK must be defined in letter_value_dict")
        self._letter_value_dict = letter_value_dict

    def get_letter_value(self, letter):
        return self._letter_value_dict[letter]

    def is_letter_valid(self, letter):
        return True if letter in self._letter_value_dict else False

    def all_letters(self):
        return self._letter_value_dict.keys()

    # TODO: This is to support a dirty copy-construction. Find a more pythonic way to do this.
    def init_params(self):
        return self._letter_value_dict
