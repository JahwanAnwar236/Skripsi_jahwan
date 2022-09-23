from tkinter import *
from tkinter.font import BOLD

root=Tk()
root.title("Menentukan Rute Terpendek Antara Baleendah Ke Perpustakaan Kawaluyaan")
root.resizable(width=False,height=False)
root.geometry("1000x600")
root.configure(background="blue")

judul =Label(root,bg='silver',text='Mencari Rute Dari Baleendah Ke Perpustakaan Kawaluyaan',font=('Times New Roman',20,BOLD),fg='black')
judul.place(relx=0.5,rely=0.03,relwidth=0.8,relheight=0.1,anchor='n')

label1 =Label(root,bg='skyblue',text='Masukkan titik awal:',font=('Times New Roman',15),fg='black')
label1.place(relx=0.35,rely=0.15,relwidth=0.20,relheight=0.06,anchor='n')

Input1 = Entry(root)
Input1.place(relx=0.6,rely=0.15,relwidth=0.1, relheight=0.05,anchor='n')

label2 =Label(root,bg='skyblue',text='Masukkan titik akhir:',font=('Times New Roman',15),fg='black')
label2.place(relx=0.35,rely=0.22,relwidth=0.20,relheight=0.06,anchor='n')

Input2 = Entry(root)
Input2.place(relx=0.6,rely=0.22,relwidth=0.1,relheight=0.05,anchor='n')

label5=Label(root,bg='silver',text='Daftar Titik Awal Dan Titik Akhir Yang Dapat Diisikan',font=('Times New Roman',15,BOLD),fg='black')
label5.place(relx=0.25,rely=0.63,relwidth=0.5,relheight=0.05,anchor='n')

label9=Label(root,bg='white',text='Baleendah = A1',font=('Times New Roman',12),fg='black')
label9.place(relx=0.15,rely=0.75,relwidth=0.3,relheight=0.05,anchor='n')

label10=Label(root,bg='white',text='Dayehkolot = B2',font=('Times New Roman',12),fg='black')
label10.place(relx=0.15,rely=0.8,relwidth=0.3,relheight=0.05,anchor='n')

label11=Label(root,bg='white',text='Bojongsoang = G3',font=('Times New Roman',12),fg='black')
label11.place(relx=0.15,rely=0.85,relwidth=0.3,relheight=0.05,anchor='n')

label12=Label(root,bg='white',text='Bandung Kidul = C4',font=('Times New Roman',12),fg='black')
label12.place(relx=0.15,rely=0.9,relwidth=0.3,relheight=0.05,anchor='n')

label13=Label(root,bg='white',text='Moh.toha = D5',font=('Times New Roman',12),fg='black')
label13.place(relx=0.5,rely=0.75,relwidth=0.3,relheight=0.05,anchor='n')

label14=Label(root,bg='white',text='Suka Ati = E5',font=('Times New Roman',12),fg='black')
label14.place(relx=0.5,rely=0.8,relwidth=0.3,relheight=0.05,anchor='n')

label15=Label(root,bg='white',text='Batu Nunggal Indah II = F7',font=('Times New Roman',12),fg='black')
label15.place(relx=0.5,rely=0.85,relwidth=0.3,relheight=0.05,anchor='n')

label16=Label(root,bg='white',text='Suka Ati = E8',font=('Times New Roman',12),fg='black')
label16.place(relx=0.85,rely=0.75,relwidth=0.3,relheight=0.05,anchor='n')

label8=Label(root,bg='white',text='Batu Nunggal Indah IV = H9',font=('Times New Roman',12),fg='black')
label8.place(relx=0.85,rely=0.8,relwidth=0.3,relheight=0.05,anchor='n')

label8=Label(root,bg='white',text='Soekarno Hatta = I10',font=('Times New Roman',12),fg='black')
label8.place(relx=0.85,rely=0.8,relwidth=0.3,relheight=0.05,anchor='n')

label8=Label(root,bg='white',text='Kawaluyaan Indah I = J11',font=('Times New Roman',12),fg='black')
label8.place(relx=0.85,rely=0.8,relwidth=0.3,relheight=0.05,anchor='n')

def graph():
    infinity = float("infinity")
    mulai = str(Input1.get())
    berhenti = str(Input2.get())
    lokasi = {
        'A1':{
            'B':5 
        },
        'B2':{
            'G':5,
            'C':17
        },
        'G3':{
            'H':20

        },
        
        'C4':{
            'D':15,
            'F':10
        },
        'D5':{
            'E':17
                    
        },
        'E6':{
            'F':8,
            'I':20
        },
        'F7':{
            'E':8,
            'H':24
        },
        'E8':{
            'I':15
            },
        'H9':{
            'I':5
            },
        'I10':{
            'J':20
            },
        'J11':{}
    }

    jarak = {}
    titik = {}
    for node in lokasi:
        jarak[node]=infinity
        titik[node]={}
        jarak[mulai]=0
        
        def rute_terpendek(jarak,not_checked):
            lowest_dist = infinity
            cheapest_node=""
            for node in jarak:
                if node in not_checked and jarak[node] <= lowest_dist:
                    lowest_dist = jarak[node]
                    cheapest_node = node
                    return cheapest_node

        ##Algoritma Dijkstra

        not_checked = [node for node in jarak]
        node = rute_terpendek(jarak,not_checked)
        while not_checked:
            dist = jarak[node]
            child_dist = lokasi[node]
            for c in child_dist:
                if jarak[c]>dist+child_dist[c]:
                    jarak[c]=dist+child_dist[c]
                    titik[c]=node

    not_checked.pop(not_checked.index(node))
    node=rute_terpendek(jarak,not_checked)

    label3=Label(root,text="Jarak yang ditempuh sejauh "+str(jarak[berhenti])+" km",font=('Times New Roman',15),bg='peachpuff')
    label3.place(relx=0.5,rely=0.5,relwidth=1,relheight=0.05,anchor='n')

    if jarak[berhenti] < infinity:
        alur=[berhenti]
        i=0
        while mulai not in alur:
            alur.append(titik[alur[i]])
            i+=1

        label4=Label(root,text="Alurnya adalah " + str(alur[::-1]),font=('Times New Roman',15), bg='peachpuff')
        label4.place(relx=0.5,rely=0.55,relwidth=1,relheight=0.05,anchor='n')
    
    else:
        label4=Label(root,text="Alurnya tidak ditemukan " + str(alur[::-1]),font=('Times New Roman',15),bg='peachpuff')
        label4.place(relx=0.5,rely=0.55,relwidth= 1,relheight=0.05,anchor='n')

def reset():
    label3.destroy()
    label4.destroy()
    Input1.delete(0,END)
    Input2.delete(0,END)

Hapus_Button = Button(root, text="Hapus", font=('Times New Roman', 15), command=reset)
Hapus_Button.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=.07)

Senin_button=Button(root,text='Enter',font=('Times New Roman',15),command=graph)
Senin_button.place(relx=0.4,rely=0.4,relwidth=0.2,relheight=0.07,anchor='n')

root.mainloop()
