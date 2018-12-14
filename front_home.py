import json
import getpass
from os import system
from model.user import load_users, edit_balance
from front import login, cek_saldo, transfer, transaction_history
from helper import input_int, input_string
from terbilang import terbilang

def setor(user):
    system('cls')
    amount = input_int('Jumlah Setoran : Rp. ')
    edit_balance(user.id, amount)
    transaction_history(amount, "setor", user.id,'')
    user.balance += amount
    print("Penyetoran berhasil")
    print(f'Anda telah melakukan penyetoran sebesar Rp. {amount:,.2f}')
    print(terbilang(amount),'Rupiah')
    system('pause')

def tarik(user):
    system('cls')
    amount = input_int('Jumlah Penarikan : Rp. ')
    if (user.balance - amount) < 0:
        print("Saldo tidak mencukupi")
    else :
        edit_balance(user.id, -amount) 
        transaction_history(amount, "tarik", user.id,'')
        print("Penarikan berhasil")
        print(f'Anda telah melakukan penarikan sebesar Rp. {amount:,.2f}')
        print(terbilang(amount),'Rupiah')
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
            user_choices = input_int('Masukkan pilihan anda : ')
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
            
main()
