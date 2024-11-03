import tkinter

window = tkinter.Tk()
window.title("UI TicTacToe")
window.geometry("300x300")
window.resizable(False, False)

area = []
turn = 1

def push(button):
    global turn
    ostatki = turn % 2
    if ostatki == 0:
        turn_char = "0"
    else:
        turn_char = "X"
    if button["text"] == "":
        turn += 1
        button["text"] = turn_char



for i in range(3):
    area.append([])
    for a in range(3):
        button = tkinter.Button(window, text = "", width = 13, height=6)
        area[i].append(button)
        area[i][a].place(x = i*100, y = a*100)
        area[i][a]["command"] = lambda selected_button = button: push(selected_button)
window.mainloop()
