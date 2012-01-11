class thebase:
    """Base class to the user defined classes """
    def __init__(self,  name):
          self.name = name
	  

class IntClass:
    """Int type """
    def __init__(self,key= None, status = 0):
        self.joo = "int"
	self.key = key
	if key:
	    self.joo = self.joo + " primary key  not null"
	elif status:
	    self.joo = self.joo + " not null"
		
		
class FloatClass:
    def __init__(self, status = None):
	"""Float type """
	self.joo = "float"
	if status :
	    self.joo = self.joo + " not null"
		
class BlobClass:
    """Blob type """
    def __init__(self, key=None):
	pass
		
class CharClass:
    """Char type """
    def __init__(self, limit=40, key=None, status = None):
	self.limit = limit
	self.joo = "char(%d) " % self.limit
	self.key = key
	if key:
	    self.joo = self.joo + " primary key  not null"
	if status :
	    self.joo = self.joo + " not null"
	

class VarCharClass:
    """VarChar type """
    def __init__(self, key=None, status = None):
	self.joo = "varchar(80)"
	self.key = key
	if key:
	    self.joo = self.joo + " primary key "
	if status :
	    self.joo = self.joo + " not null"

		
class PrimaryKey:
	def __init__(self):
		self.joo =  "int unsigned  primary key auto_increment not null  "
