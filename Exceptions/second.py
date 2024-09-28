def encode(num):
    sezar_map = {'0': '7', '1': '8', '2': '9', '3': '0', '4': '1', '5': '2', '6': '3', '7': '4', '8': '5', '9': '6'}
    num_str = str(num)
    return ''.join(f"{sezar_map[ch]}" for ch in num_str)
print(encode(10023))