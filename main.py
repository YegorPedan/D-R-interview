from typing import Optional
import re


class TextOperations:

    def __init__(self, text: str):
        self.text = text
        self.words = re.findall(r'\w+', self.text)

    def get_longest_word(self) -> Optional[str]:
        """Return the longest word in self.text"""

        if self.text is None:
            return ""

        max_length = 0
        max_word = ''
        for word in self.words:
            current_word_length = len(word)
            if current_word_length > max_length:
                max_word = word
                max_length = current_word_length

        return max_word

    def most_common_word(self):
        occured_words = {}

        for word in self.words:
            if word not in occured_words:
                occured_words[word] = 1
            else:
                occured_words[word] += 1

        return max(occured_words, key=occured_words.get)

    def get_amount_of_special_char(self):
        matches = re.findall(r'\W', self.text)
        return len(matches)

    def all_palindrom(self):
        all_palindroms = []
        for word in self.words:
            if word == word[::-1]:
                all_palindroms.append(word)
        return ','.join(all_palindroms)


s = TextOperations("Hallo, world sas")
print(s.get_longest_word())
print(s.most_common_word())
print(s.get_amount_of_special_char())
print(s.all_palindrom())
