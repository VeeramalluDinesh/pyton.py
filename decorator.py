# Decorator
def function(func):
 def myinner():
   return func().upper
 return myinner()
@function
def my_fun():
 print("Hello Dinesh")
print(my_func())

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("Dinnu"))
