import tkinter as tk

class Gui:
    """Create a GUI window"""
    def __init__(self):
        self._window = tk.Tk()
        self._window.title("FISA")
        self._window.resizable(False, False)

        self._header_frame = tk.Frame(self._window)
        self._options_frame = tk.Frame(self._window)
        self._output_frame = tk.Frame(self._window)

        # Variables
        self._surveillance = tk.BooleanVar()
        self._us_device = tk.BooleanVar()
        self._wire = tk.BooleanVar()
        self._radio = tk.BooleanVar()
        self._monitor = tk.BooleanVar()
        self._us_person = tk.BooleanVar()
        self._target = tk.BooleanVar()
        self._consent = tk.BooleanVar()
        self._sent_loc_us = tk.BooleanVar()
        self._rec_loc_us = tk.BooleanVar()
        self._int_rec_loc_us = tk.BooleanVar()
        self._acquire = tk.BooleanVar()
        self._acq_loc_us = tk.BooleanVar()
        self._intention = tk.BooleanVar()
        self._is_perm = tk.BooleanVar()
        self._REP_LE = tk.BooleanVar()

        # Header frame
        tk.Label(self._header_frame, text="FISA", font=("Times New Roman", 25)).grid(row=1, column=1)

        # Options frame
        tk.Label(self._options_frame, text="Device").grid(row=1, column=1)
        tk.Label(self._options_frame, text="Electronic, mechanical, or other surveillance device?").grid(row=2, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._surveillance).grid(row=2, column=2)
        tk.Label(self._options_frame, text="Device in the US?").grid(row=3, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._us_device).grid(row=3, column=2)
        tk.Label(self._options_frame, text="Wire communication?").grid(row=4, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._wire).grid(row=4, column=2)
        tk.Label(self._options_frame, text="Radio communication?").grid(row=5, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._radio).grid(row=5, column=2)
        tk.Label(self._options_frame, text="Installation or use of device for monitoring?").grid(row=6, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._monitor).grid(row=6, column=2)

        tk.Label(self._options_frame, text="Person").grid(row=10, column=1, pady=(10,0))
        tk.Label(self._options_frame, text="US person?").grid(row=11, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._us_person).grid(row=11, column=2)
        tk.Label(self._options_frame, text="Is person a target?").grid(row=12, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._target).grid(row=12, column=2)
        tk.Label(self._options_frame, text="Did party give consent?").grid(row=13, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._consent).grid(row=13, column=2)

        tk.Label(self._options_frame, text="Location").grid(row=20, column=1, pady=(10,0))
        tk.Label(self._options_frame, text="Sending location in the US?").grid(row=21, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._sent_loc_us).grid(row=21, column=2)
        tk.Label(self._options_frame, text="Receiving location in the US?").grid(row=22, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._rec_loc_us).grid(row=22, column=2)
        tk.Label(self._options_frame, text="All intended recipients located in the US?").grid(row=23, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._int_rec_loc_us).grid(row=23, column=2)

        tk.Label(self._options_frame, text="Acquisition").grid(row=30, column=1, pady=(10,0))
        tk.Label(self._options_frame, text="Was content acquired?").grid(row=31, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._acquire).grid(row=31, column=2)
        tk.Label(self._options_frame, text="Acquisition in US?").grid(row=32, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._acq_loc_us).grid(row=32, column=2)
        tk.Label(self._options_frame, text="Intentional acquisition?").grid(row=33, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._intention).grid(row=33, column=2)
        tk.Label(self._options_frame, text="Acquisition permissible under section 2511(2)(i) of title 18?").grid(row=34, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._is_perm).grid(row=34, column=2)

        tk.Label(self._options_frame, text="Circumstances").grid(row=40, column=1, pady=(10,0))
        tk.Label(self._options_frame, text="Reasonable expectation of privacy and warrant required for law enforcement?").grid(row=41, column=1, sticky="w")
        tk.Checkbutton(self._options_frame, variable=self._REP_LE).grid(row=41, column=2)

        tk.Button(self._options_frame, text="Submit", command=self._run_z3).grid(row=50, column=1, columnspan=2, pady=(10,0))

        # Output frame
        tk.Button(self._output_frame, text="Output").grid(row=1, column=1)

        self._header_frame.grid(row=1, column=1, columnspan=2, padx=50, pady=(50,0))
        self._options_frame.grid(row=2, column=1, padx=(50,20), pady=(10,50))
        self._output_frame.grid(row=2, column=2, padx=(20,50), pady=(10,50))

        self._window.mainloop()

    def _run_z3(self):
        # Put solver here

if __name__ == "__main__":
    Gui()
