from random import randint
class Data():
    def __init__(self):
        self.word_list = []
        self.add_word_to_list('banana')
        self.add_word_to_list('pera')
        self.add_word_to_list('melancia')
        self.add_word_to_list('kiwi')
        self.add_word_to_list('jaca')
        self.add_word_to_list('fruta do conde')
        self.add_word_to_list('mirtilo')

    def add_word_to_list(self,word):
        """ Add a word to the list of words. \n
        Example add_word_to_list('example')"""
        self.word_list.append(word)

    def take_list(self):
        """ Return the list of words, intern of the class."""
        return self.word_list

    def sort_word(self):
        """ Generate a random integer (it max, the size of list), and use that number to take one word from the list, using this number as index."""
        number = randint(0,len(self.word_list)-1)
        return self.word_list[number]