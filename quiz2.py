#define the calculate_discount function
def calculate_discount(price, discount_percent):
    #check if the discount percentage is 20% or hugher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
def main():
    try:
        original_price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    #calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    #print the final price or the original price
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else: 
        print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
        
if __name__ == "__main__":
    main()