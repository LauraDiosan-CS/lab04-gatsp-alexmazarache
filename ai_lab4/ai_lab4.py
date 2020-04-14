
from Service import *
from Repository import *


repo = Repository()
service = Service(repo)

def createNet():
   
  
    network={}
    network["noNodes"] = repo.get_length()
    network["matrix"] = repo.get_graph()
    return network


service.run(createNet())
