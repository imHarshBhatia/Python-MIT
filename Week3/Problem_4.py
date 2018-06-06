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
    # FILL IN YOUR CODE HERE...
    lettersGuessed,mistakesMade,availableLetters,guessCount = [],[],string.ascii_lowercase,8
    wordLen = len(secretWord)
    print("Welcome to the game, Hangman!\nI am thinking of a word that is " + str(wordLen)+ " letters long.\n-----------")
    availableLetters = getAvailableLetters(lettersGuessed)
    while guessCount > 0 and True:
        availableLetters = getAvailableLetters(lettersGuessed)
        print("You have " +str(guessCount)+ " guesses left.\nAvailable letters: " +availableLetters)
        userGuess = input("Please guess a letter: ").lower()
        if userGuess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed) + "\n-----------")
            continue
        else:
            lettersGuessed.append(userGuess)
            if userGuess in secretWord:
                print("Good Guess: " + getGuessedWord(secretWord,lettersGuessed) + "\n-----------")
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord,lettersGuessed) + "\n-----------")
                guessCount -= 1
        if isWordGuessed(secretWord,lettersGuessed):
            break;
    if guessCount > 0:
        print("Congratulations, you have won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord)
