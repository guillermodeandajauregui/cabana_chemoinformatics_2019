#package import
import rdkit
import pandas as pd
import numpy as np
import scipy
import networkx as nx #if I want to play around with networks
from rdkit import Chem

my_data = pd.read_csv("data/Database_CABANA.csv")

#extract smiles
smiles = list(my_data["SMILES"])

#make a list of mol
sm = list()
for i in smiles:
    sm.append(Chem.MolFromSmiles(i))


#make list for descriptors 

HBA = list()
HBD = list()