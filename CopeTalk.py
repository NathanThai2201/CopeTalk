import random

ascii_low = 32
ascii_high = 126

def encrypt(landing_input):
    input2 = double_caesar(landing_input,0)
    input2.reverse()
    input2 = fibonacci_swap(input2)
    input2 = euler_estimate_insert(input2)
    input2 = no_cap(input2,0)
    input2 = palindrome_swap(input2)
    input2 = vigenere(input2,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.')
    input2.reverse()
    input2 = vigenere(input2,'Coperime was here!')
    input2.reverse()
    input2 = double_caesar(input2,1)
    input2 = pi_estimate_insert(input2)
    input2 = zalgo(input2)
    return input2

def decrypt(landing_input):
    input2 = reverse_zalgo(landing_input)
    input2 = pi_estimate_pop(input2)
    input2 = double_caesar(input2,0)
    input2.reverse()
    input2 = vigenere_reverse(input2,'Coperime was here!')
    input2.reverse()
    input2 = vigenere_reverse(input2,'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.')
    input2 = palindrome_swap(input2)
    input2 = no_cap(input2,1)
    input2 = euler_estimate_pop(input2)
    input2 = fibonacci_swap(input2)
    input2.reverse()
    input2 = double_caesar(input2,1)
    return input2

def double_caesar(t_input,index):
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
def fibonacci_swap(t_input):
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
def euler_estimate_insert(t_input):
    e = list(str(int(((1+1/10000)**10000)*10**18)))
    f = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    j=0
    for i in range(len(e)):
        j+=int(e[i])
        if j>len(t_input): break
        index = random.randint(0, len(f) - 1)
        t_input.insert(j,f[index])
    return t_input
def euler_estimate_pop(t_input):
    e = list(str(int(((1+1/10000)**10000)*10**18)))
    j=0
    for i in range(len(e)):
        j+=int(e[i])
        if j>len(t_input): break
        t_input.pop(j)
        j-=1
    return t_input
def no_cap(t_input,index):
    amount=5

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
def palindrome_swap(t_input):
    i = 0
    j = len(t_input)-1
    while i<j:
        temp = t_input[i]
        t_input[i] = t_input[j]
        t_input[j] = temp
        i+=2
        j-=2
    return t_input
def vigenere(t_input,key):
    out = []
    key_length = len(key)
    for i in range(len(t_input)):
        shift = ord(key[i % key_length]) - 32
        encrypted_char = chr((ord(t_input[i]) - 32 + shift) % 95 + 32)
        out.append(encrypted_char)
    return out
def vigenere_reverse(t_input,key):
    out = []
    key_length = len(key)
    for i in range(len(t_input)):
        shift = ord(key[i % key_length]) - 32 
        decrypted_char = chr((ord(t_input[i]) - 32 - shift) % 95 + 32)
        out.append(decrypted_char)
    return out
def pi_estimate_insert(t_input):
    pi=list(str(31415926535897932384626433832795028841971))
    f = f = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    j=0
    for i in range(len(pi)):
        j+=int(pi[i])
        if j>len(t_input): break
        index = random.randint(0, len(f) - 1)
        t_input.insert(j,f[index])
    return t_input
def pi_estimate_pop(t_input):
    pi=list(str(31415926535897932384626433832795028841971))
    j=0
    for i in range(len(pi)):
        j+=int(pi[i])
        if j>len(t_input): break
        t_input.pop(j)
        j-=1
    return t_input
def zalgo(t_input):
    marks = list(map(chr, range(768, 879)))
    string = ''.join(map(str,t_input))
    words = string.split()
    final = ' '.join(''.join(c + ''.join(random.choice(marks) for _ in range(i // 2 + 1)) * c.isalnum() for c in word) for i, word in enumerate(words))
    final = [i for i in final]
    return final
def reverse_zalgo(t_input):
    string = ''.join(map(str,t_input))
    words = string.split()
    reconstructed_words = []

    for word in words:
        reconstructed_word = ""
        i = 0
        while i < len(word):
            reconstructed_word += word[i]
            i += 1
            while i < len(word) and ord(word[i]) >= 768 and ord(word[i]) <= 879:
                i += 1
        reconstructed_words.append(reconstructed_word)
    final = ' '.join(reconstructed_words)
    final = [i for i in final]
    return final
def main():
    landing_input = input('Input:')
    t_input = [i for i in landing_input]
    mode = input("Encrypt or Decrypt? [E/D]").lower()
    if mode == "e":
        result = encrypt(t_input)
    if mode == "d":
        result = decrypt(t_input)
    final = ''.join(map(str, result))
    print(final)
    return 0

main()