# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:41:29 2018

@author: Demon King
"""

from Read_File import Read_File  
from class_Linia import *
import os
import traceback
import sys
#import datetime
cont=1
status='y'
while cont==1:
    prod_type,prod_cat = \
    (input("Enter the product type and category separated by commas: ")).split(',')
    
    dir_name="P:\\Products\\"+prod_type+"\\"+prod_cat
    try:
        os.chdir(dir_name)
        cont=0
    except:
        print("Directory ",dir_name," not found")
        while status !='n':
            status=input("Do you wish to continue(y/n)? ")
            if status=='y':
                break
            elif status=='n':
                print("Okay, Bye!")
                sys.exit()
            else:
                print("Sorry, I didn't understand that input")
                continue
        #break
        
#os.chdir("P:\Products\RECESSED-LINIA")
order_path='order.txt'
order_list=[i for i in Read_File(order_path) if not i.startswith('#')]
o=1
err_status=0
if os.path.exists("3G_err.txt"):
    os.remove("3G_err.txt")
with open('3G_out.txt', 'w') as f:
    for order_desc in order_list:
        print("\nOrder number",o,': ',order_desc.split(',')[0],file=f)
        try:
            order = Linia(order_desc)
            order.fetch_ha_id()
            order.display(f)
            order.write_order_files()
        except Exception as e:
            err_status=1
            print(e,file=f)
            if o==1:
                option='w'
            else:
                option='a'
            with open('3G_err.txt', option) as err:
                print("Order Name: ",order_desc,file=err)
                print("\n",traceback.format_exc(),file=err)
                
        o+=1
if err_status==0:        
    print("\nProcessing complete with no errors")        
else:        
    print("\nProcessing complete with some errors, check the error file")

input("\nPress Enter to exit")    