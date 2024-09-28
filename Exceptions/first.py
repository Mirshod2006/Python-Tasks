import colorama as c
c.init(autoreset=True)

color_map = {
    **{ch: c.Fore.RED for ch in 'ABCDEFGHabcdefgh'},
    **{ch: c.Fore.YELLOW for ch in 'IJKLMNOPijklmnop'},
    **{ch: c.Fore.GREEN for ch in 'QRSTUVWXYZqrstuvwxyz'},
}
# Initializing Huge Maps With for Iteration

def colorize(s):
    # Below a string is Created and colored by the help of color_map
    colored_string = ''.join(
        f"{color_map.get(char,'')}{char}{c.Style.RESET_ALL}" if char.isalpha() else char 
        for char in s
    )
    return colored_string
print(colorize("Hello Guys, Do you add more colors to colorize!"))