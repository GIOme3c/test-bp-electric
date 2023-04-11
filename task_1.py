def main():
    min_value = 0
    max_value = 2**16-1     
    value = int(input(f"Введите целое положительное число от {min_value} и до {max_value}: "))
    bin_value = []

    for bit in range(0, 16):
        bin_value.append(value % 2)
        value //= 2

    for bit_num in range(0,8):
        bin_value[bit_num], bin_value[bit_num+8] = bin_value[bit_num+8], bin_value[bit_num]

    c = 1 #coefficient
    swap_byte_value = 0
    for bit in bin_value:
        swap_byte_value += bit * c
        c *= 2
    
    return swap_byte_value


if __name__ == "__main__":
    print("Новое значение: ",main())
