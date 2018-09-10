import tkinter

window = tkinter.Tk()

def run():
    input1 = txtone.get()
    input2 = txttwo.get()
    characters = ['spock', 'scissors', 'paper', 'rock', 'lizard']
    answers = [[0,1,2,1,2], [2,0,1,2,1], [1,2,0,1,2], [1,2,1,0,2]]
       
    def winner(a,b):
        if answers[a][b] == 0:
            lblresult = tkinter.Label(window, text="Draw", bg="#a1dbcd")
            lblresult.pack()
        elif answers[a][b] == 1:
            lblresult = tkinter.Label(window, text=str(input1) + " beats " + str(input2) + " Player One Wins", bg="#a1dbcd")
            lblresult.pack()
        else:
            lblresult = tkinter.Label(window, text=str(input2) + " beats " + str(input1) + " Player Two Wins", bg="#a1dbcd")
            lblresult.pack()
    #def find_character(character, character_list):
    #    for position in range(0, len(charater_list)):
    #        if character_list[position] == character:
    #            return position
    a = characters.index(input1)
    b = characters.index(input2)
    winner(a,b)
    
    

window.title("Rock, Paper, Scissors, Lizard, Spock")
window.geometry("150x200")

lblone = tkinter.Label(window, text="Player One Choice:", bg="#a1dbcd")
lblone.pack()
txtone = tkinter.Entry(window)
txtone.pack()

lbltwo = tkinter.Label(window, text="Player Two Choice:", bg="#a1dbcd")
lbltwo.pack()
txttwo = tkinter.Entry(window)
txttwo.pack()

btnrun = tkinter.Button(window, text="Play", command=run)
btnrun.pack()



window.configure(background="#a1dbcd")

window.mainloop()


