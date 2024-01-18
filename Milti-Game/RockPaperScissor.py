player_one = {0:'rock', 1:'paper', 2:'scissor'}
player_two = {0:'scissor', 1:'rock', 2:'paper'}

def rock_paper_scissor(num1, num2, bit1, bit2, p1name, p2name):
    p1 = int(num1[bit1])%3
    p2 = int(num2[bit2])%3
    if player_one[p1] == player_two[p2]:
        print("Draw")
    elif player_one[p1]=="paper" and player_two[p2]=='scissor':
        print(p2name, " wins!!")
    elif player_one[p1]=="paper" and player_two[p2]=='rock':
        print(p1name, " wins!!")
    elif player_one[p1]=="rock" and player_two[p2]=='scissor':
        print(p1name, " wins!!")
    elif player_one[p1]=="rock" and player_two[p2]=='paper':
        print(p2name, " wins!!")
    elif player_one[p1]=="scissor" and player_two[p2]=='rock':
        print(p2name, "Player two wins!!")
    elif player_one[p1]=="scissor" and player_two[p2]=='paper':
        print(p1name, " wins!!")

def play_RockPaperScissor():
    print("======ROCK PAPER SCISSOR======")
    p1name = input('Player 1! Please enter your name: ')
    p2name = input('Player 2! Please enter your name: ')
    while(1):
        num1 = input(f'{p1name} enter 3-digit number: ')
        num2 = input(f'{p2name} enter 3-digit number: ')
        bit1 = int(input(f'{p1name} enter the secret bit position:'))
        bit2 = int(input(f'{p2name} enter the secret bit position:'))
        rock_paper_scissor(num1, num2, bit1, bit2, p1name, p2name)
        ch = input('Do you want to continue? y/n :')
        if ch == 'n':
            print("Thanks for playing!!!")
            break
    
#play_RockPaperScissor()