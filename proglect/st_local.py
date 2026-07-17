import streamlit as st
import os
import random
 
st.set_page_config(layout="wide")
 
#--------------------- Recursion mp3
path="mp3\\mp3\\mp3\\"
paths=[]
def recu(path):
    global paths
    liste=os.listdir(path)
    for i in range(len(liste)):
        if liste[i][-4:]==".mp3":
            paths+=[path+liste[i]]
        else:
            recu(path+liste[i]+"\\")
    return paths
data=recu(path)
titles=[]
for i in range(len(data)):
    titles+=[data[i].split("\\")[-1][:-4]]
 
#--------------------- Streamlit
    #----------------- Sidebar
 
    
rand=st.sidebar.button("Random")
val=""
if rand:
    val=titles[random.randint(0,len(titles)-1)]
search=st.sidebar.text_input("chercher",value=val)
 
clir=st.sidebar.button("clear")
if clir : val=""
 
link=st.sidebar.text_input("paste an audio link here")
if link!="":
    st.text("resultat de la recherche")
    st.audio(link, format="audio/mp3",loop=1,autoplay=rand)
# --------------------- Musiques
 
 
containers=[]
letter="A"
for i in range(len(data)):
    if search.upper() in titles[i].upper():
        containers+=[st.container()]
        if titles[i][0].upper()!=letter:
            letter=titles[i][0].upper()
            containers[i].title(letter)
        print(data[i])
 
        containers[i].text(titles[i])
        containers[i].audio(data[i], format="audio/mp3",loop=1,autoplay=rand)
    else: containers+=[""]
 
