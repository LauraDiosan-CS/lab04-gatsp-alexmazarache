import os
from Repository import *
import Util

def save(c):
        filePath = os.path.join(os.getcwd(),"output.txt")
        fileOutput = open(filePath,"a")

        fileOutput.writelines("Best fitness "+str(c.fitness)+'\n')
        list = c.repres
        l2 = [x+1 for x in list]
        fileOutput.write(str(l2))

class Service(object):
    def __init__(self,repo):
        self._repo=repo

   
    def run(self, data):
        filePath = os.path.join(os.getcwd(), "easy_01_tsp.txt")
       

        popSize = 100
        generations = 50
        tsp = Util.Util(data,popSize)
        tsp.createPop()

        globalC = None
        localC =None
        genCount = 1

    
        while genCount< generations:
            genCount+=1
            tsp.newGeneration()

            localC=tsp.best()

            if globalC is None:
                globalC = localC
            elif globalC.fitness > localC.fitness:
                globalC = localC 
       

            print("------ gen: "+str(genCount)+"--------")
            print("Global: "+str(globalC.fitness))
            print("Local: "+ str(localC.fitness))
       

       
        
        save(globalC)
