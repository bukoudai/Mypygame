#!/usr/bin/env python

background_image_filename = "beijin1.jpg"
mouse_image_filename = "guangbiao1.png"
#指定图像文件名称

import sys
#向sys模块借一个exit函数用来退出程序
import pygame      
#导入pygame模块
from pygame.locals import *
#导入一些常用函数和常量



pygame.init()
#初始化pygame，为使用硬件做准备

screen = pygame.display.set_mode((1139,423),RESIZABLE,32)
#创建一个窗口
pygame.display.set_caption('我的游戏')
#设置标题

# 设置字体
font = pygame.font.SysFont("arial",16)
font_height = font.get_linesize()
event_text = []

bakground = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#加载并转换图像

while True:
#游戏主程序
    for event in pygame.event.get():
    	if event.type == QUIT:
    	#接受的退出事件后退出程序
    	    pygame.quit();
    	    sys.exit()
			
    
    screen.blit(bakground,(0,0))
    #将背景画上去

    x,y = pygame.mouse.get_pos()
    #获取光标位置
    x-= mouse_cursor.get_width()/2
    y-=mouse_cursor.get_height()/2
    #计算光标的左上角位置
    screen.blit(mouse_cursor,(x,y))
    #把光标画上去

    pygame.display.update()
    #刷新窗口
    

    	    
