# License: GNU Lesser General Public License v3.0
# Author: lazy fox chan
# Convert 教育部國語辭典 for rime-tongpin
import sys
import pandas
import convrevised
import convconcised
import convidioms

# Check args
args = sys.argv
if len(args) != 4:
    print("ERROR need 3 args: dict_revised_2015_XXXXXXXX.xlsx dict_concised_2014_XXXXXXXX.xlsx dict_idioms_2020_XXXXXXXX.xls")
    sys.exit(1)
if "dict_revised_2015_" not in args[1]:
    print('ERROR first argument: must contain "dict_revised_2015_"')
    sys.exit(1)
if "dict_concised_2014_" not in args[2]:
    print('ERROR second argument: must contain "dict_concised_2014_"')
    sys.exit(1)
if "dict_idioms_2020_" not in args[3]:
    print('ERROR third argument: must contain "dict_idioms_2020_"')
    sys.exit(1)

# Load file
print("Loading file: " + args[1])
revised_df = pandas.read_excel(args[1], sheet_name=0)
print("Loading file: " + args[2])
concised_df = pandas.read_excel(args[2], sheet_name=0)
print("Loading file: " + args[3])
idioms_df = pandas.read_excel(args[3], sheet_name=0)

# Convert
print("Converting File: " + args[1])
convrevised.convert(revised_df)
print("Converting File: " + args[2])
convconcised.convert(concised_df)
print("Converting File: " + args[3])
convidioms.convert(idioms_df)

print("Conversion completed!")
