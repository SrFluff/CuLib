# CuLib

**CuLib** is a custom Python library, current features include:

* Screen clearing via os.system and os.name
* Random number generator via random.randint
* Waiting via time.sleep

# Main purpose

**CuLib** is just meant to be placed in a dedicated ***Python*** folder, and can be used with
  
    import CuLib

or individual functions can be requested with 
  
    from CuLib import FUNCTION_NAME

I made this so I wouldn't
have to keep adding

    import os
  
    def cls():
  
      if os.name == 'nt':
  
        os.system('cls')
  
      else:
  
        os.system('clear')

CuLib features a ***Debug Environment***, if you're going to use the ***Debug Environment***  
then you must go into **CuLib.py** and add your variables to the ***Debug Environment*** so  
that

    de: var-chk

works. You must also add your variable to the variable list so that

    de: var-ls

works too.

# Debug environment

CuLib's ***Debug Environment*** is a terminal emulator that can assist in variable debugging.
Some commands include:

* de: var-chk: Returns the value of every variable
* de: var-ls: Lists all loaded variables
* de: var-res: Sets all variable to 0, False, or ""
* de: de-ex: Exits the debug environment

The ***Debug Environment*** can be initialized with

    cuLib.initDebug()

# Warnings

CuLib requires Colorama to function properly, to install colorama, click [this link](https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz) to download it  
Next extract the colorama folder to the same folder as CuLib

# Fun facts

  *  **CuLib** is pronounced as ***Queue Lib*** and is short for ***Custom User Library***  
  *  **CuLib** is a spiritual successor to ***MagLib***, a similar library that I lost 
     to an ***SD card failure***

# Credits

* Colorama - Jonathan Hartley
* Python - Guido Van Rossum
* CuLib - Franco M.
