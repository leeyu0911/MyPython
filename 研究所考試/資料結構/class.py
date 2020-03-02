class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name  # 這是定義hidden_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)


f = Duck('ASDF')
print(f.name)
