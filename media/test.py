# from Crypto.Cipher import AES
# from Crypto.Hash import SHA256
# from Crypto import Random
# import base64
# # # example 
# # dict = {0:32,1:23,2:34}
# # list  = [("x_0",0.34),("x_11",0.55),("x_13",0.55),("x_22",0.45),("x_1",0.55),("x_15",0.65),("x_42",0.35),("x_40",0.55),("x_16",0.54),("x_23",0.51),("x_24",0.50),("x_45",0.35),("x_25",0.52),("x_19",0.53)]

# # t =''
# # sum = 0
# # n = []
# # for i in list:
# #     p = i[0]
# #     for j in p:
# #         if j in '1234567890':
# #             t+=j
# #     k = int(t)//24
# #     n.append(int(t))
# #     print(k)
# #     t=''
# #     sum += i[1]*dict[k]
    
# # print(n)
# # print("sum = ",sum)   

# d0 = {0:3,1:4}
# d1= {0:2,2:5,1:3}
# d3 = {0:22,1:23}
# # l = [d0,d1]
# d = {0:d0,1:d1,3:d3}
# # for i in [0,1]:
# #     for j in range(len(l[i])):
# #         print(l[i][j])
# # for i in[0,1,3]:
# #     for j in range(len(d[i])):
# #         print(d[i][j])


# # d0 = {0:3,1:4}
# # d1= {0:2,2:5,1:3}
# # d3 = {0:22,1:23}
# # import json
# ###############
# # import ast
# # import json
# # string = '{ "website":"password","Facebook":[None] }'

# # record = ast.literal_eval(string)
# # record['Facebook'].append('fb')
# # print(record ,type(record['Facebook']))
# # # print(record,type(record))
# # l = "[1,2,4]"
# # res = l.strip('][').split(',')
# # print(res,type(res))

# # if (record['Facebook']):print('yes')
# # else:print('no')
# # print(record)
# # record = json.loads(string)
# ##############
# # while(True):
# #     print("Enter choice:")
# #     print("1.Add Password")
# #     print("2.Change Password")
# #     print("3.Exit")
# #     x = int(input())
# #     if x==1:
# #         w=input("Enter Website name : ")
# #         p = input("Enter password : ")
# #         record.update({w:p})
# #         print("Dict",record)    
# #     elif x==2:
# #         w=input("Enter Website name : ")
# #         n = input("Enter new Password : ")
# #         record[w]=n
# #         print("Dict ",record)
# #     else:break    

# # def email(m):
# #     global mail
# #     mail = m
# #     print(mail)
# # def disp():
# #     print(mail)     
# # email('hello')     
# # disp()

# # n = int(input("Enter the number : "))    
# # s = str(bin(n))
# # print(s[2:],s[2:].count('1'))

# # d = {1:2,2:'a',3:4,4:None}
# # print(str(d))

# # x=['a','b','c',None]
# # d.update({3:5})
# # print(d)
# # c=0
# # for i in d.keys():
# #     d.update({i:x[c]})
# #     c+=1
# # print(d)    
# # x = "hello"
# # print(x.encode())
# # def encrypt(key, source, encode=True):
# #     key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
# #     IV = Random.new().read(AES.block_size)  # generate Initialization vector
# #     encryptor = AES.new(key, AES.MODE_CBC, IV)
# #     padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
# #     source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
# #     data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
# #     return base64.b64encode(data).decode() if encode else data
# # password = "1234"
# # message = "hello"
# # cipher=encrypt(password.encode(),message.encode())
# # print("Cipher : ",cipher)

# # def decrypt(key, source, decode=True):
# #     if decode:
# #         source = base64.b64decode(source.encode())
# #     key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
# #     IV = source[:AES.block_size]  # extract the Initialization vector from the beginning
# #     decryptor = AES.new(key, AES.MODE_CBC, IV)
# #     data = decryptor.decrypt(source[AES.block_size:])  # decrypt
# #     padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
# #     if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
# #         raise ValueError("Invalid padding...")
# #     return data[:-padding]  # remove the padding
# # decoded=decrypt(password.encode(),cipher)
# # print("Decoded :",decoded.decode())
# # print(type(decoded))
# # print(type(decoded.decode()))

# # try :
# #     raise Exception
# # except:
# #     def show():
# #         print("Error")    
# #     show()    
# # x = [0,1,2,3,4,5,6,7,8]
# # m = 4.1
# # f = [1,9,26,39,72,52,29,7,1]
# # d = []
# # fd = []
# # for i in x:
# #     d.append(i-m)
# # for i in range(len(d)):
# #     fd.append(f[i]*(d[i]**2))
# # print(fd)
# # print(sum(fd))    
# # print("variance = ",sum(fd)/sum(f))
# # print("SD = ",(sum(fd)/sum(f))**0.5)

# # x=[2002,2003,2004,2005,2006]
# # y=[10,12,13,10,8]
# # x2=[]
# # x3=[]
# # x4=[]
# # xy=[]
# # x2y=[]
# # for i in range(len(x)):
# #     x2.append(x[i]**2)
# #     x3.append(x[i]**3)
# #     x4.append(x[i]**4)
# #     xy.append(x[i]*y[i])
# #     x2y.append((x[i]**2)*y[i])
# # print(x2,x3,x4,xy,x2y)    

# a = [16,14,15,20,12,13,18,15,14,14,15,16,15,16,14,12,15,16,18,20]
# b = [20,17,18,19,20,18,20,19,18,20,19,18,20,18,19,20,19,18,19,18,]
# c = [15,14,15,16,14,12,14,16,17,14,16,20,16,15,17,18,19,16,17,19,]
# x1 = sum(a)/20
# x2 = sum(b)/20
# x3 = sum(c)/20

# da=[]
# db=[]
# dc=[]
# for i in a:
#     da.append((i-x1)**2)
# for i in b:
#     da.append((i-x2)**2)
# for i in c:
#     dc.append((i-x3)**2)        
# va = sum(da)/20
# vb = sum(db)/20
# vc = sum(dc)/20

# print('Group-1')
# print('Mean  = ',x1,'Variance = ',va,'SD = ',va**0.5)
# print('Group-2')
# print('Mean  = ',x2,'Variance = ',vb,'SD = ',vb**0.5)
# print('Group-3')
# print('Mean  = ',x3,'Variance = ',vc,'SD = ',vc**0.5)   

# print('T test for group 1 and 2')
# s = ((sum(da)-sum(db))/38)**0.5
# t = (x1 -x2)/s/(0.1**0.5)
# print('t =',abs(t))

# print('T test for group 2 and 3')
# s = ((sum(db)-sum(dc))/38)**0.5
# t = (x2 -x3)/s/(0.1**0.5)
# print('t =',abs(t))

# print('T test for group 1 and 3')
# s = ((sum(da)-sum(db))/38)**0.5
# t = (x3 -x1)/s/(0.1**0.5)
# print('t =',t)

import pandas as pd
import numpy as np

# def make_df(cols,ind):
#     data = {c:[str(c)+str(i) for i in ind] for c in cols}
#     return pd.DataFrame(data,ind)
# a = make_df('ABC',[1,2])
# b = make_df('BCD',[1,2])
# # print(pd.concat([a,b.reindex(a.columns,axis=1)],keys=['a','b']))
# print(pd.concat([a,b],join='inner'))
# # b.index = a.index
# # print(pd.concat([a,b],axis='columns'))
# print(a._append(b))

import pandas as pd
data=pd.read_csv("C:/Users/DELL/Desktop/Train_details_22122017.csv")
stations=data[['Station Name','Station Code']]
codes=stations.groupby(['Station Name','Station Code']).sum()
print(type(codes))
codes.to_csv('final.csv')