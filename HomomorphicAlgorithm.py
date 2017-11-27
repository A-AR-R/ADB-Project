__author__ = 'Alipour'
import random
from RandomGeneratorAlgorithms import RandomGenerator
from utils import string2integer,integer2string,split_string
from PermutionAlgorithms import sattoloCycle
class HomomorphicEncryption():
    def __init__(self):
        self.srg=None
    def set_text(self,text,seed):
        self.srg=RandomGenerator(seed)
        self.text=text
        self.li_len=len(self.text)/3
        self.ri_len=len(self.text)-self.li_len
        self.li=string2integer(text[:self.li_len])
        self.ri=string2integer(text[self.li_len:])
    def get_sio(self,index):
        self.sio=self.srg.generate_ith_sio(index,self.li_len*8)
        return self.sio
    def get_cioL(self):
        self.cioL=self.sio^self.li
        return self.cioL
    def generate_homomorphic_key(self):
        self.key_len=self.ri_len/2
        self._key=[]
        if self.ri_len%2!=0:
            self.key_len+=1
        random.seed(self.cioL)
        for i in range(self.key_len):
            self._key.append(random.randint(i,self.ri_len-1))
    def get_fkio(self):
        sio_string_list=split_string(integer2string(self.sio))
        fkio=sattoloCycle(sio_string_list,self._key)
        fkio="".join(fkio)
        self.fkio=string2integer(fkio)
        return self.fkio
    def get_cioR(self):
        return self.fkio^self.ri
class ValidateHomomorphicEncryption():
    def __init__(self,enc1,enc2):
        self.cioL,self.cioR=enc1
        self.ciqL,self.ciqR=enc2
    def XorFirstHalves(self):
        self.XoredFirstHalves=self.cioL^self.ciqL
        return self.XoredFirstHalves
    def XorSecondHalves(self):
        self.XoredSecondHalves=self.cioR^self.ciqR
        return self.XoredSecondHalves
    def GenerateHomomorphicKey(self):
        self.key_len=len(integer2string(self.ciqR))/2
        self._key=[]
        if self.ciqR%2!=0:
            self.key_len+=1
        random.seed(self.XoredFirstHalves)
        for i in range(self.key_len):
            self._key.append(random.randint(i,len(integer2string(self.ciqR))-1))
    def CalulateSecondHalvesWithHomomorphicFeature(self):
        XoredFirstHalves_string_list=split_string(integer2string(self.XoredFirstHalves))
        XoredSecondHalvesWithHomomorphicFeature=sattoloCycle(XoredFirstHalves_string_list,self._key)
        XoredSecondHalvesWithHomomorphicFeature="".join(XoredSecondHalvesWithHomomorphicFeature)
        self.XoredSecondHalvesWithHomomorphicFeature=string2integer(XoredSecondHalvesWithHomomorphicFeature)
        return self.XoredSecondHalvesWithHomomorphicFeature


