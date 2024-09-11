while True:
    userinput = input("Fraction: ")
    try:
        # Let me split the userinput
        x,y = userinput.split("/")
        a = int(x)
        b= int(y)
        check = (a/b)
        if check <=1 :
            break
    except (ValueError, ZeroDivisionError):
        pass
    
    
#multiply it by 100 to make it a percentage
percent = int(round(check,2) *100)
if percent <=1:
    print("E")
elif percent >=99:
    print("F")
else:
    print(f"{percent}%")
    
    
    
    
    
    
    
    
    
