class Ceasar:
    def __init__(self):
        self.input = input()
        self.shift = int(input())
        self.cypher()
    
    def cypher(self):
        res = ""
        for i in range(len(self.input)):
            if ord(self.input[i]) >= ord('a') and ord(self.input[i]) <= ord('z'):
                res += chr(ord(self.input[i]) + self.shift)
        print(res)

test = Ceasar()