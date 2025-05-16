import random
print("You have only 6 lives so try to guess the word within 6 attempts! Good luck!!")
word_list=["apple","banana","orange","grapes","mango","pineapple","strawberry","blueberry","watermelon","peach"]
lives=6
hangman_stages = [
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   | 
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """
]
choosen_word=random.choice(word_list)
choosen_word=list(choosen_word)
no_letters=len(choosen_word)
display=[]
for i in range(no_letters):
    display.append('_')
print(display)
count=0
game_over=False
while game_over!=True:
        guess=input("Guess a letter: ").lower()
    
        for i in range(no_letters):
            letter=choosen_word[i]
            if guess==letter:
                display[i]=guess
        print(display)
        print(hangman_stages[lives])
        if guess not in choosen_word:   
             lives-=1
             print(hangman_stages[lives])
             if lives==0:
                 print("You lose the game")
                 game_over=True
            
        if '_' not in display:
             print("You win the game")
             game_over=True        
       
     

