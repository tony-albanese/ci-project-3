![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Introduction
Thermodynamic calculations are a part of every introductory high school chemistry class. Specifically, there are three 
quantities students are expected to calculate:
* Enthalpy Change (dH) - This is the change in the total heat content of a system as reactants are converted into 
products in a chemical reaction.
* Free Energy Change (dG) - Also called the Gibbs free energy change, this is a measure of the amount of useful work a 
either abosrbed or released from the system during a chemical reaction.
* Entropy (dS) - This is a measure of the change in entropy in a chemical reaction as products are formed from reactions. Entropy is 
quantity that measures how much useful energy is unavailable for useful work (per unit temperature). 

The process by which the student calculates these quantities involves the following general steps:
1. The student must have a balanced chemical equation
2. The student must then look up the thermodynamic value for each chemical in the equation in a table. 
3. For reactants (these are on the left side of the reaction arrow), the student multiplies the coeffiecient of the chemical 
in the equation by the value of the thermodynamic quantity found in the table. This is repeated for the all the
reactants and products.
4. The energies the reactants are added. The energies of the prodcuts are added.
5. The change is determined by subtracting reactants from the products.
   - sum of products - sum of reactants [//]:#(Add LaTex formula) 

This process is tedious and error-prone since students often misread data in the table, or make calculator mistakes as
they perform sums, and often confuse products with reactants.

My console app helps students perform these calculations. Students enter the reactants and products from
a data table (provided in the app) along with the coefficients from the balanced chemical equation and the values
of dH, dG, and dS are calculated and displayed neatly.

# User Stories

# UI Design
## Features

## Algorithms

# Testing

# Technology Used
github
pycharm

## Python Libraries
rich
textualize
pandas
google sheets
# Credits
The chemical data was taken from the [International Baccalaureate](https://www.ibo.org/)'s Chemistry Data Booklet. 