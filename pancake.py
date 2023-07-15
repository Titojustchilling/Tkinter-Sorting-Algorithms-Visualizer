import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random

def flip(array, i):
    start = 0
    while start < i:
        temp = array[start]
        array[start] = array[i]
        array[i] = temp
        start += 1
        i -= 1
def findMax(array, n):
    mi = 0
    for i in range(0,n):
        if array[i] > array[mi]:
            mi = i
    return mi
def pancakeSort(array, n):
    curr_size = n
    while curr_size > 1:
        mi = findMax(array, curr_size)
        if mi != curr_size-1:
            flip(array, mi)
            flip(array, curr_size-1)
        curr_size -= 1
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
                pancake_visualize()
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    array_label = tk.Label(root, text="Size of Array (Must be at least 10): ", bg='black', fg='white') 
    array_label.pack()
    array_entry = tk.Entry(root, fg='white', bg='black')
    array_entry.pack()
    submit_button = tk.Button(root, text="Submit", command=submit, bg='black', fg='white')
    submit_button.pack()

def pancake_visualize(): 
    pancake = tk.Tk(className=' Pancake Sort Visualizer')
    fig = Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=pancake)
    canvas.get_tk_widget().pack()
    ax = fig.add_subplot(111)
    N = array_size
    array = list(range(1, N + 1))
    random.shuffle(array)
    sorting = pancakeSort(array, N)
    ax.set_title("Pancake Sort")
    bar_sub = ax.bar(range(len(array)), array, align="edge", color='green')
    ax.set_facecolor('black')
    ax.set_xlim(0, N)    
    def update(array, rects):
       for rect, val in zip(rects, array):
            rect.set_height(val)
    
    anim = animation.FuncAnimation(fig,func=update,fargs=(bar_sub,),frames=sorting,repeat=True,blit=False,interval=15,save_count=90000,)
    plt.show()
    plt.close()
    pancake.mainloop() 



def create_pancake_visualization():
    collect_input() 