from graph import Node, Search
import copy

class BoardState(Node):
    
     moves = [(0,1), (0,-1), (1,0), (-1,0)]
     
     def __init__(self, board : list[list[int]] | str, isList = False):
        if isList:
            self.board = "".join(str(board[i][j])  for i in range(3) for j in range(3))
        else:
            self.board = board

     def GetNeighbors(self) -> list[Node]:
       
        for i in range(3):
            for j in range(3):
                if self.board[3*i + j] == "0":
                    zerox = i
                    zeroy = j

        ns = []  # list to hold all neighbors
        for x,y in BoardState.moves:
            neighx = zerox + x
            neighy = zeroy + y

            if (not (0 <= neighx < 3)) or (not (0 <= neighy < 3)):
                continue 

            nextBoard = list(self.board)
            nextBoard[3*zerox + zeroy], nextBoard[3 * neighx + neighy] = nextBoard[3*neighx + neighy], nextBoard[3 * zerox + zeroy]
            nextBoard = "".join(nextBoard)

            ns.append(BoardState(nextBoard))
        
        return ns
     def getsolvablestate(self, depth):
            
            currentstate = "123456780"
            
            visited = set()
            
            solvablestates = []
            
            queue = [(currentstate, 0)]

            while queue:
                state, cdepth = queue.pop(0)
                
                if cdepth == depth:
                    solvablestates.append(state)
                    continue
                
                currentboard = BoardState(state)
                
                neighbours = currentboard.GetNeighbors()
                
                for neighbour in neighbours:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour.board, cdepth + 1))

            return solvablestates




     def __eq__(self, other):
        if other == None:
            return False
        return self.board == other.board
    
     def __hash__(self):
        return self.board.__hash__()
    
    
    

    

            



