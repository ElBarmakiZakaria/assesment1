class Invoice:
    def __init__(self) -> None:
        self.itemsPrice = {
            "Clean Code": 100,
            "Appliting UML": 300,
            "Shipping": 50
        }
        self.itemsVAT = {
            "Clean Code": 0.08,
            "Appliting UML": 0.08,
            "Shipping": 0.23
        }
        
        
    def calc(self):
        total8 =0
        VAT8 =0 
        VAT23 = 0
        total23= 0
        for i in self.itemsVAT:
            if self.itemsVAT[i] == 0.08:
                VAT8 += self.itemsPrice[i]*0.08
                total8 += self.itemsPrice[i]
            else:
                VAT23 += self.itemsPrice[i]*0.23
                total23 += self.itemsPrice[i]
                
        print("|            | Total net | Total |")
        print("|------------|-----------|-------|")
        print(f"|VAT 8%      |  {VAT8}  |   {VAT8 + total8} |")
        print(f"|VAT 23%      |  {VAT23} |   {VAT23 + total23}   |")
    

Invoice().calc()