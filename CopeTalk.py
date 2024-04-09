import random
ascii_low = 32
ascii_high = 126
def decrypt(landing_input):
    input2 = p(landing_input)
    input2 = d(input2,0)
    input2.reverse()
    input2 = v(input2,g(120,seed=3))
    input2 = d(input2,1)
    input2.reverse()
    input2 = v(input2,g(500,seed=5))
    input2 = v(input2,g(441,seed=120))
    input2 = v(input2,g(441,seed=125))
    input2 = v(input2,g(128,seed=10))
    input2 = v(input2,g(300,seed=129))
    input2 = ps(input2)
    input2 = nc(input2,1)
    input2 = d(input2,0)
    input2 = e(input2)
    input2 = f(input2)
    input2.reverse()
    input2 = r(input2)
    input2 = d(input2,1)

    return input2
def d(t_input,index):
    for i in range(len(t_input)):
        if index == 0:
            temp = ord(t_input[i])-3
            index = 1
        else:
            temp = ord(t_input[i])+3
            index = 0
        if temp < ascii_low:
            temp += (ascii_high-ascii_low)+1
        if temp > ascii_high:
            temp -= (ascii_high-ascii_low)+1
        t_input[i]=chr(temp)
    return t_input
def f(t_input):
    fib = [0,1]
    i=2
    while fib[i-1]<len(t_input):
        fib.append(fib[i-1]+ fib[i-2])   
        index1 = fib[i] 
        i+=1
        fib.append(fib[i-1]+ fib[i-2])   
        index2 = fib[i] 
        i+=1
        if index1 < len(t_input) and index2 < len(t_input):
            temp =t_input[index1]
            t_input[index1] = t_input[index2]
            t_input[index2] = temp
    return t_input
def e(t_input):
    e = list(str(int(((1+1/10000)**10000)*10**18)))
    j=0
    for i in range(len(e)):
        j+=int(e[i])
        if j>len(t_input): break
        t_input.pop(j)
        j-=1
    return t_input
def nc(t_input,index):
    amount=5
    random.seed()
    if index == 1:
        return t_input[amount:len(t_input)-amount]
    if index == 0:
        f = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        for i in range(amount):
            index2 = random.randint(0, len(f) - 1)
            t_input.insert(0, f[index2]) 
            index2 = random.randint(0, len(f) - 1)
            t_input.append(f[index2])
        return t_input
def ps(t_input):
    i = 0
    j = len(t_input)-1
    while i<j:
        temp = t_input[i]
        t_input[i] = t_input[j]
        t_input[j] = temp
        i+=2
        j-=2
    return t_input
def v(t_input,key):
    out = []
    key_length = len(key)
    for i in range(len(t_input)):
        shift = ord(key[i % key_length]) - 32 
        decrypted_char = chr((ord(t_input[i]) - 32 - shift) % 95 + 32)
        out.append(decrypted_char)
    return out
def p(t_input):
    pi=list(str(31415926535897932384626433832795288419716939937515))
    j=0
    for i in range(len(pi)):
        j+=int(pi[i])
        if j>len(t_input): break
        t_input.pop(j)
        j-=1
    return t_input
def r(t_input):
    pad_const=9
    if t_input[0].isdigit():
        length = int(t_input[0])
        if length <= pad_const:
            for i in range(pad_const - length):
                t_input.pop(0)
            t_input.pop(0)
    else:
        t_input.pop(0)
    return t_input
def g(length, seed=None):
    if seed is not None:
        random.seed(seed)
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    random_string = ''.join(random.choice(characters) for _ in range(length)) 
    return random_string
def main():
    with open("in.txt", 'r') as file:
        landing_input = file.read()
    t_input = [i for i in landing_input]
    result = decrypt(t_input)
    final = ''.join(map(str, result))
    print(final)
main()