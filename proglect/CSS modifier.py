import os.path,os,math
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *
import matplotlib.pyplot as plt
import numpy as np
#fond d'écran


#recupération des anciennes couleurs
lect=open("cssrcp.txt","r",encoding="utf-8")
noms = lect.read() + "₾"
lect.close()
tab = tuple()
i, j = 0, 0
st = ""
while noms[i] != "₾":
    while noms[i] != "\n" and noms[i] != "₾":
        st += noms[i]
        i += 1

    tab = tab + (st,)
    st = ""
    i += 1




#choix des couleurs

root = Tk()
root.title('Tkinter Color Chooser')

##----------------couleur du bouton  bt
bt=tab[2]
canvas = Canvas(root, width=15, height=15, background=bt)
canvas.grid(row=2,column=0,padx=5,pady=5)
def change_color_button():
      global bt
      colors = askcolor(title="Tkinter Color Chooser")
      bt=colors[1]
      canvas = Canvas(root, width=15, height=15, background=bt)
      canvas.grid(row=2,column=0,padx=5,pady=5)
buton=Button(
    root,
    text='choisis une couleur pour le bouton',
    command=change_color_button).grid(row=1,column=0,padx=5,pady=5)
##----------------couleur du texte   color_text
color_text=tab[0]
canvas = Canvas(root, width=15, height=15, background=color_text)
canvas.grid(row=2,column=1,padx=5,pady=5)
def change_color_text():
      global color_text
      colors = askcolor(title="Tkinter Color Chooser")
      color_text=colors[1]
      canvas = Canvas(root, width=15, height=15, background=color_text)
      canvas.grid(row=2,column=1,padx=5,pady=5)
text=Button(
    root,
    text='Choisis une couleur pour le texte',
    command=change_color_text).grid(row=1,column=1,padx=5,pady=5)
##----------------couleur de la bande   color_band
color_band=tab[1]
canvas = Canvas(root, width=15, height=15, background=color_band)
canvas.grid(row=2,column=2,padx=5,pady=5)
def change_color_band():
      global color_band
      colors = askcolor(title="Tkinter Color Chooser")
      color_band=colors[1]
      canvas = Canvas(root, width=15, height=15, background=color_band)
      canvas.grid(row=2,column=2,padx=5,pady=5)
band=Button(
    root,
    text='Choisis une couleur pour la bande',
    command=change_color_band).grid(row=1,column=2,padx=5,pady=5)

##----------------Fond d'écran    Background
Background=tab[3]
def change_bck():
      global Background,image,bt
      Background = askopenfilename(title="Ouvrir un fond d'écran",filetypes=[('Jpeg files','.jpg'),('png files','.png'),('all files','.*')])
      image=plt.imread(Background)
      R=hex(round(np.mean(image[:,:,0])))[2:]
      G=hex(round(np.mean(image[:,:,1])))[2:]
      B=hex(round(np.mean(image[:,:,2])))[2:]
      bt="#"+R+G+B
      canvas = Canvas(root, width=15, height=15, background=bt)
      canvas.grid(row=2,column=0,padx=5,pady=5)
      
bck=Button(
    root,
    text='Choisis un fond d\'écran',
    command=change_bck).grid(row=1,column=3,padx=5,pady=5)
root.mainloop()

##----------------couleur de la bande en focus   color_darkband

R=round(int(color_band[1]+color_band[2],base=16)*0.8)
G=round(int(color_band[3]+color_band[4],base=16)*0.81)
B=round(int(color_band[5]+color_band[6],base=16)*0.91)
Rh=hex(R)
Gh=hex(G)
Bh=hex(B)
color_darkband="#"+Rh[2]+Rh[3]+Gh[2]+Gh[3]+Bh[2]+Bh[3]
##ecriture dans le css.css

fichier=open("css.css","w",encoding="utf-8")

fichier.write("body {background-color:#222244;\n")
fichier.write("background-image: url(\""+Background+"\");\n")
fichier.write("background-attachment:fixed;\n")
fichier.write("background-size:cover;\n")
fichier.write("background-repeat:no-repeat}\n")

fichier.write("p {font-size:20px;\n")
fichier.write("font-family:didot;\n")
fichier.write("font-weight:900;\n")
fichier.write("border-radius:10px;\n")
fichier.write("padding-left:20px;\n")
fichier.write("padding-right:20px;\n")
fichier.write("margin-top:30px;\n")
fichier.write("--background-color:#222244;\n")
fichier.write("color:"+color_text+";\n")#
fichier.write("opacity:1;\n")
fichier.write("--width:fit-content;\n")
fichier.write("text-align:center;\n")
fichier.write("align-self:center;\n")
fichier.write("filter:drop-shadow(3px 3px 3px #111);}\n")

fichier.write("audio {margin-left:100px;\n")
fichier.write("width:1500px;\n")
fichier.write("height:40px;}\n")

fichier.write("audio::-webkit-media-controls-panel {background-color:"+color_band+";}\n")#

fichier.write("audio:hover {transform: scale(1.001);\n")
fichier.write("filter: drop-shadow(2px 3px 3px #333);}\n")

fichier.write("audio:focus::-webkit-media-controls-panel {background-color:"+color_darkband+";\n")#
fichier.write("color:white;}\n")

fichier.write("audio:hover::-webkit-media-controls-play-button {filter:drop-shadow(2px 3px 3px #333);}\n")

fichier.write("audio::-webkit-media-controls-play-button {background-color:"+bt+";\n")#
fichier.write("border-radius:100px;\n")
fichier.write("width:20px}\n")

fichier.write("audio::-webkit-media-controls-timeline {padding-left:400px;width:100px}\n")

fichier.write("--audio:focus{\n")
fichier.write("transform:rotate(-90deg);\n")
fichier.write("position:fixed;\n")
fichier.write("top:400px;\n")
fichier.write("left:1200px;\n")
fichier.write("width:800px;\n")
fichier.write("background-color:red;}\n")
fichier.close()
i=0
name="css"+str(i)+".txt"
while os.path.exists("CSS\\"+name):
    i+=1
    name="css"+str(i)+".txt"
fichier=open("CSS\\"+name,"w")
fichier.write(color_text+"\n"+color_band+"\n"+bt+"\n"+Background+"\n")
fichier.close()
fichier=open("cssrcp.txt","w",encoding="utf-8")
fichier.write(color_text+"\n"+color_band+"\n"+bt+"\n"+Background+"\n")
fichier.close()

