class laptops:
    shop_name="laptop world"
    def __init__(self,name,RAM):
        self.name=name
        self.RAM=RAM

laptop=[
    laptops("lenovo",40000),
    laptops("hp",350000),
    laptops("dell",45000),
    laptops("asus",60000)
]

for laptops in laptop:
    print(laptops.name,laptops.RAM,laptops.shop_name)