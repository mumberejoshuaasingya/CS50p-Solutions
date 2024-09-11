y=input("Greeting: ").lstrip(" ")
if y.startswith("Hello"):
    print("$0")
elif y.startswith("hello"):
    print("$0")
elif y.startswith("h"):
    print("$20")
elif y.startswith("H"):
    print("$20")
else: print("$100")
