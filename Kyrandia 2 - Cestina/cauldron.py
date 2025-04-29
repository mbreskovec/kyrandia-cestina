# -*- coding: utf-8 -*-

import sys

import package
import dlg
import emc

if __name__ == "__main__":
    try:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print """
Welcome to Ondinha's Cauldron 1!
--------------------------------
Author:  Sandro Dutra, Ondinha
Website: romhacking.trd.br
Contact: hexodin@gmail.com

Several modifications and EMC support: Ondrej Necas, dousabel@seznam.cz
--------------------------------
How to use:
-----------
-u or --unpack: Unpacks a PAK file.
                Example: cauldron --unpack ORIGINAL.PAK

-r or --repack: Repacks a PAK file.
                Obs: The unpacked files and original pak file
                must be in the directory.
                Example: cauldron --repack ORIGINAL.PAK REPACKED.PAK

-e or --extract:Extracts text from DLG file to a TXT file.
                Example: cauldron --extract ORIGINAL.DLG TEXT.TXT

-i or --insert: Insert TXT file in DLG file.
                Example: cauldron --insert ORIGINAL.DLG TEXT.TXT

-ee:            Extracts text from EMC file to a TXT file.
                Example: cauldron --ee ORIGINAL.EMC TEXT.TXT

-ii:            Insert TXT file to EMC file.
                Example: cauldron -ii ORIGINAL.EMC TEXT.TXT
                Warning: ORIGINAL.EMC will be rewrited


-----------
"""
            raw_input("[>]Press any key to exit.")
        elif sys.argv[1] == "-u" or sys.argv[1] == "--unpack":
            package.Package(sys.argv[2]).unpack()
        elif sys.argv[1] == "-r" or sys.argv[1] == "--repack":
            package.Package(sys.argv[2]).repack(sys.argv[3])
        elif sys.argv[1] == "-e" or sys.argv[1] == "--extract":
            dlg.DLG(sys.argv[2]).extract(sys.argv[3])
        elif sys.argv[1] == "-i" or sys.argv[1] == "--insert":
            dlg.DLG(sys.argv[2]).insert(sys.argv[3])
        elif sys.argv[1] == "-ee":
            emc.EMC(sys.argv[2]).extract(sys.argv[3])
        elif sys.argv[1] == "-ii":
            emc.EMC(sys.argv[2]).insert(sys.argv[3])
        else:
            raw_input("[-]ERROR: Bad command line argument.\n[+]Try use -h or --help.\n[>]Press any key to abort.")
    except IndexError:
        raw_input("[-]ERROR: Bad command line argument.\n[+]Try use -h or --help.\n[>]Press any key to abort.")
