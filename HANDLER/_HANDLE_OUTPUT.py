import pandas as pd
from io import StringIO

def GenerateCSV(strIn : str, dir : str):
    try:
        with open(dir, "w", encoding="utf-8") as f:
            f.write(strIn)
        print("| DEV_LABEL.csv generated.")
    except FileNotFoundError:
        print("| ERROR: File not generated. Directory error")
    except PermissionError:
        print("| ERROR: You don't have permission. You might have the file opened")
    except UnicodeDecodeError:
        print("| ERROR: File encoding error.")
    except Exception as e:
        print(f"| ERROR: Unexpected error: {e}")

def GenerateXLSX(strIn : str, dir : str):
    try:
        stripped = strIn.strip()
        stripped = pd.read_csv(StringIO(stripped))
        stripped.to_excel(dir, index=False)
        print("| LOC_VAR.xlsx generated.")
    except FileNotFoundError:
        print("| ERROR: File not generated. Directory Error")
    except PermissionError:
        print("| ERROR: You don't have permission. You might have the file opened")
    except UnicodeDecodeError:
        print("| ERROR: File encoding error.")
    except Exception as e:
        print(f"| ERROR: Unexpected error: {e}")
        
def GenerateTXT(arrIn : list[str], dir : str):
    scripts = []
    
    for i in range(len(arrIn)):
        if len(arrIn[i]) > 0:
            scripts.append("\n".join(arrIn[i]))
    
    final_script = "\n".join(scripts)
    
    try:
        with open(dir, "w") as file:
            file.write(final_script)
        print("| STRUCT_TEXT.txt generated.")
    except FileNotFoundError:
        print("| ERROR: File not generated. Directory Error.")
    except PermissionError:
        print("| ERROR: You don't have permission. You might have the file opened")
    except UnicodeDecodeError:
        print("| ERROR: File encoding error.")
    except Exception as e:
        print(f"| ERROR: Unexpected error: {e}")