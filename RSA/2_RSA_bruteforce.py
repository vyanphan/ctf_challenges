# RSA without d, but the numbers are small enough to factor quickly

def egcd(a,b):
    if a==0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b%a, a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a,m)
    if g!=1:
        raise Exception('no mod inverse')
    else:
        return x%m

#given information
n = 135906943524542517383614001105925563441567
e = 65537
C = 47670555806570176976539860452571518974695

#our two prime factors, thanks to WolframAlpha
p = 165190996343484901039
q = 822726096051557953553
m = (p-1) * (q-1)

#private key
d = modinv(e,m)

# C = M^e mod n; M = C^d mod n
M = pow(C, d, n) #outputs 0x656173796374667b7768336e5f7930755f683476655f7026715f5253415f697a5f657a5f34386635376136327d
M = hex(M)[2:-1].decode('hex')

print(M)