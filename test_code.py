import user_prompt

# a test of searching for mens shoes that are red and are apart of the lebron shoeline that are size 12 
assert (user_prompt.User_Request('men','lebron',200,'red','',12))

# a test of womens running shoes that cost below 150 that are black 
assert (user_prompt.User_Request('women','',150,'black','running',9))

# a test of any mens show that is below $50
assert (user_prompt.User_Request('men','',50,'','',10.5))

# test of the zoom shoe line that is below $125 that are size 13, blue, and meant for running
assert (user_prompt.User_Request('men','zoom',125,'blue','running',13))

# a test that seraches for the same result above but below the price range for any of the matched shows 
assert (user_prompt.User_Request('men','zom',50,'blue','running',13))

# a test of womens running shoes that cost below 150 that are black 
assert (user_prompt.User_Request('women','',150,'black','running',9))

# a test where the user can input thier own show reccomendation 
user_ask = user_prompt.Ask_User()
first_request = user_prompt.User_Request(user_ask.user_gender,user_ask.user_shoe_name, user_ask.user_price,user_ask.user_color,user_ask.user_type,user_ask.user_size)

