num = int(input("enter num: "))
ls = []
ls.append(num)
while num != "": 
    num = input("enter num: ")
    if num == "":
        break
    try:
        ls.append(int(num))
    except ValueError:
        pass
print(sum(ls))