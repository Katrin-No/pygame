import random
HANGMAN_PICS = ['''
 +----+
 |
 |
 |
 ===''', '''
 +----+ 
 |    0
 |
 |
 ===''', '''
 +----+
 |    0
 |    |
 |
 ===''', '''
 +----+
 |    0 
 |   /| 
 |
 ===''', '''
 +----+
 |    0 
 |   /|\ 
 |
 ===''', '''
 +----+
 |    0 
 |   /|\ 
 |   / 
 ===''', ''' 
 +-----+
 | ¯\_(ツ)_/¯
 |      |
 |    _/ \_
 ===''']
words = 'aggressiv ängstlich arrogant böse brutal dickköpfig doppelzüngig eigensinnig faul feindselig frech gemein gierig geringschätzig gleichgültig grausam grob langweilig neidisch niederträchtig unehrlich ungeduldig übelnehmerisch'.split()
# split() возвращает список, сформированный из строковых переменных, на которые разбивается строка.


def getRandomWord(wordList):
  # Эта функция возвращает случайную строку из переданного списка.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Diese gibt es nicht:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # Показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву
    while True:
        print('Gib mir bitte eine Buchstabe ')
        guess = input()
        guess = guess.lower()  # umwandelt große Buchstabe in kleine
        if len(guess) != 1:
            print('Bitte, gib mir nur eine Buchstabe ')
        elif guess in alreadyGuessed:
            print('Die war schon, gib mir bitte eine andere.')
        elif guess not in 'qwertzuiopüasdfghjklöäyxcvbnm':
            print('Hey, das ist ja keine Buchstabe!')
        else:
            return guess


def playAgain():
    # Эта функция возвращает значение True, если игрок хочет сыграть заново; в противном случае возвращает False.
    print('Nochmal? (y/n)')
    return input().lower().startswith('y')


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Позволяет игроку ввести букву.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Проверяет, выиграл ли игрок.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('JA! Das war - "' +
                  secretWord + '"! Richtig!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

    # Проверяет, превысил ли игрок лимит попыток и проиграл.
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('Du hast keine Versuche mehr!\n Die falschen Buchstaben: '
              + str(len(missedLetters))
              + ' und die richtigen: '
              + str(len(correctLetters))
              + '. Es war: "'
              + secretWord + '".')
        gameIsDone = True

    # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
