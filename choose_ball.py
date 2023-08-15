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
    cur_dir = os.path.dirname(__file__)
    log_path = os.path.join(cur_dir, "info.log")
    logging.basicConfig(filename=log_path, level=logging.DEBUG, encoding='utf-8')
    logging.Formatter("%(asctime)s - %(message)s")

    # 设置页面
    tk_obj = Tk()
    tk_obj.iconbitmap(os.path.join(cur_dir,"ball.ico"))
    tk_obj.geometry('400x280')
    tk_obj.resizable(0, 0)
    tk_obj.config(bg='white')
    tk_obj.title('双色球选号助手')
    Label(tk_obj, text='欢迎来到双色球选号系统', font='宋体 20 bold', bg='white').pack()

    # 设置红球
    Label(tk_obj, font='宋体 15 bold', text='请输入您要选择的红球数量:', bg='white').place(x=50, y=60)
    red_ball_nums_str = StringVar()
    Entry(tk_obj, textvariable=red_ball_nums_str, width=2, font='宋体 12').place(x=210, y=60)
    
   
    # 设置蓝球
    Label(tk_obj, font='宋体 15 bold', text='请输入您要选择的蓝球数量:', bg='white').place(x=50, y=110)
    blue_ball_nums_str = StringVar()
    Entry(tk_obj, textvariable=blue_ball_nums_str, width=2, font='宋体 12').place(x=210, y=110)
    
    
    # 所需支付金额
    #amount = comb(red_ball_nums,6)*comb(blue_ball_nums,1)*2

    # Label(tk_obj, font='宋体 15 bold', text='请支付%s元'%amount, bg='white').place(x=50, y=110)
    # logging.info('需支付金额%s'%amount)

    def get_amount():
        red_ball_nums = int(red_ball_nums_str.get())
        logging.info('红球数量：%s'%red_ball_nums)
        blue_ball_nums = int(blue_ball_nums_str.get())
        logging.info('蓝球数量：%s'%blue_ball_nums)
        amount = comb(red_ball_nums,6)*comb(blue_ball_nums,1)*2


    # 开始
    Button(tk_obj, text='START', bd='5', command=get_amount, bg='green', font='宋体 10 bold').place(x=150, y=220)
    tk_obj.mainloop()

    # # 文件路径
    # cur_dir = os.path.dirname(__file__)
    # log_path = os.path.join(cur_dir, "info.log")
    # logging.basicConfig(filename=log_path, level=logging.DEBUG, encoding='utf-8')
    # # 欢迎语 
    # print('欢迎来到双色球选号系统！')
    # # 需要的红球和蓝球数量
    # red_ball_nums = int(input('请输入红球数量：'))
    # logging.info('红球数量：%s'%red_ball_nums)
    # blue_ball_nums = int(input('请输入蓝球数量：'))
    # logging.info('蓝球数量：%s'%blue_ball_nums)

    # # 所需金额
    # amount = comb(red_ball_nums,6)*comb(blue_ball_nums,1)*2
    # print('请支付%s元'%amount)
    # red_list = get_ball(red_ball_nums,'red')
    # blue_list = get_ball(blue_ball_nums,'blue')
    # res = red_list+blue_list
    # print('您选的号码为：\n%s'%res+'\n祝您中大奖!')
    # logging.info('所选号码为：%s'%res)




