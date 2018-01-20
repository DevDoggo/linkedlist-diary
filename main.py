



import datetime
import sqlite3
from linkedlistNode import linkedlistNode

database = "llNodes.db"
conn=sqlite3.connect(database)
cur=conn.cursor()

#Connects
def connect():
    cur.execute("CREATE TABLE IF NOT EXISTS nodes (id INTEGER PRIMARY KEY, name text, date text, notebooktext text)")
    conn.commit()

#Inserts new Node info into database
def insertNode(name, date, text):
    cur.execute("INSERT INTO nodes VALUES (NULL, ?, ?, ?)", (name, date, text))
    conn.commit()

def getNodes():
    cur.execute("SELECT name, date, notebooktext FROM nodes")
    rows = cur.fetchall()
    return rows

def updateNode(text, curNode):
    curNode.addText(text)
    cur.execute("UPDATE nodes SET notebooktext=? WHERE name=?", (curNode.text, curNode.name))
    conn.commit()
    return curNode

def jumpToNode(name, curNode, listhead):
    nodeIter = listhead
    while(True):
        if nodeIter.name == name:
            print("Node found.")
            nodeIter.statCall()
            return nodeIter
        else:
            if nodeIter.next == None:
                print("No node of that name found.")
                return curNode
            nodeIter = nodeIter.getNextNode()

def formatInput(text):
    text = text.replace(" ", "")
    return text

def jumpToLastNode(curNode):
    while curNode.next != None:
        curNode = curNode.next
    return curNode

#LoadNodes works just fine! Don't touch! 
def loadNodes(listhead): 
    nodeArray = getNodes() 
    if len(nodeArray) > 0:
        curNode = listhead
        for i in range(1, len(nodeArray)):
            curNode = curNode.addNode(name = nodeArray[i][0], date = nodeArray[i][1], text = nodeArray[i][2])  
            #print(str(curNode.name) + "\n" + str(curNode.date) + "\n" + str(curNode.text) + "\n")
        return curNode
    return listhead


def printCommandHelp(commandList, instructionList):
    listLength = len(commandList)
    maxLength = 0
    for item in instructionList:
        if len(item) > maxLength:
            maxLength = len(item)
    outputString = "\n"
    i = 0
    for i in range(0, listLength):
        instruction = instructionList[i]
        command = commandList[i]

        spaces = " "*(maxLength-len(instruction))
        outputString = outputString + instruction + spaces + " -   " + command + "\n"
    print("\n"*50)
    print(outputString)



def mainloop():

    connect()
    listhead = linkedlistNode(None, None, "Page 0", "Default Page", "Default text for first page") 
    curNode = loadNodes(listhead) 
    print("\ntype: 'com' for commands.")
    
    while(True):
        x = formatInput(input("\nInput: "))
        

        #NextNode
        if x == "n":
            curNode = curNode.getNextNode()
   

        #PrevNode
        elif x == "p": 
            curNode = curNode.getPrevNode()
    

        #Add Page
        elif x =="a":
            date = str(datetime.datetime.now().date())
            curNode = jumpToLastNode(curNode)
            if curNode.date != date:
                nameNumber = str(int(curNode.name[5:]) + 1)
                name = "Page " +  nameNumber
                curNode = curNode.addNode(name, date)
                insertNode(curNode.name, curNode.date, curNode.text) 
            else:
                curNode.statCall()
                print("\nA page for that date already exsits.\n")
                continue
                

        #Update Page
        elif x =="u":
            if curNode.name == "Page 0":
                print("\nSorry, you can't edit the default page.\n")
                continue
            else:
                inputText = input("Edit text: ")
                curNode = updateNode(inputText, curNode)


        #Clear Page
        elif x =="c":
            clear = formatInput(input("You're about to delete all text on this page, are you sure? [y/n]: "))
            if clear in ["y", "Y", "yes", "Yes", "YES"]:
                curNode.clearPage()
                updateNode("", curNode)
                print ("Page was cleared.")
            else:
                curNode.statCall()
                print ("Page was not cleared.")
                continue


        #Jump to Page
        elif x == "j":
            nodeNumber = formatInput(input("Page number: "))
            curNode = jumpToNode(("Page " + nodeNumber), curNode, listhead)
            continue


        #Commands
        elif x == "com":
            commandList = ["[n]", "[p]", "[a]", "[u]", "[j]", "[c]", "[x]"]
            instructionList = ["Next Page", "Previous Page", "Add Page", "Update Text", "Jump To Page #", "Clear Page", "Exit Program"]
            if len(commandList) != len(instructionList):
                print("The programmer has implemented the command-list incorrectly! Please notify him!")
            else:
                printCommandHelp(commandList, instructionList)
            continue

        elif x == "x":
            break




        curNode.statCall()


mainloop() 
