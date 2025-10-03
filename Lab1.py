class DisplayName:
      def displayName(self):
            pass

class DisplayDuration:
     def displayDuration(self):
          pass

class Course(DisplayName, DisplayDuration):

     Subscribers = 0
     CoursePrice = 100

     def __init__(self, course_name, course_duration):

         self.Name = course_name
         self.__CourseDuration = course_duration



     def displayName(self):
          print(f"Name: {self.Name}")

     def displayDuration(self):
          print(f"Course Duration: {self.__CourseDuration}")     

     def AddSubscriber(self):
          Course.Subscribers += 1
          print(f"Total Subscribers: {Course.Subscribers}")     

     @staticmethod
     def printWelcomeMessage():
           print("Welcome to the Course Management System!")

     @classmethod
     def coursePriceInfo(cls):
           print(f"Course Price Info: {cls.CoursePrice}")



class Teacher(Course):

     def __init__(self, name):
          self.Name = name
          
     def displayName(self):
          print(f"Name: {self.Name}")



print()
teacher = Teacher("John Doe")
course = Course("Python Programming", "3 months")

course.printWelcomeMessage()
for name in (teacher, course):
     name.displayName()


course.coursePriceInfo()
course.displayDuration()

course.AddSubscriber()
course.AddSubscriber()


