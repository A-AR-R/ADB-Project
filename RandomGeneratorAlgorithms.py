__author__ = 'Alipour'
import random

class RandomGenerator():
    def __init__(self,seed):
        self.seed=seed
        self.index=0
        random.seed(seed)
    def generate_ith_sio(self,i,length):
        random.seed(self.seed)
        while i>0:
            random.getrandbits
            i-=1
        return random.getrandbits(length)
    def get_sio(self,length):
        sio=random.getrandbits(length)
        self.index+=1
        return self.index-1,sio