# Patrick Roscio
# Lab_11/smootconverter.py
# Description: Developes a GUI using tkinter that converts between smoots and meters. 
#  Also provides a short description of smoots and their history. 

import tkinter 
import tkinter.messagebox as messagebox


class SmootGUI:
    def __init__(self): 
        self.__main_window = tkinter.Tk()
        self.__main_window.title("Smoot Converter")
        self.__main_window.geometry("800x600")
        self.__smootInfo = """  The smoot /\'smu:t/ is a nonstandard, humorous unit of length created as
part of an MIT fraternity prank. It is named after Oliver R. Smoot, a
fraternity pledge to Lambda Chi Alpha, who in October 1958 lay down
repeatedly on the Harvard Bridge (between Boston and Cambridge,
Massachusetts) so that his fraternity brothers could use his height to
measure the length of the bridge.
    One smoot is equal to Oliver Smoot\'s height at the time of the prank, 5
feet 7 inches (1.70 m). The bridge\'s length was measured to be 364.4
smoots (2,035 ft; 620.1 m) \"+/- 1 εar\" with the \"+/-\" showing
measurement uncertainty and spelled with an epsilon to further indicate
possible error in the measurement. Over the years the \"+/-\" portion and
\"ε\" spelling have gone astray in many citations, including some markings
at the site itself, but the \"+/-\" is recorded on a 50th-anniversary plaque
at the bridge\'s end."""
        self.__smootTextArea = tkinter.Text(self.__main_window,wrap=tkinter.WORD)
        self.__smootTextArea.insert(tkinter.END, self.__smootInfo)
        self.__smootTextArea.configure(state=tkinter.DISABLED)
        self.__inputFrame = tkinter.Frame(self.__main_window)
        self.__buttonFrame = tkinter.Frame(self.__main_window)
        self.__smootField = tkinter.Entry(self.__inputFrame, width=10)
        self.__smootLabel = tkinter.Label(self.__inputFrame, text = "Smoots")
        self.__meterField = tkinter.Entry(self.__inputFrame, width= 10)
        self.__meterLabel = tkinter.Label(self.__inputFrame, text = "Meters")
        self.__smootMeterButton = tkinter.Button(self.__buttonFrame, text = "Smoot-to-Meter", command = self.getSmoots)
        self.__meterSmootButton = tkinter.Button(self.__buttonFrame, text = "Meter-to-Smoot", command = self.getMeters)
        self.__quitButton = tkinter.Button(self.__buttonFrame, text = "Quit", command= self.__main_window.destroy)
        self.__smootField.pack(side = tkinter.LEFT)
        self.__smootLabel.pack(side = tkinter.LEFT)
        self.__meterField.pack(side = tkinter.LEFT)
        self.__meterLabel.pack(side = tkinter.LEFT)
        self.__smootMeterButton.pack(side=tkinter.LEFT, padx=50)
        self.__meterSmootButton.pack(side=tkinter.LEFT, padx=50)
        self.__quitButton.pack(side=tkinter.LEFT, padx=50)
        self.__smootTextArea.pack(side=tkinter.TOP)
        self.__inputFrame.pack(side=tkinter.TOP)
        self.__buttonFrame.pack(side=tkinter.TOP)

    def getSmoots(self):
        smoots = self.__smootField.get()
        try:
            smoots = float(smoots)
        except:
            messagebox.showerror(title = "Bad Value!", message = "Value is not a valid distance" )
            return 0
        value = str("{:.2f}".format(smoots*0.178))
        self.__meterField.delete(0,tkinter.END)
        self.__meterField.insert(0,value)

    def getMeters(self):
        meters = self.__meterField.get()
        try:
            meters = float(meters)
        except:
            messagebox.showerror(title = "Bad Value!", message = "Value is not a valid distance" )
            return 0
        value = str("{:.2f}".format(meters/0.178))
        self.__smootField.delete(0,tkinter.END)
        self.__smootField.insert(0,value)

    def run(self):
        self.__main_window.mainloop()

def main():
    self = SmootGUI()
    self.run()
main()