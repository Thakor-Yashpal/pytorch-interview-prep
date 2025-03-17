class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

e1 = employee("John",22,"70k") 
e2 = employee("Nova",21,"50k")
print(e1.name, e1.age,e1.salary)
print(e2.name, e2.age,e2.salary)   


class student :
    def __init__(self,st_name,classs,st_id):
        self.st_name = st_name
        self.classs = classs
        self.st_id = st_id
      

N1 = student("Yashpalsinh",'11th',"Fye_yash_088")
N2 = student("surpalsinh",'12th','fly_surl_0091')

print(N1.st_name,N1.classs,N1.st_id)
print(N2.st_name,N2.classs,N2.st_id)