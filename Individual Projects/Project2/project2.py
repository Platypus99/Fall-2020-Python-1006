# Perry Flamer
# Take-home project 2

def read_markets(filename):
    
    """
    Read in the farmers market data from the file named filename and return 
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    """


    zip_to_list_farmers_market = {}
    towns_to_zip_code = {}
    seen_zip = set()
    seen_town = set()
        
    f = open(filename, 'r')
    for line in f:  # actor_to_movie_set= {}
  
         line = line.strip()
         fields = line.split("#")
         zipc = fields[4]
         if not zipc.isdigit():
             continue
                 
         li = fields[0:5]
         tupled_list = tuple(li)
         town = fields[3]
         
         

         if zipc in seen_zip:
             testing1 = zip_to_list_farmers_market[zipc]
             testing2 = testing1.append(tupled_list)
             updated_list = testing1
             zip_to_list_farmers_market[zipc] = updated_list
         else:
             zip_to_list_farmers_market[zipc] = [tupled_list]
             seen_zip.add(zipc)
             
             
             # towns_to_zip_code
         if town in seen_town:
             testing4 = towns_to_zip_code[town]
             testing5 = testing4.add(zipc)
             updated_list4 = testing4
             towns_to_zip_code[town] = updated_list4
         else:
             towns_to_zip_code[town] = {zipc}
             seen_town.add(town)             
                 
                 

    return zip_to_list_farmers_market, towns_to_zip_code
       

def print_market(market):
    (state, market_name, street_address, city, zip_code) = market
        
    human_readable_string = market_name + "\n" + street_address + "\n" + city + ", " + state + " " + zip_code
        
    return human_readable_string
    
    """
    Returns a human-readable string representing the farmers market tuple
    passed to the market parameter.
    Example:
    Columbia University Greenmarket
    E. Side of Broadway between 114th & 115th Streets
    New York, New York 10027
    """
    # return "" # replace this line

if __name__ == "__main__":
    
    
    
    # This main program first reads in the markets.txt once (using the function
    # from part (a)), and then asks the user repeatedly to enter a zip code or
    # a town name (in a while loop until the user types "quit").

    FILENAME = "markets.txt"

    try: 
        zip_to_market, town_to_zips = read_markets(FILENAME)
  
        # your main loop should be here
        g = (input("Please enter a zip code or a town name: "))   
        if not g =='quit':
            while not g =='quit':
               # if a zip code is entered
                if g.isdigit():
                    if g in zip_to_market.keys():
                        market_tuple_list = zip_to_market[g]
                        for x in market_tuple_list:
                            readable_string =  print_market(x)
                            print(readable_string, "\n")
                        # print("hits if statement")
                    else:
                        print("Not Found")   
                else:
                    # print("hits else statement")
                    if g in town_to_zips.keys():
                        zip_codes_in_town = town_to_zips[g]
                        # print(zip_codes_in_town)
                        # print("Input is: ", g)
                        for a in zip_codes_in_town:
                            if  a.isdigit():  
                                market_tuple_list = zip_to_market[a]
                                for x in market_tuple_list:
                                    readable_string =  print_market(x)
                                    print(readable_string, "\n")
                    else:
                        print("Not Found")
                            

                g = (input("Please enter a zip code or a town name: "))



    except (FileNotFoundError, IOError): 
        print("Error reading {}".format(FILENAME))
