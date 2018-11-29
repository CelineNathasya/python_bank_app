import re
import smtplib
 
def send_email(email, desc):
    gmail_user = "sayacintais2018@gmail.com"
    gmail_pwd = "IS20182018"
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

def input_int(desc):
    """
    request user input with validation that return an int
    will loop until valid input entered
    :return:
    """
    while True:
        try:
            return int(input(desc))
        except:
            print("Maaf, terjadi kesalahan input. Silahkan ulangi lagi.")

def input_string(desc):
    while True:
        user_input = input(desc)
        if user_input == "":
            print("Tidak boleh kosong")
        else: 
            break
    return user_input
