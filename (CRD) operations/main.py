import threading
import time
import os
d={}
f= "Pythonfil.txt" #Creating a File 
def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                  
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

#read operation
            
def read(key):
  
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        x=str(d)
        file = open(f,"w")
        file.write(x) 
        file= os.popen(f,"w")
        b=d[key] 
        
        if b[1]!=0:
           
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation

def delete(key):
    
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                x=str(d)
                file = open(f,"w")
                file.write(x) 
                file= os.popen(f,"w")
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            x=str(d)
            file = open(f,"w")
            file.write(x) 
            file= os.popen(f,"w")
            print("key is successfully deleted")


