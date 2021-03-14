import subprocess
import os

print("\t\t\t\t\t\t\t\t!! Hello There !!")
print("\t\t\t\t\t      Welcome to our LVM Partition using Python program\n\n")
print("Choose from the following requirements: ")
print()
while True:

    print("1) Create Physical Volume\n 1.1) Display Status")
    print()
    print("2) Create  Volume Group\n 2.1) Display Status")
    print()
    print("3) Create Logical Volume\n 3.1) Display Status")
    print()
    print("4) Create Folder to Mount\n 4.1) Display Status")
    print()
    print("5) Create Increase/Decrease Size\n 5.1) Display Status\n")
    print("6) Add hard disk to a Volume Group to increase Size ")
    print("7) exit ")
    print()
    ch = input("Enter your Requirement: ")
    try:
        if int(ch) == 1:
            fdisk = subprocess.getoutput("fdisk -l")
            disk = input("Enter Your Disk Name: ")
            z = subprocess.getoutput("pvcreate {}".format(disk))
            print(z)
            
        elif int(ch) == 1.1:
            disk = input("Enter Your Disk Name: ")
            display = subprocess.getoutput("pvdisplay {}".format(disk))
            print(display)
            
        elif int(ch) == 2:
            print("intially creating  volume group with the help of two hard disk only:")
            hd1=input("Enter the name of first hard disk: ")
            hd2=input("Enter the name of second hard disk: ")
            vgname=input("Enter the name of volume group you want to create: ")
            z=subprocess.getoutput("vgcreate {} {} {}".format(hd1,hd2,vgname))
            print(z)
            
        elif int(ch) == 2.1:
            vgname=input("enter the name of the volume group")
            z=subprocess.getoutput("vgdisplay {}".format(vgname))

        elif int(ch) == 3:
            size=int(input("enter the size for volume group:"))
            vgname=input("Please enter  the volume group name to create LV: ")
            lv=input("Enter the name to create logical volume: ")
            z=subprocess.getoutput("lvcreate --size {}G --name {} {}".format(size,lv,vgname))
            print(z)
            
        elif int(ch) == 3.1:
            dir=input("enter full directory of LV ex. [vgname/lvname]")
            z=subprocess.getoutput("lvdisplay {}".format(dir))

        elif int(ch)==4:
            dir=input("please enter the directory name contributed to hadoop  : ")
            lv=input("please enter the full name of  volume group that is to be mount :  ")
            z=subprocess.getoutput("mkdir {}".format(dir))
            y=subprocess.getoutput("mount {} {}".format(lv,dir))
            
        elif int(ch)==4.1:
            print("full details of mounted folders are as follows: ")
            print(subprocess.getoutput("df -h"))
            
        elif int(ch)==5:
            size=int(input("please enter the size do you want to contribute:"))
            z=subprocess.getoutput("lvresize --resizefs --size {}G lv".format(size))
            
        elif int(ch)==7:
            exit()
            
        elif int(ch) ==6 :
            hd=input("Enter name of hard disk to add: ")
            vgname=input("Enter the name of volume group: ")
            z=subprocess.getoutput("vgextend {} {}".format(vgname,hd))
            
        print("press enter to continue")
        input()
        os.system("cls")
        
    except:
         print("Something went wrong!!")
