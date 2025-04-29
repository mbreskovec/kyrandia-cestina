# -*- coding: utf-8 -*-
#Odstrani diakritiku ze zadaneho retezce, v kodovani ISO-latin nebo Win-1250
def RemDia(s):
    nahr = [(chr(0xE1),"a"),(chr(0xE9),"e"),(chr(0xED),"i"),(chr(0xF3),"o"),(chr(0xFA),"u"),
            (chr(0xF9),"u"),(chr(0xFD),"y"),(chr(0xC1),"A"),(chr(0xC9),"E"),(chr(0xCD),"I"),
            (chr(0xD3),"O"),(chr(0xDA),"U"),(chr(0xD9),"U"),(chr(0xDD),"Y"),(chr(0xEC),"e"),
            (chr(0xB9),"s"),(chr(0xE8),"c"),(chr(0xF8),"r"),(chr(0xBE),"z"),(chr(0xCC),"E"),
            (chr(0xA9),"S"),(chr(0xC8),"C"),(chr(0xD8),"R"),(chr(0xAE),"Z"),(chr(0xEF),"d"),
            (chr(0xBB),"t"),(chr(0xF2),"n"),(chr(0xCF),"D"),(chr(0xAB),"T"),(chr(0xD2),"N"),
            (chr(0x9A),"s"),(chr(0x8A),"S"),(chr(0x9E),"z"),(chr(0x8E),"Z"),(chr(0x9D),"t"),(chr(0x8D),"T")]
    for (co,cim) in nahr:
        s = s.replace(co,cim)
    return s
