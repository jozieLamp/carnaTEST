'''
HemoPheno4HF
SCRIPT DESCRIPTION: Main Runner Class for Learning Scores from the Trained MVDDs
CODE DEVELOPED BY: Josephine Lamp, Steven Lamp
ORGANIZATION: University of Virginia, Charlottesville, VA
LAST UPDATED: 8/24/2020
'''

from ..util import MVDD_Generator as gen
import pandas as pd

# import Params as params




#Expects param dict of 27 parameters, and select one of 4 outcomes
#Returns a text file location to display the graph, a integer score value and a string phenotype to be displayed
#Outcome can be "ALL", "DEATH" "REHOSPITALIZATION" "READMISSION" (passed in all caps)
def runHemo(paramDict, outcome):
    # print("outcome", outcome)
    #check for strings in paramDict
    for p in paramDict:
        # print(p, paramDict[p])
        if paramDict[p] == "":
            paramDict[p] = 0
        else:
            paramDict[p] = float(paramDict[p])

    #Convert input into dataframe
    input = pd.Series(paramDict)
    input = input.to_frame() 
    input = input.T

    #get outcome
    if outcome == "readmission":
        modelName = 'main/util/TreeFiles/Hemo_Readmission'
    elif outcome == "death":
        modelName = 'main/util/TreeFiles/Hemo_Death'
    elif outcome == "rehospitalization":
        modelName = 'main/util/TreeFiles/Hemo_Rehosp'
    else:
        modelName = 'main/util/TreeFiles/Hemo_AllOutcomes'

    #load model
    mvdd = gen.loadMVDDFromFile(modelName)
    print("found", mvdd)

    #Predict score
    score, path = mvdd.predictScore(input)
    print("score", score, "path", path)

    if score == 5:
        stringPath = "Returned Score of " + str(score) + ", Risk Level: HIGH\nIndicates a >= 40% chance of the outcome " + outcome
    elif score == 4:
        stringPath = "Returned Score of " + str(score) + ", Risk Level: INTERMEDIATE - HIGH\nIndicates a 30-40% chance of the outcome " + outcome
    elif score == 3:
        stringPath = "Returned Score of " + str(score) + ", Risk Level: INTERMEDIATE\nIndicates a 20-30% chance of the outcome " + outcome
    elif score == 2:
        stringPath = "Returned Score of " + str(score) + ", Risk Level: LOW - INTERMEDIATE\nIndicates a 10-20% chance of the outcome " + outcome
    elif score == 1:
        stringPath = "Returned Score of " + str(score) + ", Risk Level: LOW\nIndicates a < 10% chance of the outcome " + outcome


    stringPath = ""
    if path != None:
        stringPath = ' and '.join(path)

    imageName = modelName + '.png'

    return imageName, score, stringPath #will be displayed on webpage


#Expects a param dict of 119 parameters and the specified outcome
#Returns a text file location to display the graph, a integer score value and a string phenotype to be displayed
#Outcome can be "ALL", "DEATH" "REHOSPITALIZATION" "READMISSION" (passed in all caps)
def runAllData(paramDict, outcome):
    # check for strings in paramDict
    for p in paramDict:
        if paramDict[p] == "":
            paramDict[p] = 0
        else:
            paramDict[p] = float(paramDict[p])

    # Convert input into dataframe
    input = pd.Series(paramDict)
    input = input.to_frame()
    input = input.T

    # get outcome
    if outcome == "READMISSION":
        modelName = 'TreeFiles/AllData_Readmission'
    elif outcome == "DEATH":
        modelName = 'TreeFiles/AllData_Death'
    elif outcome == "REHOSPITALIZATION":
        modelName = 'TreeFiles/AllData_Rehosp'
    else:
        modelName = 'TreeFiles/AllData_AllOutcomes'

    # load model
    mvdd = gen.loadMVDDFromFile(modelName)

    # Predict score
    score, path = mvdd.predictScore(input)

    if score == 5:
        stringPath = "Returned Score of " + str(
            score) + ", Risk Level: HIGH\nIndicates a >= 40% chance of the outcome " + outcome
    elif score == 4:
        stringPath = "Returned Score of " + str(
            score) + ", Risk Level: INTERMEDIATE - HIGH\nIndicates a 30-40% chance of the outcome " + outcome
    elif score == 3:
        stringPath = "Returned Score of " + str(
            score) + ", Risk Level: INTERMEDIATE\nIndicates a 20-30% chance of the outcome " + outcome
    elif score == 2:
        stringPath = "Returned Score of " + str(
            score) + ", Risk Level: LOW - INTERMEDIATE\nIndicates a 10-20% chance of the outcome " + outcome
    elif score == 1:
        stringPath = "Returned Score of " + str(
            score) + ", Risk Level: LOW\nIndicates a < 10% chance of the outcome " + outcome


def main():
    paramDict = {"Age": "60", "BPDIAS": "63", "BPSYS": "80", "CI": "2.02", "CO": "4.52", "CPI": "10", "PCWP": "10", "EjF": "20", "HRTRT": "30",
     "MAP": "", "MIXED": "", "MPAP": "20", "PAD": "", "PAMN": "", "PAPP": "", "PAS": "11", "PCWPA": "32", "PCWPMN": "90",
     "PCWPMod": "", "PP": "", "PPP": "", "PPRatio": "0.9", "RAP": "", "RAT": "", "RATHemo": "10", "SVRHemo": "",
     "SVR": ""}

    filename, score, path = runHemo(paramDict, "REHOSPITALIZATION")




if __name__ == "__main__":
    main()