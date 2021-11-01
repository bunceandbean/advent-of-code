input = "1321131112"

def look_and_say(input,times):
    for i in range(times):
        chain = []
        stitch = []
        for char in input:
            if len(chain) == 0 or chain[0] == char:
                chain.append(char)
            else:
                stitch.append(str(len(chain)) + chain[0])
                chain = [char]
        stitch.append(str(len(chain)) + chain[0])
        input = "".join(stitch)
    return input

las_40_str = look_and_say(input,40)
answer_one = str(len(las_40_str))
answer_two = str(len(look_and_say(las_40_str,10)))
print("p1: " + answer_one)
print("p2: " + answer_two)
