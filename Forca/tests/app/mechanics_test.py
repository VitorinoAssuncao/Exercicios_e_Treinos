import unittest

from app.hangman.mechanics import Hangman

class Mechanics_Test(unittest.TestCase):

    def test_if_the_word_in_initializer_is_null(self):
        hangman = Hangman('teste')
        self.assertEqual(hangman._word,'teste')

    def test_number_of_erros_is_0_in_initialization(self):
        hangman = Hangman('teste')
        self.assertEqual(hangman.letters_wrong,0)

    def test_if_selected_letters_is_null_in_initialization(self):
        hangman = Hangman('teste')
        self.assertTrue(len(hangman.selected_letters) == 0)

    def test_len_of_new_string_masked(self):
        hangman = Hangman('teste')
        word_masked = hangman.masked_word()
        self.assertTrue(len(word_masked) == (3 * len(hangman._word)))

    def test_if_the_mask_is_correct(self):
        hangman = Hangman('teste')
        word_masked = hangman.masked_word()
        self.assertIn('__ ',word_masked)

    def test_if_the_mask_respect_the_presence_of_space(self):
        hangman = Hangman('teste 1')
        word_masked = hangman.masked_word()
        self.assertIn('  ',word_masked)

    def test_letters_wrong_in_a_error(self):
        hangman = Hangman('teste')
        hangman.masked_word()
        hangman.find_letter('x')
        self.assertTrue(hangman.letters_wrong == 1)

    def test_if_the_letters_is_substitued(self):
        hangman = Hangman('teste')
        hangman.masked_word()
        new_word = hangman.find_letter('t')
        self.assertIn('t',new_word)

    def test_win_condition_string_correct_and_errors_0(self):
        hangman = Hangman('teste')
        hangman.new_string = 'teste'
        self.assertTrue(hangman.win_condition())

    def test_win_condition_string_incomplete_and_errors_5(self):
        hangman = Hangman('teste')
        hangman.masked_word()
        hangman.letters_wrong = 5
        self.assertTrue(hangman.win_condition())

    def test_win_condition_string_incomplete_and_errors_3(self):
        hangman = Hangman('teste')
        hangman.masked_word()
        hangman.letters_wrong = 3
        self.assertFalse(hangman.win_condition())

    def test_icons_3_errors(self):
        hangman = Hangman('teste')
        hangman.masked_word()
        hangman.letters_wrong = 3
        msg=hangman.errors_icons()
        self.assertIn(' ☠ ',msg)