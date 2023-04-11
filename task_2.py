def main():
    n = int(input("Введите n: "))
    w = int(input("Введите w: ")) 
    d = int(input("Введите d: ")) 
    p = int(input("Введите p: ")) 

    coin_sum = (n*(n-1))//2
    coin_mass = coin_sum * w
    for i in range(1,n):
        if coin_mass - (i*d) == p:
            return i
    return n


if __name__ == "__main__":
    print(f"Номер корзины с фальшивыми монетами: {main()}")