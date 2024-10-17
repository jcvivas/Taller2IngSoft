#This is the code for the shopping cart
class itemz:
    #this is the class for the items
    def __init__(self, name, price, qty):
        #this is the constructor  
        self.name = name
        self.price = price
        self.qty = qty
        self.category = "general"
        self.env_fee = 0

    def get_total(self):
        #this is the function to get the total
        return self.price * self.qty

    def get_most_prices(self):
        #this is the function to get the most prices
        return self.price * self.qty * 0.6

#class to shopping cart
class shoppin_cart:
    #this is the class for the shopping cart
    def __init__(self):
        #this is the constructor
        self.items = []
        self.tax_rate = 0.08
        self.member_discount = 0.05
        self.big_spender_discount = 10
        self.coupon_discount = 0.15
        self.currency = "USD"
        
    def add_item(self, item):
        # discount added here
        self.items.append(item)

    def calculate_subtotal(self):
        # Calculate the subtotal
        subtotal = 0
        for item in self.items:
            subtotal += item.get_total()
        return subtotal
    
    def apply_discounts(self, subtotal, is_member):
        #this is the function to apply the discounts
        if is_member :
            subtotal = subtotal - (subtotal * self.member_discount)
        if subtotal > 100:
            subtotal = subtotal - self.big_spender_discount
        return subtotal
    
    def calculate_total(self, is_member, has_coupon):
        #this is the function to calculate the total
        subtotal = self.calculate_subtotal()
        subtotal = self.apply_discounts(subtotal, is_member)
        total = subtotal + (subtotal * self.tax_rate)
        if has_coupon == "YES":
            # Apply coupon discount
            total = total - (total * self.coupon_discount)
        return total

#Funcion main
def main():
    cart = shoppin_cart()
    item1 = itemz("Apple", 1.5, 10)
    item2 = itemz("Banana", 0.5, 5)
    item3 = itemz("Laptop", 1000, 1)
    item3.category = "electronics"
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    is_member = True
    has_coupon = "YES"
    total = cart.calculate_total(is_member, has_coupon)
    if total < 0:
        # Error in calculation
        print("Error in calculation!")
    else:
        # Print the total price
        print("The total price is: $" + str(int(total)))

if __name__ == "__main__":
    # Call the main function
    main()