def main():
    name=convert()
    print(name)

def convert():
    message=(input("")).replace(":)","🙂").replace(":(","🙁")
    return (message)
    
main()  