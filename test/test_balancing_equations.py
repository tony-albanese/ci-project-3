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


def test_stoichiometry():
    reaction = generate_reaction()
    result = calculate_stoichiometry_by_mass(reaction, 1, 10)
    if(result.status == True):
        print(result.formula_amounts)
    else:
        print(result.message)

    mole_result = calculate_stoichiometry_by_mole(reaction, 1, 4)
    if (mole_result.status == True):
        print(mole_result.formula_amounts)
    else:
        print(mole_result.message)


test_stoichiometry()