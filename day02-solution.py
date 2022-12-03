"""
part 1:
"""
with open("day02-input", "r") as data:
    input_list = (data.read()).split("\n")

x_list = []
for x in input_list:
    x = x.replace(" ","").replace("A","1").replace("B","2").replace("C","3").replace("X","1").replace("Y","2").replace("Z","3")
    x_list.append(x)                   
input_list = x_list

lose    = 0
draw    = 3
win     = 6

def pass_list_to_var(x):
    theirs  = int(x[0])
    ours    = int(x[1])
    return theirs, ours

def get_part_score(theirs, ours):      
    score = check_move_point(ours)
    score += check_win_status(theirs, ours)
    return score
    
def check_move_point(ours):
    score = ours
    return score 

def check_win_status(theirs, ours):
    score = 0

    if   ours == 1 and theirs == 3:
        score += win
    elif ours == 3 and theirs == 1:
        score += lose

    elif ours > theirs: 
        score += win
    elif ours < theirs:
        score += lose
    elif ours == theirs:
        score += draw

    else:
        exit("error:001")
    return score

def get_total_score(input_list):
    total_score = 0
    for x in input_list:
        theirs, ours = pass_list_to_var(x)
        total_score += get_part_score(theirs, ours)
    return total_score

print("pt1:"+str(get_total_score(input_list)))

"""
part 2:
"""
test_list = ["12", "21", "33"]

def pt2_main(my_list):
    ours        = 0
    score       = 0
    score_total = 0
    for x in my_list:
        theirs  = int(x[0])
        outcome = int(x[1])
        if outcome == 1: #lose
            if theirs == 1:
                ours = 3
            else:
                ours = theirs - 1
            score += lose


        if outcome == 2: #draw
            ours = theirs
            score += draw
            #print("draw")

        if outcome == 3: # win
            if theirs == 3:
                ours = 1
            else:
                ours = theirs + 1
            score += win
            #print("win")

        score       += ours
        score_total += score
        #print(score)
        #print(score_total)
        score       = 0 #reset
    return score_total


print("pt2:"+str(pt2_main(input_list)))
