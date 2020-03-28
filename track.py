import tkinter as Tk
import requests
from bs4 import BeautifulSoup


window = Tk.Tk()
window.title("Covid 19")
window.geometry("900x300")
window.resizable(False,False)
window.config(bg = "blue")

Cases = Tk.Label(text = "Cases: ",bg = "orange",width = 40)
Cases.config(font = ("Courier",20))
Cases.place(x = 100,y = 50)

Deaths = Tk.Label(text = "Deaths: ",bg = "red",width = 40)
Deaths.config(font = ("Courier",20))
Deaths.place(x = 100,y = 90)

Recoveries = Tk.Label(text = "Recoveries: ",bg = "green",width = 40)
Recoveries.config(font = ("Courier",20))
Recoveries.place(x = 100,y = 130)



def Update():
    response = requests.get("https://www.worldometers.info/coronavirus/")
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    currentCases = soup.find_all(class_="number-table-main")
    closedCases = soup.find_all(class_="number-table")
    activeCases = currentCases[0].text.strip()
    recoveredCases = closedCases[2].text.strip()
    deaths = closedCases[3].text.strip()
    Cases.config(text = f"Current cases: {activeCases}")
    Recoveries.config(text = f"Recoveries: {recoveredCases}")
    Deaths.config(text=f"Deaths: {deaths}")

refreshButton = Tk.Button(text = "Refresh",bg = "yellow",command = Update)
refreshButton.config(font = ("Courier",20))
refreshButton.place(x = 340,y = 170)

window.mainloop()
