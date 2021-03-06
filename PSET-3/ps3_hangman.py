def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i = 0
    for char in lettersGuessed:
        if char in secretWord:
            i += 1
    if i < len(secretWord):
        return False
    else:
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    for char in secretWord:
        if char in lettersGuessed:
            ans = ans + str(char)
        else:
            ans = ans + ' _ '
    return ans

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    az = string.ascii_lowercase
    for char in range(0, len(lettersGuessed)):
        az = az.replace(lettersGuessed[char], '')
    return az

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", str(len(secretWord)), "letters long."
    print "-------------"

    mistakesMade = 0
    lettersGuessed = []

    while mistakesMade < 8:
        print "You have", str(8-mistakesMade), "guesses left."
        print "Available letters:", str(getAvailableLetters(lettersGuessed))

        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()

        if guess in getAvailableLetters(lettersGuessed):
            lettersGuessed.append(guess)       
            if guess in getGuessedWord(secretWord, lettersGuessed):
                print "Good guess:", str(getGuessedWord(secretWord, lettersGuessed))
            else:
                mistakesMade += 1
                print "Oops! That letter is not in my word:", str(getGuessedWord(secretWord, lettersGuessed))
        else:
            print "Oops! You've already guessed that letter:", str(getGuessedWord(secretWord, lettersGuessed))

        print "------------"

        if isWordGuessed(secretWord, lettersGuessed) == True:
            print "Congratulations, you won!"
            break
        if mistakesMade == 8:
            print "Sorry, you ran out of guesses. The word was", str(secretWord), "."
