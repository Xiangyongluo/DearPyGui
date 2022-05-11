import shutil
import os
from os import path
import sys

# arg 1 - Location (i.e. /../../cmake-build-release/DearPyGui/Release/dearpygui.pyd)
# arg 2 - File     (i.e. dearpygui.pyd, dearpygui.so)
# arg 3 - Version Number

script_dir = os.getcwd()
location = sys.argv[1]
vnum = sys.argv[2] 

# create the necessary directories if they do not exist
if not os.path.isdir(f"{script_dir}/dearpygui/"):
    os.mkdir(f"{script_dir}/dearpygui/")

# copy add items to temporary location
shutil.copy(location, f"{script_dir}/dearpygui")
shutil.copy(
    f"{script_dir}/../DearPyGui/dearpygui/core.pyi", f"{script_dir}/dearpygui"
)

shutil.copy(
    f"{script_dir}/../DearPyGui/dearpygui/simple.py", f"{script_dir}/dearpygui"
)

shutil.copy(
    f"{script_dir}/../DearPyGui/dearpygui/demo.py", f"{script_dir}/dearpygui"
)


with open(f"{script_dir}/dearpygui/__init__.py", 'w') as file:
    file.write("pass\n")

# create information file used by setup.py
with open(f"{script_dir}/distinfo.txt", 'w') as file:
    file.write(vnum + '\n')
