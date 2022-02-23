import numpy as np 
import pandas as pd
import glob
from random import randint

AllInOne = pd.DataFrame()

frame = []
NCM = []
Nome = []
CEST = []
IdCode = []



class main():
    def __init__(self):
     print("Executing")
     XLS = SearchBases()
     FusionOfBases(XLS)
     print("Code Executed")
     
def FilterBase(base):
    
    for index,i in base.iterrows():
        if pd.isna(i['NCM']) != True:
            NCM.append(i['NCM'])
            CEST.append(i['cCEST'])
            Nome.append(i['Mercadoria'])  
            IdCode.append(GenerateIds())
            
    DatabaseFiltered = pd.DataFrame()        
    #------------------------------
    DatabaseFiltered['Code'] = IdCode
    DatabaseFiltered['Nome'] = Nome
    DatabaseFiltered['NCM'] = NCM
    DatabaseFiltered['cCEST'] = CEST
    return DatabaseFiltered
    
def SearchBases():       
    ListXLS = glob.glob("../@BASES/*.xls")
    return ListXLS
def FusionOfBases(xls):
    executions = 0
    for i in xls:
        executions = executions + 1
        PorCent = executions*100/len(xls)
        print("CONVERTENDO --------> %d P/Cent" % (PorCent))
        base = pd.read_excel(i)        
        BaseFiltered = FilterBase(base)
        frame.append(BaseFiltered)    
    AllInOne = pd.concat(frame)    
    AllInOne.to_excel("../@RESULTS/ALLINONE.xlsx")

def FirebaseSender():
    print("Seending")
    
def GenerateIds(): 
    group0 = ""
    IdGenerated = ""
    for t in range(3):
        for i in range(4):
            value = randint(0, 9)
            group0 = group0 + str(value)
        if t < 2:
            group0 = group0 + " "
        IdGenerated = group0 
    return IdGenerated    
    

main()
