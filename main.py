import tkinter
from tkinter import * 
from bubbles import create_bubble_visualization
from selection import create_selection_visualization
from insertion import create_insertion_visualization
from quicksort import create_quicksort_visualization
from pancake import create_pancake_visualization
from heapsort import create_heapsort_visualization
from shellsort import create_shellsort_visualization

def startScreen(): 
    home = Tk(className=' Sorting Algorithmn Visualizer')
    home.configure(bg='black')
    heading=Label(home, text="Tkinter's Sorting Algorithm Visualizer", fg='white', bg='black', font=("Helvetica", 16))
    heading.grid(row=1, column=3)
    bubble_button = Button(home, text=" Bubble Sort Visualizer", fg='white', command=create_bubble_visualization, width=25, bg='black')
    bubble_button.grid(row=2, column=2)
    selection_button = Button(home, text=" Selection Sort Visualizer", fg='white', command=create_selection_visualization, width=25, bg='black')
    selection_button.grid(row=2, column=3) 
    insertion_button = Button(home, text=" Insertion Sort Visualizer", fg='white', command=create_insertion_visualization, width=25, bg='black')
    insertion_button.grid(row=2, column=4)
    quicksort_button = Button(home, text=" Quicksort Visualizer", fg='white', command=create_quicksort_visualization, width=25, bg='black') 
    quicksort_button.grid(row=2, column=5) 
    pancake_button = Button(home, text="Pancake Visualizer", fg='white', command=create_pancake_visualization, width=25, bg='black')
    pancake_button.grid(row=3, column=3) 
    heapsort_button = Button(home, text=" Heapsort Visualizer", fg='white', command=create_heapsort_visualization, width=25, bg='black')
    heapsort_button.grid(row=3, column=2)
    shellsort_button = Button(home, text='Shellsort Visualizer', fg='white', command=create_shellsort_visualization, width=25, bg='black')
    shellsort_button.grid(row=3, column=4) 
    home.mainloop()

if __name__ == "__main__":
    startScreen()
