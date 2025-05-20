# HEADER:
# Name, Type, Description, Usage, Retain

from HANDLER._UTILS import (
    DataClass,
    remove_
)

def di(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_DI,DTag_I_Sts,{DATA.descIn1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagIn1)},NPAS_DI_STS,{DATA.descIn1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagIn1)},BOOL,{DATA.descIn1} Raw Value,VAR,0")
    script = "\n".join(s_)
    return script

def do(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagOut1}_DO,DTag_O_Sts,{DATA.descOut1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagOut1)},NPAS_DO_STS,{DATA.descOut1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagOut1)},BOOL,{DATA.descOut1} Raw Value,VAR,0")
    script = "\n".join(s_)
    return script

def ai(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_AI,{DATA.DTagAIType},{DATA.descIn1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagIn1)},{DATA.npasAIType},{DATA.descIn1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagIn1)},REAL,{DATA.descIn1} Raw Value,VAR,0")
    script = "\n".join(s_)
    return script

def ao(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagOut1}_AO,DTag_O_Anlg,{DATA.descOut1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagOut1)},NPAS_AO_ANLG,{DATA.descOut1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagOut1)},REAL,{DATA.descOut1} Raw Value,VAR,0")
    script = "\n".join(s_)
    return script

def pvi(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_AI,{DATA.DTagAIType},{DATA.descIn1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagIn1)},{DATA.npasAIType},{DATA.descIn1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagIn1)},REAL,{DATA.descIn1} Raw Value,VAR,0")
    s_.append(f"{DATA.tagIn1},NPAS_PVI,{DATA.descIn1},VAR,0")
    s_.append(f"{DATA.tagIn1}_OUT,CData_Real,{DATA.descIn1},VAR,0")
    s_.append(f"{DATA.tagIn1}_ENG,SD_NPENG_PVI,{DATA.descIn1} ENG Var,VAR,0")
    s_.append(f"{DATA.tagIn1}_PRM,SD_NPPRM_PVI,{DATA.descIn1} PRM Var,VAR,0")
    script = "\n".join(s_)
    return script

def mld(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagOut1}_AO,DTag_O_Anlg,{DATA.descOut1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagOut1)},NPAS_AO_ANLG,{DATA.descOut1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagOut1)},REAL,{DATA.descOut1} Raw Value,VAR,0")
    s_.append(f"{DATA.tagOut1},NPAS_MLD,{DATA.descOut1},VAR,0")
    s_.append(f"{DATA.tagOut1}_ENG,SD_NPENG_MLD,{DATA.descOut1} ENG Var,VAR,0")
    s_.append(f"{DATA.tagOut1}_PRM,SD_NPPRM_MLD,{DATA.descOut1} PRM Var,VAR,0")
    s_.append(f"{DATA.tagOut1}_TSI,INT,{DATA.descOut1} Tracking Switch,VAR,0")
    s_.append(f"{DATA.tagOut1}_TIN,CData_REAL,{DATA.descOut1} Tracking Input,VAR,0")
    script = "\n".join(s_)
    return script

def pid(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_AI,{DATA.DTagAIType},{DATA.descIn1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagIn1)},{DATA.npasAIType},{DATA.descIn1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagIn1)},REAL,{DATA.descIn1} Raw Value,VAR,0")
    s_.append(f"{DATA.tagOut1}_AO,DTag_O_Anlg,{DATA.descOut1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagOut1)},NPAS_AO_ANLG,{DATA.descOut1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagOut1)},REAL,{DATA.descOut1} Raw Value,VAR,0")
    s_.append(f"{DATA.npasName},NPAS_PID,{DATA.npasDesc},VAR,0")
    s_.append(f"{DATA.npasName}_ENG,SD_NPENG_PID,{DATA.npasDesc} ENG Var,VAR,0")
    s_.append(f"{DATA.npasName}_PRM,SD_NPPRM_PID,{DATA.npasDesc} PRM Var,VAR,0")
    s_.append(f"{DATA.npasName}_TSI,INT,{DATA.npasDesc} Tracking Switch,VAR,0")
    s_.append(f"{DATA.npasName}_TIN,CData_REAL,{DATA.npasDesc} Tracking Input,VAR,0")
    s_.append(f"{DATA.npasName}_ITLK,INT,{DATA.npasDesc} Interlock Switch,VAR,0")
    script = "\n".join(s_)
    return script

def sio22(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_DI,DTag_I_Sts,{DATA.descIn1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagIn1)},NPAS_DI_STS,{DATA.descIn1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagIn1)},BOOL,{DATA.descIn1} Raw Value,VAR,0")
    s_.append(f"{DATA.tagIn2}_DI,DTag_I_Sts,{DATA.descIn2} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagIn2)},NPAS_DI_STS,{DATA.descIn2} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagIn2)},BOOL,{DATA.descIn2} Raw Value,VAR,0")
    s_.append(f"{DATA.tagOut1}_DO,DTag_O_Sts,{DATA.descOut1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagOut1)},NPAS_DO_STS,{DATA.descOut1} FB,VAR,0")
    # s_.append(f"{remove_(DATA.tagOut1)},BOOL,{DATA.descOut1} Raw Value,VAR,0")
    s_.append(f"{DATA.tagOut2}_DO,DTag_O_Sts,{DATA.descOut2} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagOut2)},NPAS_DO_STS,{DATA.descOut2} FB,VAR,0")
    # s_.append(f"{remove_(DATA.tagOut2)},BOOL,{DATA.descOut2} Raw Value,VAR,0")
    s_.append(f"{DATA.npasName},NPAS_SIO_22,{DATA.npasDesc},VAR,0")
    s_.append(f"{DATA.npasName}_ENG,SD_NPENG_SIO,{DATA.npasDesc} ENG Var,VAR,0")
    s_.append(f"{DATA.npasName}_PRM,SD_NPPRM_SIO,{DATA.npasDesc} PRM Var,VAR,0")
    s_.append(f"{DATA.npasName}_TSI,INT,{DATA.npasDesc} Tracking Switch,VAR,0")
    s_.append(f"{DATA.npasName}_ITLK,INT,{DATA.npasDesc} Interlock Switch,VAR,0")
    s_.append(f"{DATA.npasName}_SWI,INT,{DATA.npasDesc} ANS Bypass Switch,VAR,0")
    script = "\n".join(s_)
    return script

def sio21(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_DI,DTag_I_Sts,{DATA.descIn1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagIn1)},NPAS_DI_STS,{DATA.descIn1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagIn1)},BOOL,{DATA.descIn1} Raw Value,VAR,0")
    s_.append(f"{DATA.tagIn2}_DI,DTag_I_Sts,{DATA.descIn2} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagIn2)},NPAS_DI_STS,{DATA.descIn2} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagIn2)},BOOL,{DATA.descIn2} Raw Value,VAR,0")
    s_.append(f"{DATA.tagOut1}_DO,DTag_O_Sts,{DATA.descOut1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagOut1)},NPAS_DO_STS,{DATA.descOut1} FB,VAR,0")
    # s_.append(f"{remove_(DATA.tagOut1)},BOOL,{DATA.descOut1} Raw Value,VAR,0")
    s_.append(f"{DATA.npasName},NPAS_SIO_21,{DATA.npasDesc},VAR,0")
    s_.append(f"{DATA.npasName}_ENG,SD_NPENG_SIO,{DATA.npasDesc} ENG Var,VAR,0")
    s_.append(f"{DATA.npasName}_PRM,SD_NPPRM_SIO,{DATA.npasDesc} PRM Var,VAR,0")
    s_.append(f"{DATA.npasName}_TSI,INT,{DATA.npasDesc} Tracking Switch,VAR,0")
    s_.append(f"{DATA.npasName}_ITLK,INT,{DATA.npasDesc} Interlock Switch,VAR,0")
    s_.append(f"{DATA.npasName}_SWI,INT,{DATA.npasDesc} ANS Bypass Switch,VAR,0")
    script = "\n".join(s_)
    return script

def sio12(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_DI,DTag_I_Sts,{DATA.descIn1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagIn1)},NPAS_DI_STS,{DATA.descIn1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagIn1)},BOOL,{DATA.descIn1} Raw Value,VAR,0")
    s_.append(f"{DATA.tagOut1}_DO,DTag_O_Sts,{DATA.descOut1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagOut1)},NPAS_DO_STS,{DATA.descOut1} FB,VAR,0")
    # s_.append(f"{remove_(DATA.tagOut1)},BOOL,{DATA.descOut1} Raw Value,VAR,0")
    s_.append(f"{DATA.tagOut2}_DO,DTag_O_Sts,{DATA.descOut2} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagOut2)},NPAS_DO_STS,{DATA.descOut2} FB,VAR,0")
    # s_.append(f"{remove_(DATA.tagOut2)},BOOL,{DATA.descOut2} Raw Value,VAR,0")
    s_.append(f"{DATA.npasName},NPAS_SIO_12,{DATA.npasDesc},VAR,0")
    s_.append(f"{DATA.npasName}_ENG,SD_NPENG_SIO,{DATA.npasDesc} ENG Var,VAR,0")
    s_.append(f"{DATA.npasName}_PRM,SD_NPPRM_SIO,{DATA.npasDesc} PRM Var,VAR,0")
    s_.append(f"{DATA.npasName}_TSI,INT,{DATA.npasDesc} Tracking Switch,VAR,0")
    s_.append(f"{DATA.npasName}_ITLK,INT,{DATA.npasDesc} Interlock Switch,VAR,0")
    s_.append(f"{DATA.npasName}_SWI,INT,{DATA.npasDesc} ANS Bypass Switch,VAR,0")
    script = "\n".join(s_)
    return script

def sio11(DATA : DataClass):
    s_ = []
    s_.append(f"{DATA.tagIn1}_DI,DTag_I_Sts,{DATA.descIn1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagIn1)},NPAS_DI_STS,{DATA.descIn1} FB,VAR,0")
    s_.append(f"{remove_(DATA.tagIn1)},BOOL,{DATA.descIn1} Raw Value,VAR,0")
    s_.append(f"{DATA.tagOut1}_DO,DTag_O_Sts,{DATA.descOut1} /*: Automatically added by Logic Generator */,VAR_EXTERNAL,0")
    s_.append(f"_{remove_(DATA.tagOut1)},NPAS_DO_STS,{DATA.descOut1} FB,VAR,0")
    # s_.append(f"{remove_(DATA.tagOut1)},BOOL,{DATA.descOut1} Raw Value,VAR,0")
    s_.append(f"{DATA.npasName},NPAS_SIO_11,{DATA.npasDesc},VAR,0")
    s_.append(f"{DATA.npasName}_ENG,SD_NPENG_SIO,{DATA.npasDesc} ENG Var,VAR,0")
    s_.append(f"{DATA.npasName}_PRM,SD_NPPRM_SIO,{DATA.npasDesc} PRM Var,VAR,0")
    s_.append(f"{DATA.npasName}_TSI,INT,{DATA.npasDesc} Tracking Switch,VAR,0")
    s_.append(f"{DATA.npasName}_ITLK,INT,{DATA.npasDesc} Interlock Switch,VAR,0")
    s_.append(f"{DATA.npasName}_SWI,INT,{DATA.npasDesc} ANS Bypass Switch,VAR,0")
    script = "\n".join(s_)
    return script