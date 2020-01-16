import tkinter as tk

from Dcard import SexIMG

def Scrap():

    SI = SexIMG()

    titles,urls = SI.Get_Artitles_URL("https://www.dcard.tw")
    SI.Scrap_Images(titles,urls)


root=tk.Tk()

root.title("D卡 西斯圖")

root.geometry("400x200")

frame = tk.Frame(root)
frame.pack()

middle_frame = tk.Frame(root)
middle_frame.pack()

La=tk.Label(frame,text='按下去就對了',font=('Aprial',20),fg='purple')
La.pack(side=tk.TOP)
#command=lambda:SI.Scrap_Images(titles,urls) 
Scrap=tk.Button(root,text='爬蟲',bg='darkred',fg='gold',height=2,width=6,command=Scrap)
Scrap.pack(side=tk.BOTTOM)
root.mainloop()