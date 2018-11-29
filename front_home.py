import json
import getpass
from os import system
from model.user import User, load_users, add_user, remove_user, edit_user, block_user, edit_balance
from front import login, cek_saldo, load_user, transfer

# def refresh_user(id):
#     users = load_users()
#     return list(filter(lambda user: user.id == id, users))[0]


def setor(user):
    #validation
    amount = int(input('Jumlah Setoran : Rp. '))
    edit_balance(user.id, amount)
    user.balance += amount
    print(f'Anda telah melakukan penyetoran sebesar Rp. {amount:,.2f}')
    system('pause')

def tarik(user):
    #validation
    amount = int(input('Jumlah Penarikan : Rp. '))
    edit_balance(user.id, -amount)
    user.balance -= amount
    print(f'Anda telah melakukan penarikan sebesar Rp. {amount:,.2f}')
    system('pause')

def main():
    while True:
        user = login() #login page
        system('pause')

        while True:     #user page
            system('cls')
            print("\nWelcome, {} ".format(user.name))
            print('''     
            1. Cek Saldo                      
            2. Setor                            
            3. Tarik                            
            4. Transfer                       
            5. Exit
               ''')
            # try:
            user_choices = int(input('Your Choices : '))
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
