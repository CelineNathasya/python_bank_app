import re
import smtplib
from easygui import passwordbox

def send_email(email, desc):
    gmail_user = "bankITU.18IS01@gmail.com"
    gmail_pwd = "bankITU1234"
    TO = email
    SUBJECT = "Transaksi Bank ITU"
    TEXT = desc
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    BODY = '\r\n'.join(['To: %s' % TO,
            'From: %s' % gmail_user,
            'Subject: %s' % SUBJECT,
            '', TEXT])

    server.sendmail(gmail_user, [TO], BODY)
    print ('Email sent!')

def input_password(desc):
    """
    request user password input with validation
    will loop until valid input entered
    :return:
    """
    while True:
        password = passwordbox(desc)
        if len(password) < 8:
            print("Pastikan jumlah karakter lebih dari 8 karakter")
        elif re.search('[0-9]',password) is None:
            print("Pastikan terdapat angka")
        elif re.search('[A-Z]',password) is None:
            print("Pastikan terdapat huruf kapital")
        elif re.search('[a-z]',password) is None:
            print("Pastikan terdapat huruf kecil")
        else:
            break
    return password

def input_pin(desc):
    while True:
        pin = passwordbox(desc)
        if not pin:
            return False
        elif len(pin) != 6:
            print("Jumlah karakter pin harus 6")
        elif pin.isnumeric():
            print("Pin valid")
            break
        else:
            print("Pin harus angka")
    return pin

def input_email(desc):
    while True:
        email = input_string(desc)
        if re.search('@', email) is None:
            print("Input valid email")
        else:
            break
    return email

def input_int(desc):
    """
    request user input with validation that return an int
    will loop until valid input entered
    :return:
    """
    while True:
        try:
            user_input = int(input(desc))
            if user_input == "":
                print("Tidak boleh kosong")
            elif user_input <= 0:
                print("Angka tidak boleh lebih kecil dari 0")
            else: 
                break
        except: 
            print("Terjadi kesalahan input")
    return user_input

def input_string(desc):
    """
    request user input with validation that return a string
    will loop until valid input entered
    :return:
    """
    while True:
        user_input = input(desc)
        if user_input == "":
            print("Tidak boleh kosong")
        else: 
            break
    return user_input
