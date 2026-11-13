import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="",
    client_secret="",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-modify-playback-state user-read-playback-state"
))

root = tk.Tk()
root.title("My music player")
root.geometry("300x200")

song_label = tk.Label(root, text="no song loaded")
song_label.pack()
def update_song_info():
    current = sp.current_playback()
    if current is not None and current['item'] is not None:
        song_name = current['item']['name']
        artist_name = current['item']['artists'][0]['name']
        song_label.config(text=f"{song_name} - {artist_name}")
    else:
        song_label.config(text="Nothing playing")
    song_label.update_idletasks()
def play_pause():
    current = sp.current_playback()
    isplaying= current['is_playing']
    if isplaying:
        sp.pause_playback()
    else:
        sp.start_playback()
    
    update_song_info()
def next_track():
    sp.next_track()
    root.after(300, update_song_info)
    
def previous_track():
    sp.previous_track()
    root.after(300, update_song_info)
    
back_button = tk.Button(root, text="< back", command=previous_track)
back_button.pack(side="left", padx=10)

play_button = tk.Button(root, text="play", command=play_pause)
play_button.pack(side="left", padx=10)

next_button = tk.Button(root, text="next >", command=next_track)
next_button.pack(side="left", padx=10)

update_song_info()
root.mainloop()