class Selling_shoes :
    def __init__(self , name , lastname , Shoe_type ,id, color , size , price ):
        self.__name = name 
        self.__lastname = lastname 
        self.__Shoe_type = Shoe_type 
        self.__id = id 
        self.__color = color 
        self.__size = size 
        self.__price = price 


    def get_full_name(self) :
        return "%s %s" %(self.__name , self.__lastname)
    def get_price(self):
        return self.__price
    def set_price(self , price):
        self.__price = price
    def del_color(self):
        #del self.__color
        self.__color = None
    def get_size(self):
        return self.__size
    def get_color(self):
        return self.__color
Customer1 =Selling_shoes("mahdi" , "fakoorvand" , "man" ,55856 , "black" , 41 , 20000 )

print(Customer1.get_full_name())
Customer1.set_price(80000)
print(Customer1.get_price())
print(Customer1.get_size())
Customer1.del_color()
print(Customer1.get_color())
