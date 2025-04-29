# -*- coding: utf-8 -*-

#import cestina

class DLG:
    """Dump & insert txt from Kyrandia 2 dl* files."""
    def __init__(self, dlgFilename):
        try:
            self.dlgFile = open(dlgFilename, "r+b")
            self.dlgFile.seek(0xA0)
        except IOError, error:
            raw_input("[-]ERROR: %s. Relative to: %s." % (error[1], dlgFilename))
            exit()

        self.invertTwoBytes = lambda tb: tb >> 8 | tb - ((tb >> 8) << 8) << 8

    def __readedToInt(self, readed):
        """Readed bytes will be int type."""
        readed_int = 0
        for x in readed:
            readed_int = (readed_int << 8) | ord(x)
        return readed_int

    def extract(self, txtFilename):
        """Dump text data from Kyrandia 2 dl* Files."""
        try:
            txtFile = open(txtFilename, "w+b")
        except IOError, error:
            raw_input("[-]ERROR: %s. Relative to: %s." % (error[1], txtFilename))
            exit()

        print "[+]Writing file, wait..."
        while True:
            command = self.invertTwoBytes(self.__readedToInt(self.dlgFile.read(2))) # Get first 2 bytes
            if not command:
                break
            elif command == 0x0A or command == 0x04: # It's command bytes
                cmdId = self.invertTwoBytes(self.__readedToInt(self.dlgFile.read(2)))
                txtFile.write("<c:%d|i:%d>\n" % (command, cmdId))
            else: # It's a character id
                lenght = self.invertTwoBytes(self.__readedToInt(self.dlgFile.read(2)))
                txtId = self.invertTwoBytes(self.__readedToInt(self.dlgFile.read(2)))
                textData = self.dlgFile.read(lenght)
                txtFile.write("<p:%d|l:%d|i:%d>%s\n" % (command, lenght, txtId, textData))
        raw_input("[>]Process Finish!!!\nPress any key to exit.")

    def insert(self, txtFilename):
        try:
            txtFile = open(txtFilename, "r+b")
        except IOError, error:
            raw_input("[-]ERROR: %s. Relative to: %s." % (error[1], txtFilename))
            exit()

        commandAddressList = list()
        print "[+]Inserting file, wait..."
        while True:
            line = txtFile.readline() # Read a line
            #line = cestina.RemDia(line)
            if not line:
                break
            # Treatment and write of commands
            elif line[:2] == "<c":
                splitedCommandLine = line.split("|")
                data1 = int(splitedCommandLine[0].replace("<c:", "")) # Get the value
                replace1 = splitedCommandLine[1].replace("i:", "") # Start the treatment of other 2 bytes
                data2 = int(replace1.replace(">", ""))
                # Write the command byte
                self.dlgFile.write(chr(data1 & 0xFF))
                self.dlgFile.write(chr(data1 >> 8))
                # Write the id
                if data1 != 10 or data2 != 0:
                    self.dlgFile.write(chr(data2 & 0xFF))
                    self.dlgFile.write(chr(data2 >> 8))
                if data1 == 10 and data2 != 0:
                    commandAddressList.append(self.invertTwoBytes(self.dlgFile.tell()))
                    
            # Treatment and write of String
            elif line[:2] == "<p":
                splitedTextLine = line.split(">")
                splitedValues = splitedTextLine[0].split("|")
                dataOne = int(splitedValues[0].replace("<p:", ""))
                dataTwo = int(splitedValues[1].replace("l:", ""))
                dataThree = int(splitedValues[2].replace("i:", ""))
                # Writing the character id
                self.dlgFile.write(chr(dataOne & 0xFF))
                self.dlgFile.write(chr(dataOne >> 8))
                # Writing the new String lenght
                splitedTextLine[1] = splitedTextLine[1][:-1] # Retrieve the ends
                self.dlgFile.write(chr((len(splitedTextLine[1])) & 0xFF))
                self.dlgFile.write(chr((len(splitedTextLine[1])) >> 8))
                # Writing the text id
                self.dlgFile.write(chr(dataThree & 0xFF))
                self.dlgFile.write(chr(dataThree >> 8))
                # Finally, write the new string
                self.dlgFile.write(splitedTextLine[1])
        # Finally!
        commandAddressList.append(0x0500)
        self.dlgFile.seek(0x0A, 0)
        for cmdAddr in commandAddressList:
            self.dlgFile.write(chr(cmdAddr >> 8))
            self.dlgFile.write(chr(cmdAddr & 0xFF))
        raw_input("[>]Process Finish!!!\nPress any key to exit.")
