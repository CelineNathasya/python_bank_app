# import uuid
import django.utils.crypto as djID
import io
import json
import os
from model.user import User, load_users, add_user, remove_user, edit_user, block_user


def startupCheck():
    PATH = os.path.dirname(__file__)
    if os.path.isfile(PATH + '/User.json') and os.access(PATH + '/User.json', os.R_OK):
        # checks if file exists
        print("File exists and is readable")
    else:
        print("Either file is missing or is not readable, creating file...")
        with io.open(os.path.join(PATH, 'User.json'), 'w') as db_file:
            db_file.write(json.dumps([]))


def print_menu():
    print("""
        1. Add rekening
        2. Remove rekening
        3. Edit rekening
        4. Blok rekening
        5. Cek saldo user
        6. Print list rekening
        7. Cek history transaksi user
        8. Admin
        """)


# selection
def main():
    startupCheck()
    print_menu()
    user_input = input_range()
    if user_input == 1:
        add_rekening()
    elif user_input == 2:
        remove_rekening()
    elif user_input == 3:
        edit_rekening()
    elif user_input == 4:
        blok_rekening()
    elif user_input == 5:
        cek_saldo_user()
    elif user_input == 6:
        print_list_rekening()
    elif user_input == 7:
        history_transaksi_user()
    elif user_input == 8:
        admin()


def input_range():
    """
    request user input with validation that return an int
    will loop until valid input entered
    :return:
    """
    while True:
        try:
            return int(input("Masukkan pilihan anda: "))
        except:
            print("Maaf, terjadi kesalahan. Silahkan ulangi lagi.")


def add_rekening():
    users = load_users()
    user_name = input("Nama lengkap: ")
    user_age = int(input("Umur: "))
    while True:
        user_id = input("Id: ")
        if user_id not in [user.id for user in users]:
            break
        else:
            print("Id telah digunakan")
    #validasi pin
    user_pin = input("Pin: ")
    user = User(user_id, user_name, user_pin, user_age, 0, "active")
    add_user(user)


def remove_rekening():
    users = load_users()
    user_id = input("Masukkan Id: ")
    if user_id in [user.id for user in users]:
        remove_user(user_id)
    else:
        print("Id tidak ditemukan")


def edit_rekening():
    users = load_users()
    user_id = input("Masukkan Id:")
    if user_id in [user.id for user in users]:
        user_new_pin = input("Masukkan pin baru: ")
        edit_user(user_id, user_new_pin)
    else:
        print("Id tidak ditemukan")


def blok_rekening():
    users = load_users()
    user_id = input("Masukkan Id: ")
    if user_id in [user.id for user in users]:
        block_user(user_id)
    else:
        print("Id tidak ditemukan")


def cek_saldo_user():
    users = load_users()
    user_id = input("Masukkan Id: ")
    if user_id in [user.id for user in users]:
        for user in users:
            if user_id== user.id:
                print(f"{user_id}'s balance = Rp {user.balance:,}")
    else:
        print("Id tidak ditemukan")


def print_list_rekening():
    users = load_users()
    print(users)
    print(f"{'No':>4} {'Id':<10} {'Nama':<10}")
    for idx, user in enumerate(users)  :
        print(f"{(idx+1):3}. {user.id:<10} {user.name:<10}")



def history_transaksi_user():
    pass


def admin():
    print("")


if __name__ == '__main__':
    main()
