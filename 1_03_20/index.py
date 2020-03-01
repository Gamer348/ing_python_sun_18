# class Ceasar:
#     def __init__(self):
#         self.input_str = input('Enter the string to code ')
#         self.shift = int(input()) % 26
#         self.code()
    
#     def code(self):
#         output_str = ""
#         for i in range(len(self.input_str)):
#             if self.input_str[i] >= 'a' and self.input_str[i] <= 'z' or self.input_str[i] >= 'A' and self.input_str[i] <= 'Z':
#                 if chr(ord(self.input_str[i]) + self.shift) > 'Z' or chr(ord(self.input_str[i]) + self.shift) > 'z':
#                     output_str += chr(ord(self.input_str[i]) + (self.shift - 26))
#                 else:
#                     output_str += chr(ord(self.input_str[i]) + (self.shift))
#             else:
#                 output_str += self.input_str[i]
#         print(output_str)

# Ceasar_test = Ceasar()

size_matrix = int(input())
list_db = [[0] * size_matrix for i in range(size_matrix)]
    
for i in range(size_matrix):
    for j in range(size_matrix):
        print(list_db[i][j], end=' ')
    print()


