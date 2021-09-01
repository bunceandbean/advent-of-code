import hashlib
answer = 0

input = 'bgvyzdsv'

num = 0
while(True):
    condition = input + str(num)
    condition = condition.encode('utf-8')
    if hashlib.md5(condition).hexdigest()[:6] == "000000":
        answer = num
        break
    num += 1

print(answer)
