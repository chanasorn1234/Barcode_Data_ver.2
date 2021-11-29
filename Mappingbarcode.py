import random
class MappingBarcode:
    def __init__(self):
        self.checkid = None
        self.input = None
        self.file_read = None
        self.file2_read = None
        self.file3_read = None
    def Mapping(self):
        self.file_read = open("DataBarcode.txt")
        self.file3_read = open("DataBarcodemapping.txt",'w')
        while(True):
            #print("666")
            self.input = str(self.file_read.readline())#[9:13]
            if(self.input == ""):
                break
            self.file2_read = open("data.txt",encoding='utf-8')
            while(True):
                #print(self.input[9:13])
                self.checkid = str(self.file2_read.readline())#[2:6]
                if(self.checkid[9:13] == self.input[9:13]):
                    #print("kuy")
                    #self.file3_read.write(self.input[0:9])
                    self.file3_read.write(self.checkid)
                    self.file3_read.write("\n")
                    self.file2_read.close()                  
                    break
                if(self.checkid == ""):
                    break
        self.file_read.close()
        self.file2_read.close()
        self.file3_read.close()
        self.input = None
        self.checkid = None

    def CleardataInfile(self):
        self.file_read = open("DataBarcodemapping.txt")
        x = str(self.file_read.readline())
        while(x != ""):
            write2 = open("DataBarcodemapping.txt",'w')
            write2.write('\n')
            write2.close()
            x = str(self.file_read.readline())

test = MappingBarcode()
test.CleardataInfile()
test.Mapping()








# o = open("DataBarcodemapping.txt",'w')

# #o.write("666")
# o.write("\n")
# o.write("\n")
# o.write("777")
# #print(o.readline())

