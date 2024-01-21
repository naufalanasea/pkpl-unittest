def jumlah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def pangkat(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def kalkulator(a, b, operasi):
    if operasi == "jumlah":
        return a + b
    elif operasi == "kurang":
        return a - b
    elif operasi == "kali":
        return a * b
    elif operasi == "bagi":
        return a / b
    elif operasi == "pangkat":
        return a ** b
    elif operasi == "akar":
        return a ** 0.5
    elif operasi == "modulus":
      return 10 % 2