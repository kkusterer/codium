import os
import time
def up_pos():
    print("*---------------------------------------*")
    print("*                 |                     *")
    print("*                 |                     *")
    print("*                 |                     *")
    print("*                 |                     *")
    print("*                 @                     *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*---------------------------------------*")

def up_right_pos():
    print("*---------------------------------------*")
    print("*                           _-^         *")
    print("*                        _-^            *")
    print("*                     _-^               *")
    print("*                  _-^                  *")
    print("*                 @                     *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*---------------------------------------*")

def right_pos():
    print("*---------------------------------------*")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                 @------------------   *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*---------------------------------------*")

def right_down_pos():
    print("*---------------------------------------*")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                 @                     *")
    print("*                  ^-_                  *")
    print("*                     ^-_               *")
    print("*                        ^-_            *")
    print("*                           ^-_         *")
    print("*---------------------------------------*")


def down_pos():
    print("*---------------------------------------*")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                 @                     *")
    print("*                 |                     *")
    print("*                 |                     *")
    print("*                 |                     *")
    print("*                 |                     *")
    print("*---------------------------------------*")

def down_down_pos():
    print("*---------------------------------------*")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                 @                     *")
    print("*              _-^                      *")
    print("*           _-^                         *")
    print("*        _-^                            *")
    print("*     _-^                               *")
    print("*---------------------------------------*")

def left_pos():
    print("*---------------------------------------*")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*  ---------------@                     *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*---------------------------------------*")

def left_up_pos():
    print("*---------------------------------------*")
    print("*     ^-_                               *")
    print("*        ^-_                            *")
    print("*           ^-_                         *")
    print("*              ^-_                      *")
    print("*                 @                     *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*                                       *")
    print("*---------------------------------------*")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    up_pos()
    time.sleep(0.5)

    clear_screen()
    up_right_pos()
    time.sleep(0.5)

    clear_screen()
    right_pos()
    time.sleep(0.5)

    clear_screen()
    right_down_pos()
    time.sleep(0.5)

    clear_screen()
    down_pos()
    time.sleep(0.5)

    clear_screen()
    down_down_pos()
    time.sleep(0.5)

    clear_screen()
    left_pos()
    time.sleep(0.5)

    clear_screen()
    left_up_pos()
    time.sleep(0.5)