def Tower_Of_Hanoi(n, src, aux, des):
    if n == 1:
        print(f"{src} -> {des}")
        return
    Tower_Of_Hanoi(n - 1, src, des, aux)
    print(f"{src} -> {des}")
    Tower_Of_Hanoi(n - 1, aux, src, des)


n = int(input("Enter Length Of Tower : "))
Tower_Of_Hanoi(n, 'A', 'C', 'B')
