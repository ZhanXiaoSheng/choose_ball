#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   choose_ball.py
@Time    :   2023/08/15 08:49:51
@Author  :   zhangsheng 
@Version :   1.0
@Desc    :   选号
'''

# here put the import lib

import random 
from scipy.special import comb
import logging
import os
from tkinter import *
from PIL import Image,ImageTk
import sys


def get_ball(num,color):
    list=[]
    if color=='red':
        b=33
    else :
        b=16
    a=0
    while a<num:
        ball = random.randint(1,b)
        if ball not in list:
            list.append(ball)
            a+=1
    list.sort()
    return list


if __name__=="__main__":

    # 文件路径
    #cur_dir = os.path.dirname(sys.executable)
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    #cur_dir = os.getcwd()
    log_path = os.path.join(cur_dir, "info.log")
    logging.basicConfig(filename=log_path, 
                        level=logging.DEBUG,
                        encoding='utf-8',
                        format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                        datefmt='%a %d %b %Y %H:%M:%S')

    # 设置页面
    tk_obj = Tk()
    im = Image.open(os.path.join(cur_dir,"ball.png"))
    photo = ImageTk.PhotoImage(im)
    tk_obj.wm_iconphoto(True,photo)
    #tk_obj.iconbitmap(os.path.join(cur_dir,"ball.ico"))
    tk_obj.geometry('400x400')
    tk_obj.resizable(0, 0)
    tk_obj.config(bg='white')
    tk_obj.title('双色球助手')
    Label(tk_obj, text='双色球选号系统', font='宋体 15 bold', bg='white').place(x=100, y=20)

    #设置说明
    Label(tk_obj, text='玩法说明：', fg='red',font='宋体 7 bold', bg='white').place(x=40, y=60)
    Label(tk_obj, text='红球数不少于6,蓝球数不少于1',fg='red', font='宋体 7 bold', bg='white').place(x=40, y=75)
    # 设置红球
    Label(tk_obj, font='宋体 12 bold', text='请输入您要选择的红球数量:', bg='white').place(x=30, y=100)
    red_ball_nums_str = StringVar()
    Entry(tk_obj, textvariable=red_ball_nums_str, width=3, font='宋体 12').place(x=250, y=100)
    
   
    # 设置蓝球
    Label(tk_obj, font='宋体 12 bold', text='请输入您要选择的蓝球数量:', bg='white').place(x=30, y=130)
    blue_ball_nums_str = StringVar()
    Entry(tk_obj, textvariable=blue_ball_nums_str, width=3, font='宋体 12').place(x=250, y=130)
    # 选择支付方式
    def pay_photo():
        dict={1:os.path.join(cur_dir,"wechatpay.png"),2:os.path.join(cur_dir,"alipay.png")}
        img_path = dict.get(v.get())
        global image
        # 使用全局变量 防止图片不显示
        image = Image.open(img_path).resize((250,300))
        imgx = ImageTk.PhotoImage(image)
        Label(tk_obj,image=imgx).place(x=50,y=50).pack()
        #label3.grid(row=1, column=1, sticky=W + E + N + S, padx=10, pady=10) #sticky=W + E + N + S 表示填充控件

    v=IntVar()
    # 所需支付金额
    def get_amount():
        red_ball_nums = int(red_ball_nums_str.get())
        logging.info('红球数量：%s'%red_ball_nums)
        blue_ball_nums = int(blue_ball_nums_str.get())
        logging.info('蓝球数量：%s'%blue_ball_nums)
        amount = comb(red_ball_nums,6)*comb(blue_ball_nums,1)*2
        # 生成一组号码
        red_list = get_ball(red_ball_nums,'red')
        blue_list = get_ball(blue_ball_nums,'blue')
        res = red_list+blue_list
        logging.info('所选号码为：%s'%res)
        Label(tk_obj, font='宋体 12 bold', text='您选的号码为:', bg='white').place(x=30, y=160)
        Label(tk_obj, font='楷体 15 bold', text='%s'%res, bg='red').place(x=10, y=200)
        Label(tk_obj, font='宋体 13 bold',fg='red', text='祝您中大奖!', bg='white').place(x=150, y=240)

        Label(tk_obj, font='宋体 16 bold',fg='blue', text='需支付人民币:%s元'%amount, bg='white').place(x=100, y=270)
        Label(tk_obj, font='宋体 10 bold', text='请选择支付方式:微信/支付宝', bg='white').place(x=10, y=310)

        pay()

    def pay():    
        pay_way=[('微信',1),('支付宝',2)]
        for name,num in pay_way:
            radio_button = Radiobutton(tk_obj,text=name,variable=v,value=num,command=pay_photo)
            radio_button.pack(anchor='w')


    # 开始
    Button(tk_obj, text='START', bd='5', command=get_amount, bg='green', font='宋体 10 bold').place(x=150, y=350)
    tk_obj.mainloop()





