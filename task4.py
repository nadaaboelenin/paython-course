emplyeeList=list()
def __init__(self,empName,empAge,empSal):
         self.empName, self.empAge, self.empSal= empName,empAge,empSal
def addNewEmployee(self):
    emplyeeList.append(__init__)  
def getEmpList(self): 
    return emplyeeList    
def updateEmpByName(self,empSal):
    for emp in emplyeeList:
        if(emp.getEmpName()==empName):
            emp.empSal=empSal
            return True
        return False        
def removeEmpByAge(self,empAge):
    for emp in emplyeeList:
        if(emp.getEmpAge()>=empAge):
            emplyeeList.remove(emp)
            return True
        return False    
def setEmpName (self,empName):
    self.empName=empName
def getEmpName(self):
    return self.empName
def setEmpSal(self,empSal):
    self.empSal=empSal
def getEmpSal(self):
    return self.empSal
def setEmpAge(self,empAge):
    self.empAge=empAge
def getEmpAge(self):
    return self.empAge
   

choice=1
while choice >=1 and choice <=4:
    print("\n\n1.add new emplyee\n2.Get All Employee List\n3.update employee salary\n4.remove Employee by age")
    choice=int(input('enter your choice:'))
    if(choice==1):
        empName=input('enter employee name:')
        empAge=int(input('enter employee age:'))
        empSal=int(input('enter employee salary:'))
        emp= (empName, empAge,empSal)
        addNewEmployee(emp)
    elif (choice == 2):
        print('\n')
        for emp in getEmpList(emp):
            print(f" Employee:{empName} hasage {empAge} and salary {empSal}")
    elif(choice ==3):
         empName=input('enter employee name:')
         empSal=int(input('enter employee  new salary:'))
         emp= updateEmpByName(empSal)
         if( emp == False):
             print('Employee not found')
         else:
             print('succesfully Updated')    
    elif (choice==4):
        ageRange_1=int(input('enter your age from'))
        ageRange_2=int(input('enter your age from'))
        empAge=(ageRange_1 and ageRange_2)
        emp=removeEmpByAge(empAge)
        if(emp==False):
            print('Employee not found')
        else:
            print('sucess')    
    


        

 
    
