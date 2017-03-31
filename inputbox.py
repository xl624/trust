# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message,x,y,color,font,fontSize,backColor):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(font,fontSize)
  if len(message) != 0:
    pygame.draw.rect(screen,backColor,[x,y,screen.get_width(),fontSize])
    screen.blit(fontobject.render(message, 1, color),(x,y))
  pygame.display.flip()

def ask(screen, question,x,y,color,font,fontSize,backColor):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": ",x,y,color,font,fontSize,backColor)
  display_box(screen, string.join(current_string,""),x,y+fontSize,color,font,fontSize,backColor)
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
      pygame.draw.rect(screen,backColor,[x,y+fontSize*1.2,screen.get_width(),fontSize])
      display_box(screen, string.join(current_string,""),x,y+fontSize*1.2,color,font,fontSize,backColor)
    elif inkey == K_RETURN:
      break
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": ",x,y,color,font,fontSize,backColor)
    display_box(screen, string.join(current_string,""),x,y+fontSize*1.2,color,font,fontSize,backColor)
  return string.join(current_string,"")

def main():
  screen = pygame.display.set_mode((320,240))
  print ask(screen, message,x,y,color,font,fontSize,backColor) + " was entered"

if __name__ == '__main__': main()
