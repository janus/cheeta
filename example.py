import model

  

class UserTable(model.thebase):
	name = model.CharClass()
	age = model.IntClass()
	place_of_birth = model.CharClass()
	
class AddressTable(model.thebase):
	user_name = UserTable("name")
	street_name = model.CharClass()
	city_name = model.CharClass()
	street_number = model.IntClass()
	state_name = model.CharClass()
	country_name = model.CharClass()
	
	
	

	
	
		    

