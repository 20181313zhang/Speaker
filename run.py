import sys
import threading
import time
from random import random

import keyboard
import cutscreen
import main
from PyQt5.QtWidgetAs import QApplication, QWidget, QPushButton
flag=0

def run():
    keyboard.wait('shift+a')
    cutscreen.cut()
    print("pppppp")
    main.mm()
    print("llll")



def dianji(self):
    global flag
    flag=flag+1
    while(1):
        bt.setEnabled(False)
        w.hide()
        QApplication.processEvents()
        run()



if __name__ == '__main__':
 # 创建QApplication实例
    app=QApplication(sys.argv)#获取命令行参数
    #创建一个窗口
    w=QWidget()
    #设置窗口的尺寸
    w.resize(250,50)#宽，高
    bt=QPushButton(w)
    strlist=["|ω･`)暗中观察","❛‿˂̵✧","✧˖°꒰๑'ꀾ'๑꒱°˖✧","₍˄·͈༝·͈˄₎◞","|(•_•) |•_•) |_•) |•) | )","ლ(•̀ _ •́ ლ)","꒰๑•⌓︎•๑꒱ᵎᵎᵎ","_(:з」∠)_","奥特曼( o|o)ノ三三三三三","─=≡Σ((( つ•̀ω•́)つ超人","(☆_☆)","(๑¯ ³ ¯๑)","＼(⌒∀⌒*)/","(o゜▽゜)o☆","(￢_￢)瞄","ヾ(✿ﾟ▽ﾟ)ノ","!!!∑(ﾟДﾟノ)ノ","(*^▽^*)","ლ(´ڡ`ლ)好吃的.","ᕙ༼ ͝°益° ༽ᕗ","(=￣ω￣=)喵了个咪","(눈‸눈)","(乂｀д´)哼","ʕ •ɷ•ʔฅ 晚安","(ﾉﾟ▽ﾟ)ﾉ","(≖ᴗ≖)✧","(★ᴗ★)","罒ω罒","ヽ(。>д<)ｐ","ლ(❛◡❛✿)ლ","｡◕ᴗ◕｡","(^_−)☆","（ゝω・）","凸(｀0´)凸","d=====(￣▽￣*)b 顶","(๑*◡*๑)","(((((ી(･◡･)ʃ)))))","(づ｡◕ᴗᴗ◕｡)づ","＜(▰˘◡˘▰)","╮(‵▽′)╭","(★＞U＜★)","Y(^o^)Y","(^.^)Y Ya!!","(!)_(!)","d(･｀ω´･d*)","( • ̀ω•́ )✧","ヾ(•ω•`。)","（ゝω・）","(・ω≦)","(・ω<)","(o´ω`o)ﾉ","(づ●─●)づ","ლ(́◉◞౪◟◉ლ)","(.ω.)","~(@^_^@)~"]
    bt.setText(""+strlist[int(len(strlist)*random())])
    bt.resize(250,50)
    bt.clicked.connect(dianji)

#移动窗口左上角坐标，其实就移动了窗口
    w.move(0,300)
    #设置窗口标题
    w.setWindowTitle('Speaker')
    #显示窗口
    from PyQt5.QtCore import Qt
    w.setWindowFlags(Qt.WindowStaysOnTopHint)
    w.show()
    '''
    进入程序主循环，循环扫描响应在窗口上的事件，让整个程序不会退出
    通过exit函数确保主循环安全结束
    '''
    sys.exit(app.exec_())

