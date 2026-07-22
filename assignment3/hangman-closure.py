#Task 4

def make_hangman(secret_word):

    empty_guesses = []

    def hangman_closure(letter):
        empty_guesses.append(letter)
        result = ""
        for i in secret_word:
            if i in empty_guesses:
                result += i
            else:
                result += "_"

        print(result)
        if result == secret_word:
            return True
        else:
            return False

    return hangman_closure
#game
secret_w = input("what is the secret word?")
hangman_game = make_hangman(secret_w)
letter = input("give me a letter")
while hangman_game(letter) is False:

    letter = input("give me a letter")
