# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('简易五子棋')        #窗口标题
root.resizable(False, False)    #固定窗口大小
windowWidth = 840               #获得当前窗口宽
windowHeight = 660              #获得当前窗口高
screenWidth,screenHeight = root.maxsize()     #获得屏幕宽和高
geometryParam = '%dx%d+%d+%d'%(windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight - windowHeight)/2)
root.geometry(geometryParam)    #设置窗口大小及偏移坐标

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# 创建一个Canvas，设置其背景色为白色
cv = tk.Canvas(root,width =660,height=660,bg = 'white')

# 创建一个矩形，坐标为(30,30,630,630)
cv.create_rectangle(30,30,630,630)

user = 1 
board = np.zeros((21,21))

def paint(event):
    global user
    global board
    if user == 1:
        color = 'black'
    elif user == -1:
        color = 'white'
    x = round(event.x/30)
    y = round(event.y/30)
    if x >= 1 and x <= 21 and y >= 1 and y <= 21 and board[(x-1),(y-1)] == 0: 
        x1,y1 = (x*30-10),(y*30-10)
        x2,y2 = (x*30+10),(y*30+10)
        cv.create_oval(x1,y1,x2,y2,fill=color)
        board[(x-1),(y-1)] = user
        
        count = 1
        # 向右搜索
        for i in range(5):
            if x ==  21:
                break
            if board[(x-1+(i+1)),(y-1)] == user:
                count += 1
            else:
                break
        # 向左搜索
        for i in range(5):
            if x == 1:
                break
            if board[(x-1-(i+1)),(y-1)] == user:
                count += 1
            else:
                break
        if count >= 5:
            messagebox.showinfo('','Game over, %s win' % color)
            
        count = 1
        # 向下搜索
        for i in range(5):
            if y == 21:
                break
            if board[(x-1),(y-1+(i+1))] == user:
                count += 1
            else:
                break
        # 向上搜索
        for i in range(5):
            if y == 1:
                break
            if board[(x-1),(y-1-(i+1))] == user:
                count += 1
            else:
                break
        if count >= 5:
            messagebox.showinfo('','Game over, %s win' % color)
            
        count = 1
        # 向右下搜索
        for i in range(5):
            if x == 21 or y == 21:
                break
            if board[(x-1+(i+1)),(y-1+(i+1))] == user:
                count += 1
            else:
                break
        # 向左上搜索
        for i in range(5):
            if x == 1 or y == 1:
                break
            if board[(x-1-(i+1)),(y-1-(i+1))] == user:
                count += 1
            else:
                break
        if count >= 5:
            messagebox.showinfo('','Game over, %s win' % color)
            
        count = 1
        # 向右上搜索
        for i in range(5):
            if x == 21 or y == 1:
                break
            if board[(x-1+(i+1)),(y-1-(i+1))] == user:
                count += 1
            else:
                break
        # 向左下搜索
        for i in range(5):
            if x == 1 or y == 21:
                break
            if board[(x-1-(i+1)),(y-1+(i+1))] == user:
                count += 1
            else:
                break
        if count >= 5:
            messagebox.showinfo('','Game over, %s win' % color)

        user = -user
    
cv.bind('<Button-1>',paint)

cv.place(x=0,y=0)

for i in range(1,21):
    if i % 2 == 0:
        cv.create_line((30,i*30),(630,i*30),width=1,dash=(4,4))#制作一条水平线
        cv.create_line((i*30,30),(i*30,630),width=1,dash=(4,4))#制作一条竖直线
    else:
        cv.create_line((30,i*30),(630,i*30),width=1)#制作一条水平线
        cv.create_line((i*30,30),(i*30,630),width=1)#制作一条竖直线

btn1=tk.Button(root,text='重玩',cursor='hand2',height=2,width=8,relief='ridge',highlightbackground='white',fg='gray')
btn1.place(x=700,y=100)

btn2=tk.Button(root,text='悔棋',cursor='hand2',height=2,width=8,relief='ridge',highlightbackground='white',fg='gray')
btn2.place(x=700,y=150)

btn3=tk.Button(root,text='认输',cursor='hand2',height=2,width=8,relief='ridge',highlightbackground='white',fg='gray')
btn3.place(x=700,y=200)
    
root.mainloop()

