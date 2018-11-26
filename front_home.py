import json
import getpass
from os import system
from model.user import User, load_users, add_user, remove_user, edit_user, block_user
from model.front import login, cek_saldo, setor, tarik, load_user, transfer

def user_setor():
    #validation
    setoran = int(input('Jumlah Setoran : Rp. '))
    return setoran

def user_tarik():
    #validadtion
    user_input = int(input('Tarik berapa : Rp. '))
    return user_input

def main():
    while True:
        data_user = login() #login page
        system('pause')

        while True:     #user page
            system('cls')
            print("\nWelcome, {} ".format(data_user["name"]))

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
                cek_saldo(data_user)
                system('pause')
            elif user_choices == 2:
                setor(user_setor(),data_user)
            elif user_choices == 3:
                tarik(user_tarik(),data_user)
            elif user_choices == 4:
                transfer(data_user)
            elif user_choices == 5:
                break   
            # except:
                # print('Input Number')
main()
