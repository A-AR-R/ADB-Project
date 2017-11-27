# -*- coding: utf-8 -*-
# from random import randint, random,randrange
# from math import floor
#
# def fisher_yates_shuffle(the_list):
#     list_range = range(0, len(the_list))
#     keys=[]
#     key=[4, 6, 5, 6, 4, 5, 6]
#     for i in list_range:
#     # for i in range(4):
#         j = randint(list_range[i], list_range[-1])
#         keys.append(j)
#         j=key[i]
#         the_list[i], the_list[j] = the_list[j], the_list[i]
#     return the_list,keys
#
#
# def fisher_yates_shuffle_improved(the_list):
#     amnt_to_shuffle = len(the_list)
#     # We stop at 1 because anything * 0 is 0 and 0 is the first index in the list
#     # so the final loop through would just cause the shuffle to place the first
#     # element in... the first position, again.  This causes this shuffling
#     # algorithm to run O(n-1) instead of O(n).
#     while amnt_to_shuffle > 1:
#         # Indice must be an integer not a float and floor returns a float
#         i = int(floor(random() * amnt_to_shuffle))
#         # We are using the back of the list to store the already-shuffled-indice,
#         # so we will subtract by one to make sure we don't overwrite/move
#         # an already shuffled element.
#         amnt_to_shuffle -= 1
#         # Move item from i to the front-of-the-back-of-the-list. (Catching on?)
#         the_list[i], the_list[amnt_to_shuffle] = the_list[amnt_to_shuffle], the_list[i]
#     return the_list
# print fisher_yates_shuffle([1,3,4,7,8,9,3])
# print fisher_yates_shuffle([2,4,7,6,12,11,15])
# while True:
#     # i,j=fisher_yates_shuffle([1,3,4,7,8,9,3])
#     i,j=fisher_yates_shuffle([2,4,7,6,12,11,15])
#     if i==[12,15,11,4,2,7,6]:
#         print j
#         break
#
#
# def sattoloCycle(items):
#     i = len(items)
#     while i > 1:
#         i = i - 1
#         j = randrange(i)  # 0 <= j <= i-1
#         items[j], items[i] = items[i], items[j]
#     return items
# print "------------------"
# print sattoloCycle([2,4,7,6,12,11,15])

# import random
# import binascii
# import base64
# from AES import string2bin,bin2string,char2bin,string2integer,integer2string
# from AES import AESCipher
# import time


import datetime
from random import randrange


# def encrypt(text):
#     random.seed(datetime.datetime.now())
#     l=len(text)
#     s0= random.getrandbits(6*8)
#     s0_s = integer2string(s0)
#     print "random seed is :",s0
#     l0=string2integer(text[:6])
#     print "left part of string is :",l0
#     r0=string2integer(text[6:])
#     print "right part of string is :",r0
#     cl=s0^l0
#     print "left part of encryption is : ",cl
#
#     _key=[]
#
#     random.seed(cl)
#     for i in range(4):
#         _key.append(random.randint(i,len(integer2string(r0))-1))
#     print "permution key is : ",_key
#     list_s0_s=split_string(integer2string(s0))
#     # print p_key
#     cr=sattoloCycle(list_s0_s,_key)
#     cr="".join(cr)
#     cr=string2integer(cr)
#     print "right part of encryptio is :",cr
#     return cl,cr
# def validate(enc1,enc2):
#     print "--------"
#     clXorCr=enc1[0]^enc2[0]
#     print "sio xor siq is :",clXorCr
#     print "fkio(si0)XORfkiq is :", enc1[1]^enc2[1]
#     random.seed(enc1[0]^enc2[0])
#     _key=[]
#     for i in range(4):
#         _key.append(random.randint(i,6))
#     print "permution key is : ",_key
#     list_cl=split_string(integer2string(enc1[0]^enc2[0]))
#     cr=sattoloCycle(list_cl,_key)
#     cr="".join(cr)
#     cr=string2integer(cr)
#     print "fkioxorfkiq(sioXorsiq)XOR is :", cr
# e1=encrypt(p)
# print e1
# time.sleep(1)
# e2=encrypt(p)
# print e2
# validate(e1,e2)
import time
from HomomorphicAlgorithm import HomomorphicEncryption,ValidateHomomorphicEncryption
from datetime import datetime
h=HomomorphicEncryption()
h.set_text("advanced_database",datetime.now())
print "---------------"
sio=h.get_sio(0)
print "sio is :",sio
cioL=h.get_cioL()
print "cioL is :",cioL
_key=h.generate_homomorphic_key()
print "homomorphic key is :",_key
pad=h.get_fkio()
cioR=h.get_cioR()
print "cioR is :",cioR
time.sleep(1)
h2=HomomorphicEncryption()
h2.set_text("advanced_database",datetime.now())
print "---------------"
sio2=h2.get_sio(0)
print "sio is :",sio2
cioL2=h2.get_cioL()
print "cioL is :",cioL2
_key2=h2.generate_homomorphic_key()
print "homomorphic key is :",_key2
h2.get_fkio()
cioR2=h2.get_cioR()
print "cioR is :",cioR
print "---------------"

v=ValidateHomomorphicEncryption((cioL,cioR),(cioL2,cioR2))
v.XorFirstHalves()
v.GenerateHomomorphicKey()
if v.XorSecondHalves()==v.CalulateSecondHalvesWithHomomorphicFeature():
    print "matched"
else:
    print "didnt match"


print "**************************************"

h3=HomomorphicEncryption()
h3.set_text("advanced_database",datetime.now())
print "---------------"
sio3=h3.get_sio(0)
print "sio is :",sio3
cioL3=h3.get_cioL()
print "cioL is :",cioL3
_key3=h3.generate_homomorphic_key()
print "homomorphic key is :",_key3
pad3=h3.get_fkio()
cioR3=h3.get_cioR()
print "cioR is :",cioR3
time.sleep(1)
h4=HomomorphicEncryption()
h4.set_text("database_advanced",datetime.now())
print "---------------"
sio4=h4.get_sio(0)
print "sio is :",sio4
cioL4=h4.get_cioL()
print "cioL is :",cioL4
_key4=h4.generate_homomorphic_key()
print "homomorphic key is :",_key4
h4.get_fkio()
cioR4=h4.get_cioR()
print "cioR is :",cioR4
print "---------------"

v=ValidateHomomorphicEncryption((cioL3,cioR3),(cioL4,cioR4))
v.XorFirstHalves()
v.GenerateHomomorphicKey()
if v.XorSecondHalves()==v.CalulateSecondHalvesWithHomomorphicFeature():
    print "matched"
else:
    print "didnt match"
