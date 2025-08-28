'''
Name: 9001341-A2.py
Author: Chris Szabla
Date Created: 2021-07-16
Date last modified: 2024-07-17
Date Due: 2024-07-24

Purpose: The purpose of this program is to calculate the total cost of a customers food order
based off 6 menu items, their cost and qty selected. Once calculated, the program will print 
a reciept to screen and to a text file. The reciept will include the customers information, 
order details and pricing. The program will check to see if the customer is a student and 
apply a discount if true. The program will check if the user is in an apartment and adjust 
the address printout. The Program will check to see if the order is for delivery or pickup 
and adjust the cost and printout of the reciept. The program will also calculate the tip and 
adjust pricing and printout accordingly. 

This program was designed specifically for Arnold's Amazing Eats! 
'''

''' 
Defining dictionaries to store menu and customer/order information and a list of tuples for storing constants 

'''

# Importing OS module for file management functionality  
import os

# Dictionary to store all menu items and pricing
menuDict={"1" : {"name" : "Cheese Pizza", "price" : 8.99},
      "2" : {"name" : "Pepperoni Pizza", "price" : 9.99},
      "3" : {"name" : "Hawaiian Pizza", "price" : 12.99},
      "4" : {"name" : "Canadian Pizza", "price" : 13.99},
      "5" : {"name" : "Deluxe Pizza", "price" : 14.99},
      "6" : {"name" : "Vegetarian Pizza", "price" : 12.99},
      "companyName" : " Arnold's Amazing Eats! "
      }

# Dictionary to store all customer and order information 
customerDict={"First Name:": "",	
        "Last Name:": "",
        "Phone Number:" : "", 
        "Student:": "",
        "Delivery Instructions:" : "",
        "Delivery:" : "",
        "Street Number:" : "",
        "Street Name:" : "",
        "Unit Number:" : "",
        "City:" : "",
        "Province:" : "",
        "Postal Code:" : "",
        "OrderDic": {
            "1" : {"name" : "Cheese Pizza", "price" : 0, "quantity" : 0}, 
            "2" : {"name" : "Pepperoni Pizza", "price" : 0, "quantity" : 0},
            "3" : {"name" : "Hawaiian Pizza", "price" : 0, "quantity" : 0},
            "4" : {"name" : "Canadian Pizza", "price" : 0, "quantity" : 0},
            "5" : {"name" : "Deluxe Pizza", "price" : 0, "quantity" : 0},
            "6" : {"name" : "Vegetarian Pizza", "price" : 0, "quantity" : 0},
            "discountAmount" : 0,
            "hstAmount" : 0,            
            "subtotal" : 0,            
            "totalAmount" : 0,            
            "deliveryCharge" : 0,
            "tip" : 0,
            "tipAmount" : 0            
            }
        }

# Using a list of tuples to store constants
constants = [
    ("tax", 1.13),
    ("studentDiscount", .9),
    ("deliveryFee", 5)
]

# Name for reciept file can be changed here
recieptFileName = "amazingEatsReciept.txt"


''' 
Defining functions to control various parts of the program flow

'''

# Function:     getConstant
# Description:  Function return a desired constant when given a type i.e tax
# Parameters:   type: Type of constant required i.e tax                 
# Return value: constant: Actual value
# 
def getConstant(type):
    for constant in constants:
        if constant[0] == type:
            return(constant[1])


# Function:     welcomeBanner 
# Description:  Function displays the assignment welcome banner
# Parameters:   name: Company name                  
# Return value: none
#
def welcomeBanner(name):
    print('{0:#^60s}'.format(''))
    print('{0:#^60s}'.format(name["companyName"].upper()))
    print('{0:#^60s}'.format(' ORDERING SYSTEM '))
    print('{0:#^60s}'.format(' Created by: Chris Szabla '))
    print('{0:#^60s}'.format(' PROG1783 '))
    print('{0:#^60s}'.format(' Prof. Ivkovic '))
    print('{0:#^60s}'.format(''))


# Function:     welcomeMessage
# Description:  Function displays user welcome message, instructs user on what to do to get started 
# Parameters:   name: Company name                    
# Return value: none
# 
def welcomeMessage(name):
    print("")
    print("Welcome to{}Ordering System!".format(name["companyName"]))
    print("")
    print("You've started a new order. To complete your order, please follow the prompts and provide the requested customer information.")
    print("")


# Function:     collectCustomerDetails
# Description:  Collects customer information, updates customerDict and checks if inputs are valid  
# Parameters:   customerDict: Stores customer information                 
# Return value: customerDict
#
def collectCustomerDetails(customerDict):        
    
    # Collecting basic customer information
    while True:   
        
        try:

            customerDict["First Name:"] = input("First name: ").strip().capitalize()
            
            if customerDict["First Name:"] == '' or customerDict["First Name:"].isalpha() == False:
                
                raise ValueError("Please enter a valid first name. Press [Enter] to continue...")
            
            else:
                
                break
        
        except ValueError as inputError:           
            
            print("{}".format(inputError),end=" ")
            input("")
            continue
        
    while True:
        
        try:    
            
            customerDict["Last Name:"] = input("Last name: ").strip().capitalize()
            
            if customerDict["Last Name:"] == '' or customerDict["Last Name:"].isalpha() == False:
                
                raise ValueError("Please enter a valid last name. Press [Enter] to continue...")
            
            else:
                
                break  
        
        except ValueError as inputError:           
            
            print("{}".format(inputError),end=" ")
            input("")
            continue

    while True:
        
        try:    
            
            customerDict["Phone Number:"] = input ("Phone #: ").strip()
            
            if customerDict["Phone Number:"] == '' or customerDict["Phone Number:"].isnumeric() == False:
                
                raise ValueError("Please enter a valid phone number. Press [Enter] to continue...")
            
            else:
                
                break

        except ValueError as inputError:           
            
            print("{}".format(inputError),end=" ")
            input("")
            continue

    # Asks if customer is a student, will execute at least once, if doesn't recieve correct input will restart and ask again until correct input provided
    while True:
        
        try:
            
            isStudent = input("Student? [Y/N]: ").strip().lower()
            
            # Setting flag for whether student or not
            if isStudent != ('y') and isStudent != ('n') and isStudent != ('yes') and isStudent != ('no'):
                
                raise ValueError("Please select either Yes or No. Press [Enter] to continue...")

            elif isStudent == ('n') or isStudent == ('no'):
                
                customerDict["Student:"] = False
                break

            elif isStudent == ('y') or isStudent == ('yes'):
                
                customerDict["Student:"] = True
                break

        except ValueError as inputError:           
            
            print("{}".format(inputError),end=" ")
            input("")
            continue

    # Asks if delivery, sets flag for delivery if True        
    while True:
        
        try:
            
            isDelivery = input("Delivery? [Y/N]: ").strip().lower()
            
            # Setting flag for no delivery
            if isDelivery != ('y') and isDelivery != ('n') and isDelivery != ('yes') and isDelivery != ('no'):
                
                raise ValueError("Please select either Yes or No. Press [Enter] to continue...")

            elif isDelivery == ('n') or isDelivery == ('no'):
                
                customerDict["Delivery:"] = False
                break

        except ValueError as inputError:           
            
            print("{}".format(inputError),end=" ")
            input("")
            continue

        # If delivery is true, set flag   
        if isDelivery == ('y') or isDelivery == ('yes'):
            
            
            customerDict["Delivery:"] = True
        
            # Collecting address and tip information if delivery          
            while True:
                
                try:
                    
                    customerDict["OrderDic"]["tip"] = input("Please select either 5, 10 or 15 for the tip amount(%): ").strip()
                    
                    if customerDict["OrderDic"]["tip"] == "5" or customerDict["OrderDic"]["tip"] == "10" or customerDict["OrderDic"]["tip"] == "15":
                        
                        break
                    
                    else:
                        
                        raise ValueError("You've entered an invalid input, enter 5, 10 or 15 for the tip amount(%). Press [Enter] to continue...")
                
                except ValueError as inputError:           
                    
                    print("{}".format(inputError),end=" ")
                    input("")
                    continue           

            customerDict["Delivery Instructions:"] = input("Special delivery instructions: ").strip().capitalize()
            
            while True:
                
                try:
                    customerDict["Street Number:"] = input("Street #: ").strip()
                    
                    if customerDict["Street Number:"].isnumeric() == False or customerDict["Street Number:"] == '':
                        
                        raise ValueError("Please enter a valid street number. Press [Enter] to continue...")
                    
                    else:
                        
                        break 

                except ValueError as inputError:           
                    
                    print("{}".format(inputError),end=" ")
                    input("")
                    continue   

            while True:
                
                try:        
                    customerDict["Street Name:"] = input("Street name: ").strip().title()
                    
                    if customerDict["Street Name:"] == '':
                        
                        raise ValueError("Please enter a valid street name. Press [Enter] to continue...")
                    
                    else:
                        
                        break 
                
                except ValueError as inputError:           
                    
                    print("{}".format(inputError),end=" ")
                    input("")
                    continue

            customerDict["Unit Number:"] = input("Unit number or leave blank: ").strip()  
            
            while True:
                
                try:
                    
                    customerDict["City:"] = input("City: ").strip().capitalize()
                    
                    if customerDict["City:"].isalpha() == False or customerDict["City:"] =='':
                        
                        raise ValueError("Please enter a valid City. Press [Enter] to continue...")
                    
                    else:
                        
                        break

                except ValueError as inputError:                             
                    
                    print("{}".format(inputError),end=" ")
                    input("")
                    continue

            while True: 
                
                try:       
                    customerDict["Province:"] = input("Province: ").strip().capitalize()
                    
                    if customerDict["Province:"].isalpha() == False or customerDict["Province:"] == '':
                        
                        raise ValueError("Please enter a valid Province. Press [Enter] to continue...")
                    
                    else:
                        
                        break 
                
                except ValueError as inputError:           
                    
                    print("{}".format(inputError),end=" ")
                    input("")
                    continue
            
            while True:   
                
                try:     
                    customerDict["Postal Code:"] = input("Postal Code: ").strip()
                    
                    if customerDict["Postal Code:"].isalnum() == False or customerDict["Postal Code:"] == '':
                        
                        raise ValueError("Please enter a valid Postal Code. Press [Enter] to continue...")
                    else:
                        
                        break
                
                except ValueError as inputError:           
                    
                    print("{}".format(inputError),end=" ")
                    input("")
                    continue                        
            break

    return customerDict


# Function:     printMenu  
# Description:  Function to print ordering menu 
# Parameters:   menuDict: Contains menu items                   
# Return value: none
#
# 
def printMenu(menuDict):
    i=1 # Counter so last option will always be Accept Order
    
    print("{0:_^58s}".format(''))
    print("")
    print("{0:^58s}".format('MENU'))
    print("{0:_^58s}".format(''))
    
    for menuNumber, item in menuDict.items():
        if menuNumber.isnumeric() == True:
            
            print("{}. {} ${}".format(menuNumber,item['name'],item['price']))
            i+=1
            
    print("{}. [Accept Order]".format(i))


# Function:     runOrderMenu 
# Description:  Function that loops through the menu options and adds quantities to the order until user accepts the order  
# 
# Parameters:   customerDict: to store order information in orderDict
#               menuDict: Used to retrieve menu item information for printing                  
# 
# Return value: customerDict 
#
def runOrderMenu(customerDict, menuDict):
    
    # Valid menu selections and exit selection
    validMenuSelections = ["1","2","3","4","5","6"]
    exit = '7'

    while True:
        
        try:
            
            while True:
                
                # Prints Order Menu 
                printMenu(menuDict)
                
                # Prompts user for menu selection 
                menuSelection=input("\nChoose a menu item. Select [7. Accept Order] when done: ").strip()
                
                # Checks what option was selected, asks for quantity and confirmation.
                # If user selects option 1 
                if menuSelection in validMenuSelections:
                    
                    while True:
                        
                        try:
                            
                            # Asks user to input quantity, cannot be 0, must be numeric 
                            customerDict["OrderDic"][str(menuSelection)]["quantity"] = input("Enter the number of {}'s on the order: ".format(menuDict[str(menuSelection)]["name"])).strip()

                            if customerDict["OrderDic"][str(menuSelection)]["quantity"] == '0':
                                
                                raise ValueError("You've entered an invalid input, value can't be 0. Press [Enter] to continue...")
                            
                            elif customerDict["OrderDic"][str(menuSelection)]["quantity"].isnumeric():
                                
                                break                            
                            
                            else:
                                
                                raise ValueError("You've entered an invalid input. Press [Enter] to continue...")
                        
                        except ValueError as inputError:           
                            
                            print("{}".format(inputError),end=" ")
                            input("")
                            continue

                    while True:    
                        
                        try:
                           
                           # Asks to confirm selection, if not confirmed will repeat until confirmed. User has option to cancel and return to menu 
                            proceed = input("You've selected {} {}'s. Proceed? [Y/N] or type [cancel] to remove item from order and return to main menu: ".format(customerDict["OrderDic"][str(menuSelection)]["quantity"], menuDict[str(menuSelection)]["name"])).strip().lower()
                            
                            if proceed == ('y') or proceed == ('yes'):
                                
                                break

                            elif proceed == 'cancel' or proceed == 'c':

                                customerDict["OrderDic"][str(menuSelection)]["quantity"] = 0
                                break
                            
                            elif proceed == ('n') or proceed == ('no'):
                                
                                while True:
                                    
                                    try:
                                        customerDict["OrderDic"][str(menuSelection)]["quantity"] = input("Enter the number of {}'s on the order: ".format(menuDict[str(menuSelection)]["name"])).strip()
                                        
                                        if customerDict["OrderDic"][str(menuSelection)]["quantity"] == '0':
                                            
                                            raise ValueError("You've entered an invalid input, value can't be 0. Press [Enter] to continue...")
                                        
                                        elif customerDict["OrderDic"][str(menuSelection)]["quantity"].isnumeric():
                                            
                                            break                            
                                        
                                        else:
                                            
                                            raise ValueError("You've entered an invalid input. Press [Enter] to continue...")
                                        
                                    except ValueError as inputError:   

                                        print("{}".format(inputError),end=" ")
                                        input("")
                                        continue                   
                            else:

                                raise ValueError("You've entered an invalid entry. Please select Yes or No. Press [Enter] to continue...")
                            
                        except ValueError as inputError:           
                            
                            print("{}".format(inputError),end=" ")
                            input("")
                            continue                    

                elif menuSelection == (exit):
                    
                    # Checks to make sure order has at least one item
                    
                    itemCount = 0
                    
                    for key in customerDict["OrderDic"]:
                        
                        # Only checks item quantities in order dict
                        if key.isnumeric():
            
                            itemCount += int(customerDict["OrderDic"][key]["quantity"]) 
                    
                    # If the orde has no items, ask user if they want to return to order menu or quit. 
                    if itemCount == 0:
                        
                        while True:                
                        
                            try:
                                
                                # Asks to confirm selection, if not confirmed will repeat until confirmed. 
                                proceed = input("Warning, you currently have no items added to your order. Would you like to return to menu? Select Yes to return to menu or No to exit. ").strip().lower()
                                
                                if proceed == ('y') or proceed == ('yes'):
                                    
                                    break

                                elif proceed == 'no' or proceed == 'n':

                                    quit()                            
                            
                                else:

                                    raise ValueError("You've entered an invalid entry. Please select Yes or No. Press [Enter] to continue...")   
                                
                            except ValueError as inputError:           
                
                                print("{}".format(inputError),end=" ")
                                input("")
                                continue
                        continue
                           
                    # Once items verified on order, breaks
                    else:
                        break           
                    
                # If wrong menu selection, display error message and restart menu selection process until user makes the right selection or exits by selecting accept. 
                else:
                    
                    raise ValueError("{0:^60s}".format("\n\nERROR: You've entered an invalid menu option. Please enter a valid menu option. Press [Enter] to continue. "))
            
            break
        
        except ValueError as inputError:           
            
            print("{}".format(inputError),end=" ")
            input("")

    return customerDict


# Function:     calculateItemSubtotals
# Description:  Calculates subtotal of each individual menu item and updates customers order dictionary
# Parameters:   
#               customerDict: Stores customers subtotals 
#               menuDict: Used to get pizza prices to calculate subtotal based off quantity selected
#                 
# Return value: customerDict
#
def calculateItemSubtotals(customerDict, menuDict):

    # Fucntion optimized to use a loop to calculate each item suubtotal
    for key in customerDict["OrderDic"]:     

        # Only checks menu items in orderDic
        if key.isnumeric():
            
            # Calculates each items subtotal and adds to customers order dictionary 
            customerDict["OrderDic"][key]["price"] = float(customerDict["OrderDic"][key]["quantity"]) * float(menuDict[key]["price"])    

    return customerDict


# Function:     calculateOrderCosts
# Description:  Function that calculates subtotal, total price, discount amount, tip amount, and the actual amount of taxes and updates customer order dictionary
# Parameters:   customerDict: To retrieve customers subtotals and store totals                
# Return value: customerDict
#
def calculateOrderCosts(customerDict):
    
    # Loops through cusomters order dictionary to add up subtotal of all menu items
    for key in customerDict["OrderDic"]:
        
        if key.isnumeric():
            
            customerDict["OrderDic"]["subtotal"] += customerDict["OrderDic"][key]["price"] 
       
    # If student updates subtotal and discount amounts
    if customerDict["Student:"] == True:
        
        customerDict["OrderDic"]["discountAmount"] = customerDict["OrderDic"]["subtotal"] - (customerDict["OrderDic"]["subtotal"] * getConstant("studentDiscount"))
        customerDict["OrderDic"]["subtotal"] = customerDict["OrderDic"]["subtotal"] * getConstant("studentDiscount")
        
    # Calculate costs based off delivery status
    if customerDict["Delivery:"] == True:
        
        customerDict["OrderDic"]["tipAmount"] = (int(customerDict["OrderDic"]["tip"])/100) * customerDict["OrderDic"]["subtotal"]
    
        # Calculates totals, adds $5 delivery fee if order is less than $30
        if customerDict["OrderDic"]["subtotal"] < 30:
            
            customerDict["OrderDic"]["totalAmount"] = (customerDict["OrderDic"]["subtotal"] * getConstant("tax")) + customerDict["OrderDic"]["tipAmount"] + getConstant("deliveryFee")
            customerDict["OrderDic"]["hstAmount"] = customerDict["OrderDic"]["totalAmount"] - customerDict["OrderDic"]["subtotal"] - customerDict["OrderDic"]["tipAmount"] - getConstant("deliveryFee")
            customerDict["OrderDic"]["subtotal"] = customerDict["OrderDic"]["subtotal"] + getConstant("deliveryFee")

        else:
            
            customerDict["OrderDic"]["totalAmount"] = (customerDict["OrderDic"]["subtotal"] * getConstant("tax")) + customerDict["OrderDic"]["tipAmount"]
            customerDict["OrderDic"]["hstAmount"] = customerDict["OrderDic"]["totalAmount"] - customerDict["OrderDic"]["subtotal"] - customerDict["OrderDic"]["tipAmount"]
    else:

        customerDict["OrderDic"]["totalAmount"] = (customerDict["OrderDic"]["subtotal"] * getConstant("tax"))
        customerDict["OrderDic"]["hstAmount"] = customerDict["OrderDic"]["totalAmount"] - customerDict["OrderDic"]["subtotal"]  
    
    return customerDict


# Function:     saveReciept
# Description:  Function saves the order reciept to a .txt file
# Parameters:   
#               menuDict: Used for printing items and individual pricing 
#               customerDict: Used for retrieving customer information and order information 
#               recieptFileName: Contains filename to create file with                
# Return value: none
#
def saveReciept(menuDict, customerDict, recieptFileName):    
    
    reciept = open(recieptFileName, 'w')

    # reciept.writes company information
    reciept.write("{0:_^58s}\n".format(""))
    reciept.write("\n")
    reciept.write("{0:^58s}\n".format(menuDict["companyName"]))
    reciept.write("{0:_^58s}\n".format(""))
    reciept.write("\n")
    
    # reciept.writes customer information
    reciept.write("{0:^58s}\n".format("Customer Information"))
    reciept.write("\n")
    
    # reciept.writes Delivery or Pick-up order
    if customerDict["Delivery:"] == True:

        reciept.write("Order Type: {0}\n".format("Delivery"))

    else:

        reciept.write("Order Type: {0}\n".format("Pick-up"))
    
    # reciept.writes customer name on one line
    reciept.write("Name: {0} {1}\n".format(customerDict["First Name:"].capitalize(), customerDict["Last Name:"].capitalize()))
    reciept.write("Phone Number: {0}\n".format(customerDict["Phone Number:"]))
    
    if customerDict["Delivery:"] == True:

    # Checks if there is a unit # and adjusts the reciept.writeout accordingly, reciept.writes all on one line.  
        if customerDict["Unit Number:"] == (''):

            reciept.write("Address: {0} {1}\n".format(customerDict["Street Number:"], customerDict["Street Name:"].title()))

        else:

            reciept.write("Address: {0} {1}, Unit: {2}\n".format(customerDict["Street Number:"], customerDict["Street Name:"].title(), customerDict["Unit Number:"]))
            
        # reciept.writes rest of address information 
        reciept.write("{3:9}{0} {1}, {2}\n".format(customerDict["City:"].capitalize(), customerDict["Province:"].upper(), customerDict["Postal Code:"].upper(), ""))
        reciept.write("Delivery Instructions: \n{0}".format(customerDict["Delivery Instructions:"].capitalize()))
    
    # reciept.writes out order details and pricing 
    reciept.write("\n{0:_^58s}\n\n".format(""))
    reciept.write("")    
    reciept.write("{0:^58s}\n".format("Order Information"))
    reciept.write("\n")
    reciept.write("{0:<30s} {1:>5s} {2:>10s} {3:>10s}\n".format('','Item','Item',''))
    reciept.write("{0:<30s} {1:>5s} {2:>10s} {3:>10s}\n".format('Order','Qty','Price','Total'))
    reciept.write("{0:_<20s} {4:8s} {1:_>6s} {5:2} {2:_>7s} {6:2} {3:_>7s}\n".format('','','','','','',''))
    
    # Based on amount of items ordered, reciept.writeout will adjust 
    # As long as there is a akey in customerDict[OrderDic], will keep looping to reciept.write all items that have a quantity greater than 0
    for key in customerDict["OrderDic"]:
        
        # Prevents looping through non food menu related items in dictionary 
        if key.isnumeric():
            if int(customerDict["OrderDic"][key]["quantity"]) > 0:
                reciept.write("{0:<30s} {1:>5s} {4:2s} ${2:>6.2f} {4:2s} ${3:>6.2f}\n".format(menuDict[key]["name"], customerDict["OrderDic"][key]["quantity"], menuDict[key]["price"],  customerDict["OrderDic"][key]["price"],'',''))
            
    reciept.write("\n")
    
    # Checks isStudent flag, if true adds student discount message and total savings, checks delivery tag, order < or > $30, adjusts and reciept.writes out subtotal, hst, tip, totals 
    if customerDict["Student:"] == True: 
        
        reciept.write("{0:<30s} {1:>14s} {3:3s} -$ {2:>5.2f}\n".format('10% Student Savings','', customerDict["OrderDic"]["discountAmount"], ''))
        
    if customerDict["Delivery:"] == True:
            
        if customerDict["OrderDic"]["subtotal"] < 30:
                
            reciept.write("{0:<30s} {1:>15s} {3:3s} $ {2:>5.2f}\n".format('Delivery Fee','', getConstant("deliveryFee"), ''))
                
        else:
                
            reciept.write("{0:<30s} {1:>15s} {3:3s} {2:>5s}\n".format('Delivery Fee','', 'Waived!', ''))

        reciept.write("Tip Amount ({0:2}%) {1:33s} $ {2:>5.2f}\n".format(customerDict["OrderDic"]["tip"],'', customerDict["OrderDic"]["tipAmount"]))    
        reciept.write("{0:38s}{1:10s}{3:2s} ${2:>6.2f}\n".format('','Sub Total', customerDict["OrderDic"]["subtotal"] + customerDict["OrderDic"]["tipAmount"], ''))

    else:    
            
        reciept.write("{0:38s}{1:10s}{3:2s} ${2:>6.2f}\n".format('','Sub Total', customerDict["OrderDic"]["subtotal"], ''))        

    reciept.write("{0:38s}{1:10s}{3:2s} ${2:>6.2f}\n".format('','Tax (13%)', customerDict["OrderDic"]["hstAmount"], ''))
    reciept.write("{0:51}{1:_>7}\n".format('',''))
    reciept.write("{0:42s}{1:6s}{3:2s} ${2:>6.2f}\n".format('','TOTAL', customerDict["OrderDic"]["totalAmount"], ''))   

    reciept.write("\n")
    reciept.write("\n")

    # reciept.writes thank you message centered
    thankYou = ('Thank you for eating at{}\n'.format(menuDict["companyName"]))
    reciept.write("{:^60s}".format(thankYou))
    reciept.write("\n")
    reciept.close()


# Function:     printReciept 
# Description:  Function prints the order reciept to screen
# Parameters:   
#               menuDict: Used for printing items and individual pricing 
#               customerDict: Used for retrieving customer information and order information 
#               recieptFileName: Contains filename to print location of .txt file              
# Return value: none
#
def printReciept(menuDict, customerDict, recieptFileName):    
    
    # Prints company information
    print("{0:_^58s}".format(""))
    print("")
    print("{0:^58s}".format(menuDict["companyName"]))
    print("{0:_^58s}".format(""))
    print("")
    
    # Prints customer information
    print("{0:^58s}".format("Customer Information"))
    print("")
    
    # Prints Delivery or Pick-up order
    if customerDict["Delivery:"] == True:

        print("Order Type: {0}".format("Delivery"))

    else:

        print("Order Type: {0}".format("Pick-up"))
    
    # Prints customer name on one line
    print("Name: {0} {1}".format(customerDict["First Name:"].capitalize(), customerDict["Last Name:"].capitalize()))
    print("Phone Number: {0}".format(customerDict["Phone Number:"]))
    
    if customerDict["Delivery:"] == True:

    # Checks if there is a unit # and adjusts the printout accordingly, prints all on one line.  
        if customerDict["Unit Number:"] == (''):

            print("Address: {0} {1}".format(customerDict["Street Number:"], customerDict["Street Name:"].title()))

        else:

            print("Address: {0} {1}, Unit: {2}".format(customerDict["Street Number:"], customerDict["Street Name:"].title(), customerDict["Unit Number:"]))
            
        # Prints rest of address information 
        print("{3:9}{0} {1}, {2}".format(customerDict["City:"].capitalize(), customerDict["Province:"].upper(), customerDict["Postal Code:"].upper(), ""))
        print("Delivery Instructions: \n{0}".format(customerDict["Delivery Instructions:"].capitalize()))
    
    # Prints out order details and pricing 
    print("{0:_^58s}".format(""))
    print("")    
    print("{0:^58s}".format("Order Information"))
    print("")
    print("{0:<30s} {1:>5s} {2:>10s} {3:>10s}".format('','Item','Item',''))
    print("{0:<30s} {1:>5s} {2:>10s} {3:>10s}".format('Order','Qty','Price','Total'))
    print("{0:_<20s} {4:8s} {1:_>6s} {5:2} {2:_>7s} {6:2} {3:_>7s}".format('','','','','','',''))
    
    # Based on amount of items ordered, printout will adjust 
    # As long as there is a akey in customerDict[OrderDic], will keep looping to print all items that have a quantity greater than 0
    for key in customerDict["OrderDic"]:
        
        # Prevents looping through non food menu related items in dictionary 
        if key.isnumeric():
            if int(customerDict["OrderDic"][key]["quantity"]) > 0:
                print("{0:<30s} {1:>5s} {4:2s} ${2:>6.2f} {4:2s} ${3:>6.2f}".format(menuDict[key]["name"], customerDict["OrderDic"][key]["quantity"], menuDict[key]["price"],  customerDict["OrderDic"][key]["price"],'',''))
            
    print("")
    
    # Checks isStudent flag, if true adds student discount message and total savings, checks delivery tag, order < or > $30, adjusts and prints out subtotal, hst, tip, totals 
    if customerDict["Student:"] == True: 
        
        print("{0:<30s} {1:>14s} {3:3s} -$ {2:>5.2f}".format('10% Student Savings','', customerDict["OrderDic"]["discountAmount"], ''))
    
    if customerDict["Delivery:"] == True:
        
        if customerDict["OrderDic"]["subtotal"] < 30:
            
            print("{0:<30s} {1:>15s} {3:3s} $ {2:>5.2f}".format('Delivery Fee','', getConstant("deliveryFee"), ''))
            
        else:
            
            print("{0:<30s} {1:>15s} {3:3s} {2:>5s}".format('Delivery Fee','', 'Waived!', ''))

        print("Tip Amount ({0:2}%) {1:33s} $ {2:>5.2f}".format(customerDict["OrderDic"]["tip"],'', customerDict["OrderDic"]["tipAmount"]))    
        print("{0:38s}{1:10s}{3:2s} ${2:>6.2f}".format('','Sub Total', customerDict["OrderDic"]["subtotal"] + customerDict["OrderDic"]["tipAmount"], ''))

    else:    
        
        print("{0:38s}{1:10s}{3:2s} ${2:>6.2f}".format('','Sub Total', customerDict["OrderDic"]["subtotal"], ''))        
    
    
    print("{0:38s}{1:10s}{3:2s} ${2:>6.2f}".format('','Tax (13%)', customerDict["OrderDic"]["hstAmount"], ''))
    print("{0:51}{1:_>7}".format('',''))
    print("{0:42s}{1:6s}{3:2s} ${2:>6.2f}".format('','TOTAL', customerDict["OrderDic"]["totalAmount"], ''))

    print("")
    print("")

    # Prints thank you message centered
    thankYou = ('Thank you for eating at{}'.format(menuDict["companyName"]))
    print("{:^60s}".format(thankYou))
    print("")
    print("\nA confirmation reciept has been saved to: {}".format(os.path.join(os.getcwd(), recieptFileName)))
    print("")

''' 
This is the programs main flow control! 

'''

# Prints welcome banner
welcomeBanner(menuDict)

# Prints welcome message and what to do 
welcomeMessage(menuDict)

# Collects all customer information and returns updated customer dictionary
collectCustomerDetails(customerDict)

# Collects all customer order information and returns updated customer dictionary
runOrderMenu(customerDict, menuDict)

# Calculates all item subtotals before calculating total order cost and updates customer dictionary
calculateItemSubtotals(customerDict, menuDict)

# Calculates all order costs and updates customer dictionary
calculateOrderCosts(customerDict)

# Saves reiept to file. 
saveReciept(menuDict, customerDict, recieptFileName)

# Prints reciept using all the order details stored in customer dictionary 
printReciept(menuDict, customerDict, recieptFileName)


