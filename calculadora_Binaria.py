def binary_converter(n):
    x=n
    y=""
    while x>2:
        if x%2==0:
            x//=2
            y+="0"
        else:
            x//=2
            y+="1"
    if x==2:
        y+="01"
    else:
        y+="1"
    y="".join(reversed(y))
    return(f'{n} --> {y}')

print(binary_converter(int(input("Ingrese un numero decimal: "))))