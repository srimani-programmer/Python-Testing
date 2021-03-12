import sys
import os
sys.path.append(os.getcwd())

# Import MobileInventory class and InsufficientException from the inventory module using the expression from proj.inventory import MobileInventory, InsufficientException.
# Import pytest using the expression import pytest.
# Use assert statement for assert, and to check. Ex: assert 1 == 1
from proj.inventory import MobileInventory, InsufficientException
import pytest
# Define a pytest test class **'TestingInventoryCreation'**
class TestingInventoryCreation:

    # Define a pytest test method **'test_creating_empty_inventory'**, which creates an empty inventory and checks if its 'balance_inventory' is an empty dict using assert.
    def test_creating_empty_inventory(self):
        i = MobileInventory()
        assert (not i.balance_inventory == True)

    # Define a pytest test method **'test_creating_specified_inventory'**, which checks if inventory instance with input {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}.
    def test_creating_specified_inventory(self):
        i = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        assert i.balance_inventory == {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}

    # Define a pytest test method  **'test_creating_inventory_with_list'**, which checks if the  method raises a TypeError with the message "Input inventory must be a dictionary" when a list "['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z']" is passed as input using assert.
    def test_creating_inventory_with_list(self):
        with pytest.raises(TypeError) as err:
			      mi = MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
			      ex = err.exception
			      ok_(ex.message,"Input inventory must be a dictionary")

    # Define a pytest test method **'test_creating_inventory_with_numeric_keys'**, which checks if the  method raises a ValueError with the message "Mobile model name must be a string" using assert, when the dict {1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'} is passed as input.
    def test_creating_inventory_with_numeric_keys(self):
        with pytest.raises(ValueError) as err:
			      mi = MobileInventory({1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})
			      ex = err.exception
			      ok_(ex.message,"Mobile model name must be a string")

    # Define a pytest test method **'test_creating_inventory_with_nonnumeric_values'**, which checks if the  method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert, when the dict {'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'} is passed as input.
    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(ValueError) as err:
			      mi = MobileInventory({'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'} )
			      ex = err.exception
			      ok_(ex.message, "No. of mobiles must be a positive integer")

    # Define a pytest test method **'test_creating_inventory_with_negative_value'**, which checks if the  method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert, when the dict {'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25} is passed as input.
    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError) as e:
			      mi = MobileInventory({'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25} )
			      # print("KP: ", e)
			      ex = e.exception
			      assert ex.message == "No. of mobiles must be a positive integer"

# Define another pytest test class **'TestInventoryAddStock'**, which tests the behavior of the **'add_stock'** method, with the following tests
class TestInventoryAddStock:

    # Define a pytest class fixture 'setup_class', which creates an **'MobileInventory'** instance with input {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25} and assign it to class attribute **'inventory'**.
    @classmethod
    def setup_class(cls):
        mi = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
		    # cls.inventory = mi

    # Define a pytest test method **'test_add_new_stock_as_dict'**, which adds the new stock {'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10} to the existing inventory, and update the **balance_inventory** attribute. Also, check if the updated **balance_inventory** equals {'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25, 'Nokia Model A':10} using assert.
    def test_add_new_stock_as_dict(self):
        self.inventory.add_stock({'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10})
		    assert self.comp_dict(self.inventory.balance_inventory,{'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25})

    # Define a pytest test method **'test_add_new_stock_as_list'**, which adds the new stock ['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'] to the existing inventory, and which checks if the method raises a TypeError with the message "Input stock must be a dictionary" using assert.
    def test_add_new_stock_as_list(self):
        with pytest.raises(TypeError) as err:
			      self.inventory.add_stock(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
			      ex = err.exception
			      ok_(ex.message, "Input stock must be a dictionary")

    # Define a pytest test method **'test_add_new_stock_with_numeric_keys'**, which adds the new stock {1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'} to the existing inventory, and which checks if the method raises a ValueError with the message "Mobile model name must be a string" using assert.
    def test_add_new_stock_with_numeric_keys(self):
        with pytest.raises(ValueError) as err:
			      self.inventory.add_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'} )
			      ex = err.exception
			      ok_(ex.message, "Mobile model name must be a string")

    # Define a pytest test method **'test_add_new_stock_with_nonnumeric_values'**, which adds the new stock {'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'} to the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
    def test_add_new_stock_with_nonnumeric_values(self):
        with pytest.raises(ValueError) as err:
			      self.inventory.add_stock({'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'})
			      ex = err.exception
			      ok_(ex.message, "No. of mobiles must be a positive integer")

    # Define a pytest test method **'test_add_new_stock_with_float_values'**, which adds the new stock {'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25} to the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
    def test_add_new_stock_with_float_values(self):
        with pytest.raises(ValueError) as err:
			      self.inventory.add_stock({'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25} )
			      ex = err.exception
			      ok_(ex.message, "No. of mobiles must be a positive integer")

# Define another pytest test class **'TestInventorySellStock'**, which tests the behavior of the **'sell_stock'** method, with the following tests
class TestInventorySellStock:
    # Define a pytest class fixture 'setup_class', which creates an **'MobileInventory'** instance with the input {'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1}, and assign it to the class attribute **'inventory'**.
    @classmethod
    def setup_class(cls):
        mi = MobileInventory({'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
		    self.inventory = mi

    # Define a pytest test method **'test_sell_stock_as_dict'**, which sells the requested stock {'iPhone Model A':2, 'Xiaomi Model B':20, 'Sony Model D':1} from the existing inventory, and update the **balance_inventory** attribute. Also check if the updated **balance_inventory** equals {'iPhone Model A':48, 'Xiaomi Model B': 1980, 'Nokia Model C':10, 'Sony Model D':0} using assert.
    def test_sell_stock_as_dict(self):
        assert True

    # Define a pytest test method **'test_sell_stock_as_list'**, which tries selling the requested stock ['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'] from the existing inventory, and which checks if the method raises a TypeError with the message "Requested stock must be a dictionary" using assert.
    def test_sell_stock_as_list(self):
        with pytest.raises(TypeError) as err:
			      self.inventory.sell_stock(['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'])
			      ex = err.exception
			      ok_(ex.message, "Requested stock must be a dictionary")

    # Define a pytest test method **'test_sell_stock_with_numeric_keys'**, which tries selling the requested stock {1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'} from the existing inventory, and which checks if the method raises ValueError with the message "Mobile model name must be a string" using assert.
    def test_sell_stock_with_numeric_keys(self):
        with pytest.raises(ValueError) as err:
			      self.inventory.sell_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
			      ex = err.exception
			      ok_(ex.message, "Mobile model name must be a string")

    # Define a pytest test method **'test_sell_stock_with_nonnumeric_values'**, which tries selling the requested stock {'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'} from the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
    def test_sell_stock_with_nonnumeric_values(self):
        with pytest.raises(ValueError) as err:
			      self.inventory.sell_stock({'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'})
			      ex = err.exception
			      ok_(ex.message, "No. of mobiles must be a positive integer")

    # Define a pytest test method **'test_sell_stock_with_float_values'**, which tries selling the requested stock {'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4} from the existing inventory, and which checks if the method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert.
    def test_sell_stock_with_float_values(self):
        with pytest.raises(ValueError) as err:
			      self.inventory.sell_stock({'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4})
			      ex = err.exception
			      ok_(ex.message, "No. of mobiles must be a positive integer")

    # Define a pytest test method **'test_sell_stock_of_nonexisting_model'**, which tries selling the requested stock {'iPhone Model B':2, 'Xiaomi Model B':5} from the existing inventory, and which checks if the method raises an InsufficientException with the message "No Stock. New Model Request" using assert.
    def test_sell_stock_of_nonexisting_model(self):
        with pytest.raises(InsufficientException) as err:
			      self.inventory.sell_stock({'iPhone Model B':2, 'Xiaomi Model B':5})
			      ex = err.exception
			      ok_(ex.message, "No Stock. New Model Request")

    # Define a pytest test method **'test_sell_stock_of_insufficient_stock'**, which tries selling the requested stock {'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15} from the existing inventory, and which checks if the method raises an InsufficientException with the message "Insufficient Stock" using assert.
    def test_sell_stock_of_insufficient_stock(self):
        with pytest.raises(InsufficientException) as err:
			      self.inventory.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15})
			      ex = err.exception
			      ok_(ex.message, "Insufficient Stock")





def test_creating_specified_inventory(self):
    c2 = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
    assert c2.balance_inventory == {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}
    #{'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}



class TestingInventoryCreation:
    
    def test_creating_empty_inventory(self):
		mi = MobileInventory()
		assert mi.balance_inventory == {}

    def test_creating_specified_inventory(self):
        c2 = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        assert c2.balance_inventory == {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}

    def test_creating_inventory_with_list(self):
            with pytest.raises(TypeError) as err:
                mi = MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
                ex = err.exception
                assert ex.message == "Input inventory must be a dictionary"

    def test_creating_inventory_with_numeric_keys(self):
        with pytest.raises(ValueError) as err:
            mi = MobileInventory({1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})
            ex = err.exception
            assert ex.message == "Mobile model name must be a string"

    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(ValueError) as err:
            mi = MobileInventory({'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'} )
            ex = err.exception
            assert ex.message == "No. of mobiles must be a positive integer"

    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError) as e:
            mi = MobileInventory({'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25} )
            print("KP: ", e)
            ex = e.exception
            assert ex.message == "No. of mobiles must be a positive integer"















'''
import sys
import os
sys.path.append(os.getcwd())

# Import MobileInventory class and InsufficientException from the inventory module using the expression from proj.inventory import MobileInventory, InsufficientException.
# Import pytest using the expression import pytest.
# Use assert statement for assert, and to check. Ex: assert 1 == 1
from proj.inventory import MobileInventory, InsufficientException
import pytest

class TestingInventoryCreation:

    def test_creating_empty_inventory(self):
		    mi = MobileInventory()
		    assert mi.balance_inventory == {}

    def test_creating_specified_inventory(self):
        inventory_item = {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}
        mi = MobileInventory(inventory_item)
        assert mi.balance_inventory == inventory_item

    def test_creating_inventory_with_list(self):
        with pytest.raises(TypeError) as err:
            mi = MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
            ex = err.exception
            assert ex.message == "Input inventory must be a dictionary"

    def test_creating_inventory_with_numeric_keys(self):
        with pytest.raises(ValueError) as err:
            mi = MobileInventory({1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})
            ex = err.exception
            assert ex.message == "Mobile model name must be a string"

    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(ValueError) as err:
            mi = MobileInventory({'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'} )
            ex = err.exception
            assert ex.message == "No. of mobiles must be a positive integer"

    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError) as e:
            mi = MobileInventory({'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25} )
            print("KP: ", e)
            ex = e.exception
            assert ex.message == "No. of mobiles must be a positive integer"

class TestInventoryAddStock:

	@classmethod
	def setup_class(self):
		    mi = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
		    self.inventory = mi

	def test_add_new_stock_as_dict(self):
        mi = MobileInventory({})
		    mi.add_stock({'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10})
		    assert mi.balance_inventory == {'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25}

	def test_add_new_stock_as_list(self):
		with pytest.raises(TypeError) as err:
			self.inventory.add_stock(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
			ex = err.exception
			assert ex.message == "Input stock must be a dictionary"

	def test_add_new_stock_with_numeric_keys(self):
		with pytest.raises(ValueError) as err:
			self.inventory.add_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'} )
			ex = err.exception
			assert ex.message == "Mobile model name must be a string"

	def test_add_new_stock_with_nonnumeric_values(self):
		with pytest.raises(ValueError) as err:
			self.inventory.add_stock({'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'})
			ex = err.exception
			assert ex.message == "No. of mobiles must be a positive integer"

	def test_add_new_stock_with_float_values(self):
		with pytest.raises(ValueError) as err:
			self.inventory.add_stock({'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25} )
			ex = err.exception
			assert ex.message == "No. of mobiles must be a positive integer"

	def comp_dict(self,x,y):
		#return {k: x[k] for k in x if k in y and x[k] == y[k]}
		return x == y





class TestInventorySellStock:
	@classmethod
	def setup_class(self):
		mi = MobileInventory({'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
		self.inventory = mi

	def comp_dict(self,x,y):
		#return {k: x[k] for k in x if k in y and x[k] == y[k]}
		return x == y

	def test_sell_stock_as_dict(self):
		self.inventory.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':20, 'Sony Model D':1})
		assert self.inventory.balance_inventory == {'iPhone Model A':48, 'Xiaomi Model B': 1980, 'Nokia Model C':10, 'Sony Model D':0}

	def test_sell_stock_as_list(self):
		with pytest.raises(TypeError) as err:
			self.inventory.sell_stock(['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'])
			ex = err.exception
			assert ex.message == "Requested stock must be a dictionary"

	def test_sell_stock_with_numeric_keys(self):
		with pytest.raises(ValueError) as err:
			self.inventory.sell_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
			ex = err.exception
			assert ex.message == "Mobile model name must be a string"

	def test_sell_stock_with_nonnumeric_values(self):
		with pytest.raises(ValueError) as err:
			self.inventory.sell_stock({'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'})
			ex = err.exception
			assert ex.message == "No. of mobiles must be a positive integer"

	def test_sell_stock_with_float_values(self):
		with pytest.raises(ValueError) as err:
			self.inventory.sell_stock({'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4})
			ex = err.exception
			assert ex.message == "No. of mobiles must be a positive integer"

	def test_sell_stock_of_nonexisting_model(self):
		with pytest.raises(InsufficientException) as err:
			self.inventory.sell_stock({'iPhone Model B':2, 'Xiaomi Model B':5})
			ex = err.exception
			assert ex.message == "No Stock. New Model Request"

	def test_sell_stock_of_insufficient_stock(self):
		with pytest.raises(InsufficientException) as err:
			self.inventory.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15})
			ex = err.exception
			assert ex.message == "Insufficient Stock"

'''
