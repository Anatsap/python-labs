class WaterPump:

    def __init__(self, power_consumption: int = 0, brand: str = "", volume_ph: int = 0, price: float = 0.0, name: str = ""):
        self.__power_consumption = power_consumption 
        self.__brand = brand
        self.__volume_ph = volume_ph
        self.price = price
        self.name = name


    
    def get_power_consumption(self)-> int :
        return self.__power_consumption
    def get_brand(self)-> str :
        return self.__brand
    def get_volume_ph(self)-> int :
        return self.__volume_ph



    def __str__(self)-> str :
        return f"Power consumption = {self.__power_consumption},Brand = {self.__brand}, Volume per hour = {self.__volume_ph}, Price = {self.price}, Name = {self.name}"

    def __repr__(self)-> str :
        return f"WaterPump(power_consumption='{self.__power_consumption}', brand='{self.__brand}', volume_ph='{self.__volume_ph}', price='{self.price}', name='{self.name}')"


    def __del__ (self):
        print("WaterPump destroyed")


def main():
    waterpump_default = WaterPump()
    waterpump_ultra = WaterPump(480, "Amio", 80, 3000.0, "Water pump superultra")
    waterpump_samsung = WaterPump(500, "Samsung", 100, 4500.0, "Water pump FE23")
    waterpumps = [waterpump_default, waterpump_ultra, waterpump_samsung]
    for waterpump in waterpumps:
        print(waterpumps)
    

if __name__ == "__main__":
    main()
    
    



