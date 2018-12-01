import json
import getpass
from os import system
from model.user import User, load_users, add_user, remove_user, edit_user, block_user, edit_balance
from front import login, cek_saldo, transfer
from helper import input_int, input_string

# def refresh_user(id):
#     users = load_users()
#     return list(filter(lambda user: user.id == id, users))[0]


def setor(user):
    system('cls')
    amount = input_int('Jumlah Setoran : Rp. ')
    edit_balance(user.id, amount)
    user.balance += amount
    print("Penyetoran berhasil")
    print(f'Anda telah melakukan penyetoran sebesar Rp. {amount:,.2f}')
    system('pause')

def tarik(user):
    system('cls')
    amount = input_int('Jumlah Penarikan : Rp. ')
    if (user.balance - amount) < 0:
        print("Saldo tidak mencukupi")
    else :
        edit_balance(user.id, -amount) 
        print("Penarikan berhasil")
        print(f'Anda telah melakukan penarikan sebesar Rp. {amount:,.2f}')
        user.balance -= amount
    system('pause')

def main():
    while True:
        user = login() #login page
        system('pause')

        while True:     #user page
            system('cls')
            print("\nWelcome, {} ".format(user.name))
            print()
            print("1. Cek Saldo")
            print("2. Setor")
            print("3. Tarik")
            print("4. Transfer")
            print("5. Exit")                      
            print()  
            # try:
            user_choices = input_int('Your Choices : ')
            if user_choices == 1:
                system('cls')
                cek_saldo(user)
                system('pause')
            elif user_choices == 2:
                setor(user)
            elif user_choices == 3:
                tarik(user)
            elif user_choices == 4:
                transfer(user)
            elif user_choices == 5:
                break   
            # except:
                # print('Input Number')
            # user = refresh_user(user)
main()
