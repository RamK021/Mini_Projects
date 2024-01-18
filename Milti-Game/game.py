def play_game_1():
    import JumbledWords
    JumbledWords.play_JumbledWords()

def play_game_2():
    import GuessTheMovieName
    GuessTheMovieName.play_GuessTheMovieName()

def play_game_3():
    import RockPaperScissor
    RockPaperScissor.play_RockPaperScissor()

def play_game_4():
    import TicTacToe
    TicTacToe.play_TicTacToe()

def play_game_5():
    import SnakesLadders
    SnakesLadders.play_SnakesLadders()

def game():
    while True:
        print("*----------------------------*")
        print("|[1] Jumble Words            |")
        print("|[2] Guess The Movie Name    |")
        print("|[3] Rock, Paper & Scissor   |")
        print("|[4] Tic Tac Toe             |")
        print("|[5] Snakes & Ladders        |")
        print("|[6] Exit                    |")
        print("*----------------------------*")
        choice = input("Enter your choice : ")

        if choice == '1':
            play_game_1()
        elif choice == '2':
            play_game_2()
        elif choice == '3':
            play_game_3()
        elif choice == '4':
            play_game_4()
        elif choice == '5':
            play_game_5()
        elif choice == '6':
            print('Your exited successfully!!')
            break
        else:
            print("Invalid input, Try Again!!")

game()

