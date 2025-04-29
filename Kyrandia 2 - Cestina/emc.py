# -*- coding: utf-8 -*-

#import cestina - slouzilo k odstraneni diakritiky, kdyz jsem jeste nemel ceske fonty

class EMC:
    """Dump & insert txt from Kyrandia 2 EMC files."""
    def __init__(self, emcFilename):
        try:
            self.emcFile = open(emcFilename, "r+b")
            self.emcFile.seek(0x10)
            self.textStart = self.__readedToInt(self.emcFile.read(4)) + 0x14   # textOffset = textStart + 8
            self.emcFile.seek(self.textStart+0x4)
            self.textLength = self.__readedToInt(self.emcFile.read(4)) #+ self.textStart + 0x08
            self.textDataStart = self.__readedToInt(self.emcFile.read(2)) + self.textStart + 0x08
        except IOError, error:
            raw_input("[-]ERROR: %s. Relative to: %s." % (error[1], emcFilename))
            exit()

        #self.invertTwoBytes = lambda tb: tb >> 8 | tb - ((tb >> 8) << 8) << 8

    def __readedToInt(self, readed):
        """Readed bytes will be int type."""
        readed_int = 0
        for x in readed:
            readed_int = (readed_int << 8) | ord(x)
        return readed_int

    def extract(self, txtFilename):
        """Dump text data from Kyrandia 2 EMC Files."""
        try:
            txtFile = open(txtFilename, "w+b")
        except IOError, error:
            raw_input("[-]ERROR: %s. Relative to: %s." % (error[1], txtFilename))
            exit()

        print "[+]Writing file, wait..."
        I = self.textStart + 0x8
        while I<self.textDataStart:
            self.emcFile.seek(I)
            stringPos = self.__readedToInt(self.emcFile.read(2)) + self.textStart + 0x8
            I = I + 2
            self.emcFile.seek(stringPos)
            stringData = ""
            stringChar = self.__readedToInt(self.emcFile.read(1))
            while stringChar>0:
                stringData = stringData + chr(stringChar)
                stringChar = self.__readedToInt(self.emcFile.read(1))
            txtFile.write(stringData+"\n")
        txtFile.close()
        raw_input("[>]Process Finish!!!\nPress any key to exit.")

    def insert(self, txtFilename):
        try:
            txtFile = open(txtFilename, "r+b")
        except IOError, error:
            raw_input("[-]ERROR: %s. Relative to: %s." % (error[1], txtFilename))
            exit()

        stringsList = list()
        stringPos = self.textDataStart - self.textStart - 0x08   #first line offset
        self.emcFile.seek(self.textDataStart)
        
        print "[+]Inserting file, wait..."
        while True:
            line = txtFile.readline() # Read a line
            #line = cestina.RemDia(line)
            if not line:
                break
            stringsList.append(stringPos)
            line = line[:-1]    #bez zalomeni
            stringPos = stringPos + len(line) + 1
            self.emcFile.write(line)
            self.emcFile.write(chr(0x00))
        
        self.emcFile.seek(self.textStart + 0x08)
        for cmdAddr in stringsList:
            #raw_input(cmdAddr)
            self.emcFile.write(chr(cmdAddr >> 8))
            self.emcFile.write(chr(cmdAddr & 0xFF))
        raw_input("[>]Process Finish!!!\nPress any key to exit.")
        self.emcFile.close()
