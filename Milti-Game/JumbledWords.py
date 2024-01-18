import random
# Jumbled Words
def choose():
    words = ['guarantee','cricket','science','science','engineer','manages','flower','conveys','friends','computer',
             'services', 'mathematics', 'practical', 'exercise', 'keyboard', 'algorithm', 'structure', 'conceptually',
             'country', 'problems', 'dynamic', 'solutions', 'problem', 'accuracy', 'artificial', 'platform']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = ''.join(random.sample(word, len(word))) 
    return jumbled

def thank(p1n, p2n, p1, p2):
    print(p1n,' Your score is:', p1)
    print(p2n,' Your score is:', p2)
    

def play_JumbledWords():
    print("======JUMBLED WORDS======")
    p1name = input('Player 1, Please enter your name: ')
    p2name = input('Player 2, Please enter your name: ')
    pp1 = 0
    pp2 = 0
    turn = 0
    while(1):
        #Computer's task
        picked_word = choose()
        #Create question
        qn = jumble(picked_word)
        print(qn)
        #Player 1
        if turn%2 == 0:
            print(p1name, ' Your turn. ')
            ans = input('what is on my mind? ')
            if ans == picked_word:
                pp1 += 1
                print('Your score is ', pp1)
            else:
                print('Better luck next time. I thougth:', picked_word)
            c = int(input('Press 1 to continue and 0 to quit:'))
            if c==0:
                thank(p1name, p2name, pp1, pp2)
                break
        else:
            print(p2name, ' Your turn. ')
            ans = input('what is on my mind? ')
            if ans == picked_word:
                pp2 += 1
                print('Your score is ', pp2)
            else:
                print('Better luck next time. I thougth:', picked_word)
            c = int(input('Press 1 to continue and 0 to quit:'))
            if c==0:
                thank(p1name, p2name, pp1, pp2)
                return "Thanks for playing!!"
        turn += 1

#play_JumbledWords()
