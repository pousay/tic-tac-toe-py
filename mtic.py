from tkinter import messagebox
from tkinter import *

#app
mainwin = Tk()
mainwin.geometry("500x500") 
mainwin.minsize(500,500) 
mainwin.maxsize(500,500) 
mainwin.title("Tic Tac Toe")



#variables
txtul = ""
txtum = ""
txtur = ""
txtvl = ""
txtvm = ""
txtvr = ""
txtdl = ""
txtdm = ""
txtdr = ""
#player score
def mainreset():
    global scplayer2,scplayer1
    scplayer1 = 0
    scplayer2 = 0

    lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
    lblscore1.place(x = 195,y = 57)

    lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
    lblscore2.place(x = 295,y = 57)
    
scplayer1 = 0
scplayer2 = 0


#draw list

draw = [1,1,1,1,1,1,1,1,1]

#user turn
p1 = [1,3,5,7,9] #x
p2 = [2,4,6,8]   #o
turn = 1

#mainfuncs
def tnupl():
    global txtul, turn, p1, p2,scplayer1,scplayer2,draw,lbldm
    draw.remove(1)
    if turn in p1 :
        lblupl = Label(text = "X",fg = "red",bg = "#DDFF00",font=("arial",60,"bold"))
        lblupl.place(y = 140,x = 90,width=100,height=100)
        turn +=1
        txtul = "X"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57) 

              
            if messagebox.OK:
                reset1()

        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57) 
            if messagebox.OK:
                reset1()
        else : 
            if 1 not in draw :
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()



    elif turn in p2 :
        lblupl = Label(text = "O",fg = "blue",bg = "#DDFF00",font=("arial",60,"bold"))
        lblupl.place(y = 140,x = 90,width=100,height=100)
        turn +=1
        txtul = "O"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)                         
            if messagebox.OK:
                reset1()  
         
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)
            if messagebox.OK:
                reset1()

        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()




def tnupm():
    global txtum, turn,p1,p2,scplayer1,scplayer2,draw,lbldm
    draw.remove(1) 
    if turn in p1 :
        lblupm = Label(text = "X",fg = "red",bg = "#DDFF00",font=("arial",60,"bold"))
        lblupm.place(y = 140,x = 195,width=100,height=100)
        turn +=1
        txtum = "X"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  
              
            if messagebox.OK:
                reset1()                                
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)
            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()


    elif turn in p2 :
        lblupm = Label(text = "O",fg = "blue",bg = "#DDFF00",font=("arial",60,"bold"))
        lblupm.place(y = 140,x = 195,width=100,height=100)
        turn +=1
        txtum = "O"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)                     
 
            if messagebox.OK:
                reset1()               
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()
    
    
def tnupr():
    global txtur,turn, p1, p2,scplayer1,scplayer2,draw,lbldm
    draw.remove(1)
    if turn in p1 :
        lblupr = Label(text = "X",fg = "red",bg = "#DDFF00",font=("arial",60,"bold"))
        lblupr.place(y = 140,x = 300,width=100,height=100)
        turn +=1
        txtur = "X"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  
             
            if messagebox.OK:
                reset1()                                
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()

    elif turn in p2 :
        lblupr = Label(text = "O",fg = "blue",bg = "#DDFF00",font=("arial",60,"bold"))
        lblupr.place(y = 140,x = 300,width=100,height=100)
        turn +=1
        txtur = "O"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  

            if messagebox.OK:
                reset1()                                   
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()
    

def tnvl():
    global txtvl,turn, p1, p2,scplayer1,scplayer2,draw,lbldm
    draw.remove(1)
    if turn in p1 :
        lblvl = Label(text = "X",fg = "red",bg = "#DDFF00",font=("arial",60,"bold"))
        lblvl.place(y = 245,x = 90,width=100,height=100)
        turn +=1
        txtvl = "X"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  
            
            if messagebox.OK:
                reset1()                                   
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1() 
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()

    elif turn in p2 :
        lblvl = Label(text = "O",fg = "blue",bg = "#DDFF00",font=("arial",60,"bold"))
        lblvl.place(y = 245,x = 90,width=100,height=100)
        turn +=1
        txtvl = "O"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)    
 
            if messagebox.OK:
                reset1()                                
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1() 
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()
    #else :

def tnvm():
    global txtvm,turn, p1, p2,scplayer1,scplayer2,draw,lbldm
    draw.remove(1) 
    if turn in p1 :
        lblvm = Label(text = "X",fg = "red",bg = "#DDFF00",font=("arial",60,"bold"))
        lblvm.place(y = 245,x = 195,width=100,height=100)
        turn +=1
        txtvm = "X"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  
            
            if messagebox.OK:
                reset1()                                  
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)
            if messagebox.OK:
                reset1()

        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()

    elif turn in p2 :
        lblvm = Label(text = "O",fg = "blue",bg = "#DDFF00",font=("arial",60,"bold"))
        lblvm.place(y = 245,x = 195,width=100,height=100)
        turn +=1
        txtvm = "O"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  

            if messagebox.OK:
                reset1()                                  
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()
    # #else :

def tnvr():
    global txtvr,turn, p1, p2,scplayer1,scplayer2,draw,lbldm
    draw.remove(1) 
    if turn in p1 :
        lblvr = Label(text = "X",fg = "red",bg = "#DDFF00",font=("arial",60,"bold"))
        lblvr.place(y = 245,x = 300,width=100,height=100)
        turn +=1
        txtvr = "X"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  
            
            if messagebox.OK:
                reset1()                                  
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1() 
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()

    elif turn in p2 :
        lblvr = Label(text = "O",fg = "blue",bg = "#DDFF00",font=("arial",60,"bold"))
        lblvr.place(y = 245,x = 300,width=100,height=100)
        turn +=1
        txtvr = "O"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  

            if messagebox.OK:
                reset1()                                  
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()
    # #else : 

def tndl():

    global txtdl,turn, p1, p2,scplayer1,scplayer2,draw,lbldm
    draw.remove(1) 
    if turn in p1 :
        lbldl = Label(text = "X",fg = "red",bg = "#DDFF00",font=("arial",60,"bold"))
        lbldl.place(y = 350,x = 90,width=100,height=100)
        turn +=1
        txtdl = "X"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57) 
             
            if messagebox.OK:
                reset1()                                  
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()

    elif turn in p2 :
        lbldl = Label(text = "O",fg = "blue",bg = "#DDFF00",font=("arial",60,"bold"))
        lbldl.place(y = 350,x = 90,width=100,height=100)
        turn +=1
        txtdl = "O"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57) 

            if messagebox.OK:
                reset1()                                  
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()
    #else : 

def tndm():
    global txtdm,turn, p1, p2,scplayer1,scplayer2,draw,lbldm
    draw.remove(1) 
    if turn in p1 :
        lbldm = Label(text = "X",fg = "red",bg = "#DDFF00",font=("arial",60,"bold"))
        lbldm.place(y = 350,x = 195,width=100,height=100)
        turn +=1
        txtdm = "X"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  
             
            if messagebox.OK:
                reset1()                                 
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()

    elif turn in p2 :
        lbldm = Label(text = "O",fg = "blue",bg = "#DDFF00",font=("arial",60,"bold"))
        lbldm.place(y = 350,x = 195,width=100,height=100)
        turn +=1
        txtdm = "O"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)
  
            if messagebox.OK:
                reset1()                                  
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()
    #else : 

def tndr():
    global txtdr,turn, p1, p2,scplayer1,scplayer2,draw,lbldm
    draw.remove(1) 
    if turn in p1 :
        lbldm = Label(text = "X",fg = "red",bg = "#DDFF00",font=("arial",60,"bold"))
        lbldm.place(y = 350,x = 300,width=100,height=100)
        turn +=1
        txtdr = "X"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")
        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  
            
            if messagebox.OK:
                reset1()                                  
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()

    elif turn in p2 :
        lbldm = Label(text = "O",fg = "blue",bg = "#DDFF00",font=("arial",60,"bold"))
        lbldm.place(y = 350,x = 300,width=100,height=100)
        turn +=1
        txtdr = "O"
        if turn == 2 or turn == 4 or turn == 6 or turn == 8:
            labelwitit.config(text = "Turn : player 2")
        else : 
            labelwitit.config(text = "Turn : player 1")

        if (txtul== "X" and txtum== "X" and txtur== "X") or (txtvl== "X" and txtvm== "X" and txtvr== "X")or (txtdl== "X" and txtdm== "X" and txtdr== "X") or (txtdl== "X" and txtvl== "X" and txtul== "X") or (txtdm== "X" and txtvm== "X" and txtum== "X") or (txtdr== "X" and txtvr== "X" and txtur== "X") or (txtul== "X" and txtvm== "X" and txtdr== "X") or (txtur== "X" and txtvm== "X" and txtdl== "X") :
            messagebox.showinfo("Game Over","player1 won")  
            scplayer1 += 1  
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)  

            if messagebox.OK:
                reset1()                                 
        elif (txtul== "O" and txtum == "O" and txtur== "O") or (txtvl== "O" and txtvm== "O" and txtvr== "O") or (txtdl== "O" and txtdm== "O" and txtdr== "O") or (txtdl== "O" and txtvl== "O" and txtul== "O")  or (txtdm== "O" and txtvm== "O" and txtum== "O") or (txtdr== "O" and txtvr== "O" and txtur== "O") or (txtul== "O" and txtvm== "O" and txtdr== "O") or (txtur== "O" and txtvm== "O" and txtdl== "O") :
            messagebox.showinfo("Game Over","player2 won") 
            scplayer2 += 1
            lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
            lblscore1.place(x = 195,y = 57)

            lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
            lblscore2.place(x = 295,y = 57)

            if messagebox.OK:
                reset1()
        else : 
            if len(draw) == 0:
                messagebox.showinfo("Game Over","draw")
                if messagebox.OK :
                    reset1()



#reset
def reset1():
    global txtul,txtum,txtur,txtvl,txtvm,txtvr,txtdl,txtdm,txtdr,turn,draw
    txtul = ""
    txtum = ""
    txtur = ""
    txtvl = ""
    txtvm = ""
    txtvr = ""
    txtdl = ""
    txtdm = ""
    txtdr = ""
    
    turn = 1

    btnupl = Button(bg = "#DDFF00",command=tnupl)
    btnupl.place(y = 140,x = 90,width=100,height=100)

    btnupm = Button(bg = "#DDFF00",command=tnupm)
    btnupm.place(y = 140,x = 195,width=100,height=100)

    btnupr = Button(bg = "#DDFF00",command=tnupr)
    btnupr.place(y = 140,x = 300,width=100,height=100)

    btnvl = Button(bg = "#DDFF00",command=tnvl)
    btnvl.place(y = 245,x = 90,width=100,height=100)

    btnvm = Button(bg = "#DDFF00",command=tnvm)
    btnvm.place(y = 245,x = 195,width=100,height=100)

    btnvr = Button(bg = "#DDFF00",command=tnvr)
    btnvr.place(y = 245,x = 300,width=100,height=100)

    btndl = Button(bg = "#DDFF00",command=tndl)
    btndl.place(y = 350,x = 90,width=100,height=100)

    btndm = Button(bg = "#DDFF00",command=tndm)
    btndm.place(y = 350,x = 195,width=100,height=100)

    btndr = Button(bg = "#DDFF00",command=tndr)
    btndr.place(y = 350,x = 300,width=100,height=100)


    draw = [1,1,1,1,1,1,1,1,1]

    labelwitit.config(text = "Turn : player 1")

#draw point





#app cover
lblwin =  Label(bg = "#770CD1")
lblwin.place(width=250,height=250)

lblwin1 = Label(bg = "#8415E2")
lblwin1.place(x = 250,width=250,height=250)

lblwin2 = Label(bg = "#8415E2")
lblwin2.place(y = 250,width=250,height=250)

lblwin3 = Label(bg = "#770CD1")
lblwin3.place(x = 250,y=250,width=250,height=250)

#players name
lblname1 = Label(text = "player 1",fg = "white",bg = "#770CD1",font = ("arial",15,"bold"))
lblname1.place(x = 160,y=30)

lblname2 = Label(text = "player 2",fg = "white",bg = "#8415E2",font = ("arial",15,"bold"))
lblname2.place(x = 260,y = 30)


lblscore1 = Label(text =scplayer1,font = ("arial",17,"bold"),bg = "#770CD1")
lblscore1.place(x = 195,y = 57)

lblscore2 = Label(text = scplayer2,font = ("arial",17,"bold"),bg = "#8415E2") 
lblscore2.place(x = 295,y = 57)

#player icon
lblic = Label(text = "X",fg = "red",bg = "#770CD1",font = ("arial",15,"bold"))
lblic.place(x = 195,y=90)

lblic2 = Label(text = "O",fg = "blue",bg = "#8415E2",font = ("arial",15,"bold"))
lblic2.place(x = 295,y = 90)



#buttons

btnupl = Button(bg = "#DDFF00",command=tnupl)
btnupl.place(y = 140,x = 90,width=100,height=100)

btnupm = Button(bg = "#DDFF00",command=tnupm)
btnupm.place(y = 140,x = 195,width=100,height=100)

btnupr = Button(bg = "#DDFF00",command=tnupr)
btnupr.place(y = 140,x = 300,width=100,height=100)

btnvl = Button(bg = "#DDFF00",command=tnvl)
btnvl.place(y = 245,x = 90,width=100,height=100)

btnvm = Button(bg = "#DDFF00",command=tnvm)
btnvm.place(y = 245,x = 195,width=100,height=100)

btnvr = Button(bg = "#DDFF00",command=tnvr)
btnvr.place(y = 245,x = 300,width=100,height=100)

btndl = Button(bg = "#DDFF00",command=tndl)
btndl.place(y = 350,x = 90,width=100,height=100)

btndm = Button(bg = "#DDFF00",command=tndm)
btndm.place(y = 350,x = 195,width=100,height=100)

btndr = Button(bg = "#DDFF00",command=tndr)
btndr.place(y = 350,x = 300,width=100,height=100)


btnreset = Button(text = "Reset",font = ("arial",10,"bold"),command=mainreset,bg = "#A8F75D")
btnreset.place(x = 225,y = 110)


"winner"

#who is turn is it

labelwitit = Label(text = "Turn : player 1",font=("arial",10,"bold"),bg = "#5DF7EE")
labelwitit.place(x = 200,y = 7,width= 100, height= 20)



mainwin.mainloop()