import random as r
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l', 'm', 'n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['0','1','2','3','4','5','6','7','8','9']

datas = [alphabets , symbols , numbers]

length = int(input("Enter the length of the password to be generated:"))
password = ""
data_ch = 0
for i in range(0,length):
    dataset_ch = r.randint(0,2)
    if dataset_ch == 0:
        data_ch = r.randint(0,25)
    else:
        data_ch = r.randint(0,9)
    password += str(datas[dataset_ch][data_ch])


print("Generated Password:{0}".format(password))

