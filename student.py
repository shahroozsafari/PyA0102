class Student :

    university = "Tehran uni"

    def __init__(self,first_name,last_name,std_id,code):
        self.first_name = first_name
        self.last_name = last_name
        self.std_id = std_id
        self.code_melli = code
        self.courses = {}
    
    def add_course(self,course,score):
        self.courses[course] = score

    @property
    def std_id(self):
        return self._student_id
    
    @std_id.setter
    def std_id(self, value):
        # if len(str(value)) == 6 :
        if 100000 <= value <= 999999 :
            self._student_id = value
        else :
            raise ValueError("Student ID Must be 6 digits !")
        
    @property
    def avg(self):
        score =list(self.courses.values())
        return round(sum(score) / len(score) ,2)
    

#------------------- Main --------------

std1 = Student("Ali","Ahmadi",123456,"6598659865")
std1.add_course("math",15)
std1.add_course("programming",19)
std1.add_course("Physics",16)
print(std1.avg)
