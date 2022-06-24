# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]


def get_total_cash(shop):
    return shop["admin"]["total_cash"]


def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount


def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]


def increase_pets_sold(shop, amount):
    shop["admin"]["pets_sold"] += amount


def get_stock_count(shop):
    total_pets = len(shop["pets"])
    return total_pets


def get_pets_by_breed(shop, breed_of_pet):
    total_breed_of_pet = []
    for pet in shop["pets"]:
        if pet["breed"] == breed_of_pet:
            total_breed_of_pet.append(pet)
    return total_breed_of_pet


def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(shop, name):
    for pet in range(len(shop["pets"])):
        if shop["pets"][pet]["name"] == name:
            del shop["pets"][pet]
            break


def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, amount):
    customer["cash"] -= amount


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


# optional tasks


def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False


# integration tests
def sell_pet_to_customer(shop, pet, customer):
    if customer_can_afford_pet(customer, pet):
        pet_cost = pet["price"]
        remove_customer_cash(customer, pet_cost)
        add_or_remove_cash(shop, pet_cost)
        increase_pets_sold(shop, 1)
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(shop, pet["name"])
