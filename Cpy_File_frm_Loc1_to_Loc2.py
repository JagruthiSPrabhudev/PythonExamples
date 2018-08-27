## Command to run this script: Find below
## python Cpy_File_frm_Loc1_to_Loc2.py --src_path <Source path> --tgt_path <target Path> --bkp_folder <bakup path>
## Command on CMD console: python C:/Users/irstdnt/Desktop/Python_Projects/Cpy_File_frm_Loc1_to_Loc2.py C:\Users\irstdnt\Desktop\Src C:\Users\irstdnt\Desktop\Tgt C:\Users\irstdnt\Desktop\Backup

import hashlib
from shutil import copyfile,copy
import os
import sys

"""
import argparse
if __name__ == "__main__":
    args_fr_cpy = argparse.ArgumentParser()
    args_fr_cpy.add_argument("--src_path", help="Source Directory")
    args_fr_cpy.add_argument("--tgt_path", help="Target Directory")
    args_fr_cpy.add_argument("--Bkp_path", help="Backup Directory")
    paths = args_fr_cpy.parse_args()

src = paths.src_path
dst = paths.tgt_path
bkp_folder = paths.Bkp_path

"""

##script = sys.argv[0]
script = "C:/Users/irstdnt/Desktop/Python_Projects/Cpy_File_frm_Loc1_to_Loc2.py"
src = r'C:\Users\irstdnt\Desktop\Src'
##src = sys.argv[1]
dst = r'C:\Users\irstdnt\Desktop\Tgt'
##dst = sys.argv[2]
##bkp_folder = sys.argv[3]
bkp_folder = r'C:\Users\irstdnt\Desktop\Backup'

BLOCKSIZE = 65536
def Find_MD5_VAL(dir,file_name):
    hasher = hashlib.md5()
    file_name_including_path = dir + '\\' + file_name
    with open(file_name_including_path,'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

dest_path = dst

for root, dirs, files in os.walk(src):
    file_Name = files

for i in range(0,len(file_Name)):
    count = 0
    Val = file_Name[i]
    src_chksum = Find_MD5_VAL(src,Val)
    srce_path_file_name = src + '\\' + Val
    dest_path_check = dst + '\\' + Val
    if os.path.isfile(dest_path_check):
        copy(dest_path_check, bkp_folder)
        count = 1

    copy(srce_path_file_name, dest_path)
    dest_chksum = Find_MD5_VAL(dst, Val)

    if src_chksum == dest_chksum:
        print("Successfully copied file named",Val," from Source path",src," to destination path",dst)
        if count == 1:
            os.remove(bkp_folder + '\\' + Val)
    else:
        print("Unable to copy file named",Val," from Source path",src," to destination path",dst)
        print("Reason: Checksum Didnot Match")
        copy(bkp_folder + '\\' + Val, dest_path)
