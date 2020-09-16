from app.hangman.data import Data

class Hangman():

    def __init__(self,word):
        self._word = word
        self.new_string = []
        self.letters_wrong = 0
        self.selected_letters = ''

    def masked_word(self):
        """ 
        Create a mask to the word selected, using as base the length of the word \n
        Example: Word - pera \n
                 Return - __ __ __ __         
         """
        for i in range(0,len(self._word)):
            if self._word[i] == ' ':
                self.new_string.append(' ')
            else:
                self.new_string.append('__ ')

        return self.print_new_word(self.new_string)
    
    def find_letter(self,letter):
        """
        Verify if the letter inputed by the players it's in the word select. \n
        For that he overwrite new_string, and call print_new_word, to remake the word. \n
        Example: List   - ['p','e','r','a']
                 Input  - 'a'
                 Output - '__ __ __ a' 
        """
        for i in range(0,len(self._word)):
            if self._word[i] == letter:
                self.new_string[i] = letter

        if letter not in self._word:
            self.letters_wrong += 1

        self.selected_letters += letter + ', '
        return self.print_new_word(self.new_string)            

    def print_new_word(self,word):
        """
        Take a list of letters/simbols, and rewrites to a string.
        """
        new_word = ''
        for i in word:
            new_word+= i
        return new_word

    def win_condition(self):
        """
        Evaluate if the player attained the conditions to win the game, or lose the game. \n
        Rules - Have find all the letters of the word, and made less than 5 errors.
        """
        if self.letters_wrong < 5:
            if '__ ' in self.new_string:
                return False
            else:
                return True
        else:
            return True

    def errors_icons(self):
        """
        Print a icon for each error the player made
        """
        msg_errors_lifes = ''
        for i in range(0,5):
            if self.letters_wrong <= i:
                msg_errors_lifes += ' ♥ '
            else:
                msg_errors_lifes += ' ☠ '        
        return msg_errors_lifes