from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

import numpy as np

# Class that creates the Bayesian Network model using the pgmpy library.
# This class may be used alongside the Probability class.
class Bayesian:

    # Constructor of the class. It receives the model as a list of lists.
    def __init__(self, model):
        self.model = model                       
        self.network = BayesianNetwork()

        self.nodes = set()
        self.edges = []
        self.cpds = []

        self.create_nodes()
        self.create_edges()
        self.create_cpds()
        self.create_bayesian()

    # Method that creates the nodes of the network.
    def create_nodes(self):
        for item in self.model:
            node = item[0].split(" | ")[0].split(" ")

            if node[0][0] == "!":
                node[0] = node[0][1:]

            self.nodes.update(node)

        self.nodes = sorted(list(self.nodes))

    # Method that creates the edges
    def create_edges(self):
        for item in self.model:
            variable = item[0].split(" | ")[0].split(" ")

            if variable[0][0] == "!":
                variable[0] = variable[0][1:]

            if "|" in item[0]:
                evidence = item[0].split(" | ")[1].split(", ")

                if evidence[0][0] == "!":
                    evidence[0] = evidence[0][1:]
                self.edges.append([evidence[0], variable[0]])

                if len(evidence) > 1:

                    if evidence[1][0] == "!":
                        evidence[1] = evidence[1][1:]
                    self.edges.append([evidence[1], variable[0]])

        self.edges = list(set([tuple(edge) for edge in self.edges]))
    
    # Method that creates the conditional probability distributions of the network.
    def create_cpds(self):
        for node in self.nodes:
            variable = node
            variable_card = 2
            values = [[],[]]
            evidence = []
            evidence_card = []

            for edge in self.edges:
                if edge[1] == node:
                    evidence.append(edge[0])

            for item in self.model:
                
                if "|" in item[0]:

                    if item[0].split(" | ")[0].split(" ")[0][1:] == node:
                        values[0].append(item[1])
                        values[1].append(1-item[1])

                    elif item[0].split(" | ")[0].split(" ")[0] == node:
                        values[0].append(1-item[1])
                        values[1].append(item[1])
                        

                elif "|" not in item[0] and len(evidence) == 0:

                    if item[0][0] == "!" and item[0][1:] == node:
                        values[0].append(item[1])
                        values[1].append(1-item[1])
                        break
                    elif item[0][0] == node:
                        values[0].append(1-item[1])
                        values[1].append(item[1])
                        break

            for var in evidence:
                evidence_card.append(2)

            self.cpds.append(TabularCPD(variable=variable, variable_card=variable_card, values=values, evidence=evidence, evidence_card=evidence_card))


    # Method that creates the network.
    def create_bayesian(self):
        self.network.add_nodes_from(self.nodes)
        self.network.add_edges_from(self.edges)

        for cpd in self.cpds:
            self.network.add_cpds(cpd)

        self.network.check_model()

    # Method that returns a string with the visual representation of the network.
    def get_string_representation(self):
        representarion = ""
        for parent, child in self.edges:
            representarion += "\n" + parent + " -> " + child

        return representarion

    # Method that returns boolean if network is fully observed.
    def is_fully_observed(self):
        contador = [0, len(self.nodes)]
        for node in self.nodes:
            if self.network.get_cpds(node):
                contador[0] += 1

        check = self.network.check_model()

        return (contador[0] == contador[1]) and (check == True)

    # Method that returns the probabilities of each node.
    def get_factors(self):
        factores = []
        for cpd in self.network.get_cpds():
            factores.append(cpd)
        return factores

    # Method that returns a probability inference of a node given the evidence.
    def get_inference(self, node, evidence):
        #replace 0 by 1 and viceversa on evidence

        inference = VariableElimination(self.network)
        return inference.query([node], evidence=evidence)








