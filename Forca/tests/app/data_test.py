import unittest
import random

from unittest.mock import Mock,patch
from app.hangman.data import Data

class Data_Test(unittest.TestCase):
    def test_add_word_to_list(self):
        """ test if method add_word_to_list insert the value desired in the list """        
        data = Data()
        data.add_word_to_list('teste')
        self.assertIn('teste',data.word_list)

    def test_list_is_read(self):
        """ test if the function 'take_list' return the values in word_list """
        data = Data()
        list_words = data.take_list()
        self.assertTrue(len(list_words) > 0)

    @patch('app.hangman.data.randint')
    def test_word_sorted_is_the_correct_value(self,mock_rng):
        """ test if the word sorted by the function 'sort_word' is the value in index 2 """
        mock_rng.return_value=2
        data = Data()
        word = data.sort_word()
        self.assertEqual(word,'melancia')

    def test_word_sorted_is_not_void(self):
        """ test if the world returned by the function 'sort_word' is not void (' ') """
        data = Data()
        word = data.sort_word()
        self.assertTrue(word != '')