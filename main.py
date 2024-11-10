import tkinter
import tkinter.messagebox as mb

window = tkinter.Tk()
window.title("UI TicTacToe")
window.geometry("290x290")
window.resizable(False, False)
window.configure(bg = "green")
area = []
turn = 1

def check_winner():
    if area[0][0]["text"] == "X" and area[0][1]["text"] == "X" and area[0][2]["text"] == "X":
        return "X"
    if area[1][0]["text"] == "X" and area[1][1]["text"] == "X" and area[1][2]["text"] == "X":
        return "X"
    if area[2][0]["text"] == "X" and area[2][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "X" and area[1][0]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    if area[0][1]["text"] == "X" and area[1][1]["text"] == "X" and area[2][1]["text"] == "X":
        return "X"
    if area[0][2]["text"] == "X" and area[1][2]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "X" and area[1][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][2]["text"] == "X" and area[1][1]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "0" and area[0][1]["text"] == "0" and area[0][2]["text"] == "0":
        return "0"
    if area[1][0]["text"] == "0" and area[1][1]["text"] == "0" and area[1][2]["text"] == "0":
        return "0"
    if area[2][0]["text"] == "0" and area[2][1]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][0]["text"] == "0" and area[1][0]["text"] == "0" and area[2][0]["text"] == "0":
        return "0"
    if area[0][1]["text"] == "0" and area[1][1]["text"] == "0" and area[2][1]["text"] == "0":
        return "0"
    if area[0][2]["text"] == "0" and area[1][2]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][0]["text"] == "0" and area[1][1]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    if area[0][2]["text"] == "0" and area[1][1]["text"] == "0" and area[2][0]["text"] == "0":
        return "0"
    return "*"

def new_game():
    global area, turn
    turn = 1
    for i in range(3):
        for j in range(3):
            area[i][j]["text"] = ""

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

    if check_winner() == "X":
        print("Победили экс (Илон Маск всегда побеждает)")
        mb.showinfo("Elon Musk победил!", "Победили экс (Илон Маск всегда побеждает)")
        new_game()
    if check_winner() == "0":
        print("Победили полные нули")
        mb.showinfo("Жаль что нули победили...", "Победили полные нули")
        new_game()
    if turn > 9 and check_winner() == "*":
        print("Ничья")
        mb.showinfo("Ничья", "Лучше бы иксы...")
        new_game()



for i in range(3):
    area.append([])
    for a in range(3):
        button = tkinter.Button(window, text = "", width = 13, height=6, bg = "black", fg = "gold", font=("ArialBold", 8))
        area[i].append(button)
        area[i][a].place(x = i*100, y = a*100)
        area[i][a]["command"] = lambda selected_button = button: push(selected_button)
window.mainloop()

