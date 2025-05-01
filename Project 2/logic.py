from PyQt6.QtWidgets import *
from gui import *
import random

class Logic(QMainWindow, Ui_Hangman):
    count = 0
    guessed_letters = []

    def __init__(self) -> None:
        """
        This method initializes the class and hides the hangman to be revealed later.
        Next it opens a text file and selects a random word from it and displays it in a text box.
        Lastly, the buttons are connected to make them functional.
        """
        super().__init__()
        self.setupUi(self)

        self.head.hide()
        self.body.hide()
        self.left_arm.hide()
        self.right_arm.hide()
        self.left_leg.hide()
        self.right_leg.hide()

        self.easy.clicked.connect(self.easy_level)
        self.medium.clicked.connect(self.medium_level)
        self.hard.clicked.connect(self.hard_level)
        self.submit.clicked.connect(self.submitted)
        self.retry.clicked.connect(self.clear)
        self.retry1.clicked.connect(self.clear)
        self.retry2.clicked.connect(self.clear)

    def submitted(self) -> None:
        """
        This method takes an input from a word box and checks it for correctness in order for this program to work.
        After getting the correct input, it clears the box and checks if it's in the word.
        If the letter is in the word, the letters replace underscores and become visible, turning the corresponding box
        green, and if the letter is not in the word, it turns the box red, shows a body part, and increases count.
        Lastly, if count reaches 6 you lose or if you guess the word you win. You can restart afterword.
        """
        letter = self.letter_box.text().upper()
        passed = False

        if len(letter) < 1:
            self.error.setText('Enter a character')
        elif len(letter) > 1:
            self.error.setText('Only enter one letter')
        elif not letter.isalpha():
            self.error.setText('Enter an alphabetic character')
        elif letter in self.guessed_letters:
            self.error.setText('Cannot guess same letter')
        else:
            self.error.setText('')
            passed = True
        self.letter_box.clear()

        if passed:
            if letter in self.guessed_word:
                for num, char in enumerate(self.guessed_word):
                    if char == letter:
                        self.blank_guess[num] = letter
                label_widget = getattr(self, letter)
                label_widget.setStyleSheet("background-color: rgb(0, 255, 0)")
                self.guess.setText(" ".join(self.blank_guess))

            if letter not in self.guessed_word:
                label_widget = getattr(self, letter)
                label_widget.setStyleSheet("background-color: rgb(255, 0, 0)")
                self.count += 1
                if self.count == 1:
                    self.head.show()
                elif self.count == 2:
                    self.body.show()
                elif self.count == 3:
                    self.left_arm.show()
                elif self.count == 4:
                    self.right_arm.show()
                elif self.count == 5:
                    self.left_leg.show()
                elif self.count == 6:
                    self.right_leg.show()
                    self.loss()

            self.win()

        self.guessed_letters.append(letter)

    def win(self) -> None:
        """
        This method changes to the win screen if all the letters in the word are guessed.
        """
        if '_' not in self.blank_guess:
            self.stackedWidget.setCurrentIndex(2)

    def loss(self) -> None:
        """
        This method changes to the loss screen when you are out of guesses and shows the word.
        """
        self.stackedWidget.setCurrentIndex(1)
        self.guess1.setText(self.guessed_word)

    def clear(self) -> None:
        """
        This method takes a list of all the letters guess and reverts their boxes back to the original color, then it
        clears the list. After, it reopens the input box for entry and resets count. Next, it hides all the body parts
        and clears the input box and the box that displays text. Lastly, it changes to starting page.
        """
        for letter in self.guessed_letters:
            label_widget = getattr(self, letter)
            label_widget.setStyleSheet("background-color: rgb(0, 170, 255)")
        self.letter_box.setDisabled(False)

        self.count = 0
        self.guessed_letters = []

        self.head.hide()
        self.body.hide()
        self.left_arm.hide()
        self.right_arm.hide()
        self.left_leg.hide()
        self.right_leg.hide()

        self.letter_box.clear()
        self.error.setText('')
        self.stackedWidget.setCurrentIndex(3)


    def easy_level(self) -> None:
        """
        This method opens a text file depending on the difficulty and randomly chooses a word. Next, it creates blank_guess
        , which generates the blank spaces and turns the screen to the game page and displays the difficulty.
        """
        with open('easy.txt', 'r') as file:
            content = file.read()
            words = eval(content)
            self.guessed_word = words[random.randint(0, 100)].upper()
            self.blank_guess = ['_' if i.isalpha() else i for i in self.guessed_word]
        self.guess.setText(" ".join(self.blank_guess))
        self.stackedWidget.setCurrentIndex(0)
        self.difficulty.setText('Easy')

    def medium_level(self) -> None:
        """
        This method opens a text file depending on the difficulty and randomly chooses a word. Next, it creates blank_guess
        , which generates the blank spaces and turns the screen to the game page and displays the difficulty.
        """
        with open('medium.txt', 'r') as file:
            content = file.read()
            words = eval(content)
            self.guessed_word = words[random.randint(0, 100)].upper()
            self.blank_guess = ['_' if i.isalpha() else i for i in self.guessed_word]
        self.guess.setText(" ".join(self.blank_guess))
        self.stackedWidget.setCurrentIndex(0)
        self.difficulty.setText('Medium')

    def hard_level(self) -> None:
        """
        This method opens a text file depending on the difficulty and randomly chooses a word. Next, it creates blank_guess
        , which generates the blank spaces and turns the screen to the game page and displays the difficulty.
        """
        with open('hard.txt', 'r') as file:
            content = file.read()
            words = eval(content)
            self.guessed_word = words[random.randint(0, 100)].upper()
            self.blank_guess = ['_' if i.isalpha() else i for i in self.guessed_word]
        self.guess.setText(" ".join(self.blank_guess))
        self.stackedWidget.setCurrentIndex(0)
        self.difficulty.setText('Hard')