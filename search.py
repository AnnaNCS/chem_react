import sys

from graphchem import reactants, products


# Each matrix should represent a reaction/synthesis pathway from the class Reaction
# The goal of this code is to read the synthesis pathway and calculate the total reaction rate of the synthesis pathway 
    #assumming that we already know the concentration of the reactions and reaction rates
# Each time the graphchem is building a pathway it builds also a matrix for that whole system 


def find_root_react(pathway, final_react, to_be_searched):
    """Creates a the disctionanry with key and value, that can be a tuple if multiple reactions are producing the same compound.
    
    Arguments: 
        pathway(FrozenSet[Set[str]]): one single pathway
        final_react(): the final target compound of the network 
        to_be_searched(list): recursive tuple list that grows as more values are added to it.

    Returns: 
        list: the tuple list, returned into the loop to be checked again until all_key_present = True
    """

    #find reactions with products as the final_reactions reactants

    for reaction in pathway:
        prod = products(reaction)
        for x in prod:
            if x in reactants(final_react):
                if reaction not in to_be_searched.values():
                    # how to append to a kye multiple values 
                    if x in to_be_searched.keys():
                        # check for the repetition of values within the same key 
                        if reaction not in to_be_searched[x]:   
                            to_be_searched[x].append(reaction)
                    if x not in to_be_searched.keys():
                        # check for key, whether present or not added yet
                        to_be_searched[x] = []
                        to_be_searched[x].append(reaction)
                print("Root Reaction added ---> key:", x, ", values:", to_be_searched[x])
        
    return to_be_searched
    

def find_final_reaction(working_path, final_product):
    """Create .
    
    Arguments: 
        working_path(FrozenSet[Set[str]]): one single pathway
        final_product(): the final target compound of the network

    Returns: 
        reaction(str): the reaction that produces the final_product
    """

    for reaction in working_path:
        if final_product in products(reaction):
            return reaction

def next_key_present(pathway, react, to_be_searched):
    """Check  .
    
    Arguments: 
        pathway(FrozenSet[Set[str]]): one single pathway
        react(str): the compound to be checked  
        to_be_searched(list): the tuple list with reactions as values 

    Returns: 
        bool: True or False, whether the next key is already present in the tuple or not.
    """

    for reaction in pathway:
        prod = products(reaction)
        for x in prod:
            if x in reactants(react):
                #if key in to_be_searched.keys(): 
                if x in to_be_searched.keys():
                    return True
                else:
                    return False

def all_key_present():
    """Checks that all keys have been visited and added into the tuple"""
    return True
                        
       
def search_roots(working_path, final_product):
    """Prints the dictionary in the root_serach.txt file, where the key is each unique product in the given pathway, 
       and the values are all the reactions that produce the product.
    
    Arguments: 
        working_path(FrozenSet[Set[str]]): specific single pathway to be searched
        final_react(): 

    Returns: 
        None
    """

    print('The working pathway is:', working_path)

    to_be_searched = {}

    # find last reaction with final product and add it to the dict (the dict keeps track of the reactions already visited)
    # Add "final" rection to the list in order to keep the pathways acyclic     
    final_react = find_final_reaction(working_path, final_product)
    to_be_searched[final_product] = []
    to_be_searched[final_product].append(final_react)

    # start a loop that will find the root reaction of each reaction, starting with the final reaction   
    # until len(to_be_searched) = num of reactions --> stop CHECK HOW TO STOP 
    # everytime you loop the to_be_searched has to be updated with the new values from the previous looping
    # repeat the find_root_react for the last item in the dictionary until we looped thtought every reaction, 
    # until every reaction .......    
    # keep track of last added element or check the next key --> next_key_present
    # to break check if all keys have been found

    breaking = False
    len_loop = len(working_path) * 2

    for x in range(0, len_loop, 1):
        if len(to_be_searched[list(to_be_searched)[-1]]) == 1:
            if (next_key_present(working_path, to_be_searched[list(to_be_searched)[-1]][0], to_be_searched) == True):
                break
            to_be_searched = find_root_react(working_path, to_be_searched[list(to_be_searched)[-1]][0], to_be_searched)
        if len(to_be_searched[list(to_be_searched)[-1]]) > 1:
            print('Tuple present:', to_be_searched[list(to_be_searched)[-1]])
            # check all instances in the tuple, if all are present then break
            check = []
            for i in to_be_searched[list(to_be_searched)[-1]]:
                if (next_key_present(working_path, i, to_be_searched) == True):
                    check.append(True)
                else:
                    check.append(False)
            print(check)
            if all(check) == True:
                breaking = True
                break
            for i in to_be_searched[list(to_be_searched)[-1]]:
                print('Searching...', i)
                to_be_searched = find_root_react(working_path, i, to_be_searched)
                print("Search done.")
        if breaking == True:
            break
        
    for i in list(to_be_searched):
        print("The key is:", i, ", and the Values are:", to_be_searched[i])


def create_system(reactions, pathways, pathway, paths_num, index, final_product):
    """Calls the search_root function."""

    print("\n")
    print("----- Index of pathway to be searched:", index, "-----")
    
    search_roots(pathway, final_product)

    # compare the possible reactions rates
    # TODO 



    
    
    

