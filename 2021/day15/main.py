with open("input.txt") as f:
    content = [list(map(int,x)) for x in f.read().split("\n")[:~0]]

def risk_neighbors(node):
    risk = content[node[0]][node[1]]
    risk_1 = 1000000
    risk_2 = 1000000
    try:
        risk_1 = risk + content[node[0] + 1][node[1]]
    except:
        pass
    try:
        risk_2 = risk + content[node[0]][node[1]+1]
    except:
        pass
    return min([risk_1,risk_2])

def find_path():
    risk = 0
    while cur_node != (len(content[0])-1,len(content)-1):
        

answer_one = find_path()
#answer_two =
print("p1:",answer_one)
#print("p2:",answer_two)
