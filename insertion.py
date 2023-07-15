import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random

def insertionSort(array): 
    
    for i in range(1, len(array)): 
        key = array[i] 

        j = i-1
        while j >= 0 and key < array[j]: 
            array[j + 1] = array[j] 
            j -= 1
        array[j + 1] = key
        yield array 
        
def collect_input():
    root = tk.Tk()
    root.configure(bg='black') 
    def submit():
        try:
            global array_size
            array_size = int(array_entry.get())
            if array_size < 10:
                array_entry.delete(0, tk.END)
                print("Invalid array size. Please enter a value greater than or equal to 10.")
            else:
                root.destroy()
                insertion_visualize()
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    array_label = tk.Label(root, text="Size of Array (Must be at least 10): ", bg='black', fg='white') 
    array_label.pack()
    array_entry = tk.Entry(root, fg='white', bg='black')
    array_entry.pack()
    submit_button = tk.Button(root, text="Submit", command=submit, bg='black', fg='white')
    submit_button.pack()


def insertion_visualize(): 
    insertion = tk.Tk(className=' Insertion Sort Visualizer')
    fig = Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=insertion)
    canvas.get_tk_widget().pack()
    ax = fig.add_subplot(111)
    N = array_size
    array = list(range(1, N + 1))
    random.shuffle(array)
    sorting = insertionSort(array)
    ax.set_title("Insertion Sort")
    bar_sub = ax.bar(range(len(array)), array, align="edge", color='green')
    ax.set_facecolor('black')
    ax.set_xlim(0, N)
    
    def update(array, rects):
       for rect, val in zip(rects, array):
            rect.set_height(val)
    
    anim = animation.FuncAnimation(fig,func=update,fargs=(bar_sub,),frames=sorting,repeat=True,blit=False,interval=15,save_count=90000,)
    plt.show()
    plt.close()
    insertion.mainloop() 



def create_insertion_visualization():
    collect_input() 