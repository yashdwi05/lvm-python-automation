import os
import getpass

os.system("clear")
print("\t\t\t\tLVM Automation")
print("\t\t\t\t--------------")

passwd = getpass.getpass()
if passwd != "arth":
    print("Incorrect Password")
    exit()


print("""
Press 1: Check filesystem
Press 2: Create LV
Press 3: Exit
""")

value = input("Enter Option: ")

if int(value)==1:
    os.system("fdisk -l")

elif int(value)==2:
    while True:
        i = input("create pv(y/n): ")
        if i=="y":
            x=input("Enter file-system: ")
            os.system("pvcreate {}".format(x))
        else:
            break
    v = input("Enter VG Name: ")
    pv = input("Enter PV: ")
    os.system("vgcreate {} {}".format(v,pv))
    while True:
        ch = input("Do you want to extand vg(y/n): ")
        if ch == "y":
            x=input("Enter PV to extend: ")
            os.system("vgextend {} {}".format(v,x))
        else:
            break
    lv = input("Enter LV Name: ")
    size = input("Enter LV size: ")
    size = int(size)
    os.system("lvcreate --size {}G --name {} {}".format(size,lv,v))
    print()
    print("formatting lv...")
    os.system("mkfs.ext4 {}/{}".format(v,lv))
    d = input("Enter directory name to mount LV: ")
    os.system("mkdir /{}".format(d))
    os.system("mount /dev/{}/{} {}".format(v,lv,d))
    os.system("tput setaf 2")
    print("lv created successfully..")
    os.system("tput setaf 7")
    os.system("df -hT")

    while True:
        ext = input("Do you want to entend LV(y/n): ")
        if ext == "y":
            extsize = input("Enter Volume size(GiB) to extend: ")
            extsize = int(extsize)
            print("resizing...")
            os.system("lvextend --size +{}G {}/{}".format(extsize,v,lv))
            os.system("resize2fs {}/{}".format(v,lv))
        else:
            break
    
    os.system("tput setaf 2")
    print("Task Completed!")
    os.system("tput setaf 7")


else:
    exit()
