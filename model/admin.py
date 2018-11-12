import json

class Admin:

    def __init__(self, id, name, password, age):
        self.id = id
        self.name = name
        self.password = password
        self.age = age

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'password': self.password,
        }


def admin_add(admin):
    admins = load_admins()
    with open('Admin.json', 'w') as f:
        admins.append(admin)
        f.seek(0)
        f.write(json.dumps(convert_Admin_object_to_dictionary(admins), indent=4))
        f.truncate()


def admin_remove(id):
    admins = load_admins()
    with open('Admin.json', 'w') as f:
        # listfilter menghasilkan array of User object
        admins = list(filter(lambda admin: admin.id != id, admins))
        f.write(json.dumps(convert_Admin_object_to_dictionary(admins), indent=4))


# def edit_user(id, new_pin):
#     users = load_admins()
#     with open('User.json', 'w') as f:
#         for user in users:
#             if user.id == id:
#                 user.pin = new_pin
#         f.write(json.dumps(convert_Admin_object_to_dictionary(users), indent=4))


def load_admins():
    with open('Admin.json') as f:
        admins = json.load(f)
    #using list comprehension to convert each dictionary to User object
    return [Admin(admin['id'], admin['name'], admin['password'], admin['age']) for admin in admins]


def convert_Admin_object_to_dictionary(admins):
    return [admin.to_dict() for admin in admins]
