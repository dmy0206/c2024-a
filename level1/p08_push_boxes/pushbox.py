import tkinter as tk
class Game:
    def __init__(self):
        self.window = tk.Tk()

        self.rows = 5
        self.cols = 5

        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()

        # 定义游戏地图，0表示空地，1表示墙，2表示箱子，3表示目标点，4表示玩家
        self.map = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 3, 0, 1],
            [1, 1, 1, 1, 1]
        ]

        self.player_x = 1
        self.player_y = 1

        self.draw_map()

        self.window.bind("<Up>", self.move_up)
        self.window.bind("<Down>", self.move_down)
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)

    def draw_map(self):
        # 绘制游戏地图
        cell_size = 80
        for i in range(self.rows):
            for j in range(self.cols):
                x = j * cell_size
                y = i * cell_size
                if self.map[i][j] == 1:
                    self.canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill='gray')
                elif self.map[i][j] == 2:
                    self.canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill='blue')
                elif self.map[i][j] == 3:
                    self.canvas.create_oval(x + 20, y + 20, x + 60, y + 60, fill='yellow')
                elif self.map[i][j] == 0:
                    self.canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill='white')

                if i == self.player_y and j == self.player_x:
                    self.canvas.create_oval(x + 30, y + 30, x + 50, y + 50, fill='red')

    def move_up(self, event):
        new_y = self.player_y - 1
        if self.can_move(new_y, self.player_x):
            self.player_y = new_y
            self.update_map()

    def move_down(self, event):
        new_y = self.player_y + 1
        if self.can_move(new_y, self.player_x):
            self.player_y = new_y
            self.update_map()

    def move_left(self, event):
        new_x = self.player_x - 1
        if self.can_move(self.player_y, new_x):
            self.player_x = new_x
            self.update_map()

    def move_right(self, event):
        new_x = self.player_x + 1
        if self.can_move(self.player_y, new_x):
            self.player_x = new_x
            self.update_map()

    def can_move(self, new_y, new_x):
        if self.map[new_y][new_x] == 1:  # 若为墙，不可移动
            return False
        elif self.map[new_y][new_x] == 2:  # 若为箱子
            box_y = new_y
            box_x = new_x
            if new_y == self.player_y:
                if new_x < self.player_x:
                    box_x -= 1
                else:
                    box_x += 1
            else:
                if new_y < self.player_y:
                    box_y -= 1
                else:
                    box_y += 1

            if box_x < 0 or box_x >= self.cols or box_y < 0 or box_y >= self.rows or self.map[box_y][box_x]!= 0:
                return False
            else:
                self.move_box(box_y, box_x)
        return True

    def move_box(self, box_y, box_x):
        self.map[box_y][box_x] = 2
        self.map[self.player_y][self.player_x] = 0
        self.player_y = box_y
        self.player_x = box_x

    def update_map(self):
        self.canvas.delete("all")
        self.draw_map()


if __name__ == '__main__':
    game = Game()
    tk.mainloop()