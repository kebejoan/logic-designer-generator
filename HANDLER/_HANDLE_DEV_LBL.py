# HEADER:
# DeviceLabel,Comment,Signal,Task,ScaleLow,ScaleHigh,Unit,PulseRate,RangeLow,RangeHigh,Address

from HANDLER._UTILS import DataClass

def di(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_DI,{DATA.descIn1},I_Sts,Task0,,,,,,,")
    script = "\n".join(s_)
    return script

def do(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagOut1}_DO,{DATA.descOut1},O_Sts,Task0,,,,,,,")
    script = "\n".join(s_)
    return script

def ai(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_AI,{DATA.descIn1},{DATA.anlgInType},Task0,{DATA.anlgInLo},{DATA.anlgInHi},{DATA.anlgInUnit},,,,")
    script = "\n".join(s_)
    return script

def ao(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagOut1}_AO,{DATA.descOut1},O_Anlg,Task0,{DATA.anlgOutLo},{DATA.anlgOutHi},{DATA.anlgOutUnit},,,,")
    script = "\n".join(s_)
    return script

def pvi(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_AI,{DATA.descIn1},{DATA.anlgInType},Task0,{DATA.anlgInLo},{DATA.anlgInHi},{DATA.anlgInUnit},,,,")
    script = "\n".join(s_)
    return script

def mld(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagOut1}_AO,{DATA.descOut1},O_Anlg,Task0,{DATA.anlgOutLo},{DATA.anlgOutHi},{DATA.anlgOutUnit},,,,")
    script = "\n".join(s_)
    return script

def pid(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_AI,{DATA.descIn1},{DATA.anlgInType},Task0,{DATA.anlgInLo},{DATA.anlgInHi},{DATA.anlgInUnit},,,,")
    s_.append(f"{DATA.tagOut1}_AO,{DATA.descOut1},O_Anlg,Task0,{DATA.anlgOutLo},{DATA.anlgOutHi},{DATA.anlgOutUnit},,,,")
    script = "\n".join(s_)
    return script

def sio22(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_DI,{DATA.descIn1},I_Sts,Task0,,,,,,,")
    s_.append(f"{DATA.tagIn2}_DI,{DATA.descIn2},I_Sts,Task0,,,,,,,")
    s_.append(f"{DATA.tagOut1}_DO,{DATA.descOut1},O_Sts,Task0,,,,,,,")
    s_.append(f"{DATA.tagOut2}_DO,{DATA.descOut2},O_Sts,Task0,,,,,,,")
    script = "\n".join(s_)
    return script

def sio21(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_DI,{DATA.descIn1},I_Sts,Task0,,,,,,,")
    s_.append(f"{DATA.tagIn2}_DI,{DATA.descIn2},I_Sts,Task0,,,,,,,")
    s_.append(f"{DATA.tagOut1}_DO,{DATA.descOut1},O_Sts,Task0,,,,,,,")
    script = "\n".join(s_)
    return script

def sio12(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_DI,{DATA.descIn1},I_Sts,Task0,,,,,,,")
    s_.append(f"{DATA.tagOut1}_DO,{DATA.descOut1},O_Sts,Task0,,,,,,,")
    s_.append(f"{DATA.tagOut2}_DO,{DATA.descOut2},O_Sts,Task0,,,,,,,")
    script = "\n".join(s_)
    return script

def sio11(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_DI,{DATA.descIn1},I_Sts,Task0,,,,,,,")
    s_.append(f"{DATA.tagOut1}_DO,{DATA.descOut1},O_Sts,Task0,,,,,,,")
    script = "\n".join(s_)
    return script