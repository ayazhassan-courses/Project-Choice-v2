#PLEASE READ ALL THE COMMENTS WHILE GOING THROUGH THE CODE
# All names and values used throughout are test values

#--------------------------------------------------------------------------------------------
#This is the first data structure
#It uses list of tuples in a dictionary
#PROS: 
# 1. Easier/Faster to write
#CONS:
# 1. Have to be careful with positioning of elements when writing code
# 2. Hard to debug numbers

datastructure1 = {
    'Chp1_Node1':[
        ('Choice1',10, ('Ali',-5),'Chp1_Node5'), #2nd object (number) is stress. (Ali,-5) is relationship counter and name
        ('Choice2',-10, ('Ayesha',8),'Chp1_Node6') 
        ],
    'Chp1_Node2':[
        ('Choice1',3, ('John',4),'Chp1_Node7'),
        ('Choice2',-4, ('Adam',-3),'Chp1_Node8')
        ] 
}

#--------------------------------------------------------------------------------------------------------

#This is the second data structure
#It uses nested dictionaries
#PROS: 
# 1. Easier to index/Find elements
# 2. Easier to debug/Less chance of bugs
#CONS:
# 1. May cause problems with RenPy (has to be tested)
# 2. Slower to write/Annoying
''' #NOT WORKING
datastructure2 = {
    'Chp1_Node1':{
        'Choice1':{'Stress':10, 'Relationship':('Ali',-5),'ToNode':'Chp1_Node5'},
        'Choice2':{'Stress':-10, 'Relationship':('Ayesha',8),'ToNode':'Chp1_Node6'}
    },
    'Chp1_Node2':{
        'Choice1':{'Stress':3, 'Relationship':('John',4),'ToNode':'Chp1_Node7'},
        'Choice2':{'Stress':-4, 'Relationship':('Adam',-3),'ToNode':'Chp1_Node8'}
    } 
}
'''
#-----------------------------------------------------------------------------------------------------

#Dictionary storing relations with each character
relationshipdict = {
    'Ali':4,
    'Ayesha':10,
    'John':8,
    'Adam':2
}

#Stress counter
Stress = 16


#--------------------------------------------------------------------------------------------------------

# print(datastructure1['Chp1_Node1'])
# print(datastructure2['Chp1_Node1'])

#------------------------------------------------------------------------------------------------------

#Helper functon for the first data structure

def helper1(ds, currentnode, choice):
    global relationshipdict
    global Stress
    for i in ds[currentnode]:
        if i[0]==choice:
            Stress+=i[1]
            relationshipdict[i[2][0]]+=i[2][1]
            if relationshipdict[i[2][0]]<0:
                relationshipdict[i[2][0]]=0
            return i[-1]


''' #NOT WORKING
def helper2(ds, currentnode, choice):
    global relationshipdict
    global Stress
    Stress+=ds[currentnode][choice]['Stress']
    relationshipdict[ds[currentnode][choice]['Relationship'][0]]+=[ds[currentnode][choice]['Relationship'][1]]
    if relationshipdict[ds[currentnode][choice]['Relationship'][0]]<0:
        relationshipdict[ds[currentnode][choice]['Relationship'][0]]=0
    return [ds[currentnode][choice]['ToNode']]
'''

#------------------------------------------------------------------------------------------------------------

#Check whether helper function works or not

# print('Previous Relationships:',relationshipdict,'\n','Previous Stress:',Stress)
# print('Next Node is:',helper1(datastructure1, 'Chp1_Node1', 'Choice1'))
# print('New Relationships:',relationshipdict,'\n','New Stress:',Stress)

#It works!!
#------------------------------------------------------------------------------------------------------------


#Test run for this using sample text based game:

#Function to test whether this method works or not
def Chp1_Node1():
    print('Boooooo')

def Chp1_Node5():
    print('You made your choice and reached Chapter1 Node5')

#This dictionary takes the return output and converts it into callable function
stringtofunction = {
    'Chp1_Node1':Chp1_Node1,
    'Chp1_Node5':Chp1_Node5
}



def main():
    #We assume that this is the staring node:
    currentNode = 'Chp1_Node1'

    print('Hello adventurer, please choose:')
    choiceMade = 'Choice1'  #Here we assume player chose option 1 and choiceMade is == Choice1

    #This will take the string output and convert into a callable function
    stringtofunction[helper1(datastructure1, currentNode, choiceMade)]()  #The () run the callable function

# main()


#------------------------------------------------------------------------------------------

#VisitedNodes
Visited = {
    'Chp1_Node1': False,
    'Chp1_Node2': False,
    'Chp1_Node3': False,
    'Chp1_Node4': False,
    'Chp1_Node5': False,
    'Chp1_Node6': False,
    'Chp1_Node7': False,
    'Chp1_Node8': False
}

#Here we have modified the helper function to also check mark visited Nodes:

def helper1Modified(ds, currentnode, choice):
    global relationshipdict
    global Stress
    for i in ds[currentnode]:
        if i[0]==choice:
            Stress+=i[1]
            relationshipdict[i[2][0]]+=i[2][1]
            if relationshipdict[i[2][0]]<0:
                relationshipdict[i[2][0]]=0
            Visited[currentnode]=True
            Visited[i[-1]]=True
            return i[-1]

# print('Previous Relationships:',relationshipdict,'\n','Previous Stress:',Stress,'\n',Visited)
# print('Next Node is:',helper1Modified(datastructure1, 'Chp1_Node1', 'Choice1'))
# print('New Relationships:',relationshipdict,'\n','New Stress:',Stress,'\n',Visited)