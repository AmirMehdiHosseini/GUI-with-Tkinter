from tkinter import *
from os import *
import pygame


class MusicPlayer():
    
        def __init__(self):
        
            self.win = Tk()
            self.win.resizable(0,0)
            self.win.config(bg = 'blue')
            self.win.geometry('1100x400')
            self.win.title('Music player')
            

            pygame.init()
            pygame.mixer.init()


            self.track = StringVar()
            self.status = StringVar()


            self.track_frame = LabelFrame(self.win, text = 'Song track', font=("times new roman",18,"bold"),
            bg = 'orange', fg = 'blue', relief= 'groove')
            self.track_frame.place(relx=0,rely=0,width=810,height=100)


            self.song_track = Label(self.track_frame, textvariable = self.track,font=("times new roman",11,"bold"),
            width = 65, bg = 'blue', fg = 'orange')
            self.song_track.place(relx = 0.05, rely = 0.2)


            self.track_status = Label(self.track_frame, textvariable = self.status , font=("times new roman",11,"bold"),
            width = 15, bg = 'blue', fg = 'orange')
            self.track_status.place(relx = 0.80,rely = 0.2)


            self.button_frame = LabelFrame(self.win, text = 'Control', font=("times new roman",18,"bold"),
            bg = 'orange', fg = 'blue', relief= 'groove')
            self.button_frame.place(relx= 0, rely =0.26, width = 810, height = 170)
        
        
            self.play_button = Button(self.win, text = 'PLAY',font=("times new roman",16,"bold"), 
            command =self.play_song ,activebackground = 'purple',width = 10, height = 2, bg = 'blue', fg = 'orange' )
            self.play_button.place(relx = 0.04, rely = 0.45)


            self.pause_button = Button(self.win, text = 'PAUSE',font=("times new roman",16,"bold"),
            command =self.pause_song,activebackground = 'purple', width = 10, height = 2, bg = 'blue', fg = 'orange' )
            self.pause_button.place(relx = 0.18, rely = 0.45)


            self.resume_button = Button(self.win, text = 'RESUME',font=("times new roman",16,"bold"), 
            command =self.unpause_song,activebackground = 'purple', width = 10, height = 2, bg = 'blue', fg = 'orange' )
            self.resume_button.place(relx = 0.32, rely = 0.45)


            self.stop_button = Button(self.win, text = 'STOP',font=("times new roman",16,"bold"), 
            command =self.stop_song,activebackground = 'purple', width = 10, height = 2, bg = 'blue', fg = 'orange' )
            self.stop_button.place(relx = 0.46, rely = 0.45)


            self.stop_button = Button(self.win, text = 'EXIT',font=("times new roman",16,"bold"), 
            command =self.win.destroy,activebackground = 'purple', width = 10, height = 2, bg = 'blue', fg = 'orange' )
            self.stop_button.place(relx = 0.6, rely = 0.45)


            self.playlist_frame = LabelFrame(self.win,  text = 'Playlist', font=("times new roman",18,"bold"),
            bg = 'orange',fg = 'blue',  relief= 'groove',)
            self.playlist_frame.place(relx = 0.74, rely = 0, width = 280, height = 395)


            self.track_frame = LabelFrame(self.win, text = 'Directory', font=("times new roman",18,"bold"),
            bg = 'orange', fg = 'blue', relief= 'groove')
            self.track_frame.place(relx=0,rely=0.695,width=810,height=117)


            self.scrol = Scrollbar(self.playlist_frame, orient = 'vertical')


            self.playlist = Listbox(self.playlist_frame,  font=("times new roman",11,"bold"),
            yscrollcommand = self.scrol.set, selectbackground = 'orange',
            selectmode = 'single',height = 300, bg = 'orange', fg = 'blue', relief='groove')


            self.scrol.pack(side = 'right', fill = 'y')
            self.scrol.config(command = self.playlist.yview)
            self.playlist.pack(fill = 'both')


            self.directory_var = StringVar()
            self.dir_entry = Entry(self.win, textvariable = self.directory_var,font=("times new roman",11,"bold"),
            width = 65, bg = 'blue', fg = 'orange')    #self.directory_var.set('C:/Users/Lenovo_ws/Desktop/')
            self.dir_entry.place(relx = 0.05, rely = 0.88)
 
            
            self.change_btn = Button(self.track_frame, text = 'CHANGE', font=("times new roman",16,"bold"), 
            command = self.change_directory,
            activebackground = 'purple', width =10, height = 1, bg = 'blue', fg = 'orange' )
            self.change_btn.place(relx = 0.8, rely = 0.3)


        def play_song(self):

            self.track.set(self.playlist.get(ACTIVE))
            self.status.set('Playing')
            pygame.mixer.music.load(self.playlist.get(ACTIVE))
            pygame.mixer.music.play()


        def stop_song(self):

            self.status.set('Stopped')
            pygame.mixer.music.stop()
            self.track.set('')


        def pause_song(self):

            self.status.set('Paused')
            pygame.mixer.music.pause()


        def unpause_song(self):

            self.status.set('Playing')
            pygame.mixer.music.unpause()

        def change_directory(self):
            
            chdir(self.directory_var.get())
            self.all_tracks = listdir()
            for track in self.all_tracks:
                self.playlist.insert(END, track)


obj = MusicPlayer()
obj.win.mainloop()