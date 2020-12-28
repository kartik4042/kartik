import json #for file saving and uploading
import time

#master={} do only one time
temp={}

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

x= input("Do you want to import master database and perform operations on it yes/no :")
if(x== 'yes'):
    #load master database
    print('Loading master database in temp....')
    with open('master.json', 'r') as masteropen:
        data_load = json.load(masteropen)
temp=data_load
print('Loaded master database')
print(temp)

d=temp

#for read operation
#use syntax "read(key_name)"

def read(k):
    if k not in d:
        print("Error:This key is not present")
    else:
        b=d[k]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(k)+":"+str(b[0])
                return stri
            else:
                print("Error: time-to-live of",k,"has expired")
        else:
            if(x==1):
                key=input('enter key for input')
                value=int(input('Enter its corresponding value '))
                #timeout=int(input('Enter time, default is 0'))
            if(x==2):
                key=input('Enter key to read')
                delete(key)
                print('key delete')
            if(x==3):
                key=input('Enter key')
                delete(key)
                print('key deleted')
            if(x==4):
                print(d)
            
import json
temp=d
with open('temp.json','w') as fp:
    json.dump(temp,fp)

print('Your database after operations are :')
print(temp)

x=input('is this first ever operation yes/no ')
if(x=='yes'):
    with open('master.json','w') as fp:
        json.dump(temp,fp)
    print("thank you")
    exit()

x=input('Do you want to save this is the master database yes/no :')
if(x=='yes'):
    data={}
    import jason
    with open('master.json','r') as fp:
        json.dump(master,fp)


print('All task done , thanks')
