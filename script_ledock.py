#! /bin/python
import os
import subprocess
import glob, shutil
import timeit

#start timer
start_time = timeit.default_timer()

#clean output files and dirs
shutil.rmtree("my_test", ignore_errors= True)

if glob.glob("pro.pdb"):
    os.remove("pro.pdb")

if glob.glob("ligands"):
    os.remove("ligands")

#make output dir
os.makedirs("my_test")

#list mol2 files
my_mol2 = glob.glob("*.mol2")

#move mol2 files to testing dir
for i in my_mol2:
    path_new = "my_test/" + i 
    shutil.copy(i, path_new)
    with open("ligands", 'a') as miarch:
        miarch.write(i + "\n")


#run lepro for protein
subprocess.check_call("./lepro_linux_x86 *.pdb -metal -p", shell=True)

#run ledock over ligands
print("ya llegamos a lo dificil") #a checkpoint flag
old_files = glob.glob("*") #list files before running ledock
subprocess.check_call("./ledock_linux_x86 dock.in", shell=True)
new_files = glob.glob("*") #list files after ledock

#print files generated by ledock
print(set(new_files) - set(old_files))

stop_time = timeit.default_timer() #stop timer 
print("listo el posho") #final print
print(stop_time - start_time) #show time
