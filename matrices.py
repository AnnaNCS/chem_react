import numpy as np
import matplotlib.pyplot as plt 

from graphchem import Reaction

"""np.set_printoptions(precision=3) 
np.set_printoptions(suppress=True)

data = np.array([[1.2, 0.7], [-0.3, 0.5]])

labels = np.array([1, 2])

def plot_data(data, labels):
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    ax.scatter(data[:,0], data[:,1], c=labels, cmap=plt.cm.Set3, s=50, zorder=50)
    nudge = 0.08
    for i, d in enumerate(data):
        ax.annotate(f'{i}', (d[0]+nudge,d[1]+nudge))
    ax.set_aspect('equal', 'datalim')
    plt.show()

#plot_data(data, labels)
print(data.mean()) #data.std() """

# Each matrix should represent a reaction/synthesis pathway from the class Reaction
# The goal of this code is to read the synthesis pathway and calculate the total reaction rate of the synthesis pathway 
    #assumming that we already know the concentration of the reactions and reaction rates
# Each time the graphchem is building a pathway it builds also a matrix for that pathway 


def set_up_concentrations(paths_num):
    
    concentrations = [0] * len(paths_num)
    for i in concentrations:
        concentrations[i] = 1
        #print(concentrations.index(i))

    #print('length of concentrations array' , len(concentrations))
    #print('length of paths_num that includes pathways keys' ,len(paths_num))

def set_up_reaction_rates(reactions):
    
    reaction_rates =  [0] * (len(reactions)+1)

    x = 0
    for i in reaction_rates:
        reaction_rates[x] = (x+1)
        x += 1 
    
    dict_rates = dict(zip(reactions, reaction_rates))

    return dict_rates

    #print('length of dictionary that asigns reaction rates to rections', len(dict_rates))
    #print(dict_rates)

def add_rates(pathways, dict_rates):

    #for each pathway create an array of matrices
    #provide a overall total rection rate of that pathway 

    sum_rates = [0] * len(pathways)

    x = 0
    for i in pathways:
        
        sum_rate = 0
        path = pathways[x]
        #print(path)

        for i in path:
            if i in dict_rates:
                rate = dict_rates.get(i, None)
                #index = list(dict_rates).index(i)
                #print(rate)
            sum_rate += rate 
            #print(sum_rates) 
        
        sum_rates[x] = sum_rate
        #print(sum_rates[x])
        x += 1
       
def compare_rates(pathways, dict_rates, initial_reactants, final_product):

    working_path = pathways[19]
    print(working_path)

    # in a pathway's rection, concatenate or extract all rectant and product compounds 
    # be able to serach that compound in the initial reactants or final product
    for reaction in working_path:
        if final_product in reaction:
            print("result reaction:", reaction)
        


def create_system(reactions, pathways, paths_num, index, initial_reactants, final_product):
     
    set_up_concentrations(paths_num)

    dict_rates = set_up_reaction_rates(reactions)

    #add_rates(pathways, dict_rates)

    compare_rates(pathways, dict_rates, initial_reactants, final_product)
    



    
    
    

