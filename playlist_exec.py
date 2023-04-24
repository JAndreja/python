playlist= {'title': 'Best songs',
           'author': 'Andreja Jovanovski',
           'songs': [
               {'title':'song1','artist':['andreja'],'duration': 2.5},
               {'title':'song2','artist':['radica','kaja'],'duration': 3.2},
               {'title':'song3','artist':['mite'],'duration': 4}
           ]}

#print(playlist)

#for key,value in playlist.items():
#    print(f"{key}:{value}")

#print(f"Playlist title: {playlist['title']}")
#print(f"Playlist songs: {playlist['songs']}")

for song in playlist['songs']:
     print(song)
print("=================================")
for song in playlist['songs']:
    print(f"title: {song['title']} , artist: {song['artist']}")

# total_duration=0
# for song in playlist['songs']:
#     total_duration +=(song['duration'])
# print(total_duration)
