import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
  
def bubblesort(array):
    swapped = True

    for i in range(len(array) - 1):
        if not swapped:
            return
        swapped = False

        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
                swapped = True
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
                visualize()
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    array_label = tk.Label(root, text="Size of Array (Must be at least 10): ", bg='black', fg='white') 
    array_label.pack()
    array_entry = tk.Entry(root, fg='white', bg='black')
    array_entry.pack()
    submit_button = tk.Button(root, text="Submit", command=submit, bg='black', fg='white')
    submit_button.pack()
    
    
    
def visualize():
    bubble = tk.Tk(className=' Bubble Sort Visualizer')
    fig = Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=bubble)
    canvas.get_tk_widget().pack()
    ax = fig.add_subplot(111)
    N = array_size
    array = list(range(1, N + 1))
    random.shuffle(array)
    sorting = bubblesort(array)
    ax.set_title("Bubble Sort")
    bar_sub = ax.bar(range(len(array)), array, align="edge", color='green')
    ax.set_facecolor('black')
    ax.set_xlim(0, N)

    def update(array, rects):
        for rect, val in zip(rects, array):
            rect.set_height(val)

    anim = animation.FuncAnimation(fig,func=update,fargs=(bar_sub,),frames=sorting,repeat=True,blit=False,interval=100,save_count=90000,)
    plt.show() 
    plt.close()
    bubble.mainloop()


def create_bubble_visualization():
    collect_input()
   


