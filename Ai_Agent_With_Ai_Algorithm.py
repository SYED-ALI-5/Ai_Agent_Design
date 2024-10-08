class Sensor:
    def __init__(self, action_Name, myaction):
        self.name = action_Name
        self.Func = myaction
    def sense(self, data):
        return self.Func(data)
        

class Agent:
    def __init__(self):
        self.environment = {
            "A": ["B", "F", "I"],
            "B": ["A", "C", "E"],
            "C": ["B", "D", "E"],
            "D": ["C", "G", "H"],
            "E": ["B", "C", "G"],
            "F": ["A", "G"],
            "G": ["D", "E", "F"],
            "H": ["D"],
            "I": ["A"]
        }
        self.Sensor1 = Sensor("Start", StartNodeSetting)
        self.Sensor2 = Sensor("End", GoalNodeSetting)
        self.SensorObj = [self.Sensor1, self.Sensor2]
        self.StartTuple = ()
        self.goalNode = ""
        self.open = []
        self.close =  []
        self.actuator = Actuator()

    def sense(self):
        for node in self.SensorObj:
            if node.name == "Start":
                self.startNode = input("Enter the Start Node:")
                self.startNode = self.startNode.upper()
                self.StartTuple = node.sense([self.environment, self.startNode, "Starting"])
            if node.name == "End":
                self.endNode = input("Enter the End Node:")
                self.endNode = self.endNode.upper()
                self.goalNode = node.sense([self.environment, self.endNode, "Ending"])
                
    def act(self):
        terminateLoop = False
        self.open.append(self.StartTuple)

        while not terminateLoop:
            currentVal = self.open.pop(0)
            self.close.append(currentVal)

            if currentVal[1] == self.goalNode:
                terminateLoop = True
                continue
            
            childOfCurrentVal = self.environment[currentVal[1]]

            for Child in childOfCurrentVal:
                pair = (currentVal[1], Child, currentVal[2] + [Child])
                if pair not in self.close:
                    self.open.append(pair)
        self.actuator.action(self)
        
class Actuator:
    def action(self, agent:Agent):
        for Tuples in agent.close:
            print(Tuples) 
        print("\nShortest Path from Starting Node to Goal Node:\n")
        for data in agent.close:
            if data[1] == agent.goalNode:
                print(data[2])          
                
#----------------------------------------------------------------------------------------------------
def StartNodeSetting(data):
    startTuple = ()
    if data[1] not in data[0].keys():
        print(f"Invalid {data[2]} Node")
        exit(0)
    else:
        startTuple = ('-', data[1], [data[1]])
    return startTuple
#----------------------------------------------------------------------------------------------------
def GoalNodeSetting(data):
    goal = ""
    if data[1] not in data[0].keys():
        print(f"Invalid {data[2]} Node")
        exit(0)
    else:
        goal = data[1]
    return goal
#----------------------------------------------------------------------------------------------------

agent = Agent()
agent.sense()
agent.act()