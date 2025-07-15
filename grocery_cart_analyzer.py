items = ["milk","bread","cheese","cereal","butter"]
prices = [2.99,1.50,4.65,2.50,3.37]
 
def print_grocery_list():
    for i in range(0,len(items)):
        print(f"{items[i]} - ${prices[i]}")
    
print_grocery_list()

print("")

def total_cost():
    total_cost = sum(prices)
    print(f"Total_cost: ${total_cost}")
    
total_cost()

print("")

def most_expensive_item():
    return max(prices)
 
print(f"The most expensive item cost: ${max(prices)}")

print("")

def price_feedback():
    for price in prices:
        if price <= 3.0:
            print(f"{price}: Great Deal!")
        elif price > 3.0 and price < 5.0 :
            print(f"{price}: Reasonable Price")
        else:
            print(f"price")

price_feedback()