from io import StringIO
import pandas as pd
from HANDLER import _HANDLE_STRUCT_TEXT
from HANDLER import _HANDLE_LOC_VAR
from HANDLER import _HANDLE_DEV_LBL
from HANDLER._UTILS import (
    DataClass,
    formatTag,
    selectAIDtagType,
    selectAINpasType,
    giveHeaderFooter
    )
import time #CLI aestethic only

def ExcelMasterToCsv(master_excel_path, master_csv_path):
    # Load the Excel file
    data_sheets = ['MASTER', 'DI', 'DO', 'AI', 'AO', 'PVI', 'MLD', 'PID', 'SIO22', 'SIO21', 'SIO12', 'SIO11']

    df_combined = pd.read_excel(master_excel_path, sheet_name='MASTER')

    for name in data_sheets[1:]:
        try:
            df = pd.read_excel(master_excel_path, sheet_name=name, skiprows=1, header=None)

            # Only proceed if there's actual data
            if not df.empty:
                df.columns = df_combined.columns  # Align columns
                df_combined = pd.concat([df_combined, df], ignore_index=True)

        except Exception as e:
            print(f"| Skipping sheet '{name}' due to error: {e}")
            continue
    
    # Save result to CSV
    df_combined.to_csv(master_csv_path, index=False)
    
def MasterCsvToScripts(df, dir_dev_lbl, dir_loc_var, dir_str_text):
    
    lines_header = giveHeaderFooter()
    lines_footer = giveHeaderFooter()
    lines_di = []
    lines_do = []
    lines_ai = []
    lines_ao = []
    lines_pvi = []
    lines_pid = []
    lines_mld = []
    lines_sio11 = []
    lines_sio12 = []
    lines_sio21 = []
    lines_sio22 = []
    lines_loc_var = []
    lines_dev_lbl = []
    
    # ============= Give each lines headers ==============
    lines_di.append("(* =============DI============= *)")
    lines_do.append("(* =============DO============= *)")
    lines_ai.append("(* =============AI============= *)")
    lines_ao.append("(* =============AO============= *)")
    lines_pvi.append("(* =============PVI============= *)")
    lines_mld.append("(* =============MLD============= *)")
    lines_pid.append("(* =============PID============= *)")
    lines_sio22.append("(* =============SIO22============= *)")
    lines_sio12.append("(* =============SIO12============= *)")
    lines_sio21.append("(* =============SIO21============= *)")
    lines_sio11.append("(* =============SIO11============= *)")
    
    #Give LocVar Header
    lines_loc_var.append("Name, Type, Description, Usage, Retain") 
    
    #Give Device Label Lines Header
    lines_dev_lbl.append("#FILETYPE,Device label definition export") 
    lines_dev_lbl.append("#FILEREV,1")
    lines_dev_lbl.append("DeviceLabel,Comment,Signal,Task,ScaleLow,ScaleHigh,Unit,PulseRate,RangeLow,RangeHigh,Address")
    
    index=0
    
    for _, row in df.iterrows():
        index+=1
        print(f"| Reading data line: {index}")
        time.sleep(0.15) #CLI aestethic only
        DATA_LINE = [ row[ 'CATEGORY' ], row[ 'TAG_IN1' ], row[ 'DESC_IN1' ], row[ 'TAG_IN2' ], row[ 'DESC_IN2' ], row[ 'TAG_OUT1' ], row[ 'DESC_OUT1' ], row[ 'TAG_OUT2' ], row[ 'DESC_OUT2' ], row[ 'NPAS_SPECIFIC_NAME' ], row[ 'NPAS_SPECIFIC_DESC' ], row[ 'ANLG_IN_TYPE' ], row[ 'ANLG_IN_RANGE_LO' ], row[ 'ANLG_IN_RANGE_HI' ], row[ 'ANLG_IN_UNIT' ], row[ 'ANLG_OUT_RANGE_LO' ], row[ 'ANLG_OUT_RANGE_HI' ], row[ 'ANLG_OUT_UNIT' ] ]
        
        #input DATA_LINE to a class
        DataInstance = DataClass(
            category    = DATA_LINE[0],
            tagIn1      = formatTag(DATA_LINE[1], pd.isna(DATA_LINE[1])),
            descIn1     = DATA_LINE[2],
            tagIn2      = formatTag(DATA_LINE[3], pd.isna(DATA_LINE[3])),
            descIn2     = DATA_LINE[4],
            tagOut1     = formatTag(DATA_LINE[5], pd.isna(DATA_LINE[5])),
            descOut1    = DATA_LINE[6],
            tagOut2     = formatTag(DATA_LINE[7], pd.isna(DATA_LINE[7])),
            descOut2    = DATA_LINE[8],
            npasName    = DATA_LINE[9],
            npasDesc    = DATA_LINE[10],
            anlgInType  = DATA_LINE[11],
            anlgInLo    = DATA_LINE[12],
            anlgInHi    = DATA_LINE[13],
            anlgInUnit  = DATA_LINE[14],
            anlgOutLo   = DATA_LINE[15],
            anlgOutHi   = DATA_LINE[16],
            anlgOutUnit = DATA_LINE[17],
            npasAIType  = selectAINpasType(DATA_LINE[11], index+1) if DATA_LINE[0] in ("AI", "PVI", "PID") else "",
            DTagAIType  = selectAIDtagType(DATA_LINE[11], index+1) if DATA_LINE[0] in ("AI", "PVI", "PID") else ""
        )
        
        match DATA_LINE[0]:
            case "DI":
                lines_di.append(_HANDLE_STRUCT_TEXT.di(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.di(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.di(DataInstance))
            case "DO":
                lines_do.append(_HANDLE_STRUCT_TEXT.do(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.do(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.do(DataInstance))
            case "AI":
                lines_ai.append(_HANDLE_STRUCT_TEXT.ai(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.ai(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.ai(DataInstance))
            case "AO":
                lines_ao.append(_HANDLE_STRUCT_TEXT.ao(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.ao(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.ao(DataInstance))
            case "PVI":
                lines_pvi.append(_HANDLE_STRUCT_TEXT.pvi(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.pvi(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.pvi(DataInstance))
            case "MLD":
                lines_mld.append(_HANDLE_STRUCT_TEXT.mld(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.mld(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.mld(DataInstance))
            case "PID":
                lines_pid.append(_HANDLE_STRUCT_TEXT.pid(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.pid(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.pid(DataInstance))
            case "SIO22":
                lines_sio22.append(_HANDLE_STRUCT_TEXT.sio22(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.sio22(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.sio22(DataInstance))
            case "SIO21":
                lines_sio21.append(_HANDLE_STRUCT_TEXT.sio21(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.sio21(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.sio21(DataInstance))
            case "SIO12":
                lines_sio12.append(_HANDLE_STRUCT_TEXT.sio12(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.sio12(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.sio12(DataInstance))
            case "SIO11":
                lines_sio11.append(_HANDLE_STRUCT_TEXT.sio11(DataInstance))
                lines_loc_var.append(_HANDLE_LOC_VAR.sio11(DataInstance))
                lines_dev_lbl.append(_HANDLE_DEV_LBL.sio11(DataInstance))
            case _:
                print(f"| Line {index+1} invalid category. Check MASTER.csv")
    
    #write Dev Label Lines to .csv
    print("| Generating DEV_LABEL.csv file...")
    dev_lbl_script = "\n".join(lines_dev_lbl)
    with open(dir_dev_lbl, "w", encoding="utf-8") as f:
        f.write(dev_lbl_script)
    
    #write Local Variable Lines to .xlsx
    print("| Generating LOC_VAR.xlsx file...")
    loc_var_script = "\n".join(lines_loc_var)
    stripped = loc_var_script.strip()
    stripped = pd.read_csv(StringIO(loc_var_script))
    stripped.to_excel(dir_loc_var, index=False)
    
    array_lines = [ #array for containing all lines
        lines_header,
        lines_di,
        lines_do,
        lines_pvi,
        lines_pid,
        lines_mld,
        lines_sio11,
        lines_sio12,
        lines_sio21,
        lines_sio22,
        lines_footer
    ]
    
    scripts = [] #Var for appending all lines
    
    #join/append all lines
    for i in range(len(array_lines)):
        if len(array_lines[i]) > 0:
            scripts.append("\n".join(array_lines[i]))
    
    final_script = "\n".join(scripts)

    # Save the script to a text file
    print("| Generating STRUCT_TEXT.txt file...")
    with open(dir_str_text, "w") as file:
        file.write(final_script)