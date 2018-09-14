import chess
import sys
import threading
import time

name = "Brothfish"
author = "Alain Lou"

board = chess.Board()

def uciHandler(message):
    if message[1] == "position":
        loadPositionOnto(board)

def processMessages():
    message = input().split()
    print("haha")
    if message[0] == "stop":
        return False
#        sys.exit()
    elif message[0] == "uci":
        uciHandler(message)
        return True
    return True

thread1 = threading.Thread(target=processMessages)
thread1.daemon = True
thread1.start()

while True:
    status = processMessages()
    if not status:#right now this only executes once
        print("ok")
        break
    time.sleep(0.5)

#I need the background task to run a set intervals while the main thread always executes (for thinking)