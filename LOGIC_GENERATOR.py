import os
import sys
from HANDLER import _HANDLE_MASTER
from HANDLER._UTILS import initMessage
import pandas as pd

# Get the directory where the .exe is located
exe_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(f"exe_dir: {exe_dir}")
output_dir = os.path.join(exe_dir, "Output")
os.makedirs(output_dir, exist_ok=True) 

# Define all the paths
master_excel_path = os.path.join (exe_dir, "EXCEL_MASTER.xlsx")
master_csv_path = os.path.join(exe_dir, "MASTER.csv")
output_locvar_path = os.path.join(output_dir, "LOC_VAR.xlsx")
output_devlabel_path = os.path.join(output_dir, "DEV_LABEL.csv")
output_structext_path = os.path.join(output_dir, "STRUCT_TEXT.txt")

initMessage()
exec = False

userInput = input("| Do you have EXCEL_MASTER.xlsx on the same folder as the LOGIC_GENERATOR.exe (Y/N)?")

match userInput:
    case "Y" | "y":
        exec = True
        print("| Reading EXCEL_MASTER.xlsx file...")
    case "N" | "n":
        print("| Please put EXCEL_MASTER.xlsx in the same folder as LOGIC_GENERATOR.exe")
        exec = False
    case _:
        print("| wrong input")
        


if exec:
    if not os.path.exists(master_excel_path):
        print(f"| Error: EXCEL_MASTER.xlsx file not found at {master_excel_path}")
        input("| Press Enter to continue...")
    else:
        _HANDLE_MASTER.ExcelMasterToCsv(master_excel_path, master_csv_path)
        print("| Generating MASTER.csv file...")
        if not os.path.exists(master_csv_path):
            print(f"| Error: MASTER.csv file is not generated at {master_csv_path}")
            input("| Press Enter to continue...")
        else:
            # Read the CSV file
            df = pd.read_csv(master_csv_path)
            print("| Reading MASTER.csv file...")
            # Handle Master CSV
            _HANDLE_MASTER.MasterCsvToScripts(df, output_devlabel_path, output_locvar_path, output_structext_path)
    
    #     print(f"CSV generated and saved to {local_var_out}")
    print("|_______________________________________________________________________________________________")
    print("| ")
    print("| Source conversion in Logic Designer shall be used to convert ST Program into FBD Program")
    print("| kebejoan, 2025 - github.com/kebejoan - faishal.tahsiin@yokogawa.com")
    print("| contribute: github.com/kebejoan/logic-designer-generator")
    print("|_______________________________________________________________________________________________")
    print("| ")
    input("|                                      press enter to exit                              ")