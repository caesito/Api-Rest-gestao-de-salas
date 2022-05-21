import datetime


data=datetime.datetime(2022,5,20,4,30)
data1=datetime.datetime(2022,5,20,5,30)
data2=datetime.datetime(2022,5,20,5,30)

print(data.time())
print(data.date())

if data > data1:
    print('rolou')
elif data1 == data2:
    print('rolou de novo')
else:
    print('rolou tbm')