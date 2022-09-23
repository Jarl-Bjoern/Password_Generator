# R. C. Bjoern Herold
# Anfangsdatum 12.05.2021
# Version 0.1

# Bibliotheken_Implementierung
import os, random, time, threading, win32api, win32con, win32console, win32gui, win32clipboard
import multiprocessing as mp
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

# Globaler_Variablen_Bereich
Anzahl_Prozessoren = mp.cpu_count()
ID_CMD = win32console.GetConsoleWindow()
Passwort = ""
Programm_Beenden = 0

# Funktions_Bereich
def Programm_Schliessen():
	global Programm_Beenden

	Programm_Beenden = 1
	win32gui.PostMessage(ID_CMD, win32con.WM_CLOSE, 0, 0)

def Passwort_Generator():
	global Passwort

	Passwort = ""

	while (len(Passwort) != 32):
		Zufall = random.randint(33,124)
		Passwort += str(chr(Zufall))

def GUI():
	# GUI_Position_Ermitteln
	Bild_X = win32api.GetSystemMetrics(0)
	Bild_Y = win32api.GetSystemMetrics(1)
	Position_X = int((Bild_X - 800) / 2)
	Position_Y = int((Bild_Y - 600) / 2)

	# WIN_CMD_Entfernen
	win32gui.ShowWindow(ID_CMD, win32con.SW_HIDE)

	# Main_Bereich
	mainWindow = tk.Tk(className=' M U L T I F U N K T I O N S - T O O L (Vorab nur Passwort-Generator)')
	mainWindow.geometry('800x320+'+str(Position_X)+'+'+str(Position_Y))
	mainWindow.configure(bg='DimGray')

	# TTK_Design
	Design = ttk.Style()
	Design.theme_use('clam')
	Design.configure('btn.TButton', font=('Arial', 13), background='Black', foreground='Turquoise', borderwidth=1, bordercolor='Black')
	Design.configure('bdm.TLabel', font=('Arial', 13), background='DimGray', foreground='White', borderwidth=1, bordercolor='Black')
	Design.map('btn.TButton', background=[('active', 'Black')], foreground=[('active', 'LightBlue')])

	# Frames_Erzeugen
	Frame_Elemente = tk.Frame(mainWindow, bg='DimGray')
	Frame_Elemente.place(relx=0.0255, rely=0.05)

	# Elemente
	lb_Head = tk.Listbox(Frame_Elemente, height=1, width=84, selectbackground='Black', selectforeground='Yellow', activestyle='none', justify='center', bg='Black', fg='Yellow', font=('Arial', 13))
	lb_Head.grid(row=0, column=0)
	lb_Passwort_Ausgabe = tk.Listbox(Frame_Elemente, height=5, width=84, justify='center', bg='Black', fg='Yellow', selectbackground='Black', selectforeground='Green', activestyle='none', font=('Arial', 13))
	lb_Passwort_Ausgabe.grid(row=1, column=0)

	lb_Head.insert(0, 'P A S S W O R T - G E N E R A T O R')

	# Funktions_Bereich
	def Passwort_Einfuegen():
		Passwort_Generator()
		if (len(Passwort) == 32):
			lb_Passwort_Ausgabe.insert(0, ' ')
			lb_Passwort_Ausgabe.insert(1, ' ')
			lb_Passwort_Ausgabe.insert(2, str(Passwort))

	def btn_Passwort_Neugenerieren():
		lb_Passwort_Ausgabe.delete(0, tk.END)
		Passwort_Einfuegen()

	def btn_Kopieren():
		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardText(Passwort)
		win32clipboard.CloseClipboard()
		messagebox.showinfo("Kopiervorgang", "Das Passwort wurde erfolgreich in die Zwischenablage kopiert.")

	# Steuer_Elemente
	btn_Neugenerieren = ttk.Button(mainWindow, text='Neues Passwort', command=btn_Passwort_Neugenerieren, style='btn.TButton')
	btn_Neugenerieren.place(relx=0.15, rely=0.67)
	btn_Kopieren = ttk.Button(mainWindow, text='Zwischenablage', command=btn_Kopieren, style='btn.TButton')
	btn_Kopieren.place(relx=0.65, rely=0.67)

	# Initialien_Bereich
	L_Versionsnr = ttk.Label(mainWindow, text='Version 0.1', style='bdm.TLabel')
	L_Versionsnr.place(relx=0.025, rely=0.91)
	L_Entwickler = ttk.Label(mainWindow, text='Bjoern Herold', style='bdm.TLabel')
	L_Entwickler.place(relx=0.845, rely=0.91)

	# Erster_Aufruf
	Passwort_Einfuegen()

	mainWindow.protocol("WM_DELETE_WINDOW", Programm_Schliessen)
	mainWindow.mainloop()

# Aufruf_Bereich
if __name__ == '__main__':
	GUI()