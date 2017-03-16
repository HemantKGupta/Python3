def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32
print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
#print(KelvinToFahrenheit(-5))



try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data in IOError")
else:
   print("Written content in the file successfully")
   fh.close()


try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print("Error: can\'t find file or read data in finally")