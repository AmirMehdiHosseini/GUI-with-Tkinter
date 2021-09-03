import pytube
from tkinter import *
from tkinter import ttk


win = Tk()
win.geometry('600x200')
win.resizable(0,0)
win.title('Youtube downloader')
win.config(bg = 'pink')


link = StringVar()
enter_url = Entry(win, textvariable = link, bg = 'orange', fg = 'green', width = 60)
enter_url.place(relx = 0.2, rely = 0.1)
label_url = Label(win,  text = 'Link : ', fg = 'green')
label_url.place(relx =0.09, rely =  0.1)


itag_var = StringVar()
itag = Entry (win, width = 60,textvariable = itag_var, bg = 'orange', fg = 'green')
itag.place (relx = 0.2,rely = 0.25)
label_itag = Label(win, text = 'Itag : ', fg = 'green')
label_itag.place(relx = 0.09, rely = 0.25)


dir_var = StringVar()
directory = Entry (win, width = 60,textvariable = dir_var, bg = 'orange', fg = 'green')
directory.place (relx = 0.2,rely = 0.4)
label_directory = Label(win, text = 'Directory : ', fg = 'green')
label_directory.place(relx = 0.09, rely = 0.4)


def Itags ():
    top = Toplevel()
    top.geometry('800x500')
    top.resizable(0,1)
    top.title('Youtube video formats ')
    
    
    url = link.get()
    yt = pytube.YouTube(url)
    formats_text = Text (top , height = 50, width = 100)
    text = yt.streams
    formats_text.insert(END, text)
    formats_text.pack(fill = 'both')


def download():
    url = link.get()
    yt = pytube.YouTube(url)
    ys = yt.streams.get_by_itag(itag_var.get())
    ys.download(dir_var.get())


btn_itag = ttk.Button(win, text = 'Itags', command = Itags)
btn_itag.place(relx = 0.5, rely = 0.7)


btn_download = ttk.Button(win, text = 'Download', command = download)
btn_download.place(relx = 0.36, rely = 0.7)


exit_btn = ttk.Button(win , text = 'Exit', command = win.destroy)
exit_btn.place(relx = 0.64 , rely = 0.7)


win.mainloop()