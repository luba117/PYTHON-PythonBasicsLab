# data_types_demo.py
# Task 2: Variables, data types, operators - Compact version

import logging

logger = logging.getLogger(__name__)

class DataTypesDemo:

    
    def __init__(self):
        # Basic data types
        self.integer = 42
        self.float_num = 3.14
        self.text = "Python Lab"
        self.flag = True
        self.nothing = None
        
        # Collections
        self.numbers_list = [1, 2, 3, 4, 5]
        self.coordinates = (10, 20)  # tuple
        self.person = {"name": "Alice", "age": 30}  # dict
        self.unique_ids = {101, 102, 103}  # set
        
        logger.info("Data types initialized")
    
    def show_types(self):       
        print("\n📦 DATA TYPES:")
        for name, value in self.__dict__.items():
            if not name.startswith('_'):
                print(f"   {name}: {value} ({type(value).__name__})")
    
    def demonstrate_operators(self):       
        a, b = 15, 4
        
        print("\n🔧 OPERATORS:")
        # Arithmetic
        print(f"   {a} + {b} = {a + b}")
        print(f"   {a} - {b} = {a - b}")
        print(f"   {a} * {b} = {a * b}")
        print(f"   {a} / {b} = {a / b:.2f}")
        print(f"   {a} % {b} = {a % b}")
        print(f"   {a} ** 2 = {a ** 2}")
        
        # Comparisons
        print(f"\n   {a} > {b}? {a > b}")
        print(f"   {a} == {b}? {a == b}")
        
        # Logical
        print(f"   True and False = {True and False}")
        print(f"   True or False = {True or False}")
        
        # Membership
        print(f"   3 in list? {3 in self.numbers_list}")
        print(f"   99 in list? {99 in self.numbers_list}")
    
    def demonstrate_type_conversion(self):      
        print("\n🔄 TYPE CONVERSION:")
        num_str = "123"
        num_int = int(num_str)
        num_float = float(num_str)
        
        print(f"   String '{num_str}' → Integer {num_int} ({type(num_int).__name__})")
        print(f"   String '{num_str}' → Float {num_float} ({type(num_float).__name__})")
        print(f"   Integer 42 → String '{str(42)}'")
        print(f"   Float 3.14 → Integer {int(3.14)}")

# Simple test
if __name__ == "__main__":
    demo = DataTypesDemo()
    demo.show_types()
    demo.demonstrate_operators()
    demo.demonstrate_type_conversion()