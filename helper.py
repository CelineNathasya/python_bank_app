import re

def validate_password(desc):
    while True:
        password = input(desc)
        if len(password) < 8:
            print("Pastikan jumlah karakter lebih dari 8 karakter")
        elif re.search('[0-9]',password) is None:
            print("Pastikan terdapat angka")
        elif re.search('[A-Z]',password) is None:
            print("Pastikan terdapat huruf kapital")
        else:
            print("Berhasil")
            break
    return password
