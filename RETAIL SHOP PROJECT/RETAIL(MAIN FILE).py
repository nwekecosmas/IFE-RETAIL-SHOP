import csv	# imports csv, give the file a variable name
from time import *   ## imports time module

 									
filename = "DATA.csv"
with open(filename, "r+") as fileobject:     
	lines = csv.reader(fileobject)			#opens the file in a read and write mode
	items = []
	for line in lines:						#iterates through the file and append each item in a new list called items
		line[0] = line[0].lower()
		items.append(line)


def change_price(items, item_name, new_item_price): #defining the change price function for admin
	for item in items:
		if item[0] == item_name:
			item[2] = new_item_price
			print("\n UPDATED PRICE")
			print("\n",item)
			
def update_quantities(items, item_name, item_quantity): # used by admin to manually update quantity of commodity
	for item in items:
		if item[0] == item_name:
			item[1] = item_quantity
			print("\n UPDATED QUANTITY")
			print("\n",item)
			
	
def update_stock(items, item_name, item_quantity): #defining the update stock function automatically updates quantity of items available after user purchase
	for item in items:
		if item[0] == item_name:
			item[1] = int(item[1]) - item_quantity 
	          
		
def add_items(items, item_name, item_quantity, new_item_price): # defining the add new goods to the store by admin
	new_list = []
	new_list.append(item_name)
	new_list.append(item_quantity)
	new_list.append(new_item_price)
	items.append(new_list)



def computation(items, item_name,item_quantity):#defining the computation function
	global total  # makes the variable total a global variable
	global basket   # makes the variable basket a global variable
	if item[0] == item_name:	#checks if first item name in the list is the same with inputed item name
		if item_name not in basket:		#first check if inputed item name is not in the basket
			basket.append(item_name)					# adds inputed name to a list of our collection of items we ordered or bought 
		
		cost_price = item_quantity * int(item[2])						# total costprice for a certain quantity of an item
		
		if counter <= 5:	# counter regulates how many times the user order for new items
			VAT = 20/100 * int(item[2]) * item_quantity    # VAT CALCULATIONS
			VAT_total = VAT + cost_price 
			total += VAT_total   #WE NEEDED TO CONTINUE TO ADD VAT TOTALs from several user transactions
			
			basket.append(str(item_quantity))	# adds inputed quantity to a list of our collection of items we ordered or bought 
			basket.append(str(VAT_total))   #  adds total cost of the item quantity ordered to a list of our collection of items we ordered or bought 
			cart.append(basket)				# it appends the entire list of the item details into another list called CART
			basket = []						# it clears the basket for another round of purchase
		elif counter > 5 and counter < 10:			#checks if user purchase of different items is greater than 5 and less than 10
			VAT = 30/100 * int(item[2]) * item_quantity		# VAT CALCULATIONS
			VAT_total = VAT + cost_price 
			total += VAT_total
			
			basket.append(str(item_quantity))
			basket.append(str(VAT_total))
			cart.append(basket)
			basket = []
		elif counter > 10:#checks if user purchase of different items is greater than 10 , and gives the user a discount of N800 For each new item demanded
			VAT = 30/100 * int(item[2]) * item_quantity
			VAT_total = VAT + cost_price 
			total += VAT_total
			total = total - 800
			basket.append(str(item_quantity))
			basket.append(str(VAT_total))
			cart.append(basket)
			basket = []
	
def justify(string, space_length):
	while len(string) < space_length:
		string += " "
	return string
		
				
def Admin_items_table(items):
	index = 1
	print()
	print('=*'*50)
	print("\t\tHELLO MR NWEKE COSMAS UCHENNA(SONOVGAD)- CEO OF THIS RETAIL SHOP")
	print("\t\t LIST OF AVAILABLE STOCK, QUANTITY AND PRICE FOR ADMINS ")
	print('=*'*50)
	print(justify("ID",3),justify("ITEM",30),justify("QUANTITY",15),justify("PRICE",2))
	for item in items:
		print(justify(str(index),3), justify(item[0],30), justify(item[1],15), justify(item[2],2))
		index +=1
	print('=*'*50)

def User_items_table(items):
	index = 1
	print()
	print('=*'*50)
	print("\t\t LIST OF AVAILABLE ITEMS, QUANTITY AND PRICE FOR USERS ")
	print('=*'*50)
	print(justify("ID",3),justify("ITEM",30),justify("QUANTITY",15),justify("PRICE",2))
	for item in items:
		print(justify(str(index),3),justify(item[0],30), justify(item[1],15), justify(item[2],2))
		index +=1
	print('=*'*50)		


def Sales_record():
	global cart
	index = 1
	print('\n','=*'*50)
	print('=*'*50)
	print("\t\tSONOVGAD PROVISION RETAIL STORE SALES RECORD",ctime(time())) #PRINTS TIME AND OTHER STATEMENT                                                                                                                                                              

	print('\n',justify("ID",3), justify("ITEM",30), justify("QUANTITY",15), justify("(N)PRICE PER EACH",2))
	for item in cart:
		print(justify(str(index),3), justify(item[0],30), justify(item[1],15), justify(item[2],2))
		index +=1
	print('\t\nTHIS IS THE TOTAL CASH COLLECTED FOR TODAY FOR THE SALE OF THE ABOVE LISTED ITEMS: N',total)
		
def receipt():
	index = 1
	print('\n','=*'*50)
	print('=*'*50)
	print("\t\tSONOVGAD PROVISION RETAIL STORE OFFICIAL RECEIPT",'\n\t\t\t\t\t\t\t\t',ctime(time()))
	print("\n This is a receipt of the total goods bought by you today breakdown")
	print('\n',justify("ID",3), justify("ITEM",30), justify("QUANTITY",15), justify("(N)PRICE PER EACH",2))
	for item in cart:
		print(justify(str(index),3), justify(item[0],30), justify(item[1],15), justify(item[2],2))
		index +=1
	print('\t\t\t\t\t\t\t\t\tTotal: N',total)
	print("\nTHANK YOU FOR SHOPPING WITH US")
	print('=*'*50)
	print('=*'*50)	

	
	
while True:
	print("\n choose access: \n 1.Admin \n 2.User \n 3. Exit")
	try: 						# it prevents error message display incase the user inputs alphabet
		choice = int(input("your number-1,2 or 3 choice? : "))
		if choice == 1:
			print("\n\tADMIN MENU \n1.Display Name \n2.Set Item price\n3.Update Quantities\n4.Add New Item\n5.View Sales Record\n6.Return")
			try:			#it prevents error message display incase the user inputs alphabet
				choice = int(input("your number-1,2,3,4,5 or 6 choice? : "))
				if choice == 1:
					Admin_items_table(items)
				
				elif choice == 2:
						item_name = input("\nenter the goods name: ").lower()
						for item in items:
							if item_name == item[0]:
								new_item_price = input("enter new price: ")
								change_price(items, item_name, new_item_price)
							else:
								pass
					
				
				elif choice == 3:
					item_name = input("\nenter the goods name: ").lower()
					for item in items:
						if item_name == item[0]:
							item_quantity = input("enter the quantity: ")
							update_quantities(items, item_name, item_quantity)
						else:
							pass
					
				elif choice == 4:
					item_name = input("\nenter the goods name: ").lower()
					item_quantity = input("enter the quantity: ")
					new_item_price = input("enter new price: ")
					add_items(items, item_name, item_quantity, new_item_price)
					
				elif choice == 5:
					counter, basket , total, item_name ,cart ,TOTAL = 0, [] , 0 , "" ,[],0# defining variables to regulate user trading actions
					Sales_record()
					
					
				elif choice == 6:
					pass
					
				else:
					print("\n The number is Invalid- kindly enter 1, 2, 3, 4, 5, or 6")
					
			except ValueError:
					print('\n Please enter a non alphabet')
	
		elif int(choice) == 2:
			print("\n\tUSER MENU \n1.Display\n2.Buy Items\n3.Return") #shows users menu

			choice = int(input("your number choice? : "))		#user selects next operation
			if choice == 1:
				User_items_table(items)			
		
			elif choice == 2:
				counter, basket , total, item_name ,cart ,TOTAL = 0, [] , 0 , "" ,[],0# defining variables to regulate user trading actions
				while True:
						item_name = input("\nplease enter name of goods you wana buy or 'q' to QUIT: ").lower()
						if item_name.startswith('q'): #IT QUITS THE TRADE IF THE USER DECIDES NOT TO CONTINUE WITH THE PURCHASE
							receipt()    # IT PRINTS OUT A RECEIPT 
							break
						
						for item in items:   # we iterate the items and its details(quantity and price) one after the other, if the item name Does not start with Q
							if item_name in item:  #WE CHECK IF THE ITEM NAME IS IN EACH ITERATION 
								item_quantity = int(input("please enter the quantity you need: or 'Q' to quit: "))
				
								if item_quantity <= int(item[1]):# IF THE INPUT QUANTITY IS LESS THAN OR EQUAL TO AVAILABLE STOCK
									if item_name not in basket:	# CHECKS IF THE INPUT NAME IS NOT IN BASKET, THEN COUNTER INCREASE BY 1 
										counter += 1
									
									computation(items, item_name,item_quantity)   # Computes the customer costs
									update_stock(items, item_name, item_quantity)		#	updates the available stock
								else:
									print(item[0], 'is out of stock or you need to input a lesser quantity')					
									
			elif choice == 3:
				pass
				
			else:
				print('the number you entered is invalid- kindly enter 1, 2, or 3')
								
			
		elif choice == 3:#it quits the program
			print("\nGOODBYE!!! THANK YOU FOR VISITING US")
			break
			
		else:
			print("\n Invalid Input- enter 1, 2 or 3")
			
	except ValueError:    # It performs this action when the user inputs alphabet 
		print("\n SORRY!!! ENTER A NON- ALPHABET - 1,2 0R 3")
