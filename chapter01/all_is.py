class Nums(object):
    def __init__(self, num):
        self.num = num
    def __abs__(self):
        return abs(self.num)

my_num = Nums(-1)
print(abs(my_num))

