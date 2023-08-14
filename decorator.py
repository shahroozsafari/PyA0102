
def addline(function):
    def wrapper(*n):
        print("-------------------------------")
        function(*n)
        print("-------------------------------")
        return function
    return wrapper

@addline
def greeting(name,family):
    print("Hello "+name+family)

@addline
def test():
    print("dofhguiofhgodfhodf")

@addline
def print_numbers(a,b,c,d,e,f):
    print(a); print(b) ; print(c) ; print(d) ; print(e) ; print(f)

#-------------------- Main ---------------------
greeting("Reza","Ahmadi")
test()
print_numbers(100,200,300,400,500,600)
