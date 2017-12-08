__author__ = 'Alipour'
import random
from RandomGeneratorAlgorithms import RandomGenerator
from utils import string2integer,integer2string,split_string
from PermutionAlgorithms import sattoloCycle
import hashlib
class HomomorphicEncryption():
    def __init__(self):
        self.srg=None
    def set_text(self,text,seed):
        self.srg=RandomGenerator(seed)
        self.text=text
        # if(len(self.text))%2!=0:
        #     self.text+="0"
        self.half_len=len(self.text)/2
        self.li=string2integer(text[:self.half_len])
        self.ri=string2integer(text[self.half_len:])
    def get_li(self):
        return self.li
    def get_ri(self):
        return self.ri
    def get_sio(self):
        m = hashlib.sha256()
        m.update(integer2string(self.li))
        self.index=string2integer(m.digest()[5:7])
        self.sio=self.srg.generate_ith_sio(self.index,self.half_len*8)
        return self.sio
    def get_sio_2(self):
        m = hashlib.sha256()
        m.update(integer2string(self.li))
        self.index = string2integer(m.digest()[7:9])
        self.sio = self.srg.generate_ith_sio(self.index, self.half_len * 8)
        return self.sio
    def get_cioL(self):
        self.cioL=self.sio^self.li
        return self.cioL
    def generate_key(self):
        m = hashlib.sha256()
        m.update(integer2string(self.li))
        return m.digest()[:self.half_len/2]
    def get_index(self):
        return self.index
    def get_fkio(self):
        sio_string_list=split_string(integer2string(self.sio))
        # self.fkio=sattoloCycle(sio_string_list,self._key)
        self.fkio = sattoloCycle(sio_string_list, self.generate_key())
        # self.fkio = sattoloCycle(sio_string_list, self.cioL)
        self.fkio="".join(self.fkio)
        self.fkio=string2integer(self.fkio)
        return self.fkio
    def get_cioR(self):
        return self.fkio^self.ri
class ValidateHomomorphicEncryption():
    def __init__(self,key,enc1,enc2):
        self.key=key
        self.cioL,self.cioR=enc1
        self.ciqL,self.ciqR=enc2
    def XorFirstHalves(self):
        self.XoredFirstHalves=self.cioL^self.ciqL
        return self.XoredFirstHalves
    def XorSecondHalves(self):
        self.XoredSecondHalves=self.cioR^self.ciqR
        return self.XoredSecondHalves

    def CalulateSecondHalvesWithHomomorphicFeature(self):
        XoredFirstHalves_string_list=split_string(integer2string(self.XoredFirstHalves))
        # XoredSecondHalvesWithHomomorphicFeature=sattoloCycle(XoredFirstHalves_string_list,self._key)
        XoredSecondHalvesWithHomomorphicFeature = sattoloCycle(XoredFirstHalves_string_list, self.key)
        XoredSecondHalvesWithHomomorphicFeature="".join(XoredSecondHalvesWithHomomorphicFeature)
        self.XoredSecondHalvesWithHomomorphicFeature=string2integer(XoredSecondHalvesWithHomomorphicFeature)
        return self.XoredSecondHalvesWithHomomorphicFeature


