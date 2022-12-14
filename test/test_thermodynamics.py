from chem_calculations.thermodynamics import *

df = load_data_frame()

reacts = get_reactants()
prods = get_products()

dH = calculate_enthalpy_change(df, reacts, prods)
dG = calculate_free_energy(df, reacts, prods)
dS = calculate_entropy_change(df, reacts, prods)

print(dH)
print(dG)
print(dS)

generate_thermodynamic_calculations()
