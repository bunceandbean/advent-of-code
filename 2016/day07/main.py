with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[0:~0]

def ips(content):
    num_abba = 0
    num_ssl = 0
    for ip in content:
        hypers = ""
        while "[" in ip:
            hyper = ip[ip.index("[")+1:ip.index("]")]
            hypers += hyper + "|"
            ip = ip[:ip.index("[")] + "|" + ip[ip.index("]")+1:]
        if abba(ip) and not abba(hypers):
            num_abba += 1
        seqs = ssl_aba(ip)
        if ssl_bab(hypers, seqs):
            num_ssl += 1
    return [num_abba, num_ssl]

def abba(sec):
    for i in range(len(sec)-3):
        if sec[i:i+2] == sec[i+2:i+4][::-1] and sec[i:i+2] != sec[i+2:i+4]:
            return True
    return False

def ssl_aba(sec):
    aba = []
    for i in range(len(sec)-2):
        sec_1 = sec[i:i+2]
        sec_2 = sec[i+1:i+3]
        if sec_1 == sec_2[::-1] and sec_1 != sec_2:
            aba.append(sec[i+1] + sec[i] + sec[i+1])
    return aba

def ssl_bab(sec,aba):
    for seq in aba:
        if seq in sec:
            return True
    return False


answers = ips(content)
answer_one = str(answers[0])
answer_two = str(answers[1])
print("p1: " + answer_one)
print("p2: " + answer_two)
