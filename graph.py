from tkinter import messagebox
#defining a class Node for Reference
class Node:
    #GetNeighbors returns a list
    def GetNeighbors(self) -> list["Node"]: # Return adjacency list
        pass
    #Equating instance
    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value
    #Hashable instance
    def __hash__(self):
        return hash(self.value)
       
    #defining a search function using the BFS Strategy of Graph Theory
    def Search(start, target):
        print("Search is called")
        frontier = []
        visited = set()

        #initial node to search
        frontier.append(start)
        depth = {start : 0}
        pathTree = {start : None}
        
        while (frontier):
            curr = frontier.pop()
            visited.add(curr)

            if (curr == target):
                return depth[target]
            
            for n in curr.GetNeighbors():
                if n not in visited:
                    frontier.append(n)
                    depth[n] = depth[curr] + 1
                    pathTree[n] = curr

        return depth
#Defing a proper class for initiating the BFS
class Search:
    #defining the data storage structures to store the nodes
    def __init__(self):
        self.visited = set()
        self.frontier = []
        self.depth = {}
        self.pathTree = {}
        self.pathExists = False
        self.curr=""
        
    #running a search starting from the initial state to final
    def Run(self, start, target):
        self.frontier.append(start)
        self.depth[start] = 0
        self.pathTree[start] = ""

        while self.frontier:
            curr = self.frontier.pop(0)   # This is BFS as we take the first element added to the frontier
            self.visited.add(curr)
            #checking equality
            if curr == target:
                self.pathExists = True
                
                return
            #checking the neighbors
            for n in curr.GetNeighbors():
                if n not in self.visited:
                    self.frontier.append(n)
                    self.depth[n] = self.depth[curr] + 1
                    self.pathTree[n] = curr
    #defining function to get  a path
    def GetPathToSolvedState(self, start, target):
        path = []
        curr = target
        #obtaining the path to print
        while curr != start:
            path.append(curr)
            curr = self.pathTree[curr]
        #adding the nodes 
        path.append(start)
        path.reverse()
        return path


    
        
    
