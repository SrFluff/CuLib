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
