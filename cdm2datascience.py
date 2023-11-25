#From Data Manager to Data Scientist (LinkedIn Group)

#First, we will show a message on the screen welcoming the user
#and typing the name of the LinkedIn Group.

#Next we will ask the end user some information to be able to run our program,
#and we will save this information in variables (assumptions are made here
#we will create some data listings later on and merge with this program in the near future).

#Finally, we will write on the screen all the data that we have collected, and we will allow
#the user to write a status message.

#We are going to ask the end user for some information about their clinical project.
#For example, study name, therapeutic area, site number and so on...

#Finally we will write on the screen the data that we have collected from the user using print
#and we will ask the end user to write a message to display on the screen.

############################################################start here
print("Welcome to... ")
print("""
 #######                         ######                      
#       #####   ####  #    #    #     #   ##   #####   ##   
#       #    # #    # ##  ##    #     #  #  #    #    #  #  
#####   #    # #    # # ## #    #     # #    #   #   #    # 
#       #####  #    # #    #    #     # ######   #   ###### 
#       #   #  #    # #    #    #     # #    #   #   #    # 
#       #    #  ####  #    #    ######  #    #   #   #    # 
                                                            
#     #                                                           
##   ##   ##   #    #   ##    ####  ###### #####     #####  ####  
# # # #  #  #  ##   #  #  #  #    # #      #    #      #   #    # 
#  #  # #    # # #  # #    # #      #####  #    #      #   #    # 
#     # ###### #  # # ###### #  ### #      #####       #   #    # 
#     # #    # #   ## #    # #    # #      #   #       #   #    # 
#     # #    # #    # #    #  ####  ###### #    #      #    ####  
                                                                  
######                      
#     #   ##   #####   ##   
#     #  #  #    #    #  #  
#     # #    #   #   #    # 
#     # ######   #   ###### 
#     # #    #   #   #    # 
######  #    #   #   #    # 
                            
 #####                                              
#     #  ####  # ###### #    # ##### #  ####  ##### 
#       #    # # #      ##   #   #   # #        #   
 #####  #      # #####  # #  #   #   #  ####    #   
      # #      # #      #  # #   #   #      #   #   
#     # #    # # #      #   ##   #   # #    #   #   
 #####   ####  # ###### #    #   #   #  ####    #  

""")


#First interaction
cdm = input("Enter your name. ")
print()
print("Hola ", cdm, ", This is a Python auto-program from 'From Data Manager to Data Scientist'")
print()

#Sencond interaction
study = input("Enter your clinical study name. ")
print()

#Third interaction
siteno = int(input("Enter the number of sites participating in this trial "))
print()

#Forth interaction
thera = input("Enter the therapeutic area. ")
print()

#Let's write to the screen the information entered by the end user
print()
print("Thank you,", cdm, ". We will create the clinical listings with the information you entered.")
print("--------------------------------------------------")
print("Data Manager:  ", cdm)
print("Study:    ", study)
print("Number of Sites:", siteno)
print("Therapeutic Area:  ", thera)
print("--------------------------------------------------")
print("Thank you for the information.  We hope you enjoy this program.")
print()

#Finally, We request a message that serves to publish a user status.
mensaje = input("Now we are going to publish your first message. Did you like this program? ")
print()
print("--------------------------------------------------")
print(cdm, "says:", mensaje)
print("--------------------------------------------------")

############################################################End of program


