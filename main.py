import tkinter as tk

class Gui:
    """Create a GUI window"""
    def __init__(self):
        self._window = tk.Tk()
        self._window.title("FISA")
        self._window.geometry("800x500")
        self._window.resizable(False, False)

        self._options_frame = tk.Frame(self._window)
        self._output_frame = tk.Frame(self._window)

        tk.Button(self._options_frame, text="Button 1").grid(row=1, column=1)

        self._options_frame.grid(row=1, column=1)

        self._window.mainloop()

if __name__ == "__main__":
    Gui()
