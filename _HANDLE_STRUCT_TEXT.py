from _UTILS import (
    DataClass,
    remove_
)

def di(DATA: DataClass):
    script_lines = []
    script_lines.append(f"_{remove_(DATA.tagIn1)}(IN:={DATA.tagIn1}_DI);")
    script_lines.append(f"{remove_(DATA.tagIn1)} := _{remove_(DATA.tagIn1)}.OUT_VAL;")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script

def do(DATA: DataClass):
    script_lines = []
    script_lines.append(f"_{remove_(DATA.tagOut1)}(IN_VAL:={remove_(DATA.tagOut1)});")
    script_lines.append(f"{(DATA.tagOut1)}_DO:=_{remove_(DATA.tagOut1)}.OUT;")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script

def ai (DATA: DataClass):
    script_lines = []
    script_lines.append(f"_{remove_(DATA.tagIn1)}(IN:={DATA.tagIn1}_AI);")
    script_lines.append(f"{remove_(DATA.tagIn1)}:=_{remove_(DATA.tagIn1)}.OUT);")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script

def ao (DATA: DataClass):
    script_lines = []
    script_lines.append(f"_{remove_(DATA.tagOut1)}(IN:={remove_(DATA.tagOut1)},TSFO_SW:=FALSE);")
    script_lines.append(f"{(DATA.tagOut1)}_AO:=_{remove_(DATA.tagOut1)}.OUT;")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script

def pvi (DATA: DataClass):
    script_lines = []
    script_lines.append(f"_{remove_(DATA.tagIn1)}(IN:={DATA.tagIn1}_AI);")
    script_lines.append(f"{remove_(DATA.tagIn1)}:=_{remove_(DATA.tagIn1)}.OUT_VAL;")
    script_lines.append(f"{DATA.tagIn1}(IN:=_{remove_(DATA.tagIn1)}.OUT,ENG_RW:={DATA.tagIn1}_ENG,PRM_RW:={DATA.tagIn1}_PRM);")
    script_lines.append(f"{DATA.tagIn1}_OUT:={DATA.tagIn1}.OUT;")
    script_lines.append(f"{DATA.tagIn1}_ENG:={DATA.tagIn1}.ENG_RW;")
    script_lines.append(f"{DATA.tagIn1}_PRM:={DATA.tagIn1}.PRM_RW;")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script

def mld (DATA: DataClass):
    script_lines = []
    script_lines.append(f"{DATA.tagOut1}(TSI:={DATA.tagOut1}_TSI,TIN:={DATA.tagOut1}_TIN,ENG_RW:={DATA.tagOut1}_ENG,PRM_RW:={DATA.tagOut1}_PRM);")
    script_lines.append(f"{DATA.tagOut1}_ENG:={DATA.tagOut1}.ENG_RW;")
    script_lines.append(f"{DATA.tagOut1}_PRM:={DATA.tagOut1}.PRM_RW;")
    script_lines.append(f"_{remove_(DATA.tagOut1)}(IN:={DATA.tagOut1}.OUT,TSFO_SW:=FALSE);")
    script_lines.append(f"{(DATA.tagOut1)}_AO:=_{remove_(DATA.tagOut1)}.OUT;")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script

def pid (DATA: DataClass):
    script_lines = []
    script_lines.append(f"_{remove_(DATA.tagIn1)}(IN:={DATA.tagIn1}_AI);")
    script_lines.append(f"{DATA.npasDesc}(IN:=_{remove_(DATA.tagIn1)}.OUT,TSI:={DATA.npasDesc}_TSI,TIN:={DATA.npasDesc}_TIN,INTLOCK:={DATA.npasDesc}_ITLK,ENG_RW:={DATA.npasDesc}_ENG,PRM_RW:={DATA.npasDesc}_PRM);")
    script_lines.append(f"{DATA.npasDesc}_ENG:={DATA.npasDesc}.ENG_RW;")
    script_lines.append(f"{DATA.npasDesc}_PRM:={DATA.npasDesc}.PRM_RW;")
    script_lines.append(f"_{remove_(DATA.tagOut1)}(IN:={DATA.npasDesc}.OUT,TSFO_SW:=FALSE);")
    script_lines.append(f"{(DATA.tagOut1)}_AO:=_{remove_(DATA.tagOut1)}.OUT;")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script

def sio22(DATA: DataClass):
    script_lines = []
    script_lines.append(f"_{remove_(DATA.tagIn1)}(IN:={DATA.tagIn1}_DI);")
    script_lines.append(f"{remove_(DATA.tagIn1)}:=_{remove_(DATA.tagIn1)}.OUT_VAL;")
    script_lines.append(f"_{remove_(DATA.tagIn2)}(IN:={DATA.tagIn2}_DI);")
    script_lines.append(f"{remove_(DATA.tagIn2)}:=_{remove_(DATA.tagIn2)}.OUT_VAL;")
    script_lines.append(f"{DATA.npasName}(IN1:=_{remove_(DATA.tagIn1)}.OUT,IN2:=_{remove_(DATA.tagIn2)}.OUT,TSI:={DATA.npasName}_TSI,SWI:={DATA.npasName}_SWI,INTLOCK:={DATA.npasName}_ITLK,ENG_RW:={DATA.npasName}_ENG,PRM_RW:={DATA.npasName}_PRM);")
    script_lines.append(f"{DATA.npasName}_ENG:={DATA.npasName}.ENG_RW;")
    script_lines.append(f"{DATA.npasName}_PRM:={DATA.npasName}.PRM_RW;")
    script_lines.append(f"_{remove_(DATA.tagOut1)}(IN:={DATA.npasName}.OUT1);")
    script_lines.append(f"_{remove_(DATA.tagOut2)}(IN:={DATA.npasName}.OUT2);")
    script_lines.append(f"{(DATA.tagOut1)}_DO:=_{remove_(DATA.tagOut1)}.OUT;")
    script_lines.append(f"{(DATA.tagOut2)}_DO:=_{remove_(DATA.tagOut2)}.OUT;")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script

def sio12(DATA: DataClass):
    script_lines = []
    script_lines.append(f"_{remove_(DATA.tagIn1)}(IN:={DATA.tagIn1}_DI);")
    script_lines.append(f"{remove_(DATA.tagIn1)}:=_{remove_(DATA.tagIn1)}.OUT_VAL;")
    script_lines.append(f"{DATA.npasName}(IN:=_{remove_(DATA.tagIn1)}.OUT,TSI:={DATA.npasName}_TSI,SWI:={DATA.npasName}_SWI,INTLOCK:={DATA.npasName}_ITLK,ENG_RW:={DATA.npasName}_ENG,PRM_RW:={DATA.npasName}_PRM);")
    script_lines.append(f"{DATA.npasName}_ENG:={DATA.npasName}.ENG_RW;")
    script_lines.append(f"{DATA.npasName}_PRM:={DATA.npasName}.PRM_RW;")
    script_lines.append(f"_{remove_(DATA.tagOut1)}(IN:={DATA.npasName}.OUT1);")
    script_lines.append(f"_{remove_(DATA.tagOut2)}(IN:={DATA.npasName}.OUT2);")
    script_lines.append(f"{(DATA.tagOut1)}_DO:=_{remove_(DATA.tagOut1)}.OUT;")
    script_lines.append(f"{(DATA.tagOut2)}_DO:=_{remove_(DATA.tagOut2)}.OUT;")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script

def sio21(DATA: DataClass):
    script_lines = []
    script_lines.append(f"_{remove_(DATA.tagIn1)}(IN:={DATA.tagIn1}_DI);")
    script_lines.append(f"{remove_(DATA.tagIn1)}:=_{remove_(DATA.tagIn1)}.OUT_VAL;")
    script_lines.append(f"_{remove_(DATA.tagIn2)}(IN:={DATA.tagIn2}_DI);")
    script_lines.append(f"{remove_(DATA.tagIn2)}:=_{remove_(DATA.tagIn2)}.OUT_VAL;")
    script_lines.append(f"{DATA.npasName}(IN1:=_{remove_(DATA.tagIn1)}.OUT,IN2:=_{remove_(DATA.tagIn2)}.OUT,TSI:={DATA.npasName}_TSI,SWI:={DATA.npasName}_SWI,INTLOCK:={DATA.npasName}_ITLK,ENG_RW:={DATA.npasName}_ENG,PRM_RW:={DATA.npasName}_PRM);")
    script_lines.append(f"{DATA.npasName}_ENG:={DATA.npasName}.ENG_RW;")
    script_lines.append(f"{DATA.npasName}_PRM:={DATA.npasName}.PRM_RW;")
    script_lines.append(f"_{remove_(DATA.tagOut1)}(IN:={DATA.npasName}.OUT);")
    script_lines.append(f"{(DATA.tagOut1)}_DO:=_{remove_(DATA.tagOut1)}.OUT;")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script

def sio11(DATA: DataClass):
    script_lines = []
    script_lines.append(f"_{remove_(DATA.tagIn1)}(IN:={DATA.tagIn1}_DI);")
    script_lines.append(f"{remove_(DATA.tagIn1)}:=_{remove_(DATA.tagIn1)}.OUT_VAL;")
    script_lines.append(f"{DATA.npasName}(IN:=_{remove_(DATA.tagIn1)}.OUT,TSI:={DATA.npasName}_TSI,SWI:={DATA.npasName}_SWI,INTLOCK:={DATA.npasName}_ITLK,ENG_RW:={DATA.npasName}_ENG,PRM_RW:={DATA.npasName}_PRM);")
    script_lines.append(f"{DATA.npasName}_ENG:={DATA.npasName}.ENG_RW;")
    script_lines.append(f"{DATA.npasName}_PRM:={DATA.npasName}.PRM_RW;")
    script_lines.append(f"_{remove_(DATA.tagOut1)}(IN:={DATA.npasName}.OUT);")
    script_lines.append(f"{(DATA.tagOut1)}_DO:=_{remove_(DATA.tagOut1)}.OUT;")
    script_lines.append("")
    script = "\n".join(script_lines)
    return script