
# from collections import OrderedDict
# d=OrderedDict()
# d[100]='naresh'
# d[101]='mohan'
# d[103]='srinu'
# # print(dict)
# dt={104:'sai',105:'gopi'}
# d.update(dt)
# print(d)

# import sys
# for x,y in sys.argv:
#      print ("Argument: ", x)
#      print("Argument: ",y)

# how to give arguments in command prompt  #######
import argparse
# import sys
#
# def check_arg(args=None):
#     parser = argparse.ArgumentParser(description='Script to learn basic argparse')
#     parser.add_argument('-H', '--host',
#                         help='host ip',
#                         required='True',
#                         default='localhost')
#     parser.add_argument('-p', '--port',
#                         help='port of the web server',
#                         default='8080')
#     parser.add_argument('-u', '--user',
#                         help='user name',
#                         default='root')
#
#     results = parser.parse_args(args)
#
#     return (results.host,
#             results.port,
#             results.user)
#
# if __name__ == '__main__':
#     h, p, u = check_arg()
#     print ('h =',h)
#     print ('p =',p)
#     print ('u =',u)

# lines=0
# words=0
# chars=0
# f=open('New Text Document.txt','r')
# data=f.read()
# print(data)
# for line in data:
#     print(line)
#     print(len(line))
#     word=line.split(' ')
#     print(word)
#     print(len(word))
#     lines=lines+1
#     words=words+len(word)
#     chars=chars+len(line)
# print('chars:',chars)
# print('words:',words)
# print('lines:',lines)
# import csv
# with open('student.csv','w')as f:
#     w=csv.writer(f)
#     w.writerow(["sno","sname","saddr"])
#     n=int(input("enter number of students:"))
#     for i in range(n):
#         sno=input("enter student no:")
#         sname=input("enter student name:")
#         saddr=input("enter student addr:")
#         w.writerow(["sno","sname","saddr"])
import csv
f=open('student.csv','r')
r=csv.reader(f)
data=list(r)
print(data)
for line in data:
    for word in line:
        print("word","\t")
