import pandas.core.frame

from data.data_set import *
from rich import print
from rich.console import Console
import re

df = load_data_frame()
print(df.head())


# method to get reactants
# method to get products
# method to do calculation
# method to validate input

def calculateThermodynamicProperties():
    reactants = []
    products = []
    while True:
        print("Enter a reactant and the coefficient from the balanced equation separated by a comma.")
        print("When you are done entering reactants, type done")
        reactant = input("Reactant: ")
        if reactant == 'done':
            break


def getReactants():
    reactants = []
    while True:
        print("Enter a reactant and the coefficient from the balanced equation separated by a comma.")
        print("When you are done entering reactants, type done")
        user_input = input("Reactant: ")

        if (user_input == 'done'):
            break
        if validateReactionEntry(user_input) and valueIsValid(44, user_input):
            pair = user_input.split(",")
            row = int(pair[0])
            coefficient = int(pair[1])
            asTuple = (row, coefficient)
            reactants.append(asTuple)
        else:
            print("Invalid input")

    return reactants


def getProducts():
    products = []
    while True:
        print("Enter a product and the coefficient from the balanced equation separated by a comma.")
        print("When you are done entering products, type done")
        user_input = input("Product: ")

        if (user_input == 'done'):
            break
        if validateReactionEntry(user_input) and valueIsValid(44, user_input):
            pair = user_input.split(",")
            row = int(pair[0])
            coefficient = int(pair[1])
            asTuple = (row, coefficient)
            products.append(asTuple)
        else:
            print("Invalid input")

    print(products)
    return products


def validateReactionEntry(entry):
    pattern = '[0-9]+,[1-9]+'
    is_match = re.match(pattern, entry)
    if is_match is not None:
        return True
    else:
        return False


def valueIsValid(max, entry):
    values = entry.split(",")
    if int(values[0]) > max:
        return False
    else:
        return True


rcts = getReactants()
prods = getProducts()


def calculate_enthalpy_change(data_frame: pandas.core.frame.DataFrame, reactants: list, products: list):
    column_name = 'dH'
    sum_products = 0
    sum_reactants = 0

    for reactant in reactants:
        row = reactant[0]
        coefficient = reactant[1]
        enthalpy = data_frame._get_value(row, column_name)
        sum_reactants = sum_reactants + enthalpy * coefficient

    for product in products:
        row = product[0]
        coefficient = product[1]
        enthalpy = data_frame._get_value(row, column_name)
        sum_products = sum_products + enthalpy * coefficient

    enthalpy_change = sum_products - sum_reactants
    return enthalpy_change


def calculate_free_energy(data_frame: pandas.core.frame.DataFrame, reactants: list, products: list):
    column_name = 'dG'
    sum_products = 0
    sum_reactants = 0

    for reactant in reactants:
        row = reactant[0]
        coefficient = reactant[1]
        enthalpy = data_frame._get_value(row, column_name)
        sum_reactants = sum_reactants + enthalpy * coefficient

    for product in products:
        row = product[0]
        coefficient = product[1]
        enthalpy = data_frame._get_value(row, column_name)
        sum_products = sum_products + enthalpy * coefficient

    energy_change = sum_products - sum_reactants

    print("Sum products: ")
    print(sum_products)
    print("Sum of reactants:")
    print(sum_reactants)
    return energy_change


def calculateEntropy(data_frame: pandas.core.frame.DataFrame, reactants: list, products: list):
    column_name = 'dS'
    sum_products = 0
    sum_reactants = 0

    for reactant in reactants:
        row = reactant[0]
        coefficient = reactant[1]
        enthalpy = data_frame._get_value(row, column_name)
        sum_reactants = sum_reactants + enthalpy * coefficient

    for product in products:
        row = product[0]
        coefficient = product[1]
        enthalpy = data_frame._get_value(row, column_name)
        sum_products = sum_products + enthalpy * coefficient

    # Divide by 1000 because of J to kJ unit conversion
    entropy_change = (sum_products - sum_reactants) / 1000

    print("Sum products: ")
    print(sum_products)
    print("Sum of reactants:")
    print(sum_reactants)
    return entropy_change


print(calculate_enthalpy_change(df, rcts, prods))
