#!/usr/bin/env python

import pygame
from pygame.locals import*
import sys

pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)

font = pygame.font.SysFont('arial',16);
font_height = font.get_linesize()
event_text = []

while True:

	event = pygame.event.wait()
	event_text.append(str(event))
	#获取时间的名称
	event_text = event_text[-SCREEN_SIZE[1]:font_height:]
	#这个切片操作保证了event_text里面只有一个屏幕的文字

	if event.type == QUIT:
		pygame.quit();
		sys.exit()

	screen.fill((255,255,255))

	y = SCREEN_SIZE[1]-font_height
	#设定一个合适的起笔位置，从最下面开始但要留一行空
	for text in reversed(event_text):
		screen.blit(font.render(text,True,(0,255,0)),(0,y))
		#????
		y -= font_height
		#把笔提一行

	pygame.display.update()
