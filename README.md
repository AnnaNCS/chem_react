 # GraphChem

GraphChem, a software, written in python, generates all possible pathways to synthesize the final product from a given set of reactions and reactants. The output includes the calculation of the corresponding reaction rates within the network. The goal is to provide an efficient and optimized system to carry out chemical processes within one software.

## Required input

Before running the software, ensure you have included and updates the input data:
    in the graphchem.py file, include: 
        the set of reactions in the system; SMALL_REACTION_SET = []
        the concentrations of each compound in the system; CONC = []
        the reaction rates; RATES = [] 
        in main(), the initial reactants and final product 


## Running

GraphChem requires [Python 3] and the [networkx] package. Once networkx is installed, the following will run the software with the input provided:

    git clone git@github.com:annancs/chem_react.git
    cd graphchem
    python3 graphchem.py


Additionally, GraphChem can generate a [GraphViz] reaction network visualization:

    Copy line 1 to 36 from the graph_results.txt file and any pathway from the file that needs to be represented as a graph. Insert the code into the online generator, https://dreampuf.github.io/GraphvizOnline/. 

    [networkx]: https://networkx.github.io/
    [Python 3]: https://www.python.org/
