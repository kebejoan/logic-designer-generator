# Logic Generator: a Logic Generation Automation Tool

This is the repository for logic designer's logic generator tool. This is on Alpha release with primitive CLI base UI. 

This automation tool is intended to be used for basic design engineering. This tool will take IO Data (put inside a pre-formated excel file) as an input and will generate the script, and variables necessary to build a project during basic design phase.

As long as I develop this tool, this repository will be actively pushed with updated source codes

Cheers!

## Input and Output of the Tool

Input:
- `EXCEL_MASTER.xlsx`  : This is a pre-formatted file that will be filled by Engineer. Check README sheet

Output:

- `DEV_LABEL.csv`   : This output file is to be imported to DeviceLabelDefinition in logic designer
- `LOC_VAR.xlsx`    : This output file is to be copied to Variable Table of the script POU
- `STRUCT_TEXT.txt` : This output file is to be copied to worksheet of the script POU

## How to Download the Tool

1. For the Executable, access the /dist folder and download `LOGIC_GENERATOR.exe`
2. For the EXCEL MASTER file, download from the root `EXCEL_MASTER.xlsx`
3. Put both file in the same folder (preferably that won't need access as Administrator)

## How to Use The Executable (TL;DR)

Complete 'How to' is explained inside the README sheet in the EXCEL_MASTER.xlsx file
1. Put the EXCEL_MASTER.xlsx file in the same folder as LOGIC_GENERATOR.exe file
2. Open the EXCEL_MASTER.xlsx file and add in the I/O data that you want to be generated
3. Execute LOGIC_GENERATOR.exe
4. Import the DEV_LABEL into the logic designer
5. Copy the generated STRUCT_TEXT into a new POU
6. Copy the generated LOC_VAR into the new POU

## 🌳 Project Tree
```sh
@root                           # Project root
├── HANDLER/                    # Handler folder
│   ├── _HANDLE_DEV_LBL.py      # Script for handling dev label generation
│   ├── _HANDLE_LOC_VAR.py      # Script for handling local var generation
│   ├── _HANDLE_STRUCT_TEXT.py  # Script for handling ST logic generation
│   ├── _HANDLE_MASTER.py       # Script for handling MASTER input file
│   ├── _UTILS.py               # Functions for utilities
├── dist/                       # Distributed package folder
│   └── LOGIC_GENERATOR.exe     # Distributed package executable
├── LOGIC_GENERATOR.py          # Main script for the project
├── EXCEL_MASTER.xlsx           # Excel Master file input
└── README.md                   # Readme of the project                
```

## Contribution and Pull Requests

For my colleagues in Y, please email me through the company email

My personal email can be seen also on this Git account

## Developer's Note

A lot of improvement is still needed for this tool. Some experienced by developer are:

- UI. Currently still CLI base UI
- Feature to add custom FBs to be generated. I think this will require UI first
- Error Handling. Try-Catch can be implemented during reading or executing a function. Error message shall also be return with this Try-Catch

<br>
<br>
<br>

### Thank You for reading. Yours truly, _*Kebejoan*_
