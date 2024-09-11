from pyfiglet import Figlet
import random
import sys
figlet = Figlet()

if len(sys.argv) == 1:
    isRandFont = True
   
elif len(sys.argv) ==3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandFont = False
else:
    print("Invalid usage")
    sys.exit(1)
    
    
figlet.getFonts()

if isRandFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invaid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())
    
msg = input("Input: ")

print("Output:")
print(figlet.renderText(msg))