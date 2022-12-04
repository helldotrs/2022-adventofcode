#by hellmak.com

with open("day03-data", "r") as data:
    list_1d = (data.read()).split("\n")

char_list       =   "abcdefghijklmnopqrstuvwxyz"
char_list       +=  char_list.upper()
char_list       = str(char_list)

def make_flat_list(list):
    flat_list = []

    for x in list:
        flat_list.append(x)

    return flat_list

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
            x = x[0] #* 
            y = char_list.index(x)
            y += 1
            result += y
    return result

def solve_part1():
    list_2d = make_2d_list(list_1d)
    doubles = find_doubles(list_2d)
    #*should flatten doubles and remove line 45 but it does not work. Code works so I will just leave it
    print("pt1:"+str(calculate_points(doubles)))

solve_part1()

"""
part2:
"""
def make_groups(list):
    groups_list = []
    group       = []
    i           = 0
    for x in list_1d:
        group.append(x)
        i   += 1
        if(i>=3):       
            groups_list.append(group)
            group   = []
            i       = 0
    return groups_list

def find_trips(my_list):
    result = []
    for x in my_list:
        item1, item2, item3 = x[0], x[1], x[2]
    #stolen code start (https://www.geeksforgeeks.org/python-program-find-common-elements-three-lists-using-sets/)
        # Converting the arrays into sets
        s1 = set(item1)
        s2 = set(item2)
        s3 = set(item3)
        
        # Calculates intersection of 
        # sets on s1 and s2
        set1 = s1.intersection(s2)
        
        # Calculates intersection of sets
        # on set1 and s3
        result_set = set1.intersection(s3)
        
        # Converts resulting set to list
        final_list = list(result_set)
        #stolen code end
        result.append(final_list)
        
    return result

def solve_part1():
    groups  = make_groups(list_1d)
    trips           = find_trips(groups)
    trips_1d        = make_flat_list(trips)
    part2_solution  = calculate_points(trips_1d)
    print("pt2:"+str(part2_solution))

solve_part1()

