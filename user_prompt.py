import pandas 

class User_Request():
    """
    A class that parses through all the requirements the user puts in using the csv files.
    
    """
    def __init__(self, gender, name, price, color, shoe_type, size):
        self.gender = gender.lower() 
        self.name = name.lower()
        self.price = price
        self.color = color.lower()
        self.type = shoe_type.lower()
        self.size = size
        
        #This determines which csv will be used for the recommendation
        if self.gender == 'men' or self.gender == 'mens':
                csv_file = pandas.read_csv('shoe_dict_exported.csv')
                df = csv_file
        elif self.gender == 'woman' or self.gender == 'women' or self.gender == 'womens':
            csv_file = pandas.read_csv('women_shoe_dict_exported.csv')
            df = csv_file
        else:
            raise ValueError

    
        price_list = []
        #This creates a pirce list and iterates through everything in the shoe_price column in the csv and appends the
        #correct price to the list.
        for items in csv_file.shoe_price:
            no_dollar_items = items[1:]
            item_float = float(no_dollar_items)        
            price_list.append(item_float)  
       
        type_list = []
        #This creates a type list and iterates through everything in the shoe_type column in the csv and appends the 
        #correct type to the list
        for items in csv_file.shoe_type:
            lower_items = items.lower()
            if self.type in lower_items:
                type_list.append(lower_items)
            elif self.type == '' or self.type == ' ':
                type_list.append(lower_items)
            else: 
                type_list.append("not right type")             
                
        name_list = []
        #Creates a list of the names of the shoe and iterates through the shoe_name column the csv and appends the names 
        #to the list
        for items in csv_file.shoe_name:
            lower_items = items.lower()
            if self.name in lower_items:
                name_list.append(lower_items)
            elif self.name == '' or self.name == ' ':
                name_list.append(lower_items)
            else: 
                name_list.append("not right name")  
                
        color_list = []
        #Creates a list of the colors for the shoes and iterates through the shoe_color to convert the values of the column and add
        #them to the list
        for items in csv_file.shoe_color:
            items = items[7:]
            lower_items = items.lower()
            if self.color in lower_items:
                color_list.append(lower_items)
            elif self.color == '' or self.color == ' ':
                color_list.append(lower_items)            
            else:
                color_list.append('not right color')
                
      
        size_list = []
        #This will create the list of the sizes for the shoe and iterates through the sizes in the csv to make sure they are converted
        #correctly and added to the list
        for items in csv_file.shoe_size:
            if len(items) > 7:
                    items = items[2:4]
            item_float = float(items)        
            size_list.append(item_float)  
    
    
        df['shoe_type'] = type_list
        df['shoe_name'] = name_list
        df['shoe_color'] = color_list
        df['shoe_price'] = price_list
        df['shoe_size'] = size_list
        df.drop(df[df['shoe_name'] == 'not right name'].index, inplace = True) 
        df.drop(df[df['shoe_type'] == 'not right type'].index, inplace = True) 
        df.drop(df[df['shoe_color'] == 'not right color'].index, inplace = True)       
        df.drop(df[df['shoe_price'] > self.price].index, inplace = True)
        df.drop(df[df['shoe_size'] != self.size].index, inplace = True)       
        df.sort_values(by = ['shoe_price'],inplace = True,  ascending = True)    
        if df.empty == True:
            print("Sorry there are no shoes that match your search conditions. ")
        else:
            print(df.to_string(index = False))
    #Everything above is sorting through the lists we created to clean up the dataframe we will print for the user
    
class Ask_User():
    """
    This class provides the user questions that will form the recommendation we give them for shoes to buy.
    """
    def __init__(self):
        self.user_gender = input("What gender of shoe do want? ")
        self.user_shoe_name = input("What shoe type or shoeline are you looking for? ")
        self.user_price = float(input("What is your price max? "))
        self.user_color = input("What color scheme are you looking for? ")
        self.user_type = input("What type of shoe are you looking for? ")
        self.user_size = float(input("What shoe size are you looking for? "))
        
        
