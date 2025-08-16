print("\n")
print("Well-come to [CAL-PULS]\nHere you can perfrom arithmetic opretions between two numbers...")
while True:
    print("\n")
    num_1=int(input("Enter the first  Number:-"))
    print('\n')
    num_2=int(input("Enert the second Number:-"))
    print("\n")
    print(f"First  Number = {num_1}\nSecond Number = {num_2}")
   
  
    print(f"Choose  Arithmatic opretretor..\n\n1=Addition\n2=Subtraction\n3=Multiplication\n4=Division\n5=Modulus\n6=All those above")
    print("\n")
    

    while True:  
      
      user=int(input("Enter the opretion number:-"))
      print("\n")
      if  user>6:
         print("\nType only given options..\n")
         continue 
      
      
      elif user<=6:
         if user==1:
           print(f"The Addition of [{num_1} + {num_2} = {num_1+num_2}]\n\nThe opretion is complited\n\nEnter new values..") 
           break
           
         elif user==2:
           print(f"The Subtraction of [{num_1} - {num_2} = {num_1-num_2}]\n\nThe opretion is complited\n\nEnter new values..")
           break

         elif user==3:
          print(f"the Multiplication of [{num_2} x {num_2} = {num_1*num_2}]\n\nThe opretion is complited\n\nEnter new values..")
          break

         elif user==4:
          print(f"the Division of [{num_1} / {num_2} = {num_1/num_2}]\n\nThe opretion is complited\n\nEnter new values..")
          break
         elif user==5:
           print(f"The modulus of [{num_1}] % [{num_2}] = {num_1%num_2}\n\nThe opretion is complited\n\nEnter new values..")
           break
 
         elif user==6:
           print(f"The Addition of [{num_1} + {num_2} = {num_1+num_2}]\n\nThe subtraction of [{num_1} - {num_2} = {num_1-num_2}]\n\nthe Multipliction of [{num_2} x {num_2} = {num_1*num_2}]\n\nthe Divesion of[{num_1} / {num_2} = {num_1/num_2}]\n\nThe Modulus of [{num_1}] % [{num_2}] = {num_1%num_2}\n\nThe opretion is complited\n\nEnter new values..")
           break
         
         
     

          
        
      
          
         
      
      
      
      
       
          
        
      


    




    


          
        
      


    




    


         
         