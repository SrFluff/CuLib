# All imports MUST go here ⬇️

import os
import random
import time

from colorama import Back, Fore

# CuLib
#
# Version 1.0.0 'Journey's end'
#
# Made by Franco M.

def cls():

    # I keep adding this to my projects :3

    if os.name == 'nt': # Checks if the OS kerenel is NT(windows)

        os.system('cls') # Windows cmd command

    else: # If it's not NT then it's posix

        os.system('clear') # Not a Windows cmd command

def random10():

    # I've needed this before, somehow

    print(random.randint(0,10))

        # I love randint <3

def wait(wai):

    #zzz zzz zzz zzz zzz zzz zzz

    time.sleep(wai)

def white(whi):

    print(Back.WHITE + Fore.BLACK + whi + Fore.RESET + Back.RESET)