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
    ListXLS = glob.glob("BASES/*.xlsx")
    return ListXLS
def FusionOfBases(xls):
    executions = 0
    print(len(xls))
    if len(xls) < 1:
        base = pd.read_excel(xls[0])        
        BaseFiltered = FilterBase(base)
    else:
        for i in xls:
            executions = executions + 1
            PorCent = executions*100/len(xls)
            print("CONVERTENDO --------> %d P/Cent" % (PorCent))
            base = pd.read_excel(i)        
            BaseFiltered = FilterBase(base)
            frame.append(BaseFiltered)    
    AllInOne = pd.concat(frame)    
    AllInOne.to_excel("RESULT/ALLINONE.xlsx")

def FirebaseSender():
    print("Seending")
    
def GenerateIds(): 
    group0 = ""
    IdGenerated = ""
    numberOfGroups = 3
    numberNumbersGroup = 4
    for t in range(numberOfGroups):
        for i in range(numberNumbersGroup):
            value = randint(0, 9)
            group0 = group0 + str(value)
        if t < numberOfGroups-1:
            group0 = group0 + " "
        IdGenerated = group0 
    for x in IdCode:
        if x == IdGenerated:
            print("Duplicidade encontrada")
            GenerateIds()
    return IdGenerated    
    

main()
