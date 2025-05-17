from _UTILS import (
    DataClass,
    remove_
)

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
    script_lines.append(f"{DATA.tagIn1}(IN:=_{remove_(DATA.tagIn1)}.OUT,ENG_RW:={DATA.tagIn1}_ENG,PRM_RW:={DATA.tagIn1}_PRM);")
    script_lines.append(f"{DATA.tagIn1}_OUT:={DATA.tagIn1}.OUT;")
    script_lines.append(f"{DATA.tagIn1}_ENG:={DATA.tagIn1}.ENG_RW;")
    script_lines.append(f"{DATA.tagIn1}_PRM:={DATA.tagIn1}.PRM_RW;")
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