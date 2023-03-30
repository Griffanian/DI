import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
 
global word,word_list,letters,stage,stages
word = random.choice(wordslist)
word_list=list(word)
letters=['_' for items in word_list]
guesses=[]
stage=0
stages=[' ','''
 
     
     
     
  
 
_______
''','''
 
 |    
 |    
 |    
 | 
 |
_|_____
''','''
 ______
 |    
 |    
 |    
 | 
 |
_|_____
''','''
 ______
 |    |
 |    
 |    
 | 
 |
_|_____
''','''
 ______
 |    |
 |    o
 |    
 | 
 |
_|_____
''','''
 ______
 |    |
 |    o
 |    
 | 
 |
_|_____
''','''
 ______
 |    |
 |    o
 |    |
 | 
 |
_|_____
''','''
 ______
 |    |
 |    o
 |   /|
 |   
 |
_|_____
''','''
 ______
 |    |
 |    o
 |   /|\\
 |   
 |
_|_____
''','''
 ______
 |    |
 |    o
 |   /|\\
 |   / 
 |
_|_____
''','''
 ______
 |    |
 |    o
 |   /|\\
 |   / \\
_|_____
'''
]

def display_board(stage:int)->str:
    print(' '.join(letters))
    print('Letters guessed are:')
    print(guesses,stages[stage])

def letter_in_word(letter:str)->bool:
    if letter in word_list:
        return True
    else:
        return False
def not_in_guesses(letter:str) -> bool:
    if letter in guesses:
        return True
    else: 
        return False
def player_input(guesses)->str:
    while True:
        letter_input=input('Guess a letter. ')
        if len(letter_input)==1:
            if letter_input.isalpha() == True:
                if letter_input not in guesses:
                    break
                else:
                    print('You have already guessed that')
            else:
                print('make sure to enter a letter')
        else:
            print("Make sure to enter a single charecter!",letter_input)
    if letter_in_word(letter_input) == True:
        indices = [i for i, x in enumerate(word_list) if x == letter_input]
        for i in indices:
            letters[i]=letter_input

    else:
        global stage
        stage+=1
    
    guesses.append(letter_input)
    guesses=guesses.sort()
    display_board(stage)

def play(guesses):
    while True:
        player_input(guesses)
        if stage >11:
            print('Game Over. Well played')
            break
        if '_' not in letters:
            print('Game Over. Well played YOU WON!!!')
            break
    display_board(stage)
    
    
play(guesses)