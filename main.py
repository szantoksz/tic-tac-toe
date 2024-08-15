# import libs
import random

import tkinter as tk
from tkinter import ttk, messagebox, StringVar, IntVar


class App:
    def __init__(self):
        self.root = None
        self.window_config()

        self.style = None
        self.window_style()

        self.frame_main = None
        self.window_frame()

        self.button_0 = None
        self.button_1 = None
        self.button_2 = None
        self.button_3 = None
        self.button_4 = None
        self.button_5 = None
        self.button_6 = None
        self.button_7 = None
        self.button_8 = None
        self.button_0_value = None
        self.button_1_value = None
        self.button_2_value = None
        self.button_3_value = None
        self.button_4_value = None
        self.button_5_value = None
        self.button_6_value = None
        self.button_7_value = None
        self.button_8_value = None
        self.window_button()

        self.label_pc = None
        self.label_pc_helper = None
        self.label_user = None
        self.label_user_helper = None
        self.label_game = None
        self.label_game_helper = None
        self.label_move = None
        self.label_move_helper = None
        self.label_pc_helper_value = None
        self.label_user_helper_value = None
        self.label_game_helper_value = None
        self.label_move_helper_value = None
        self.window_label()

        self.available_cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.x = []
        self.o = []
        self.winning_pos_0 = [0, 1, 2]
        self.winning_pos_1 = [3, 4, 5]
        self.winning_pos_2 = [6, 7, 8]
        self.winning_pos_3 = [0, 3, 6]
        self.winning_pos_4 = [1, 4, 7]
        self.winning_pos_5 = [2, 5, 8]
        self.winning_pos_6 = [0, 4, 8]
        self.winning_pos_7 = [2, 4, 6]
        self.current_round = None
        self.win_pc = 0
        self.win_user = 0
        self.game = 0
        self.move = 0
        self.pc_cell = None
        self.x_check = None
        self.o_check = None
        self.winning_pos_0_check = None
        self.winning_pos_1_check = None
        self.winning_pos_2_check = None
        self.winning_pos_3_check = None
        self.winning_pos_4_check = None
        self.winning_pos_5_check = None
        self.winning_pos_6_check = None
        self.winning_pos_7_check = None
        self.win = None
        self.response = None

        self.new_game()

        self.window_run()

    def window_config(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.attributes("-fullscreen", False)
        self.root.geometry("500x250")
        self.root.title("Tic Tac Toe")

    def window_style(self):
        self.style = ttk.Style()
        self.style.configure("frame_main.TFrame", background="white")

    def window_frame(self):
        self.frame_main = ttk.Frame(self.root, style="frame_main.TFrame")
        self.frame_main.pack(fill="both", expand=True)

    def window_button(self):
        self.button_0_value = StringVar(value="N/A")
        self.button_0 = ttk.Button(self.frame_main, textvariable=self.button_0_value, command=self.button_0_click)
        self.button_0.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), ipady=22, sticky="w")

        self.button_1_value = StringVar(value="N/A")
        self.button_1 = ttk.Button(self.frame_main, textvariable=self.button_1_value, command=self.button_1_click)
        self.button_1.grid(row=0, column=1, padx=(10, 0), pady=(10, 0), ipady=22, sticky="w")

        self.button_2_value = StringVar(value="N/A")
        self.button_2 = ttk.Button(self.frame_main, textvariable=self.button_2_value, command=self.button_2_click)
        self.button_2.grid(row=0, column=2, padx=(10, 0), pady=(10, 0), ipady=22, sticky="w")

        self.button_3_value = StringVar(value="N/A")
        self.button_3 = ttk.Button(self.frame_main, textvariable=self.button_3_value, command=self.button_3_click)
        self.button_3.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), ipady=22, sticky="w")

        self.button_4_value = StringVar(value="N/A")
        self.button_4 = ttk.Button(self.frame_main, textvariable=self.button_4_value, command=self.button_4_click)
        self.button_4.grid(row=1, column=1, padx=(10, 0), pady=(10, 0), ipady=22, sticky="w")

        self.button_5_value = StringVar(value="N/A")
        self.button_5 = ttk.Button(self.frame_main, textvariable=self.button_5_value, command=self.button_5_click)
        self.button_5.grid(row=1, column=2, padx=(10, 0), pady=(10, 0), ipady=22, sticky="w")

        self.button_6_value = StringVar(value="N/A")
        self.button_6 = ttk.Button(self.frame_main, textvariable=self.button_6_value, command=self.button_6_click)
        self.button_6.grid(row=2, column=0, padx=(10, 0), pady=(10, 0), ipady=22, sticky="w")

        self.button_7_value = StringVar(value="N/A")
        self.button_7 = ttk.Button(self.frame_main, textvariable=self.button_7_value, command=self.button_7_click)
        self.button_7.grid(row=2, column=1, padx=(10, 0), pady=(10, 0), ipady=22, sticky="w")

        self.button_8_value = StringVar(value="N/A")
        self.button_8 = ttk.Button(self.frame_main, textvariable=self.button_8_value, command=self.button_8_click)
        self.button_8.grid(row=2, column=2, padx=(10, 0), pady=(10, 0), ipady=22, sticky="w")

    def window_label(self):
        self.label_pc = ttk.Label(self.frame_main, text="PC", background="white", font=('Arial', 16))
        self.label_pc.grid(row=0, column=3, padx=(50, 0), pady=(0, 40), sticky="w")

        self.label_pc_helper_value = IntVar(value=0)
        self.label_pc_helper = ttk.Label(self.frame_main, textvariable=self.label_pc_helper_value, background="white",
                                         font=('Arial', 14))
        self.label_pc_helper.grid(row=0, column=3, padx=(57, 0), pady=(0, 0), sticky="w")

        self.label_user = ttk.Label(self.frame_main, text="User", background="white", font=('Arial', 16))
        self.label_user.grid(row=0, column=4, padx=(50, 0), pady=(0, 40), sticky="w")

        self.label_user_helper_value = IntVar(value=0)
        self.label_user_helper = ttk.Label(self.frame_main, textvariable=self.label_user_helper_value,
                                           background="white", font=('Arial', 14))
        self.label_user_helper.grid(row=0, column=4, padx=(67, 0), pady=(0, 0), sticky="w")

        self.label_game = ttk.Label(self.frame_main, text="Game:", background="white", font=('Arial', 16))
        self.label_game.grid(row=1, column=3, padx=(50, 0), pady=(0, 20), sticky="w")

        self.label_game_helper_value = IntVar(value=0)
        self.label_game_helper = ttk.Label(self.frame_main, textvariable=self.label_game_helper_value,
                                           background="white", font=('Arial', 14))
        self.label_game_helper.grid(row=1, column=3, padx=(113, 0), pady=(0, 20), sticky="w")

        self.label_move = ttk.Label(self.frame_main, text="Move:", background="white", font=('Arial', 16))
        self.label_move.grid(row=1, column=3, padx=(50, 0), pady=(27, 0), sticky="w")

        self.label_move_helper_value = IntVar(value=0)
        self.label_move_helper = ttk.Label(self.frame_main, textvariable=self.label_move_helper_value,
                                           background="white", font=('Arial', 14))
        self.label_move_helper.grid(row=1, column=3, padx=(110, 0), pady=(27, 0), sticky="w")

    def button_0_click(self):
        self.available_cells.remove(0)
        self.x.append(0)
        self.current_round = "pc"
        self.new_move()

    def button_1_click(self):
        self.available_cells.remove(1)
        self.x.append(1)
        self.current_round = "pc"
        self.new_move()

    def button_2_click(self):
        self.available_cells.remove(2)
        self.x.append(2)
        self.current_round = "pc"
        self.new_move()

    def button_3_click(self):
        self.available_cells.remove(3)
        self.x.append(3)
        self.current_round = "pc"
        self.new_move()

    def button_4_click(self):
        self.available_cells.remove(4)
        self.x.append(4)
        self.current_round = "pc"
        self.new_move()

    def button_5_click(self):
        self.available_cells.remove(5)
        self.x.append(5)
        self.current_round = "pc"
        self.new_move()

    def button_6_click(self):
        self.available_cells.remove(6)
        self.x.append(6)
        self.current_round = "pc"
        self.new_move()

    def button_7_click(self):
        self.available_cells.remove(7)
        self.x.append(7)
        self.current_round = "pc"
        self.new_move()

    def button_8_click(self):
        self.available_cells.remove(8)
        self.x.append(8)
        self.current_round = "pc"
        self.new_move()

    def new_game(self):
        self.game = self.game + 1
        self.label_game_helper_value.set(self.game)
        self.current_round = "user"
        self.new_move()

    def new_move(self):
        self.move = self.move + 1
        self.label_move_helper_value.set(self.move)

        self.button_0.state(["!disabled"])
        self.button_1.state(["!disabled"])
        self.button_2.state(["!disabled"])
        self.button_3.state(["!disabled"])
        self.button_4.state(["!disabled"])
        self.button_5.state(["!disabled"])
        self.button_6.state(["!disabled"])
        self.button_7.state(["!disabled"])
        self.button_8.state(["!disabled"])

        if 0 not in self.available_cells:
            self.button_0.state(["disabled"])
        if 1 not in self.available_cells:
            self.button_1.state(["disabled"])
        if 2 not in self.available_cells:
            self.button_2.state(["disabled"])
        if 3 not in self.available_cells:
            self.button_3.state(["disabled"])
        if 4 not in self.available_cells:
            self.button_4.state(["disabled"])
        if 5 not in self.available_cells:
            self.button_5.state(["disabled"])
        if 6 not in self.available_cells:
            self.button_6.state(["disabled"])
        if 7 not in self.available_cells:
            self.button_7.state(["disabled"])
        if 8 not in self.available_cells:
            self.button_8.state(["disabled"])

        if 0 in self.x:
            self.button_0_value.set("x")
        if 1 in self.x:
            self.button_1_value.set("x")
        if 2 in self.x:
            self.button_2_value.set("x")
        if 3 in self.x:
            self.button_3_value.set("x")
        if 4 in self.x:
            self.button_4_value.set("x")
        if 5 in self.x:
            self.button_5_value.set("x")
        if 6 in self.x:
            self.button_6_value.set("x")
        if 7 in self.x:
            self.button_7_value.set("x")
        if 8 in self.x:
            self.button_8_value.set("x")

        if 0 in self.o:
            self.button_0_value.set("o")
        if 1 in self.o:
            self.button_1_value.set("o")
        if 2 in self.o:
            self.button_2_value.set("o")
        if 3 in self.o:
            self.button_3_value.set("o")
        if 4 in self.o:
            self.button_4_value.set("o")
        if 5 in self.o:
            self.button_5_value.set("o")
        if 6 in self.o:
            self.button_6_value.set("o")
        if 7 in self.o:
            self.button_7_value.set("o")
        if 8 in self.o:
            self.button_8_value.set("o")

        self.x_check = set(self.x)
        self.o_check = set(self.o)
        self.winning_pos_0_check = set(self.winning_pos_0)
        self.winning_pos_1_check = set(self.winning_pos_1)
        self.winning_pos_2_check = set(self.winning_pos_2)
        self.winning_pos_3_check = set(self.winning_pos_3)
        self.winning_pos_4_check = set(self.winning_pos_4)
        self.winning_pos_5_check = set(self.winning_pos_5)
        self.winning_pos_6_check = set(self.winning_pos_6)
        self.winning_pos_7_check = set(self.winning_pos_7)

        if self.x_check.issuperset(self.winning_pos_0_check):
            self.current_round = None
            self.win = "user"
        if self.x_check.issuperset(self.winning_pos_1_check):
            self.current_round = None
            self.win = "user"
        if self.x_check.issuperset(self.winning_pos_2_check):
            self.current_round = None
            self.win = "user"
        if self.x_check.issuperset(self.winning_pos_3_check):
            self.current_round = None
            self.win = "user"
        if self.x_check.issuperset(self.winning_pos_4_check):
            self.current_round = None
            self.win = "user"
        if self.x_check.issuperset(self.winning_pos_5_check):
            self.current_round = None
            self.win = "user"
        if self.x_check.issuperset(self.winning_pos_6_check):
            self.current_round = None
            self.win = "user"
        if self.x_check.issuperset(self.winning_pos_7_check):
            self.current_round = None
            self.win = "user"

        if self.o_check.issuperset(self.winning_pos_0_check):
            self.current_round = None
            self.win = "pc"
        if self.o_check.issuperset(self.winning_pos_1_check):
            self.current_round = None
            self.win = "pc"
        if self.o_check.issuperset(self.winning_pos_2_check):
            self.current_round = None
            self.win = "pc"
        if self.o_check.issuperset(self.winning_pos_3_check):
            self.current_round = None
            self.win = "pc"
        if self.o_check.issuperset(self.winning_pos_4_check):
            self.current_round = None
            self.win = "pc"
        if self.o_check.issuperset(self.winning_pos_5_check):
            self.current_round = None
            self.win = "pc"
        if self.o_check.issuperset(self.winning_pos_6_check):
            self.current_round = None
            self.win = "pc"
        if self.o_check.issuperset(self.winning_pos_7_check):
            self.current_round = None
            self.win = "pc"

        if self.win == "user":
            self.current_round = "na"
            self.available_cells = []
            self.x = []
            self.o = []
            self.move = 0
            self.win_user = self.win_user + 1
            self.label_user_helper_value.set(self.win_user)
            self.button_0.state(["!disabled"])
            self.button_1.state(["!disabled"])
            self.button_2.state(["!disabled"])
            self.button_3.state(["!disabled"])
            self.button_4.state(["!disabled"])
            self.button_5.state(["!disabled"])
            self.button_6.state(["!disabled"])
            self.button_7.state(["!disabled"])
            self.button_8.state(["!disabled"])
            self.button_0_value.set("N/A")
            self.button_1_value.set("N/A")
            self.button_2_value.set("N/A")
            self.button_3_value.set("N/A")
            self.button_4_value.set("N/A")
            self.button_5_value.set("N/A")
            self.button_6_value.set("N/A")
            self.button_7_value.set("N/A")
            self.button_8_value.set("N/A")
            self.move = 0
            self.response = messagebox.askquestion("You Won!", "Do you want a new round?")
            if self.response == "no":
                exit()
            if self.response == "yes":
                self.win = None
                self.move = 0
                self.available_cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                self.new_game()
        if self.win == "pc":
            self.current_round = "na"
            self.available_cells = []
            self.x = []
            self.o = []
            self.move = 0
            self.win_pc = self.win_pc + 1
            self.label_pc_helper_value.set(self.win_pc)
            self.button_0.state(["!disabled"])
            self.button_1.state(["!disabled"])
            self.button_2.state(["!disabled"])
            self.button_3.state(["!disabled"])
            self.button_4.state(["!disabled"])
            self.button_5.state(["!disabled"])
            self.button_6.state(["!disabled"])
            self.button_7.state(["!disabled"])
            self.button_8.state(["!disabled"])
            self.button_0_value.set("N/A")
            self.button_1_value.set("N/A")
            self.button_2_value.set("N/A")
            self.button_3_value.set("N/A")
            self.button_4_value.set("N/A")
            self.button_5_value.set("N/A")
            self.button_6_value.set("N/A")
            self.button_7_value.set("N/A")
            self.button_8_value.set("N/A")
            self.move = 0
            self.response = messagebox.askquestion("You Lost!", "Do you want a new round?")
            if self.response == "no":
                exit()
            if self.response == "yes":
                self.win = None
                self.move = 0
                self.available_cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                self.new_game()

        if self.available_cells == []:
            self.response = messagebox.askquestion("Draw!", "Do you want a new round?")
            if self.response == "no":
                exit()
            if self.response == "yes":
                self.move = 0
                self.available_cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                self.new_game()

        if self.current_round == "user":
            if 0 in self.available_cells:
                self.button_0.state(["!disabled"])
                self.button_0_value.set("Click!")
            if 1 in self.available_cells:
                self.button_1.state(["!disabled"])
                self.button_1_value.set("Click!")
            if 2 in self.available_cells:
                self.button_1.state(["!disabled"])
                self.button_2_value.set("Click!")
            if 3 in self.available_cells:
                self.button_1.state(["!disabled"])
                self.button_3_value.set("Click!")
            if 4 in self.available_cells:
                self.button_1.state(["!disabled"])
                self.button_4_value.set("Click!")
            if 5 in self.available_cells:
                self.button_1.state(["!disabled"])
                self.button_5_value.set("Click!")
            if 6 in self.available_cells:
                self.button_1.state(["!disabled"])
                self.button_6_value.set("Click!")
            if 7 in self.available_cells:
                self.button_1.state(["!disabled"])
                self.button_7_value.set("Click!")
            if 8 in self.available_cells:
                self.button_1.state(["!disabled"])
                self.button_8_value.set("Click!")
        if self.current_round == "pc":
            if 0 in self.available_cells:
                self.button_0.state(["disabled"])
                self.button_0_value.set(["Choosing"])
            if 1 in self.available_cells:
                self.button_1.state(["disabled"])
                self.button_1_value.set(["Choosing"])
            if 2 in self.available_cells:
                self.button_2.state(["disabled"])
                self.button_2_value.set(["Choosing"])
            if 3 in self.available_cells:
                self.button_3.state(["disabled"])
                self.button_3_value.set(["Choosing"])
            if 4 in self.available_cells:
                self.button_4.state(["disabled"])
                self.button_4_value.set(["Choosing"])
            if 5 in self.available_cells:
                self.button_5.state(["disabled"])
                self.button_5_value.set(["Choosing"])
            if 6 in self.available_cells:
                self.button_6.state(["disabled"])
                self.button_6_value.set(["Choosing"])
            if 7 in self.available_cells:
                self.button_7.state(["disabled"])
                self.button_7_value.set(["Choosing"])
            if 8 in self.available_cells:
                self.button_8.state(["disabled"])
                self.button_8_value.set(["Choosing"])
            self.pc_move()

    def pc_move(self):
        self.pc_cell = random.choice(self.available_cells)
        self.available_cells.remove(self.pc_cell)
        self.o.append(self.pc_cell)
        self.current_round = "user"
        self.new_move()

    def window_run(self):
        self.root.mainloop()


def main():
    App()


if __name__ == "__main__":
    main()
