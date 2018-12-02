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
        print("{:^50}".format('Welcome To Bank ITU'))
        print("{:^50}".format('Login'))
        print("="*50)

        user_id = input_string("ID    : ")
        user_pin = input_pin("PIN   : ")
        
        for user in users:
            if user_id == user.id:
                userid = True
                while login_fail>0:
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
                        if not user_pin:
                            login_fail = -1
                        elif user_pin == user.pin:
                            if user.status == "inactive":
                                print('Your account is blocked, contact your admin')
                                system("pause")
                                break
                            else:
                                print('Login berhasil')
                                return user
                        else:
                            print('PIN salah')
                            login_fail -= 1
                            
                    if login_fail == 0:
                        print('Your Account has been blocked')
                        print('contact admin!!')
                        system('pause')
                        block_user(user_id)
                        break
                    if login_fail == -1:
                        print('Canceled')
                        
                  
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
    system('cls')
    print(f"{'Transfer':^50}")
    print("="*50)
    print()
    list_bank = ["Bank INI", "Bank SINI", "Bank SITU", "Bank SANA", "Bank SONO", "Sesama Bank ITU"]
    print("Masukan kode Bank")
    for idx, bank in enumerate(list_bank):
        print(f"{idx+1}. {bank}")
    print()
    try:
        kode_bank = input_int('Masukan Kode Bank : ')
        if kode_bank<0 or kode_bank>6:
            print('Tidak ditemukan Bank')
            print('Kode Bank harus antara 1-6')
            system('pause')
    except:
        print('Masukan Kode Bank dalam angka')
        system('pause')


    target_transfer = input_string('ID penerima : ')
    if 0<kode_bank<6:
        for user in all_data:
            if user.id == data.id:
                nominal = input_int('Jumlah : Rp. ')
                if nominal > data.balance:
                    print('Saldo anda tidak cukup')
                else:
                    desc_sender = "Anda melakukan transfer kepada\n    Bank:{} \n   Rekening: {}\n   Sebesar Rp {:,.2f}".format(list_bank[kode_bank-1],target_transfer,nominal)
                    print(f'anda melakukan transfer ke {target_transfer}')
                    pin = input_pin('PIN : ')
                    if pin == data.pin:
                        edit_balance(user.id, nominal)
                        print('Transaksi Berhasil')
                        
                        send_email(user.email, desc_sender)
                        break

    elif kode_bank == 6:
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
                    desc_sender = "Anda melakukan transfer kepada\n   Rekening: {}\n   Sebesar Rp {:,.2f}".format(target_transfer,nominal)
                    desc_receiver = "Anda menerima transfer dari\n   Rekening: {}\n   Sebesar Rp {:,2f}".format(user,nominal)
                    print(f'Anda melakukan transfer ke {target_transfer}')
                    pin = input_pin('PIN : ')
                    if not pin:
                        print('transaksi dibatalkan')
                    elif pin == data.pin:
                        edit_balance(user.id, -nominal)
                        for user_target in all_data:
                            if user_target.id == target_transfer:
                                edit_balance(user_target.id, nominal)
                                transaction_history(nominal,data.id,target_transfer)
                        send_email(user.email, desc_sender)
                        send_email(user_target.email, desc_receiver)
                    else:
                        print('PIN anda salah')

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
    