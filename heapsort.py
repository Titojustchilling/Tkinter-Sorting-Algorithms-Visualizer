import tkinter as tk 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib .figure import Figure 
import random 



def heapify(array, N, i):
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2     
    if l < N and array[largest] < array[l]:
        largest = l
    if r < N and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, N, largest)
def heapSort(array):
    N = len(array)
    for i in range(N//2 - 1, -1, -1):
        heapify(array, N, i)
    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
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
                heapsort_visualize()
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    array_label = tk.Label(root, text="Size of Array (Must be at least 10): ", bg='black', fg='white') 
    array_label.pack()
    array_entry = tk.Entry(root, fg='white', bg='black')
    array_entry.pack()
    submit_button = tk.Button(root, text="Submit", command=submit, bg='black', fg='white')
    submit_button.pack()
def heapsort_visualize(): 
    heapSortScreen = tk.Tk(className=' Heapsort Visualizer')
    fig = Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=heapSortScreen)
    canvas.get_tk_widget().pack()
    ax = fig.add_subplot(111)
    N = array_size
    array = list(range(1, N + 1))
    random.shuffle(array)
    sorting = heapSort(array)
    ax.set_title("Heapsort")
    bar_sub = ax.bar(range(len(array)), array, align="edge", color='green')
    ax.set_facecolor('black')
    ax.set_xlim(0, N)    
    def update(array, rects):
       for rect, val in zip(rects, array):
            rect.set_height(val)
    anim = animation.FuncAnimation(fig,func=update,fargs=(bar_sub,),frames=sorting,repeat=True,blit=False,interval=15,save_count=90000,)
    plt.show()
    plt.close()
    heapSortScreen.mainloop() 

def create_heapsort_visualization(): 
    collect_input()