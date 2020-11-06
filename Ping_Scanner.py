import os
import pyfiglet

class Ping:
   def __init__(self):
      pass
   
   def ping(self):
      result = pyfiglet.figlet_format("Ping Scanner") 
      print(result)  
      ping = input("Enter an ip address to scan or a website domain\n")
      os.system(f"ping {ping}")
      print()
      if ping == "":
         os.system("cls")
         return s.ping()
      def Again():
         while True:
            root = input("Would you like to ping more ip's or website domains? [y] or [n]\n")
            if root == "y":
               os.system("cls")
               return s.ping()
            if root == "n":
               exit()
      Again()

s = Ping()
s.ping()
