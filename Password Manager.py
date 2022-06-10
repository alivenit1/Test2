
import os

# This function is for adding encrypted user credentials into the password manager text file. 
# This function requests user to key in their credentials 
# Credentials are encrypetd using rot3 algorithm and saved to the file 



def addUser(): 
    #print ("I am in Add user")
    uName = input("Enter User name : ")
    uPassword = input("Enter User password : ")
    uURL = input("Enter URL : ")
    clearText = uName + "\t" + uPassword + "\t" + uURL   # concatinating all the user credentials
    # charSet is the base for ROT3 encryption method 
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=+|\}]{[\"':;?/>.<, "
    # encText is the encrypted value of the supplied credentials
    encText = "".join([charSet[(charSet.find(c)+3)%95] for c in clearText])
    f = open("myPasswordManager.txt", "a") # opening file in append mode 
    f.write (encText + "\n") # writing  the encrypted text into text file
    f.close()
    print ("\nCredentials added successfully!")



#  This function is for displaying credentials 

def displayUser(): 
    
    if os.path.exists('myPasswordManager.txt'):
        f = open("myPasswordManager.txt", "r") # open the text file in read mode 
        print ("Username" + "     " + "Password" + "     " + "URL")
        for x in f:
            encText = x
            charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=+|\}]{[\"':;?/>.<, "
            decText = "".join([charSet[(charSet.find(c)-3)%95] for c in encText])
            
            print (decText)
            #print(myCred)
            
        f.close()
    else:   
        print("No Password Manager file exists, please enter credentils first")
        
    print("\n\nCredentials displayed successfully !")
    
    
#Begining of the main program 
 
print("\nPassword Manager Program ")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to add credentials to file.")
    print("[2] Enter 2 to display the credentials." )
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nEnter your choice ")
    
    # Respond to the user's choice.




    if choice == '1':
        print("\nAdd credentilas to Password Manager file ..\n")
        addUser() #Calling addUser function
           
    elif choice == '2':
        print("\nDisplaying User Credentials ….\n")
        displayUser() #call displayUser function

    
    elif choice == 'q':
        print("\nExiting the Program, Bye \n")

    else:
        print("\nInvalid option entered, please try again.\n")
        
# Print a message that we are all finished.

print("Program exit.")
