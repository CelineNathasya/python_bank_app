from os import system
import json
import datetime
from model.user import User, load_users, add_user, remove_user, edit_user, block_user, edit_balance, convert_User_object_to_dictionary
from helper import send_email, input_int, input_string, input_pin

def login():
    users = load_users()
    while True:
        userid = False
        login_fail = 4
        system('cls')
        print("{:=^50}".format('Welcome To Bank ITU'))
        print("{:=^50}".format('Login'))

        user_id = input_string("ID    : ")
        user_pin = input_pin("PIN   : ")
        
        for user in users:
            if user_id == user.id:
                userid = True
                while login_fail!=0:
                    if user_pin == user.pin:
                        if user.status == "inactive":
                            print('Your account is blocked, contact your admin')
                            system("pause")
                            break
                        else:
                            print('Login berhasil')
                            return user
                    else:
                        system('cls')
                        print("{:=^50}".format('Login'))
                        print('Try again, Kesempatan',login_fail)
                        print('ID    :',user_id)
                        user_pin = input_pin("PIN   : ")
                        if user_pin == user.pin:
                            if user.status == "inactive":
                                print('Your account is blocked, contact your admin')
                                system("pause")
                                break
                            else:
                                print('Login berhasil')
                                return user
                        else:
                            login_fail -= 1
                            
                    if login_fail == 0:
                        print('Your Account has been blocked')
                        print('contact admin!!')
                        system('pause')
                        block_user(user_id)
                        break
                        
                    print('PIN salah')
                    try_again_choice = ['yes',"y","no",'n']    
                    try_again = input('Continue (y/n) ? ')
                    while try_again not in try_again_choice: 
                        try_again = input_string('Continue (y/n) ? ')
                    if try_again == "n":
                        break

        if userid == False:    
            print('ID or PIN Wrong !!')
            system('pause')


def cek_saldo(data):
    all_user = load_users()
    for user in all_user:
        if user.id == data.id:
            print(f'\n\nYour Balance : Rp. {user.balance:,.2f}')

def transfer(data):
    all_data = load_users()
    list_data = []
    print('======Transfer======')

    target_transfer = input_string('ID penerima : ')
    target = False

    if data.id == target_transfer:   #jika id sender dan receiver sama
        print("Anda tidak bisa melakukan Transfer ke Rekening sendiri")
        system('pause')
        return False

    for x in all_data:
        if target_transfer == x.id:
            target = True
    if target == False:
        print('ID Tidak ditemukan')
        system('pause')
        return False

    for user in all_data:
        if user.id == data.id:
            
            nominal = input_int('Jumlah : Rp. ')
            if nominal > data.balance:
                print('Saldo anda tidak cukup')
            else:
                desc_sender = "Anda melakukan transfer kepada\nBank: ... \n   Rekening: {}\n   Sebesar Rp {:,}".format(target_transfer,nominal)
                desc_receiver = "Anda menerima transfer dari\nBank: ... \n   Rekening: {}\n   Sebesar Rp {:,}".format(user,nominal)
                print(f'Anda melakukan transfer ke {target_transfer}')
                pin = input_pin('PIN : ')
                if pin == data.pin:
                    edit_balance(user.id, -nominal)
                    for user_target in all_data:
                        if user_target.id == target_transfer:
                            edit_balance(user_target.id, nominal)
                            transaction_history(nominal,data.id,target_transfer)
                    send_email(user.email, desc_sender)
                    send_email(user_target.email, desc_receiver)
                else:
                    print('PIN anda salah')
        list_data.append(user)

    print() 
    system('pause')
    
    
def transaction_history(nominal,sender,receiver):
    date = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S %p")
    history = {}
    history['date'] = date
    history['ID Sender'] = sender
    history['receiver'] = receiver
    history['nominal'] = nominal
    with open('history.json','r') as f:
        data = json.load(f)

    data.append(history)

    with open('history.json','w') as w:
        w.write(json.dumps(data,indent=4))
    