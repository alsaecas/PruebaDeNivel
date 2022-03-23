def rotation(limits):
    goodList = []
    numbers = list(range(limits[0], limits[1]))
    for number in numbers:
        revnumber = ""
        for digit in reversed(str(number)):
            if digit == "6":
                digit = "9"
            elif digit == "9":
                digit = "6"
            elif digit == "0" or digit == "1" or digit == "8":
                digit = digit
            else:
                digit = "X"
            revnumber = revnumber + digit
        if str(number) == revnumber:
            goodList.append(number)
    return goodList, len(goodList)


if __name__ == '__main__':
    result = rotation([1, 2000])
    print("La cantidad total de numeros reversibles es: " + str(result[1]))
    print("Los numeros son:")
    for numero in result[0]:
        print(numero)
