import scheme 
from model import IntClass ,FloatClass, BlobClass,CharClass, VarCharClass, PrimaryKey
import dummy
import sys
import MySQLdb

conn = MySQLdb.connect (host = "your host", user = "user name",  passwd = "password", db = "database name") 
cursor = conn.cursor ()

def get_member_classes():
    """Returns a list of classes defined by the user"""	
    return [(item , getattr(scheme, item)) for item in dir(scheme) if item not in dir(dummy)]

def get_class_attributes(cls):
    """Gets the attributes of the class"""
    import inspect 
    boring = dir(type('dummy', (object,), {}))
    return [item for item in inspect.getmembers(cls) if item[0] not in boring]

def make_tables():
    """This function picks the classes the user has defined and from them make table(s) structure"""
    members =  get_member_classes()
    member_dict = dict()
    acc_class = []
    for member  , item  in members:
        acc_class.append(item)
	member_dict[item] = member
    acc_class = tuple(acc_class)
    table_dict = dict()
    for item in members:
        table_name = item[0]
        class_name = item[1]
        temp_str = " "
        data_dict = dict()
        primary_key = False 
        for variable, val in get_class_attributes(class_name):
	    if isinstance(val, IntClass):
	        data_dict[variable] =  variable + " " + val.joo + ", "
	        if val.key:
		    primary_key = True	   
	    if isinstance(val, FloatClass):
	        data_dict[variable] =  variable + " " + val.joo + ", "
	        if val.key:
		    primary_key = True
	    if isinstance(val, BlobClass):
	        data_dict[variable] = variable + " "+ val.joo + ", "
	        if val.key:
		    primary_key = True
	    if isinstance(val, CharClass):
	        data_dict[variable] =  variable + " " + val.joo + ", "
	        if val.key:
		    primary_key = True
	    if isinstance(val, VarCharClass):
	        data_dict[variable] =  variable + " " + val.joo + ", "
	        if val.key:
		    primary_key = True
	    for memberClass in acc_class:
	        if isinstance(val, memberClass):
		    name = member_dict[memberClass]
		    data_dict[variable]  = [val.name, name]
        if primary_key is False:
	    primary_key_val =   PrimaryKey().joo
            primary_key_name = table_name + "_id"
	    primary_key_val = primary_key_name + " " + primary_key_val + ", "
            data_dict[primary_key_name] = primary_key_val	
	    primary_key = True
        table_dict[table_name] = dict(data_dict)
    print table_dict
    table_list = list()
    for key, val in table_dict.items():
        temp_str = ""
        for akey, aval in val.items():
            if isinstance(aval, list):
		foreign =  table_dict[aval[1]][aval[0]]
		foreign =  foreign.replace(aval[0], akey).replace("primary", "").replace("autocrement", "").strip(", ")
		table_atr = foreign + "" + " references " + aval[1] + "(" + aval[0] + ")"
		temp_str = temp_str + table_atr
	        
	    else:
	        if "primary" in aval.split():
		    temp_str = aval + temp_str
	        else:
		    temp_str = temp_str + " " + aval
	table = "CREATE TABLE %s ( " % key
        temp_str =  table + temp_str.strip(", ") + ")"
        table_list.append(temp_str)
    return table_list

if __name__ == "__main__":
    try:
	    
        for item in make_tables():
	    cursor.execute(item) 
    except MySQLdb.OperationalError, e:
	print "Error ", e[0]
	print "Error ", e[1]
	sys.exit(2)
    else:
	cursor.close()
