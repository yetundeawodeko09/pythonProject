class MercySupermarket:
    def __init__(self, priceofitems, quantityofitems):
        print('You are welcome to MercySupermarket')
        
        self.quantityofitems = {'sugar':131, 'bread sliced':311, 'bread unsliced':229, 'egg':545, 'three crowns tin':201, 'peak milk tin' :230, 'peak milk satchet': 791, 'bournvita satchet':611, 'milo tin':367, 'peak milk large satchet': 889, 'milo large satchet':934, 'bournvita large satchet':758, 'custard small satchet':383, 'cornflakes small satchet':647, 'golden morn small satchet':121, 'detergent samll wawu':198, 'detergent small aerial':354, 'detergent big wawu':323, 'detergent big aerial':222, 'corn flakes big satchet': 341, 'golden morm large satchet':458, 'sprite small':134, 'pepsi small':674, 'fanta small':757, 'lacasera small': 127, 'sprite big':956, 'pepsi big':374, 'fanta big':267, 'lacasera big':786, 'coke big':546}
        self.priceofitems = {'sugar':50, 'bread sliced':200, 'bread unsliced':150, 'egg':50, 'three crowns tin':150, 'peak milk tin' :120, 'peak milk satchet': 50, 'bournvita satchet':50, 'milo tin':500, 'peak milk large satchet': 700, 'milo large satchet':700, 'bournvita large satchet':100, 'custard small satchet':200, 'cornflakes small satchet':150, 'golden morn small satchet':100, 'detergent samll wawu':120, 'detergent small aerial':115, 'detergent big wawu':200, 'detergent big aerial':250, 'corn flakes big satchet': 750, 'golden morm large satchet':650, 'sprite small':80, 'pepsi small':80, 'fanta small':80, 'lacasera small':80, 'sprite big':150, 'pepsi big':150, 'fanta big':150, 'lacasera big':150, 'coke big':150}

        print('These are the items available at MercySupermarket and their unit price in Naira', self.priceofitems)


        return

    def Askitems(self):
        items = (str(input('What do you want to buy:')))
        return items

    def Askquantity(self):
        quantity = (int(input('What quantity do you want:')))
        return quantity
class Detailsofitems:
    def __init__(self, Askitems, Askquantity):
        Askitems.__init__(self)
        Askquantity.__init__(self)
        print('Your requisition is being processed')
        
        return
    def Total(self):
        #using 4 quantities of bread(sliced) as an example
        Totalpayment = 200 * 4
        print ('Your total payment (NGN) =', Totalpayment)
        return 
    def Receipt(self):
       
        print('MercySupermarket INVOICE')
        print('items purchased: bread sliced')
        print('quantity purchased: 4')
        print('Price per unit (NGN): 200')
        print('Total Payment(NGN):800') 
    def appreciation(self):
        Discount = 10
        print('Sorry we do not offer discount for pruchase less than', Discount, 'items')
       
        print('Thank you for shopping with us')
        return
    

Myshopping = MercySupermarket('priceofitems', 'quantityofitems')
Myshopping.Askitems()
Myshopping.Askquantity()
Myshoppinglist = Detailsofitems('Askitems', 'Askquantity')
Myshoppinglist.Total()
Myshoppinglist.Receipt()
Myshoppinglist.appreciation()
