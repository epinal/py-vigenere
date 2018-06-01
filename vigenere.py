from itertools import cycle
import string

EMPTY_STR = ''
SPACE = ' '


class VigenereCypher:
    def __init__(self, alphabet: str = string.ascii_uppercase):
        self._alphabet = alphabet
        self._alphabet_len = len(alphabet)

    def encrypt(self, key_word: str, text: str) -> str:
        key_iter = cycle(key_word)
        cipher = EMPTY_STR
        for letter in text:
            letter_pos = self._alphabet.find(letter.upper())
            key_letter_pos = self._alphabet.find(next(key_iter).upper())
            cipher += self._alphabet[(letter_pos + key_letter_pos) % self._alphabet_len] if letter != SPACE else letter

        return cipher

    def decrypt(self, key_word: str, cypher_text: str) -> str:
        key_iter = cycle(key_word)
        plain_text = EMPTY_STR
        for letter in cypher_text:
            letter_pos = self._alphabet.find(letter.upper())
            key_letter_pos = self._alphabet.find(next(key_iter).upper())
            plain_text += self._alphabet[
                (letter_pos - key_letter_pos) % self._alphabet_len] if letter != SPACE else letter

        return plain_text
