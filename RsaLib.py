# coding utf-8
import math
import random
from fractions import gcd


class Rsa():
    def __init__(self):
        self.p = 0  # nombre premier p
        self.q = 0  # nombre premier q
        self.n = 0  # nombre n=p*q
        self.dn = 0  # nombre dn=(p-1)(q-1)
        self.e = 0  # p,q<e<dn (composante de la cles publique)
        self.d = 0  # p,q<d<n (composante de la cles privee)
        self.messcr = []
        self.messdcr = []

    def generateP(self):

        #On génére un nombre p premier

        tab_p=[]
        p = random.randint(155, 256)

        i=1
        while i<=p:
            if p%i==0:
                tab_p.append(i)
            if len(tab_p)>2:
                del tab_p[0:i]
                p = random.randint(155,256)
                i=0
            i+=1

        if len(tab_p)==2:
            self.p = p

    def generateQ(self):

        #On génére un nombre q premier

        tab_q = []
        q = random.randint(155, 256)
        j=1
        while j<=q:
            if q%j==0:
                tab_q.append(j)
            if len(tab_q)>2:
                del tab_q[0:j]
                q=random.randint(155,256)
                j=0
            j+=1

        if len(tab_q)==2:
            self.q = q


    def opd(self):

        self.n = self.p * self.q
        self.dn = (self.p - 1) * (self.q - 1)

    def findE(self):

        e = 0
        if (self.p > self.q):
            e = self.p + 1
        else:
            e = self.q + 1

        while gcd(self.dn, e) != 1:
            e += 1
        self.e = e

    def encrypt(self, mess, e_exp, n_exp):  # e expediteur et n expediteur (cles publique de l'expediteur)

        tab_ascii = []

        for chara in mess:
            tab_ascii.append(ord(chara))
        print(tab_ascii)

        for l in tab_ascii:
            self.messcr.append((l ** e_exp) % n_exp)
        print(self.messcr)

    def findD(self):
        d = 0

        if (self.p > self.q):
            d = self.p + 1
        else:
            d = self.q + 1

        while self.e * d % self.dn != 1:
            d += 1

        self.d = d

    def decrypt(self, mess_cr):

        mess_dcr = []

        for i in mess_cr:
            mess_dcr.append((i ** self.d) % self.n)
        print(mess_dcr)

        for j in mess_dcr:
            self.messdcr.append(chr(j))

    #SETTERS
    #AND
    #GETTERS

    def set_p(self,p):
        self.p = p

    def set_q(self,q):
        self.q = q

    def set_e(self,e):
        self.e = e

    def set_n(self,n):
        self.n = n

    def set_dn(self,dn):
        self.dn = dn

    def set_d(self,d):
        self.d = d

    def set_messcr(self,messcr):
        self.messcr = messcr

    def set_messdcr(self,messdcr):
        self.messdcr = messdcr

    def get_p(self):
        return self.p

    def get_q(self):
        return self.q

    def get_e(self):
        return self.e

    def get_n(self):
        return self.n

    def get_dn(self):
        return self.dn

    def get_d(self):
        return self.d

    def get_messcr(self):
        return self.messcr

    def get_messdcr(self):
        return self.messdcr


rsa = Rsa()
rsa.generateP()
rsa.generateQ()

print (rsa.get_p()," et ",rsa.get_q())

rsa.opd()
rsa.findE()

print ("n: ",rsa.get_n()," dn ",rsa.get_dn())
print ("e: ",rsa.get_e())

rsa.encrypt("elies",rsa.get_e(),rsa.get_n())

print(rsa.get_messcr())

rsa.findD()
print("d: ",rsa.get_d())

rsa.decrypt(rsa.get_messcr())
print(rsa.get_messdcr())
