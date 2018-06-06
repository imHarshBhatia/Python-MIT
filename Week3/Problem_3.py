import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alph_list = string.ascii_lowercase
    for x in lettersGuessed:
        alph_list = alph_list.replace(x,"")
    return alph_list
