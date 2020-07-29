import string

class Alfabeto:
    alfabeto = list(string.ascii_lowercase)
    @classmethod
    def posLetra(cls, letra):
        i = 1
        for l in cls.alfabeto:
            if letra.lower() == l:
                return i
            i += 1
        return -1
