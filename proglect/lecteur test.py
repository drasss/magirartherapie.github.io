#E:\perso\telechargement\audacity\proglect

import os.path,os,time,urllib.parse
import numpy as np

path=".." #attention le \ est ajouté automatiquement

def get_folder(path=path):
    tab=[]
    content=os.listdir(path)
    for i in content:
        if ".mp3" in i:
            tab+=[path+"""\\"""+i]
        elif not("." in i):
            tab+=list(get_folder(path+"""\\"""+i))
    return tab


#exriture du fichier html
fichier=open("lecteur.html","w",encoding="utf-8")
fichier.write("<html><style type=\"text/css\" media=\"all\">@import \"css.css\";</style>\n")
#head
fichier.write("<head>")
fichier.write("<title>Lecteur Mp3</title>") #titre
fichier.write("<link rel=\"icon\" href=\"img\icone.png\" />") #icone
fichier.write("<meta charset=\"UTF-8\">")#utf-8 pour mozilla
fichier.write("")#
#mise en place des sons
fichier.write("\n</head><body>\n")
#pour ne pas utiliser de variable j utiliser "i+1" 


tab_init=get_folder(path)

dtype=[('path', '<U121'), ('name', '<U121')]

tab_4=np.rot90(np.array((tab_init,tab_init)))
for i in range(len(tab_4)):
    tab_4[i,1]=tab_4[i,1].split("\\")[-1][:-4]
tab_unsorted=np.array(tab_4,dtype=dtype)

tab=np.sort(tab_unsorted,order="name")[::-1]

for i in range(len(tab)):
    fichier.write("<p>"+tab[i,1][0]+"</p>\n")
    fichier.write("<audio controls=\"\" preload=\"none\" loop=\"true\"><source src=\""+tab[i,0][0]+"\"  type=\"audio/mpeg\"></audio>") #urllib.parse.quote() sert a transformer le char en url
fichier.write("</body>\n</html>\n")
fichier.close()
#os.system("start lecteur.html")