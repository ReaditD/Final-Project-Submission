"""
Author, Derek Gerry (812-435-9081)
Date written: 10/11/24
Assignment: SDEV140 Final Project
Short Desc: This Tkinter project is intended to provide an easy access 
to electrical values used in the electrical field. The values are calculations from 
known elelments of a system.  
The image files must be kept in C:/Users/User Name
"""

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class MainWindow(object):
    def __init__(self):
        """ Initiates the MainWindow """
       
        self.window = Tk()
        """Creates the Screen"""

        self.window.geometry("693x400")
        """Sets the Main Window size"""
   
        self.window.title("Electro-Assis")  
        """Adds Title to Tkinter Window"""

        instructions2 = Label(self.window, text="Please use the buttons to select a function", font=('Ariel', 14))
        instructions2.grid(row=0, column=3)
        """Adds Label with instructions"""

        b1 = Button(self.window, text="Click to find Voltage", command=self.open_voltage_window,font=('Ariel', 12))
        b1.grid(row=2, column=3)
        """Creates button #1"""

        b2 = Button(self.window, text="Click to find Resistance", command=self.open_resistance_window,font=('Ariel', 12))
        b2.grid(row=2, column=1)
        """Creates button #2"""
        
        b3 = Button(self.window, text="Click to find Current", command=self.open_current_window, font=('Ariel', 12))
        b3.grid(row=2, column=4)
        """Creates button #3"""

        b4 = Button(self.window, command=self.exit_window, text="Close", font=('Ariel', 12))
        b4.grid(row=3, column=3)
        """Creates button #4"""

        Display_Pictures.main_image(self)
        Display_Pictures.second_image(self)
        """Opens pictures"""

        self.window.mainloop()
        """Starts the Tkinter Main"""

    def exit_window(self):
        """Quits the application."""
        self.window.quit()

    def open_current_window(self):
        """Initiates SecondWindow Process"""
        CurrentWindow(self.window)
    
    def open_voltage_window(self):
        """Initiates Voltage window"""
        VoltageWindow(self.window)
    
    def open_resistance_window(self):
        """Initiates Resistance window"""
        ResistanceWindow(self.window)



class Display_Pictures(object):
    """Displays Pictures in the Main Window"""
    def __init__(self, window):
        self.window = window
        str(window) # might be helpful later

    def main_image(self):
        """Opens and displays image"""
        circuit = Image.open("DC_Circuit.PNG")#("path/to/your/image.jpg")

        circuit = circuit.resize((200,120))
        """Re-sizes the image"""

        self.dc_photo = ImageTk.PhotoImage(circuit)
        """prevents Garbage collector from closing the image"""

        circuit_picture = Label(self.window, text="Below: an example of a DC Circuit")
        circuit_picture.grid(row=6, column=3)
        circuit_picture = Label(self.window, image=self.dc_photo)
        circuit_picture.grid(row=7, column=3)
        """Places the image and text in the correct spot"""

    def second_image(self):
        """Opens and displays second image"""
        ac_circuit = Image.open("AC_Circuit.PNG")
        ac_circuit = ac_circuit.resize((200,120))
        """Resizes the image"""

        self.ac_photo = ImageTk.PhotoImage(ac_circuit)
        """prevents Garbage collector from closing the image"""

        ac_circuit = Label(self.window, text="Below: an example of an AC Circuit")
        ac_circuit.grid(row=8,column=3)
        ac_circuit = Label(self.window,image=self.ac_photo)
        ac_circuit.grid(row=9, column=3)
        """Places the image and text in the correct spot"""
#777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
class ResistanceWindow(object):
    """Creates window for and calculations for Resistance"""
    def __init__(self, master):
        """Creates a new window (Toplevel)"""
        self.resistance_window = Toplevel(master)
        self.resistance_window.title("Find Resistance") 
        self.resistance_window.geometry("600x450")

        Label(self.resistance_window, text="Enter the Current and Voltage values", 
            font=('Ariel', 12), wraplength=250).pack(pady=20)
        """Labels 'Resistance', window"""
    
        Label(self.resistance_window, text="Current in Amps:").pack(pady=5)
        """Create Current label"""
        self.current_entry = Entry(self.resistance_window, width=30)
        self.current_entry.pack(pady=5)
        #***************************
        self.current_entry.insert(0, "I")
        #***************************

        Label(self.resistance_window, text="Voltage in Volts:").pack(pady=5)
        """Create Voltage Label"""
        self.voltage_entry = Entry(self.resistance_window, width=30)
        self.voltage_entry.pack(pady=5)
        #***************************
        self.voltage_entry.insert(0, "E")
        #***************************

        calc_button = Button(self.resistance_window, text="Calculate resistance", command=self.calculate_resistance)
        calc_button.pack(pady=10)
        """Adds button to run the calculate method"""

        self.result_label = Label(self.resistance_window, text="", font=('Ariel', 12))
        self.result_label.pack(pady=10)
        """Creates the results label"""

        Button(self.resistance_window, text="Clear Entries", command=self.clear_entries).pack(pady=10)
        """creates the Clear Entires, button"""

        Button(self.resistance_window, text="Close", command=self.resistance_window.destroy).pack(pady=10)
        """Closes the 'Current', window"""

    def calculate_resistance(self):
        """Calculate the Voltage using Current and Resistance values"""
        try:
            current = float(self.current_entry.get())
            voltage = float(self.voltage_entry.get())
            if current <= 0 or voltage <= 0:
                self.result_label.config(text=" Values cannot be equal to or less than zero!")
            else:
                resistance = voltage / current   # Ohm's Law: R = E/I
                self.result_label.config(text=f"Resistance: {resistance:.2f} Ohms")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter numbers.")
        """Gets User input data and ensures it is acceptable then perform the calculations"""

    def clear_entries(self):
        """Clear the input fields and result label"""
        self.current_entry.delete(0, END)
        self.voltage_entry.delete(0, END)
        self.result_label.config(text="")

#777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
class VoltageWindow(object):
    """Creates window for and calculations for Voltage"""
    def __init__(self, master):
        """Creates a new window (Toplevel)"""
        self.voltage_window = Toplevel(master)
        self.voltage_window.title("Find Voltage") 
        self.voltage_window.geometry("600x450")

        Label(self.voltage_window, text="Enter the Current and Resistance values", 
            font=('Ariel', 12), wraplength=250).pack(pady=20)
        """Labels 'Voltage', window"""
    
        Label(self.voltage_window, text="Current in Amps:").pack(pady=5)
        """Create Current label"""
        self.current_entry = Entry(self.voltage_window, width=30)
        self.current_entry.pack(pady=5)
        #***************************
        self.current_entry.insert(0,"I")
        #***************************

        Label(self.voltage_window, text="Resistance in Ohms:").pack(pady=5)
        """Create Resistance Label"""
        self.resistance_entry = Entry(self.voltage_window, width=30)
        self.resistance_entry.pack(pady=5)
        #***************************
        self.resistance_entry.insert(0, "R")
        #***************************

        calc_button = Button(self.voltage_window, text="Calculate Voltage", command=self.calculate_voltage)
        calc_button.pack(pady=10)
        """Adds button to run the calculate method"""

        self.result_label = Label(self.voltage_window, text="", font=('Ariel', 12))
        self.result_label.pack(pady=10)
        """Creates the results label"""

        Button(self.voltage_window, text="Clear Entries", command=self.clear_entries).pack(pady=10)
        """creates the Clear Entires, button"""

        Button(self.voltage_window, text="Close", command=self.voltage_window.destroy).pack(pady=10)
        """Closes the 'Current', window"""

    def calculate_voltage(self):
        """Calculate the Voltage using Current and Resistance values"""
        try:
            current = float(self.current_entry.get())
            resistance = float(self.resistance_entry.get())
            if resistance <= 0 or current <= 0:
                self.result_label.config(text=" Values cannot be equal to or less than zero!")
            else:
                voltage = current * resistance  # Ohm's Law: I = E / R
                self.result_label.config(text=f"Volts: {voltage:.2f} Volts")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter numbers.")
        """Gets User input data and ensures it is acceptable then perform the calculations"""

    def clear_entries(self):
        """Clear the input fields and result label"""
        self.current_entry.delete(0, END)
        self.resistance_entry.delete(0, END)
        self.result_label.config(text="")
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
class CurrentWindow(object):
    """Current/Amps: Creates the window for and calculations for Current"""
    def __init__(self, master):
        """Creates a new window (Toplevel)"""
        self.current_window = Toplevel(master)  
        self.current_window.title("Find Current")
        self.current_window.geometry("600x450")
        
        Label(self.current_window, text="Enter the Voltage and Resistance values", 
              font=('Ariel', 12), wraplength=250).pack(pady=20)
        """Labels 'Current', window"""

        Label(self.current_window, text="Voltage:").pack(pady=5)
        """Create Voltage label"""
        self.voltage_entry = Entry(self.current_window, width=30)
        self.voltage_entry.pack(pady=5)
        #***************************
        self.voltage_entry.insert(0, "E")
        #***************************

        Label(self.current_window, text="Resistance in ohms:").pack(pady=5)
        """Create Resistance Label"""
        self.resistance_entry = Entry(self.current_window, width=30)
        self.resistance_entry.pack(pady=5)
        #***************************
        self.resistance_entry.insert(0, "R")
        #***************************

        calculate_button = Button(self.current_window, text="Calculate Current", command=self.calculate_current)
        calculate_button.pack(pady=10)
        """Adds button to run the calculate method"""

        self.result_label = Label(self.current_window, text="", font=('Ariel', 12))
        self.result_label.pack(pady=10)
        """Creates label to display the result"""

        Button(self.current_window, text="Clear Entires", command=self.clear_Results).pack(pady=10)
        """creates the Clear Entires, button"""

        Button(self.current_window, text="Close", command=self.current_window.destroy).pack(pady=10)
        """Closes the 'Current', window"""

    def calculate_current(self):
        """Calculate the current using Voltage and Resistance values"""
        try:
            voltage = float(self.voltage_entry.get())
            resistance = float(self.resistance_entry.get())
            if resistance <= 0 or voltage <= 0:
                self.result_label.config(text=" Values cannot be equal to or less than zero!")
            else:
                current = voltage / resistance  # Ohm's Law: I = E / R
                self.result_label.config(text=f"Current: {current:.2f} Amps")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter numbers.")
        """Gets User input data and ensures it is acceptable then perform the calculations"""
                             
    def clear_Results(self):
        """Clears the entered readings for another submission"""
        self.voltage_entry.delete(0,END)
        self.resistance_entry.delete(0,END)
        self.result_label.config(text="")
#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111   
  
if __name__ == "__main__":
    MainWindow() 
