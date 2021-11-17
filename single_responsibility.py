class UserInfo:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return "{},{},{}".format(
            self.name, self.age, self.phone_number
        )
    # def write_str_to_file(self, filename):
    #     with open(filename, mode='w') as fh:
    #         fh.write(str(self))


class FileManager:
    @staticmethod
    def write_str_to_file(obj, filename):
        with open(filename, mode='w') as fh:
            fh.write(str(obj))


user_info = UserInfo('Taro', 21, '000-0000-0000')
print(str(user_info))

# use__info.write_str_to_file('tmp.txt')
FileManager.write_str_to_file(user_info, 'tmp.txt')
