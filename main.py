import re

def check(v1, v2, v3):
    msg = ""
    if bool(re.match(r"[0-9][0-9]?[0-9]?[0-9]?\.0", v2)):
        v2 = v2.split(".")
        v2 = int(v2[0])
        v2 = str(v2)

    if bool(re.match(r"[0-9][0-9]?[0-9]?[0-9]?\.0", v1)):
        v1 = v1.split(".")
        v1 = int(v1[0])
        v1 = str(v1)

    if bool(re.match(r"[0-9][0-9]?[0-9]?[0-9]?\.[0-9]", v1)):
        v1 = float(v1)
    elif bool(re.match(r"[0-9][0-9]?[0-9]?", v1)):
        v1 = int(v1)


    if bool(re.match(r"[0-9][0-9]?[0-9]?[0-9]?\.[0-9]", v2)):
        v2 = float(v2)
    elif bool(re.match(r"[0-9][0-9]?[0-9]?", v2)):
        v2 = int(v2)

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_[8]
    if msg != "":
        msg =msg_[9] + msg
        print(msg)

def is_one_digit(v):
    if v > -10 and v < 10 and type(v) == int:
        return True
    else:
        return False


def operations(oper, x, y, memory):
    result = 0
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/":
        result = x / y
    return result

def checkanswer(result, answer, memory):
    if answer == "y":
        return result

    elif answer == "n":
        return memory

memory = 0

msg_ = ["Enter an equation", "Do you even know what numbers are? Stay focused!", "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...", "Do you want to store the result? (y / n):", "Do you want to continue calculations? (y / n):",
        " ... lazy", " ... very lazy", " ... very, very lazy", "You are", "Are you sure? It is only one digit! (y / n)", "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]
x = ""
y = ""
msg_index = 0

while True:
    print(msg_[0])
    cals = input()
    all = cals.split()
    x = all[0]
    oper = all[1]
    y = all[2]
    result = 0
    if x.replace('.','',1).isdigit() and y.replace('.','',1).isdigit() or x == 'M' or y == 'M':
        if bool(re.match(r"[0-9][0-9]?[0-9]?[0-9]?\.0", str(memory))):
            memory = int(memory)
        if x == 'M':
            x = str(memory)
        if y == 'M':
            y = str(memory)
        if oper == '+' or oper == '-' or oper == '*' or (oper == '/'):
            check(x, y, oper)
        if oper == '+' or oper == '-' or oper == '*' or (oper == '/' and y != '0'):
            result = operations(oper, float(x), float(y), memory)
            print(result)
            smalloop = True
            while smalloop:
                print(msg_[4])
                answer = input()
                if answer == "y":
                    if bool(re.match(r"[0-9][0-9]?[0-9]?[0-9]?\.0", str(result))):
                        result = int(result)

                    if is_one_digit(result):
                        msg_index = 10
                        while True:
                            print(msg_[msg_index])
                            answer = input()
                            if answer == "y":
                                if msg_index < 12:

                                    msg_index = msg_index + 1
                                    continue
                                if msg_index >= 12:
                                    memory = result
                                    smalloop = False
                                    break
                            smalloop = False
                            if answer == "n":
                                smalloop = False
                                break
                            else:
                                smalloop = True
                    if is_one_digit(result) == False:
                        memory = result
                        break
                else:
                    smalloop = False
            print(msg_[5])
            answer = input()
            if answer == "y":
                continue
            elif answer == "n":
                break
            else:
                checkanswer(result, answer, memory)
        elif oper == '/' and y == '0':
            print(msg_[3])
        else:
            print(msg_[2])
    else:
        print(msg_[1])
