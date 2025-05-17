import _DIGITAL
import _ANALOG

def Logic(df):
    lines_header = []
    lines_di = []
    lines_do = []
    lines_pvi = []
    lines_pid = []
    lines_mld = []
    lines_sio11 = []
    lines_sio12 = []
    lines_sio21 = []
    lines_sio22 = []
    lines_footer = []
    lines_custom = []
    lines_locvar = []
    
    index = 0 #index for locating invalid data
    #itterate every row of csv
    for _, row in df.iterrows():
        index+=1
        print(f"Reading data line: {index}")
        DATA_LINE = [ # an array for data in a row
            row[ 'CATEGORY' ],
            row[ 'DTAG_IN1' ],
            row[ 'DESC_IN1' ],
            row[ 'DTAG_IN2' ],
            row[ 'DESC_IN2' ],
            row[ 'DTAG_OUT1' ],
            row[ 'DESC_OUT1' ],
            row[ 'DTAG_OUT2' ],
            row[ 'DESC_OUT2' ],
            row[ 'NPAS_SPECIFIC_NAME' ],
            row[ 'NPAS_SPECIFIC_DESC' ],
            row[ 'ANLG_IN_TYPE' ],
            row[ 'ANLG_IN_RANGE_LO' ],
            row[ 'ANLG_IN_RANGE_HI' ],
            row[ 'ANLG_IN_UNIT' ],
            row[ 'ANLG_OUT_RANGE_LO' ],
            row[ 'ANLG_OUT_RANGE_HI' ],
            row[ 'ANLG_OUT_UNIT' ]
        ]      
        # choose what script to write based on NPAS_CATEGORY
        match DATA_LINE[0]:
            case "DI":
                if len(lines_di) <= 0:
                    lines_di.append("(* =============DI============= *)")
                lines_di.append(_DIGITAL.di(DATA_LINE))
            case "DO":
                if len(lines_do) <= 0:
                    lines_do.append("(* =============DO============= *)")
                lines_do.append(_DIGITAL.do(DATA_LINE))
            case "PVI":
                if len(lines_pvi) <= 0:
                    lines_pvi.append("(* =============PVI============= *)")
                lines_pvi.append(_ANALOG.pvi(DATA_LINE))
            case "MLD":
                if len(lines_mld) <= 0:
                    lines_mld.append("(* =============MLD============= *)")
                lines_mld.append(_ANALOG.mld(DATA_LINE))
            case "PID":
                if len(lines_pid) <= 0:
                    lines_pid.append("(* =============PID============= *)")
                lines_pid.append(_ANALOG.pid(DATA_LINE))
            case "SIO11":
                if len(lines_sio11) <= 0:
                    lines_sio11.append("(* =============SIO11============= *)")
                lines_sio11.append(_DIGITAL.sio11(DATA_LINE))
            case "SIO12":
                if len(lines_sio12) <= 0:
                    lines_sio12.append("(* =============SIO12============= *)")
                lines_sio12.append(_DIGITAL.sio12(DATA_LINE))
            case "SIO21":
                if len(lines_sio21) <= 0:
                    lines_sio21.append("(* =============SIO21============= *)")
                lines_sio21.append(_DIGITAL.sio21(DATA_LINE))
            case "SIO22":
                if len(lines_sio22) <= 0:
                    lines_sio22.append("(* =============SIO22============= *)")
                lines_sio22.append(_DIGITAL.sio22(DATA_LINE))
            case "CUSTOM":
                lines_custom.append("") # CUSTOM FB SHALL BE PUT LATER HERE
            case _:
                print(f"Undefined category on line {index+1} in the .csv")
                
    lines_footer = []
    lines_footer.append(f"\n\n(* ################################################################## *)") 
    lines_footer.append(f"(* ####################copyright of kebejoan 2025#################### *)") 
    lines_footer.append(f"(* ################################################################## *)") 

    array_lines_script = [ #array for containing all lines
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
        lines_custom,
        lines_footer
    ]
    
    scripts = [] #Var for appending all lines
    
    #join/append all lines
    for i in range(len(array_lines_script)):
        if len(array_lines_script[i]) > 0:
            scripts.append("\n".join(array_lines_script[i]))
    
    script_output = "\n (* ========================================== *)\n".join(scripts)
    
    script_output_file = "SCRIPT_OUT.txt"
    with open(script_output_file, "w") as file:
        file.write(script_output)
    print("Script Generation complete!")
    print(f"Script generated and saved to {script_output_file}")