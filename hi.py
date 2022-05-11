import random
import time

class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1
    
class FindE:
    def __init__(self):
        self.n = 0
        self.i = 0
    def generating_numbers(self,nn):
        s=0
        for a in range(nn):
            number = random.uniform(0,1)
            s+=number
            if s>1:
                self.n=a
                for _ in range(nn):
                    self.n+=a
                    self.i+=1
                    s=0
    def value_of_e(self):
        return (self.n/self.i)
    
##  HÜSNA İBİŞ 180315033