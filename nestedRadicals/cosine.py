def main():
    angle = input("Please input an angle of the form a*pi/b: ")
    while angle.count("pi") != 1:
        angle = input("Please input an angle of the form a*pi/b: ")

    parts = angle.replace("*", "").split("pi")
    if parts[0] == "":
        parts[0] = "1"
    elif parts[0] == "-":
        parts[0] = "-1"

    if parts[1] == "":
        parts[1] = "1"
    num = int(parts[0])
    denom = int(parts[1].replace("/",""))

    while num < 0:
        num += 2 * denom

    while num >= 2 * denom:
        num -= 2 * denom

    used = []
    signs = []

    if num == 0:
        print("cos(" + angle + ") = +sqrt(2 + sqrt(2 + ...))/2 = 1")
        return

    while (num,denom) not in used:
        used.append((num, denom))
        if 2 * num < denom or 2 * num > 3 * denom:
            signs.append("+")
        elif 2 * num > denom and 2 * num < 3 * denom:
            signs.append("-")
        else:
            break
        num *= 2

        while num >= 2 * denom:
            num -= 2 * denom

    is_repeating = False

    if (num,denom) in used and len(used) == len(signs):
        signs.insert(used.index((num, denom)), "rep")
        is_repeating = True


    print("cos(" + angle + ") = ", end="")
    for i, sign in enumerate(signs):
        if sign != "rep":
            if i == 0:
                print(sign + "sqrt(2", end="")
            elif not is_repeating or i != len(signs) - 1:
                print(" " + sign + " sqrt(2", end ="")
            else:
                print(" " + sign + " ..." + ")" * (len(signs) - 1) + "/2")
        else:
            print()
            
    if not is_repeating:
        print(")" * len(signs) + "/2")


if __name__ == "__main__":
    main()