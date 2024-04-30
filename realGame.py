import tkinter as tk
from tkinter import messagebox
import time
from graph import Search
from boardGame import BoardState
import random

#defining a class for the puzzle
class SlidingPuzzleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("3x3 Sliding Puzzle")

        self.boardState = BoardState("123456780")
        solveableStates = self.boardState.getsolvablestate(8)
        self.board = random.choice(solveableStates)
        self.alwaysboard=self.board
        self.moves = 0
        self.start_time = None
        self.timer_running = False
        self.create_widgets()
        self.alwaysboard=self.board
   #developing the tiles and functions required for tkinter
    def create_widgets(self):
        
        currentState = self.board
        self.tiles = []
        for i in range(3):
            for j in range(3):
                num = currentState[3*i +j]
                text = str(num) if num != '0' else ""
                tile = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', '12', 'bold'),
                                 command=lambda i=i, j=j: self.move_tile(i, j))
                tile.grid(row=i, column=j, padx=5, pady=5)
                self.tiles.append(tile)

        self.moves_label = tk.Label(self.master, text="Moves: 0", font=('Arial', '12'))
        self.moves_label.grid(row=3, columnspan=3, padx=5, pady=5)

        self.timer_label = tk.Label(self.master, text="Time: 0:00", font=('Arial', '12'))
        self.timer_label.grid(row=4, columnspan=3, padx=5, pady=5)

        solve_button = tk.Button(self.master, text="Solve", command=self.solve)
        solve_button.grid(row=5, columnspan=3, padx=5, pady=5)
    #moves counter
    def update_moves(self):
        self.moves += 1
        self.moves_label.config(text=f"Moves: {self.moves}")
     #timer
    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            self.timer_label.config(text=f"Time: {minutes}:{seconds:02}")
            self.master.after(1000, self.update_timer)
    #start timer
    def start_timer(self):
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()
    # stop timer
    def stop_timer(self):
        self.timer_running = False
    #start timer with movement
    def move_tile(self, i, j):
        if not self.timer_running:
            self.start_timer()

        zero_row, zero_col = self.find_zero()

        if (i == zero_row and abs(j - zero_col) == 1) or (j == zero_col and abs(i - zero_row) == 1):
            # Convert (i, j) coordinates to index
            current_index = i * 3 + j
            zero_index = zero_row * 3 + zero_col

            # Swap the positions of the current tile and the zero tile in the string
            board_list = list(self.board)
            board_list[current_index], board_list[zero_index] = board_list[zero_index], board_list[current_index]
            self.board = ''.join(board_list)

            self.display_board()
            self.update_moves()
            #checking solving and stoping
            if self.is_solved():

                self.stop_timer()
                self.show_solution()
                


    #finding zero position
    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.board[i*3 + j] == '0':
                    return i, j
        return -1, -1  # Return -1, -1 if zero tile is not found

    #displaying the configuration
    def display_board(self):
        for i in range(3):
            for j in range(3):
                num = self.board[3*i + j]
                text = str(num) if num != '0' else ""
                self.tiles[i*3 + j].config(text=text)
    #checking target
    def is_solved(self):
     return self.board == '123456780'
    #solving function 
    def solve(self):
        #setting the two conditions
        if self.board!="123456780":
            startState = BoardState(self.board)
            targetState = self.boardState
            #calling search
            solver = Search()
            solver.Run(startState, targetState)
            #checking possibility of a path and graph strategy
            if solver.pathExists:
                #getting the path,steps and displaying
                moves_required = solver.depth[targetState]
                path=solver.GetPathToSolvedState(startState,targetState)
                message=""
                for i in range(len(path)):
                    mat=[]
                    matrow=[]
                    stri=path[i].board
                    for j in range(len(stri)):
                        if stri[j]=='0':
                            matrow+=["  "]
                        else:
                            matrow+=[stri[j]]
                        if (j==2) | (j==5) | (j==8):
                            mat+=[matrow]
                            matrow=[]                   
                    message+=concatenate_matrix(mat)+"\n"
                message+=f"Found the solution in {moves_required} moves!"
                messagebox.showinfo("Solution",message)
            
                    
              #incase of no solution      
            else:
                messagebox.showinfo("Solution", "No solution found!")
        else:
            #2nd condition for solving
            currboard=BoardState(self.alwaysboard)
            targetState=self.boardState
        
            solver = Search()
            solver.Run(currboard, targetState)
            
            #checking possibility of a path and graph strategy
            if solver.pathExists:
                #getting the path,steps and displaying
                moves_required = solver.depth[targetState]
                path=solver.GetPathToSolvedState(currboard,targetState)
                message=""
                for i in range(len(path)):
                    mat=[]
                    matrow=[]
                    stri=path[i].board
                    for j in range(len(stri)):
                        if stri[j]=='0':
                            matrow+=["  "]
                        else:
                            matrow+=[stri[j]]
                        if (j==2) | (j==5) | (j==8):
                            mat+=[matrow]
                            matrow=[]                   
                    message+=concatenate_matrix(mat)+"\n"
                message+=f"Found the solution in {moves_required} moves!"
                messagebox.showinfo("Solution",message)

            else:
                messagebox.showinfo("Solution", "No solution found!")

    

   #winning confirmation
    def show_solution(self):
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        messagebox.showinfo("Congratulations!", f"You solved the puzzle in {self.moves} moves and {minutes} minutes {seconds} seconds!")
#function to print the solution effectively
def pretty_print_matrix(matrix):
        return '\n'.join([' '.join(map(str, row)) for row in matrix])
#function to print the solution effectively
def concatenate_matrix(matrix):
        pretty_matrix = pretty_print_matrix(matrix)
        return f"{pretty_matrix}\n\n"
#calling the main function
def main():
    root = tk.Tk()
    game = SlidingPuzzleGame(root)
    root.mainloop()
#main function defined
if __name__ == "__main__":
    main()
