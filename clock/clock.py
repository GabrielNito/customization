from datetime import datetime
import time 
import os
from getpass import getpass

colon = ["        ", "        ", "   \x1b[37m/\x1b[35m$$  ", "  \x1b[37m|__/  ", "        ", "   \x1b[37m/\x1b[35m$$  ", "  \x1b[37m|__/  ", "        "]
numbers = [
  ["  \x1b[37m/\x1b[35m$$$$$$ "," \x1b[37m/\x1b[35m$$$\x1b[37m_  \x1b[35m$$","\x1b[37m| \x1b[35m$$$$\x1b[37m\ \x1b[35m$$","\x1b[37m| \x1b[35m$$ $$ $$","\x1b[37m| \x1b[35m$$\x1b[37m\ \x1b[35m$$$$","\x1b[37m| \x1b[35m$$ \x1b[37m\ \x1b[35m$$$","\x1b[37m|  \x1b[35m$$$$$$\x1b[37m/"," \x1b[37m\______/ "],
  ["    \x1b[37m/\x1b[35m$$   ","  \x1b[37m/\x1b[35m$$$$   "," \x1b[37m|_  \x1b[35m$$   ","   \x1b[37m| \x1b[35m$$   ","   \x1b[37m| \x1b[35m$$   ","   \x1b[37m| \x1b[35m$$   "," \x1b[37m/\x1b[35m$$$$$$$ "," \x1b[37m|______/ "],
  ["  \x1b[37m/\x1b[35m$$$$$$ "," \x1b[37m/\x1b[35m$$\x1b[37m__  \x1b[35m$$","\x1b[37m|__/  \ \x1b[35m$$","  \x1b[37m/\x1b[35m$$$$$$\x1b[37m/"," \x1b[37m/\x1b[35m$$\x1b[37m____/ ","\x1b[37m| \x1b[35m$$      ","\x1b[37m| \x1b[35m$$$$$$$$","\x1b[37m|________/"],
  ["  \x1b[37m/\x1b[35m$$$$$$ "," \x1b[37m/\x1b[35m$$\x1b[37m__  \x1b[35m$$","\x1b[37m|__/  \ \x1b[35m$$","   \x1b[37m/\x1b[35m$$$$$\x1b[37m/","  \x1b[37m|___  \x1b[35m$$"," \x1b[37m/\x1b[35m$$  \x1b[37m\ \x1b[35m$$","\x1b[37m|  \x1b[35m$$$$$$\x1b[37m/"," \x1b[37m\______/ "],
  [" \x1b[37m/\x1b[35m$$   \x1b[37m/\x1b[35m$$","\x1b[37m| \x1b[35m$$  \x1b[37m| \x1b[35m$$","\x1b[37m| \x1b[35m$$  \x1b[37m| \x1b[35m$$","\x1b[37m| \x1b[35m$$$$$$$$","\x1b[37m|_____  \x1b[35m$$","      \x1b[37m| \x1b[35m$$","      \x1b[37m| \x1b[35m$$","      \x1b[37m|__/"],
  [" \x1b[37m/\x1b[35m$$$$$$$ ","\x1b[37m| \x1b[35m$$\x1b[37m____/ ","\x1b[37m| \x1b[35m$$      ","\x1b[37m| \x1b[35m$$$$$$$ ","\x1b[37m|_____  \x1b[35m$$"," \x1b[37m/\x1b[35m$$  \x1b[37m\ \x1b[35m$$","\x1b[37m|  \x1b[35m$$$$$$\x1b[37m/"," \x1b[37m\______/ "],
  ["  \x1b[37m/\x1b[35m$$$$$$ "," \x1b[37m/\x1b[35m$$\x1b[37m__  \x1b[35m$$","\x1b[37m| \x1b[35m$$  \x1b[37m\__/","\x1b[37m| \x1b[35m$$$$$$$ ","\x1b[37m| \x1b[35m$$\x1b[37m__  \x1b[35m$$","\x1b[37m| \x1b[35m$$  \x1b[37m\ \x1b[35m$$","\x1b[37m|  \x1b[35m$$$$$$\x1b[37m/"," \x1b[37m\______/ "],
  [" \x1b[37m/\x1b[35m$$$$$$$$","\x1b[37m|_____ \x1b[35m$$\x1b[37m/","     \x1b[37m/\x1b[35m$$\x1b[37m/ ","    \x1b[37m/\x1b[35m$$\x1b[37m/  ","   \x1b[37m/\x1b[35m$$\x1b[37m/   ","  \x1b[37m/\x1b[35m$$\x1b[37m/    "," \x1b[37m/\x1b[35m$$\x1b[37m/     ","\x1b[37m|__/      "],
  ["  \x1b[37m/\x1b[35m$$$$$$ "," \x1b[37m/\x1b[35m$$\x1b[37m__  \x1b[35m$$","\x1b[37m| \x1b[35m$$  \x1b[37m\ \x1b[35m$$","\x1b[37m|  \x1b[35m$$$$$$\x1b[37m/"," \x1b[37m>\x1b[35m$$\x1b[37m__  \x1b[35m$$","\x1b[37m| \x1b[35m$$  \x1b[37m\ \x1b[35m$$","\x1b[37m|  \x1b[35m$$$$$$\x1b[37m/"," \x1b[37m\______/ "],
  ["  \x1b[37m/\x1b[35m$$$$$$ "," \x1b[37m/\x1b[35m$$\x1b[37m__  \x1b[35m$$","\x1b[37m| \x1b[35m$$  \x1b[37m\ \x1b[35m$$","\x1b[37m|  \x1b[35m$$$$$$$"," \x1b[37m\____  \x1b[35m$$"," \x1b[37m/\x1b[35m$$  \x1b[37m\ \x1b[35m$$","\x1b[37m|  \x1b[35m$$$$$$\x1b[37m/"," \x1b[37m\______/ "]
]

def printNumber():
  now = datetime.now()
  hour = list(now.strftime("%H%M%S"))
  resultado = list()
  for i in range(8):
    string = "                                                        "
    string += numbers[int(hour[0])][i]
    string += numbers[int(hour[1])][i]
    string += colon[i]
    string += numbers[int(hour[2])][i]
    string += numbers[int(hour[3])][i]
    string += colon[i]
    string += numbers[int(hour[4])][i]
    string += numbers[int(hour[5])][i]
    resultado.append(string)
  
  for i in range(len(resultado)):
    print(resultado[i])

while(True):
  os.system("clear")
  for i in range(9):
    print()
  printNumber()
  time.sleep(1)