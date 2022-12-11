from repository.balancing_equations import *
#Test method for entering formulas
#Checks to see input is valid.
def test_entering_formulas():
    compounds = enter_formulas()
    for compound in compounds:
        print(compound.formula)

#Method to test balancing formulas
def test_balance_equation():

    print("Enter reactants")
    reactants = enter_formulas()
    print("Enter products")
    products = enter_formulas()

    result= balance_reaction(reactants, products)
    if(result.status == False):
        print("The reaction could not be balanced.")
    else:
        print(result.reaction.formula)

test_balance_equation()