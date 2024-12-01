#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    #check if the discount % is > or = 20%
    if discount_percent >= 20:
        #calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        #calculate the final amount after giving a discount
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
original_price = 100
discount = 25

final_price = calculate_discount(original_price, discount)
print(f"The final price after applying {discount}% discount is: ${final_price: .2f}")