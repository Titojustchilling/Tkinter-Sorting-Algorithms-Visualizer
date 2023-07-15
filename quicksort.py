import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1    
def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        yield from quicksort(array, low, pi - 1)
        yield from quicksort(array, pi + 1, high)
    yield array 
# Function for letting user choose the number of a-axis in the array
def collect_input():
    root = tk.Tk()
    root.configure(bg='black') 
    def submit():
        try:
            global array_size
            array_size = int(array_entry.get())
            # if number is less than 10
            if array_size < 10:
                array_entry.delete(0, tk.END)  # Clear the entire content
                print("Invalid array size. Please enter a value greater than or equal to 10.")
            else:
                quicksort_visualize()
        # if user enters a string
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    array_label = tk.Label(root, text="Size of Array (Must be at least 10): ", bg='black', fg='white') 
    array_label.pack()
    array_entry = tk.Entry(root, fg='white', bg='black')
    array_entry.pack()
    submit_button = tk.Button(root, text="Submit", command=submit, bg='black', fg='white')
    submit_button.pack()

def quicksort_visualize(): 
    quickSortScreen = tk.Tk(className=' Quicksort Visualizer')
    fig = Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=quickSortScreen)
    canvas.get_tk_widget().pack()
    ax = fig.add_subplot(111)
    N = array_size 
    array = list(range(1, N + 1))
    random.shuffle(array)
    
    # Sorting contains the arrays of the sorting algorithm the user chose
    sorting = quicksort(array, 0, N-1)
    ax.set_title("Quicksort")
    bar_sub = ax.bar(range(len(array)), array, align="edge", color='green')
    ax.set_facecolor('black')
    
    # setting X-ais
    ax.set_xlim(0, N)
 
    
    # Updates each frame of animation
    def update(array, rects):
       for rect, val in zip(rects, array):
            rect.set_height(val)
    # Renders iteration
    anim = animation.FuncAnimation(fig,func=update,fargs=(bar_sub,),frames=sorting,repeat=True,blit=False,interval=15,save_count=90000,)
    # Showcasing animation on screen
    plt.show()
    plt.close()
    quickSortScreen.mainloop() 
    
    
# Program redirects to this function
def create_quicksort_visualization(): 
    collect_input()