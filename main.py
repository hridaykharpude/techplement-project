import tkinter as tk
from tkinter import ttk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configure the main window
        self.title("Multi-Page Application")
        self.geometry("400x300")
        
        # Container to hold different frames
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        
        # Dictionary to hold frames
        self.frames = {}
        
        # Create and add frames to the dictionary
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show the start page initially
        self.show_frame(StartPage)
    
    def show_frame(self, page):
        """Show a frame for the given page class"""
        frame = self.frames[page]
        frame.tkraise()  # Raise the selected frame to the front

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)
        
        # Button to navigate to PageOne
        button1 = ttk.Button(self, text="Go to Page One",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="Page One")
        label.pack(pady=10, padx=10)
        
        # Button to navigate to StartPage
        button1 = ttk.Button(self, text="Go to Start Page",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        # Button to navigate to PageTwo
        button2 = ttk.Button(self, text="Go to Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="Page Two")
        label.pack(pady=10, padx=10)
        
        # Button to navigate to StartPage
        button1 = ttk.Button(self, text="Go to Start Page",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

# Create the application instance
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
