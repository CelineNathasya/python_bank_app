import json

class User:

    def __init__(self, id, name, pin, age, balance, status):
        self.id = id
        self.name = name
        self.pin = pin
        self.age = age
        self.balance = balance
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'balance': self.balance,
            'age': self.age,
            'pin': self.pin,
            'status': self.status
        }


def add_user(user):
    users = load_users()
    with open('User.json', 'w') as f:
        users.append(user)
        f.seek(0)
        f.write(json.dumps(convert_User_object_to_dictionary(users), indent=4))
        f.truncate()


def remove_user(id):
    users = load_users()
    with open('User.json', 'w') as f:
        # listfilter menghasilkan array of User object
        users = list(filter(lambda user: user.id != id, users))
        f.write(json.dumps(convert_User_object_to_dictionary(users), indent=4))


def edit_user(id, new_pin):
    users = load_users()
    with open('User.json', 'w') as f:
        for user in users:
            if user.id == id:
                user.pin = new_pin
        f.write(json.dumps(convert_User_object_to_dictionary(users), indent=4))


def block_user(id):
    users = load_users()
    with open('User.json', 'w') as f:
        for user in users:
            if user.id == id:
                user.status = "inactive"
        f.write(json.dumps(convert_User_object_to_dictionary(users), indent=4))


def load_users():
    with open('User.json') as f:
        users = json.load(f)
    #using list comprehension to convert each dictionary to User object
    return [User(user['id'], user['name'], user['pin'], user['age'], user['balance'], user['status']) for user in users]


def convert_User_object_to_dictionary(users):
    return [user.to_dict() for user in users]
