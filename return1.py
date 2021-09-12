sandwich = "Tuna and Cucumber"

def calculate_price(product):
	if product == "Ham and Cheese":
		return 2.50
	elif product == "Tuna_and_Cucumber":
		return 2.25
	elif product == "Egg Mayo":
		return 2.25
	elif product == "Chicken Club":
		return 2.75
	else:
		return 2.50

calculate_price(sandwich)