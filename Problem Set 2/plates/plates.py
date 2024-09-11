def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6>= len(s) >=2 and s[0:2].isalpha() and s.isalnum():
        for character in s:
            if character.isdigit():
                index = s.index(character)
                if s[index:].isdigit() and int(character) != 0:
                    return True
                else:
                    return False
        return True

main()
