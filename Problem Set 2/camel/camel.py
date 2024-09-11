userinput=input("camelCase: ")

def switching(input):
    var=''
    for char in input:
        if char.isupper():
            yield var
            var=''
        var+=char
    yield var
    
    
    
list(switching(userinput))
final_output="_".join(switching(userinput)).lower()
print("snake_case: " + final_output)