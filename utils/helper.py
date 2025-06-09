import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def cat():
    ascii_art = r"""
      /\_/\
     ( o.o )
      > ^ <
    """

    print(ascii_art)
