def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    wordLen = len(secretWord)
    guessString = ['_']
    for a in range(1,wordLen):
        guessString.append('_')
    for letter in lettersGuessed:
        for x in range(wordLen):
            if secretWord[x] == letter:
                guessString[x] = letter
    return ' '.join(guessString)
