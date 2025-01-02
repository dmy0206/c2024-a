from graphics import *
from wx.lib.agw.ribbon import panel
from graphics import *
from math import *
import numpy as np
from numpy.ma.core import count
import wx
from wx import *
GRID_WIDTH =60

COLUMN = 15
ROW = 15

list1 = []  # AI
list2 = []  # human
list3 = []  # all

list_all = []  # 整个棋盘的点
next_point = [0, 0]  # AI下一步最应该下的位置

ratio = 1  # 进攻的系数   大于1 进攻型，  小于1 防守型
DEPTH = 1  # 搜索深度   只能是单数。  如果是负数， 评估函数评估的的是自己多少步之后的自己得分的最大值，并不意味着是最好的棋， 评估函数的问题


# 棋型的评估分数
shape_score = [(50, (0, 1, 1, 0, 0)),
               (50, (0, 0, 1, 1, 0)),
               (200, (1, 1, 0, 1, 0)),
               (500, (0, 0, 1, 1, 1)),
               (500, (1, 1, 1, 0, 0)),
               (5000, (0, 1, 1, 1, 0)),
               (5000, (0, 1, 0, 1, 1, 0)),
               (5000, (0, 1, 1, 0, 1, 0)),
               (5000, (1, 1, 1, 0, 1)),
               (5000, (1, 1, 0, 1, 1)),
               (5000, (1, 0, 1, 1, 1)),
               (5000, (1, 1, 1, 1, 0)),
               (5000, (0, 1, 1, 1, 1)),
               (50000, (0, 1, 1, 1, 1, 0)),
               (99999999, (1, 1, 1, 1, 1))]
GRID_WIDTH =50
COLUMN=10
ROW=10
#下面均为测试过程中的部分程序，直接跳过，因为我是第一次用wxpython库
'''def guidraw():
    win = GraphWin("wuziqi", GRID_WIDTH * COLUMN, GRID_WIDTH * ROW)
    win.setBackground("white")
    i1 = 0

    while i1 <= GRID_WIDTH * COLUMN:
        l = Line(Point(i1, 0), Point(i1, GRID_WIDTH * COLUMN))
        l.draw(win)
        i1 = i1 + GRID_WIDTH
    i2 = 0

    while i2 <= GRID_WIDTH * ROW:
        l = Line(Point(0, i2), Point(GRID_WIDTH * ROW, i2))
        l.draw(win)
        i2 = i2 + GRID_WIDTH
    return win
def createpoint():
    p2 = win.getMouse()
    a2 = round((p2.getX()) / GRID_WIDTH)
    b2 = round((p2.getY()) / GID_WIDTH)
    piece = Circle(Point(GRID_WRIDTH * a2, GRID_WIDTH * b2), 16)
    piece.setFill('red')
    piece.draw(win)
win = guidraw()
while True:
    createpoint()
win.mainloop()
win.close()'''
'''class MyFrame(wx.Frame):
    def __init__(self, parent,title):
        wx.Frame.__init__(self, parent, title=title,size=(500, 500))
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="button")
        self.Bind(wx.EVT_BUTTON, self.OnButton, self.button)
        self.textctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.Show(True)
        #self.InitUI()
        btn=wx.Button(self.panel,label="renkun")
        self.Bind(wx.EVT_BUTTON, self.OnButton, btn)
        #self.textctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        #self.Centre(wx.BOTH)
    def InitUI(self):
        panel = wx.Panel(self.panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        char=wx.StaticText(panel,label="djshuauihduhudhuaishudi")
        hbox.Add(char,proportion=1,flag=wx.EXPAND)
        hbox2.Add(hbox,proportion=1,flag=wx.EXPAND)
        btn1=wx.Button(panel,label="renkun")
        btn2=wx.Button(panel,label="renren")
        hbox2.Add(btn1,proportion=0)
        hbox2.Add(btn2,proportion=0,flag=wx.LEFT|wx.BOTTOM,border=3)
        vbox.Add(hbox2,proportion=0,flag=wx.ALIGN_RIGHT|wx.RIGHT,border=10)
        panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)
        vbox=wx.BoxSizer(wx.VERTICAL)
        hbox=wx.BoxSizer(wx.HORIZONTAL)
        #text=wx.StaticText(panel,label="text")
        hbox.Add(wx.Button(panel,label="button"),proportion=1,flag=wx.LEFT|wx.BOTTOM,border=5)
        btn=wx.Button(panel,label="button")
        btn=wx.Button(panel,label="button")
        self.Bind(wx.EVT_BUTTON,self.OnButton,btn)
        self.Centre()
        self.Show(True)
    def OnButton(self, event):
        wx.MessageBox("Hello World")'''
#以上均为测试程序，直接跳过即可
def ai():
    global cut_count
    cut_count = 0
    global search_count
    search_count = 0
    negamax(True, DEPTH, -99999999, 99999999)

    return next_point[0], next_point[1]


def negamax(is_ai, depth, alpha, beta):
    if game_win(list1) or game_win(list2) or depth == 0:
        return evaluation(is_ai)

    blank_list = list(set(list_all).difference(set(list3)))
    order(blank_list)
    for next_step in blank_list:

        global search_count
        search_count += 1

        # 如果要评估的位置没有相邻的子， 则不去评估  减少计算
        if not has_neighbor(next_step):
            continue

        if is_ai:
            list1.append(next_step)
        else:
            list2.append(next_step)
        list3.append(next_step)

        value = -negamax(not is_ai, depth - 1, -beta, -alpha)
        if is_ai:
            list1.remove(next_step)
        else:
            list2.remove(next_step)
        list3.remove(next_step)

        if value > alpha:

            '''print(str(value) + "alpha:" + str(alpha) + "beta:" + str(beta))
            print(list3)'''
            if depth == DEPTH:
                next_point[0] = next_step[0]
                next_point[1] = next_step[1]
            # alpha + beta剪枝点
            if value >= beta:
                global cut_count
                cut_count += 1
                return beta
            alpha = value

    return alpha


#  离最后落子的邻居位置最有可能是最优点
def order(blank_list):
    last_pt = list3[-1]
    for item in blank_list:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (last_pt[0] + i, last_pt[1] + j) in blank_list:
                    blank_list.remove((last_pt[0] + i, last_pt[1] + j))
                    blank_list.insert(0, (last_pt[0] + i, last_pt[1] + j))


def has_neighbor(pt):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (pt[0] + i, pt[1]+j) in list3:
                return True
    return False

def check_four():
    for i in list1:
        stack=[]
        p=[]
        top=[]
        if list1[i][0] not in p:
            p.append(list1[i][0])
            stack.append(list1[i])

def evaluation(is_ai):
    total_score = 0

    if is_ai:
        my_list = list1
        enemy_list = list2
    else:
        my_list = list2
        enemy_list = list1

    # 算自己的得分
    score_all_arr = []  # 得分形状的位置 用于计算如果有相交 得分翻倍
    my_score = 0
    for pt in my_list:
        m = pt[0]
        n = pt[1]
        my_score += cal_score(m, n, 0, 1, enemy_list, my_list, score_all_arr)
        my_score += cal_score(m, n, 1, 0, enemy_list, my_list, score_all_arr)
        my_score += cal_score(m, n, 1, 1, enemy_list, my_list, score_all_arr)
        my_score += cal_score(m, n, -1, 1, enemy_list, my_list, score_all_arr)

    #  算敌人的得分， 并减去
    score_all_arr_enemy = []
    enemy_score = 0
    for pt in enemy_list:
        m = pt[0]
        n = pt[1]
        enemy_score += cal_score(m, n, 0, 1, my_list, enemy_list, score_all_arr_enemy)
        enemy_score += cal_score(m, n, 1, 0, my_list, enemy_list, score_all_arr_enemy)
        enemy_score += cal_score(m, n, 1, 1, my_list, enemy_list, score_all_arr_enemy)
        enemy_score += cal_score(m, n, -1, 1, my_list, enemy_list, score_all_arr_enemy)

    total_score = my_score - enemy_score*ratio*0.1

    return total_score


# 每个方向上的分值计算
def cal_score(m, n, x_decrict, y_derice, enemy_list, my_list, score_all_arr):
    add_score = 0  # 加分项
    # 在一个方向上， 只取最大的得分项
    max_score_shape = (0, None)

    # 如果此方向上，该点已经有得分形状，不重复计算
    for item in score_all_arr:
        for pt in item[1]:
            if m == pt[0] and n == pt[1] and x_decrict == item[2][0] and y_derice == item[2][1]:
                return 0

    # 在落子点 左右方向上循环查找得分形状
    for offset in range(-5, 1):
        # offset = -2
        pos = []
        for i in range(0, 6):
            if (m + (i + offset) * x_decrict, n + (i + offset) * y_derice) in enemy_list:
                pos.append(2)
            elif (m + (i + offset) * x_decrict, n + (i + offset) * y_derice) in my_list:
                pos.append(1)
            else:
                pos.append(0)
        tmp_shap5 = (pos[0], pos[1], pos[2], pos[3], pos[4])
        tmp_shap6 = (pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

        for (score, shape) in shape_score:
            if tmp_shap5 == shape or tmp_shap6 == shape:
                #if tmp_shap5 == (1,1,1,1,1):
                #   print('wwwwwwwwwwwwwwwwwwwwwwwwwww')
                if score > max_score_shape[0]:
                    max_score_shape = (score, ((m + (0+offset) * x_decrict, n + (0+offset) * y_derice),
                                               (m + (1+offset) * x_decrict, n + (1+offset) * y_derice),
                                               (m + (2+offset) * x_decrict, n + (2+offset) * y_derice),
                                               (m + (3+offset) * x_decrict, n + (3+offset) * y_derice),
                                               (m + (4+offset) * x_decrict, n + (4+offset) * y_derice)), (x_decrict, y_derice))

    # 计算两个形状相交， 如两个3活 相交， 得分增加 一个子的除外
    if max_score_shape[1] is not None:
        for item in score_all_arr:
            for pt1 in item[1]:
                for pt2 in max_score_shape[1]:
                    if pt1 == pt2 and max_score_shape[0] > 10 and item[0] > 10:
                        add_score += item[0] + max_score_shape[0]

        score_all_arr.append(max_score_shape)

    return add_score + max_score_shape[0]


def game_win(list):
    for m in range(COLUMN+1):
        for n in range(ROW+1):

            if n < ROW - 4 and (m, n) in list and (m, n + 1) in list and (m, n + 2) in list and (
                    m, n + 3) in list and (m, n + 4) in list:
                return True
            elif m < ROW - 4 and (m, n) in list and (m + 1, n) in list and (m + 2, n) in list and (
                    m + 3, n) in list and (m + 4, n) in list:
                return True
            elif m < ROW - 4 and n < ROW - 4 and (m, n) in list and (m + 1, n + 1) in list and (
                    m + 2, n + 2) in list and (m + 3, n + 3) in list and (m + 4, n + 4) in list:
                return True
            elif m < ROW - 4 and n > 3 and (m, n) in list and (m + 1, n - 1) in list and (
                    m + 2, n - 2) in list and (m + 3, n - 3) in list and (m + 4, n - 4) in list:
                return True

    return False


def gobangwin():
    win = GraphWin("wuziqi", GRID_WIDTH * COLUMN, GRID_WIDTH * ROW)
    win.setBackground("white")
    i1 = 0

    while i1 <= GRID_WIDTH * COLUMN:
        l = Line(Point(i1, 0), Point(i1, GRID_WIDTH * COLUMN))
        l.draw(win)
        i1 = i1 + GRID_WIDTH
    i2 = 0

    while i2 <= GRID_WIDTH * ROW:
        l = Line(Point(0, i2), Point(GRID_WIDTH * ROW, i2))
        l.draw(win)
        i2 = i2 + GRID_WIDTH
    return win
def check():
    for m in range(list_all):
        if list_all[m] == 1 and list_all[m + 1] == 1 and list_all[m + 2] == 1:
            list_all.append([list_all[m], list_all[m + 1]])
        else:
            continue

def main():
    win = gobangwin()

    for i in range(COLUMN+1):
        for j in range(ROW+1):
            list_all.append((i, j))

    change = 0
    g = 0
    m = 0
    n = 0

    while g == 0:

        if change % 2 == 1:
            pos = ai()

            if pos in list3:
                message = Text(Point(200, 200), "???" + str(pos[0]) + "," + str(pos[1]))
                message.draw(win)
                g = 1

            list1.append(pos)
            list3.append(pos)

            piece = Circle(Point(GRID_WIDTH * pos[0], GRID_WIDTH * pos[1]), 16)
            piece.setFill('black')
            piece.draw(win)

            if game_win(list1):
                message = Text(Point(100, 100), "black win.")
                message.setSize(20)
                message.draw(win)
                g = 1
            change = change + 1

        else:
            p2 = win.getMouse()
            if not ((round((p2.getX()) / GRID_WIDTH), round((p2.getY()) / GRID_WIDTH)) in list3):

                a2 = round((p2.getX()) / GRID_WIDTH)
                b2 = round((p2.getY()) / GRID_WIDTH)
                list2.append((a2, b2))
                list3.append((a2, b2))

                piece = Circle(Point(GRID_WIDTH * a2, GRID_WIDTH * b2), 16)
                piece.setFill('red')
                piece.draw(win)
                if game_win(list2):
                    message = Text(Point(100, 100), "red win.")
                    message.setSize(20)
                    message.draw(win)
                    g = 1

                change = change + 1

    message = Text(Point(400, 400), "Game over")
    message.setSize(36)
    message.draw(win)
    win.getMouse()
    win.close()
class MyFrame2(wx.Frame):
    def __init__(self, parent,title):
        super(MyFrame2,self).__init__(parent, title=title,size=(500, 500))
        self.InitUI()
    def InitUI(self):
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        st=wx.StaticText(self.panel,label="欢迎来到jjh的无敌五子棋")
        hbox.Add(st,proportion=1,flag=wx.EXPAND)
        vbox.Add(hbox,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM,border=10)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        btn1=wx.Button(self.panel,label="人机对战")
        btn2=wx.Button(self.panel,label="人人对战")
        btn3=wx.Button(self.panel,label='ai vs ai')
        hbox2.Add(btn1,proportion=0)
        hbox2.Add(btn2,proportion=0,flag=wx.LEFT|wx.BOTTOM,border=10)
        hbox2.Add(btn3,proportion=0,flag=wx.LEFT|wx.BOTTOM,border=5)
        vbox.Add(hbox2,flag=wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM,border=10)
        self.panel.SetSizer(vbox)
        #self.Button = wx.Button(self.panel, label="button")
        self.Bind(wx.EVT_BUTTON,self.OnButton,btn1)
        self.Bind(wx.EVT_BUTTON,self.OnButton2,btn2)
        self.Bind(wx.EVT_BUTTON,self.OnButton3,btn3)
        self.Centre()
    def OnButton(self, event):
        self.run()
    def run(self):
        main()
    def OnButton2(self, event):
        def guidraw():
            win = GraphWin("wuziqi", GRID_WIDTH * COLUMN, GRID_WIDTH * ROW)
            win.setBackground("white")
            i1 = 0

            while i1 <= GRID_WIDTH * COLUMN:
                l = Line(Point(i1, 0), Point(i1, GRID_WIDTH * COLUMN))
                l.draw(win)
                i1 = i1 + GRID_WIDTH
            i2 = 0

            while i2 <= GRID_WIDTH * ROW:
                l = Line(Point(0, i2), Point(GRID_WIDTH * ROW, i2))
                l.draw(win)
                i2 = i2 + GRID_WIDTH
            return win

        def createpoint():
            p2 = win.getMouse()
            a2 = round((p2.getX()) / GRID_WIDTH)
            b2 = round((p2.getY()) / GRID_WIDTH)
            piece = Circle(Point(GRID_WIDTH * a2, GRID_WIDTH * b2), 16)
            piece.setFill('red')
            piece.draw(win)

        win = guidraw()
        while True:
            createpoint()
        win.mainloop()
        win.close()

    def OnButton3(self, event):
        wx.MessageBox("过几天再弄")
app=wx.App(False)
dog=MyFrame2(None,"Dog")
dog.Show(True)
app.MainLoop()
