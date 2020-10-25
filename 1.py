class Selling_shoes :
    def __init__(self , name , lastname , Shoe_type ,id, color , size , price ):
        self.name = name 
        self.lastname = lastname 
        self.Shoe_type = Shoe_type 
        self.id = id 
        self.color = color 
        self.size = size 
        self.price = price 


    def get_full_name(self) :
        return "%s %s" %(self.name , self.lastname)
    def get_price(self):
        return self.price
Customer1 =Selling_shoes("mahdi" , "fakoorvand" , "man" ,55856 , "black" , 41 , 20000 )
Customer1.size = 40

print(Customer1.get_full_name())
print(Customer1.get_price())
print(Customer1.size)
