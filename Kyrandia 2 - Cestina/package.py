# -*- coding: utf-8 -*-

import os.path

class Package:
    """Unpack and Repack Legend of Kyrandia 2: The Hand of Fate PAK Files."""
    def __init__(self, pakFilename):
        try:
            self.pakFile = open(pakFilename, "rb")
            self.pakFilesize = os.path.getsize(pakFilename)
        except IOError, error:
            raw_input("[-]ERROR: %s. Relative to: %s." % (error[1], pakFilename))
            exit()

        self.invertFourBytes = lambda fb: (fb & 0xFF) << 24 | (fb & 0xFF00) << 8 | (fb >> 16 & 0xFF) << 8 | (fb >> 24)

        self.fileBuffer = list()
        while True:
            fileAddress = self.invertFourBytes(self.__readedToInt(self.pakFile.read(4)))
            if fileAddress == self.pakFilesize:
                self.fileBuffer.append(fileAddress)
                break
            else:
                self.fileBuffer.append(fileAddress)
                # Get the filename
                filename = ""
                while True:
                    character = self.pakFile.read(1)
                    if ord(character) == 0:
                        break
                    else:
                        filename += character
                self.fileBuffer.append(filename)

    def __readedToInt(self, readed):
        """Readed bytes will be int type."""
        readed_int = 0
        for x in readed:
            readed_int = (readed_int << 8) | ord(x)
        return readed_int

    def unpack(self):
        """Unpack Legend of Kyrandia 2: The Hand of Fate PAK Files."""
        # Recreate and write the files
        print "[+]Writing files, wait..."
        for data in range(1, len(self.fileBuffer), 2):
            actualFile = open(self.fileBuffer[data], "w+b") # Recreate the file
            sizeToRead = (self.fileBuffer[data + 1]) - (self.fileBuffer[data - 1]) # Get the size to read
            self.pakFile.seek(self.fileBuffer[data - 1]) # Go to correct address
            actualFile.write(self.pakFile.read(sizeToRead)) # Read the correct size and write the file
        raw_input("[>]Process Finish!!!\nPress any key to exit.")

    def repack(self, repackedFilename):
        """Repack Legend of Kyrandia 2: The Hand of Fate PAK Files."""
        try:
            repackFile = open(repackedFilename, "w+b")
        except IOError, error:
            raw_input("[-]ERROR: %s. Relative to: %s." % (error[1], repackedFilename))
            exit()

        # First part: Writing the header
        print "[+]Repack Process: Phase #1 - Seting up."
        generalFilesize = 0
        headerSize = 0
        addressToWriteList = list()
        addressList = list()

        # Writing dummy bytes to reserve space for the first address
        for data in range(1, len(self.fileBuffer), 2):
            try:
                actualFile = open(self.fileBuffer[data], "rb")
                repackFile.write(chr(0) * 4)
                repackFile.write(self.fileBuffer[data] + chr(0)) # Write filename
                addressToWriteList.append(repackFile.tell())
                actualFilesize = os.path.getsize(actualFile.name)

                # Size of filename + 4 bytes (reference) + 1 (endstring)
                headerSize += len(self.fileBuffer[data]) + 5
                # Filesize + size of filename + 4 bytes (reference) + 1 (endstring)
                generalFilesize += (actualFilesize + len(self.fileBuffer[data]) + 5)
            except IOError, error:
                raw_input("[-]ERROR: %s. Relative to: %s." % (error[1], self.fileBuffer[data]))
                exit()

        # General file size + 4 bytes from the last referece + 5 null bytes.
        repackFile.write(chr(self.invertFourBytes(generalFilesize + 9) >> 24))
        repackFile.write(chr(self.invertFourBytes(generalFilesize + 9) >> 16 & 0xFF))
        repackFile.write(chr(self.invertFourBytes(generalFilesize + 9) >> 8 & 0xFF))
        repackFile.write(chr(self.invertFourBytes(generalFilesize + 9) & 0xFF))
        repackFile.write(chr(0) * 5)

        # Move file cursor to start to write the offset of the first file.
        repackFile.seek(0)
        repackFile.write(chr(self.invertFourBytes(headerSize + 9) >> 24))
        repackFile.write(chr(self.invertFourBytes(headerSize + 9) >> 16 & 0xFF))
        repackFile.write(chr(self.invertFourBytes(headerSize + 9) >> 8 & 0xFF))
        repackFile.write(chr(self.invertFourBytes(headerSize + 9) & 0xFF))
        repackFile.seek(headerSize + 9)

        # Second part: Writing the files
        print "[+]Repack Process: Phase #2 - Writing files."
        for data in range(1, len(self.fileBuffer), 2):
            try:
                fileToWrite = open(self.fileBuffer[data], "rb")
                repackFile.write(fileToWrite.read()) # Write the file, finally!
                addressList.append(repackFile.tell())
            except IOError, error:
                raw_input("[-]ERROR: %s. Relative to: %s." % (error[1], fileToWrite))
                exit()

        # Third part: Writing the address
        print "[+]Repack Process: Phase #3 - Writing address."
        for address in range(len(addressToWriteList)):
            repackFile.seek(addressToWriteList[address])
            repackFile.write(chr(self.invertFourBytes(addressList[address]) >> 24))
            repackFile.write(chr(self.invertFourBytes(addressList[address]) >> 16 & 0xFF))
            repackFile.write(chr(self.invertFourBytes(addressList[address]) >> 8 & 0xFF))
            repackFile.write(chr(self.invertFourBytes(addressList[address]) & 0xFF))
        raw_input("[>]Process Finish!!!\nPress any key to exit.")
