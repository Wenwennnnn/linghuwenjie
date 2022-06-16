# Define a chessboard with an array, and the size of the chessboard is 15 × fifteen
# The array index represents the position
# The element value represents the status of the position: 0 represents no chess pieces,
# 1 represents black chess, and -1 represents white chess.

from tkinter import *
from tkinter.messagebox import *
import os

TAG_BLACK = "1"
TAG_EMPTY = "."
TAG_WHITE = "0"
ROOT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".")


class Chess(object):

    def bf_save(self):

        path = os.path.join(ROOT_DIR, "record.txt")
        file = open(path, "w")
        for i in range(len(self.record)):
            x, y = self.record[i]
            file.write("{}: [{}, {}]\n".format("Black" if i % 2 == 0 else "White", x, y))
        file.close()

    def init_matrix(self):
        return [[TAG_EMPTY for y in range(self.column)] for x in range(self.row)]

    def __init__(self):
        #############
        #   param   #
        #######################################
        self.row, self.column = 15, 15
        self.mesh = 25
        self.ratio = 0.9
        self.board_color = "#CDBA96"
        self.header_bg = "#CDC0B0"
        self.btn_font = ("Blackbody", 12, "bold")
        self.step = self.mesh / 2
        self.chess_r = self.step * self.ratio
        self.point_r = self.step * 0.2
        self.matrix = self.init_matrix()
        self.is_start = False
        self.is_black = True
        self.record = []

        ###########
        #   GUI   #
        #######################################
        self.root = Tk()
        self.root.title("Gobang By Young")
        self.root.resizable(width=False, height=False)

        self.f_header = Frame(self.root, highlightthickness=0, bg=self.header_bg)

        self.b_start = Button(self.f_header, text="Begin", command=self.bf_start, font=self.btn_font)
        self.b_restart = Button(self.f_header, text="Start over", command=self.bf_restart, state=DISABLED, font=self.btn_font)
        self.l_info = Label(self.f_header, text="Not started", bg=self.header_bg, font=("Regular script", 18, "bold"), fg="white")
        self.b_regret = Button(self.f_header, text="Repentance chess", command=self.bf_regret, state=DISABLED, font=self.btn_font)
        self.b_lose = Button(self.f_header, text="Admit defeat", command=self.bf_lose, state=DISABLED, font=self.btn_font)

        self.c_chess = Canvas(self.root, bg=self.board_color, width=(self.column + 1) * self.mesh,
                              height=(self.row + 1) * self.mesh, highlightthickness=0)
        self.draw_board()
        self.c_chess.bind("<Button-1>", self.cf_board)

        self.b_record = Button(self.root, text="Double check", command=self.bf_record, font=self.btn_font, bg="lightblue")
        self.b_save = Button(self.root, text="preservation", command=self.bf_save, font=self.btn_font, bg="lightblue")

        self.f_header.pack(side=TOP, fill=BOTH, ipadx=10)
        self.b_start.pack(side=LEFT, padx=20)
        self.b_restart.pack(side=LEFT)
        self.l_info.pack(side=LEFT, expand=YES, fill=BOTH, pady=10)
        self.b_lose.pack(side=RIGHT, padx=20)
        self.b_regret.pack(side=RIGHT)

        self.c_chess.pack(side=TOP)

        self.b_record.pack(side=TOP, expand=YES, fill=X)
        self.b_save.pack(side=TOP, expand=YES, fill=X)

        self.root.mainloop()

    # Draw a grid at x rows and Y columns
    def draw_mesh(self, x, y):
        # A magnification.
        ratio = (1 - self.ratio) * 0.99 + 1
        center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
        # Draw background color
        self.c_chess.create_rectangle(center_y - self.step, center_x - self.step,
                                      center_y + self.step, center_x + self.step,
                                      fill=self.board_color, outline=self.board_color)
        # Then draw the grid line, where a B C D are different coefficients,
        # which are determined according to different positions of X and y, and need to be derived.
        a, b = [0, ratio] if y == 0 else [-ratio, 0] if y == self.row - 1 else [-ratio, ratio]
        c, d = [0, ratio] if x == 0 else [-ratio, 0] if x == self.column - 1 else [-ratio, ratio]
        self.c_chess.create_line(center_y + a * self.step, center_x, center_y + b * self.step, center_x)
        self.c_chess.create_line(center_y, center_x + c * self.step, center_y, center_x + d * self.step)

        # There are some special dots to draw small black dots
        if ((x == 3 or x == 11) and (y == 3 or y == 11)) or (x == 7 and y == 7):
            self.c_chess.create_oval(center_y - self.point_r, center_x - self.point_r,
                                     center_y + self.point_r, center_x + self.point_r, fill="black")

    # Draw the chess pieces at the X row and Y column, and color specifies the color of the chess pieces
    def draw_chess(self, x, y, color):
        center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
        # Draw a circle
        self.c_chess.create_oval(center_y - self.chess_r, center_x - self.chess_r,
                                 center_y + self.chess_r, center_x + self.chess_r,
                                 fill=color)

    # Draw the whole chessboard
    def draw_board(self):
        [self.draw_mesh(x, y) for y in range(self.column) for x in range(self.row)]

    # Show text in the middle
    def center_show(self, text):
        width, height = int(self.c_chess['width']), int(self.c_chess['height'])
        self.c_chess.create_text(int(width / 2), int(height / 2), text=text, font=("黑体", 30, "bold"), fill="red")

    def bf_record(self):
        Record(self.record)
        pass

    # At the beginning, set the status of each component and variable,
    # initialize the matrix, initialize the chessboard, and initialize the information
    def bf_start(self):
        self.set_btn_state("start")
        self.is_start = True
        self.is_black = True
        self.matrix = self.init_matrix()
        self.draw_board()
        self.record = []
        self.l_info.config(text="Black chess")

    # the same as the beginning
    def bf_restart(self):
        self.record = []
        self.bf_start()

    # Use last_ P to identify the position of the previous step.
    # First, use the grid to cover the chess pieces, and operate the corresponding variables.
    # If the matrix[x][y] is to be empty, you can only regret the chess once
    def bf_regret(self):
        if len(self.record) == 0:
            showinfo("Tips", "can't repent now")
            return
        x, y = self.record[-1]
        self.draw_mesh(x, y)
        self.matrix[x][y] = TAG_EMPTY
        self.record = self.record[:-1]
        self.trans_identify()

    # Several status changes and display text
    def bf_lose(self):
        self.set_btn_state("init")
        self.is_start = False
        text = self.ternary_operator("Black side concedes defeat", "White side concedes defeat")
        self.l_info.config(text=text)
        self.center_show("fail")

    def go_chess(self, x, y):
        # The color of the piece and the identification of the piece in the matrix.
        color = self.ternary_operator("black", "white")
        tag = self.ternary_operator(TAG_BLACK, TAG_WHITE)
        # Draw a chess piece first, modify the value of the corresponding point of the matrix,
        # and use last_ P record this operation point
        self.draw_chess(x, y, color)
        self.matrix[x][y] = tag
        self.record.append([x, y])
        # If you win, the game ends, the status is modified, and the center displays that a party wins
        if self.is_win(x, y, tag):
            self.is_start = False
            self.set_btn_state("init")
            text = self.ternary_operator("Black side wins", "White side wins")
            self.center_show(text)
            return
        # If the game continues, swap players
        self.trans_identify()

    # Canvas‘s click
    def cf_board(self, e):
        # Find the coordinate closest to the clicked point
        x, y = int((e.y - self.step) / self.mesh), int((e.x - self.step) / self.mesh)
        # Find the center point of the coordinate
        center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
        # Calculate the distance from the click point to the center
        distance = ((center_x - e.y) ** 2 + (center_y - e.x) ** 2) ** 0.5
        # If the distance is not within the specified circle, exit.
        # / / if there are already pieces in this position, exit. / / if the game has not started, exit
        if distance > self.step * 0.95 or self.matrix[x][y] != TAG_EMPTY or not self.is_start:
            return
        self.go_chess(x, y)

    def is_win(self, x, y, tag):
        # Get list of oblique directions
        def direction(i, j, di, dj, row, column, matrix):
            temp = []
            while 0 <= i < row and 0 <= j < column:
                i, j = i + di, j + dj
            i, j = i - di, j - dj
            while 0 <= i < row and 0 <= j < column:
                temp.append(matrix[i][j])
                i, j = i - di, j - dj
            return temp

        four_direction = []
        # Get a list of horizontal and vertical directions
        four_direction.append([self.matrix[i][y] for i in range(self.row)])
        four_direction.append([self.matrix[x][j] for j in range(self.column)])
        # Get list of oblique directions
        four_direction.append(direction(x, y, 1, 1, self.row, self.column, self.matrix))
        four_direction.append(direction(x, y, 1, -1, self.row, self.column, self.matrix))

        # Check these four directions one by one to see if they meet the requirements of the five child Lianzhu
        for v_list in four_direction:
            if tag * 5 in "".join(v_list):
                return True
        return False

    # Set whether the four buttons can be clicked
    def set_btn_state(self, state):
        state_list = [NORMAL, DISABLED, DISABLED, DISABLED] if state == "init" else [DISABLED, NORMAL, NORMAL, NORMAL]
        self.b_start.config(state=state_list[0])
        self.b_restart.config(state=state_list[1])
        self.b_regret.config(state=state_list[2])
        self.b_lose.config(state=state_list[3])

    # Because there are many and self Black related ternary operations, so they are extracted
    def ternary_operator(self, true, false):
        return true if self.is_black else false

    # Swap players
    def trans_identify(self):
        self.is_black = not self.is_black
        text = self.ternary_operator("Black chess", "White chess")
        self.l_info.config(text=text)

    def print_process(self):
        pass


class Record(object):

    def __init__(self, record):
        #############
        #   param   #
        #######################################
        self.row, self.column = 15, 15
        self.mesh = 25
        self.ratio = 0.9
        self.board_color = "#CDBA96"
        self.header_bg = "#CDC0B0"
        self.btn_font = ("Blackbody", 12, "bold")
        self.step = self.mesh / 2
        self.chess_r = self.step * self.ratio
        self.point_r = self.step * 0.2
        ###########
        self.is_black = True
        self.index = -1
        self.record = record
        ###########
        #   GUI   #
        #######################################
        self.root = Tk()
        self.root.title("Double check")
        self.root.resizable(width=False, height=False)
        self.root.bind("<Key>", self.kf_step)

        self.f_header = Frame(self.root, highlightthickness=0, bg=self.header_bg)
        self.l_info = Label(self.f_header, text="Not started", bg=self.header_bg, font=("Regular script", 18, "bold"), fg="white")

        self.c_chess = Canvas(self.root, bg=self.board_color, width=(self.column + 1) * self.mesh,
                              height=(self.row + 1) * self.mesh, highlightthickness=0)
        self.draw_board()

        self.f_header.pack(fill=BOTH, ipadx=10)
        self.l_info.pack(side=LEFT, expand=YES, fill=BOTH, pady=10)
        self.c_chess.pack()

        self.root.mainloop()

    def kf_step(self, e):
        if e.keycode not in [37, 39]:
            return
        if e.keycode == 37:
            if self.index == -1:
                self.l_info.config(text="We have reached the beginning")
                return
            x, y = self.record[self.index]
            self.draw_mesh(x, y)
            if self.index == 0:
                self.l_info.config(text="Not started")
            else:
                self.l_info.config(text="Black chess" if self.is_black else "White chess")
            self.is_black = not self.is_black
            self.index -= 1
            if self.index > 0:
                x, y = self.record[self.index]
                color = "white" if self.is_black else "black"
                self.draw_chess(x, y, color, "red")

        elif e.keycode == 39:
            if self.index == len(self.record) - 1:
                self.l_info.config(text="We have reached the end")
                return
            self.index += 1
            x, y = self.record[self.index]
            color = "black" if self.is_black else "white"
            self.draw_chess(x, y, color, "red")
            if self.index > 0:
                x, y = self.record[self.index - 1]
                color = "white" if self.is_black else "black"
                self.draw_chess(x, y, color)
            self.l_info.config(text="Black chess" if self.is_black else "White chess")
            self.is_black = not self.is_black
        else:
            pass

    # Draw a grid at x rows and Y columns
    def draw_mesh(self, x, y):
        # One magnification
        ratio = (1 - self.ratio) * 0.99 + 1
        center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
        # Draw the background color first
        self.c_chess.create_rectangle(center_y - self.step, center_x - self.step,
                                      center_y + self.step, center_x + self.step,
                                      fill=self.board_color, outline=self.board_color)
        # Then draw the grid line, where a B C D are different coefficients,
        # which are determined according to different positions of X and y, and need to be derived.
        a, b = [0, ratio] if y == 0 else [-ratio, 0] if y == self.row - 1 else [-ratio, ratio]
        c, d = [0, ratio] if x == 0 else [-ratio, 0] if x == self.column - 1 else [-ratio, ratio]
        self.c_chess.create_line(center_y + a * self.step, center_x, center_y + b * self.step, center_x)
        self.c_chess.create_line(center_y, center_x + c * self.step, center_y, center_x + d * self.step)

        # There are some special dots to draw small black dots
        if ((x == 3 or x == 11) and (y == 3 or y == 11)) or (x == 7 and y == 7):
            self.c_chess.create_oval(center_y - self.point_r, center_x - self.point_r,
                                     center_y + self.point_r, center_x + self.point_r, fill="black")

    # Draw the chess pieces at the X row and Y column, and color specifies the color of the chess pieces
    def draw_chess(self, x, y, color, outline="black"):
        center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
        # draw a circle
        self.c_chess.create_oval(center_y - self.chess_r, center_x - self.chess_r,
                                 center_y + self.chess_r, center_x + self.chess_r,
                                 fill=color, outline=outline)

    # Draw the whole chessboard
    def draw_board(self):
        [self.draw_mesh(x, y) for y in range(self.column) for x in range(self.row)]

    # Show text in the middle
    def center_show(self, text):
        width, height = int(self.c_chess['width']), int(self.c_chess['height'])
        self.c_chess.create_text(int(width / 2), int(height / 2), text=text, font=("黑体", 30, "bold"), fill="red")

    # At the beginning, set the status of each component and variable,
    # initialize the matrix, initialize the chessboard, and initialize the information


if __name__ == '__main__':
    Chess()