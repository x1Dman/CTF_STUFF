from pwn import *

b = "".encode('ascii')
conn = remote('wat.level-up.2019.tasks.cyberchallenge.ru', 19004)
key = "50393485785736294056928581103795939002"
key_test = ""
i = 0
answ = ''
while i < 10:
    conn.send(key + str(i))
    r = True
    try:
        conn.send("*")
        b = conn.recvuntil('\n', drop = True)
    except:
        r = False
    if r:
        print(b)
        key += str(i)
        print(key)
        i = 0
    conn.close()
    conn = remote('wat.level-up.2019.tasks.cyberchallenge.ru', 19004)
    i += 1
