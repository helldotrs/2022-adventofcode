#by hellmak.com

with open("day03-data", "r") as data:
    list_1d = (data.read()).split("\n")

char_list       =   "abcdefghijklmnopqrstuvwxyz"
char_list       +=  char_list.upper()
char_list       = str(char_list)

def make_2d_list(list):
    list_2d = []

    for x in list:
        length      = len(x)
        half_length = length // 2
        
        list_item1          = x[0:half_length]
        list_item2          = x[half_length:]
        list_2d.append([list_item1,list_item2])   
    return list_2d

def find_doubles(list):
    results = []
    for x in list:
        sub_list_item1  = x[0]
        sub_list_item2  = x[1] 
        doubles = [value for value in sub_list_item1 if value in sub_list_item2]
        results.append(doubles)
       
    return results

def calculate_points(list):
    result = 0
    for x in list:
        if x: #because nano and kwrite adds a blank line at the end
            x = x[0]
            y = char_list.index(x)
            y += 1
            result += y
    return result

def solve_part1():
    list_2d = make_2d_list(list_1d)
    doubles = find_doubles(list_2d)
    print("part1:"+str(calculate_points(doubles)))

solve_part1()

"""
part2:
"""
