from copy import deepcopy
import matplotlib.pyplot as plt
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    points = {tuple(map(int,x.split(","))) for x in content if "," in x}
    folds = [x[x.index("g")+2:] for x in content if "fold" in x]

def paper(points):
    first_fold = 0
    for fold in folds:
        new_points = set()
        axis = int(fold[fold.index("=")+1:])
        for point in points:
            if "x" in fold:
                if point[0] >= axis:
                    new_points.add((point[0]-(2*(point[0]-axis)),point[1]))
                else:
                    new_points.add(point)
            else:
                if point[1] >= axis:
                    new_points.add((point[0],point[1]-(2*(point[1]-axis))))
                else:
                    new_points.add(point)
        if folds.index(fold) == 0:
            first_fold = len(new_points)
        points = deepcopy(new_points)
    return [first_fold,points]

folded = paper(points)
answer_one = folded[0]
answer_two = "PLOT"
print("p1:",answer_one)
print("p2:",answer_two)
plt.scatter(*zip(*folded[1]))
plt.show()
