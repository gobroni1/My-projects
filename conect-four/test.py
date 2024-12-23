# board = ['0', '1', '2', '3', '4', '5', '🔴', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '🔴', '24', '🟢', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41']

# ls1= []
# ls2 = []

# for i in range(len(board)):
#     if board[i] == "🔴":
#         ls1.append(i)
#     elif board[i] == '🟢':
#         ls2.append(i)
        
# print(ls1)
# print(ls2)


import itertools

# Your input list
numbers = [1, 2, 3, 4, 5]

# Generate all possible quadruplets
quadruplets = [list(quad) for quad in itertools.combinations(numbers, 4)]
print(quadruplets)




def column(matrix):
    for row_index, row in enumerate(matrix): 
        for col_index in range(1, len(row)):  
            if row[col_index] - row[col_index - 1] == 7:
                return True, row_index, col_index  
    return False


 

    
print(column([[28, 30, 31, 37], [28, 30, 31, 39], [28, 30, 37, 39], [28, 31, 37, 39], [30, 31, 37, 39]]))