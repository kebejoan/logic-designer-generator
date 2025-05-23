from dataclasses import dataclass
import re

@dataclass
class DataClass:
    category    : str
    tagIn1      : str
    descIn1     : str
    tagIn2      : str
    descIn2     : str
    tagOut1     : str
    descOut1    : str
    tagOut2     : str
    descOut2    : str
    npasName    : str
    npasDesc    : str
    anlgInType  : str
    anlgInLo    : str
    anlgInHi    : str
    anlgInUnit  : str
    anlgOutLo   : str
    anlgOutHi   : str
    anlgOutUnit : str
    npasAIType  : str
    DTagAIType   : str
    
def remove_ (string: str) -> str:
    return string.replace("_", "")

def formatTag (string: str, isNan: bool) -> str:
    if isNan:
        return ""
    else: return re.sub(r"[-\s]", "_", string)

def selectAINpasType (string: str, idx) -> str:
    match (string):
        case "I_Anlg":
            return "NPAS_AI_ANLG"
        case "I_Temp":
            return "NPAS_AI_TEMP"    
        case _:
            print(f"| AI Type Wrong Definition at line {idx}. Must be either 'I_Anlg' or 'I_Temp'")
            return "NPAS_AI_ANLG"
    
def selectAIDtagType (string: str, idx) -> str:
    match (string):
        case "I_Anlg":
            return "DTag_I_Anlg"
        case "I_Temp":
            return "DTag_I_Temp"    
        case _:
            print(f"| AI Type Wrong Definition at line {idx}. Must be either 'I_Anlg' or 'I_Temp'")
            return "DTAG_I_Anlg"
    
def giveHeaderFooter():
    s_ = []
    s_.append("")
    s_.append("(*========================================================================*)")
    s_.append("(*==========THIS STRUCTURED TEXT IS GENERATED BY LOGIC GENERATOR==========*)")
    s_.append("(*=====Questions?, maybe I'm still here: faishal.tahsiin@yokogawa.com=====*)")
    s_.append("(*=====Or contribute at: github.com/kebejoan/logic-designer-generator=====*)")
    s_.append("(*============================== Cheers  !================================*)")
    s_.append("(*========================================================================*)")
    s_.append("")
    return s_

def initMessage():
    print("________________________________________________________________________________________________")
    print("|                                                                                               |")
    print("|    ,                                   ,-.                                 .                  |")
    print("|    |                  o               /                                    |                  |")
    print("|    |      ,-.   ,-:   .   ,-.         | -.   ,-.   ;-.   ,-.   ;-.   ,-:   |-    ,-.   ;-.    |")
    print("|    |      | |   | |   |   |           \  |   |-'   | |   |-'   |     | |   |     | |   |      |")
    print("|    `--'   `-'   `-|   '   `-'          `-'   `-'   ' '   `-'   '     `-;   `-'   `-'   '      |")
    print("|                 `-'                                                     ,-. ;  ,-. . . ,-.    |")
    print("|                                                                         |-| |  |-' |-| |-|    |")
    print("|                                                                         ' ' `- '   ' ' ' '    |")
    print("|_______________________________________________________________________________________________|")
    print("|                                                                                               |")
    print("|                           kebejoan 2025 // faishal.tahsiin@yokogawa.com                       |")
    print("|_______________________________________________________________________________________________|")
    print("|                                                                                               |")
    print("|                     contribute at: github.com/kebejoan/logic-designer-generator               |")
    print("|__________________________________________.......______________________________________________|")
    print("|                                                                                               '")