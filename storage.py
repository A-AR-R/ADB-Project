import os
class Storage():
    def __init__(self):
        self.keywords=[]
        if os.path.exists("database.bin"):
            self.database = open("database.bin", "rb")
            line = self.database.readline()
            while line:
                h, cioL, cioR = line.strip().split(",,,,")
                self.keywords.append([h.decode("hex"), int(cioL.decode("hex")), int(cioR.decode("hex"))])
                line = self.database.readline()
            self.database.close()
            self.database = open("database.bin", "ab")
        else:
            self.database = open("database.bin", "w+")
    def set_new_keyword(self,h,cioL,cioR):
        self.keywords.append([h,cioL,cioR])
        self.database.write(h.encode("hex")+",,,,"+str(cioL).encode("hex")+",,,,"+str(cioR).encode("hex")+"\n")