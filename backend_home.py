import io
import json
import os
from model.user import User, load_users, add_user, remove_user, edit_user, block_user, unblock_user
from model.admin import Admin, load_admins, admin_add, admin_remove, admin_edit
from helper import input_password, input_int, input_string, input_email, input_pin

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
    print("Selamat Datang...")
    print()
    print("1. Add rekening")
    print("2. Remove rekening")
    print("3. Edit rekening")
    print("4. Blok rekening")
    print("5. Un-blok rekening")
    print("6. Cek saldo user")
    print("7. Print list rekening")
    print("8. Cek history transfer user")
    print("9. Add admin")
    print("10. Remove admin")
    print("11. List admin")
    print("12. Edit admin")
    print("13. Exit")


# selection
def main():
    login_admin()
    startupCheck()
    while True:
        os.system('cls')
        print_menu()
        print()
        user_input = input_int("Masukkan pilihan anda: ")
        if user_input == 1:
            add_rekening()
        elif user_input == 2:
            remove_rekening()
        elif user_input == 3:
            edit_rekening()
        elif user_input == 4:
            blok_rekening()
        elif user_input == 5:
            unblok_rekening()
        elif user_input == 6:
            cek_saldo_user()
        elif user_input == 7:
            print_list_rekening()
        elif user_input == 8:
            history_transfer_user()
        elif user_input == 9:
            add_admin()
        elif user_input == 10:
            remove_admin()
        elif user_input == 11:
            list_admin()
        elif user_input == 12:
            edit_admin()
        elif user_input == 13:
            os.system('cls')
            print("Terima kasih telah mempercayai Bank ITU sebagai bank pilihan anda\n")
            os.system('pause')
            break

def add_rekening():
    os.system('cls')
    users = load_users()
    print(f"{'Add rekening baru':^50}")
    print("="*50)
    user_name = input_string("Nama lengkap: ")
    user_age = input_int("Umur: ")
    while True:
        user_id = input_string("Id: ")
        if user_id not in [user.id for user in users]:
            break
        else:
            print("Id telah digunakan")
    #validasi pin
    user_pin = input_pin("Pin: ")
    user_email = input_email("Email: ")
    user = User(user_id, user_name, user_pin, user_age, 0, "active", user_email)
    add_user(user)
    print('Rekening berhasil ditambahkan')
    os.system('pause')


def remove_rekening():
    os.system('cls')
    print(f"{'Remove rekening':^50}")
    print("="*50)
    users = load_users()
    user_id = input_string("Masukkan Id: ")
    if user_id in [user.id for user in users]:
        remove_user(user_id)
        print("Rekening berhasil dihapus")
    else:
        print("Id tidak ditemukan")
    print()
    os.system('pause')


def edit_rekening():
    os.system('cls')
    print(f"{'Edit pin rekening':^50}")
    print("="*50)
    users = load_users()
    user_id = input_string("Masukkan Id:")
    if user_id in [user.id for user in users]:
        user_new_pin = input_pin("Masukkan pin baru: ")
        edit_user(user_id, user_new_pin)
        print("Pin berhasil diedit")
    else:
        print("Id tidak ditemukan")
    print()
    os.system('pause')


def blok_rekening():
    os.system('cls')
    print(f"{'Blok rekening':^50}")
    print("="*50)
    users = load_users()
    user_id = input_string("Masukkan Id: ")
    if user_id in [user.id for user in users]:
        block_user(user_id)
        print("Blok berhasil")
    else:
        print("Id tidak ditemukan")
    print()
    os.system('pause')

def unblok_rekening():
    os.system('cls')
    print(f"{'Unblock rekening':^50}")
    print("="*50)
    users = load_users()
    user_id = input_string("Masukkan Id: ")
    if user_id in [user.id for user in users]:
        unblock_user(user_id)
        print("Unblock berhasil")
    else:
        print("Id tidak ditemukan")
    print()
    os.system('pause')

def cek_saldo_user():
    os.system('cls')
    print(f"{'Cek saldo pengguna':^50}")
    print("="*50)
    users = load_users()
    user_id = input_string("Masukkan Id: ")
    if user_id in [user.id for user in users]:
        for user in users:
            if user_id== user.id:
                print(f"{user_id}'s balance = Rp {user.balance:,.2f}")
    else:
        print("Id tidak ditemukan")
    print()
    os.system('pause')


def print_list_rekening():
    os.system('cls')
    print(f"{'List rekening':^50}")
    print("="*50)
    users = load_users()
    print(f"{'No':>4} {'Id':<20} {'Nama':<25}")
    for idx, user in enumerate(users)  :
        print(f"{(idx+1):3}. {user.id:<20} {user.name:<25}")
    print()
    os.system('pause')



def history_transfer_user():
    os.system('cls')
    print(f"{'History transfer pengguna':^50}")
    print("="*50)
    with open ("History.json") as f:
        datas = json.load(f)
        user_id = input_string("Id: ")
        print(f"{'Tanggal':^30} {'Status':6} {'Jumlah':^33} ")
        for data in datas:
            if data["ID Sender"] == user_id:
                print(f"{data['date']:^30} {'kirim':6} {'Rp ':3}{data['nominal']:30,.2f}")
            elif data["receiver"] == user_id:
                print(f"{data['date']:^30} {'terima':6} {'Rp ':3}{data['nominal']:30,.2f}")
    print()
    os.system('pause')


def login_admin():
    os.system('cls')
    admins = load_admins()
    loop = True
    login = False
    print(f"{'Admin Login':^50}")
    print("="*50)
    while loop:
        admin_id = input_string("Id: ")
        for admin in admins:
                if admin.id == admin_id:
                    login == True
                    admin_pass = input_password("Password: ")
                    if admin.password == admin_pass:
                        print("Logged in as admin")
                        loop = False
                        break
                    else: 
                        print("Password salah")
        if login == False:
            print("Id tidak ditemukan")
            break


def add_admin():
    os.system('cls')
    print(f"{'Add admin baru':^50}")
    print("="*50)
    admins = load_admins()
    admin_name = input_string("Nama lengkap: ")
    admin_age = input_int("Umur: ")
    while True:
        admin_id = input_string("Id: ")
        if admin_id not in [admin.id for admin in admins]:
            break
        else:
            print("Id telah digunakan")
    admin_password = input_password("Password: ")
    admin = Admin(admin_id, admin_name, admin_password, admin_age)
    admin_add(admin)
    print("Admin berhasil ditambahkan")
    os.system('pause')

def remove_admin():
    os.system('cls')
    print(f"{'Remove admin':^50}")
    print("="*50)
    admins = load_admins()
    admin_id = input_string("Masukkan Id: ")
    if admin_id in [admin.id for admin in admins]:
        admin_remove(admin_id)
        print("Admin berhasil dihapus")
    else:
        print("Id tidak ditemukan")
    print()
    os.system('pause')

def list_admin():
    os.system('cls')
    print(f"{'List admin':^50}")
    print("="*50)
    admins = load_admins()
    print(f"{'No':>4} {'Id':<20} {'Nama':<25}")
    for idx, admin in enumerate(admins)  :
        print(f"{(idx+1):>3}. {admin.id:<20} {admin.name:<25}")
    print()
    os.system('pause')

def edit_admin():
    os.system('cls')
    print(f"{'Edit password admin':^50}")
    print("="*50)
    admins = load_admins()
    admin_id = input_string("Masukkan Id:")
    if admin_id in [admin.id for admin in admins]:
        admin_new_password = input_password("Masukkan password baru: ")
        admin_edit(admin_id, admin_new_password)
        print("Password berhasil diedit")
    else:
        print("Id tidak ditemukan")
    print()
    os.system('pause')


if __name__ == '__main__':
    main()
