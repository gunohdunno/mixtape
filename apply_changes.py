from os import error
import sys
import json
import collections

def main(argv):
    global songDict
    global userDict
    global playlistDict
    # load json data from mixtape and changes files
    if len(argv) < 2:
        raise Exception("mixtape and changes files required as command-line arguments")
    
    with open(argv[0], "r") as f:
        mixtapeJSON = json.load(f)

    with open(argv[1], "r") as f:
        changesJSON = json.load(f)

    # store into individual dictionaries for quick validation and access times
    songDict = listToDict(mixtapeJSON["songs"])
    userDict = listToDict(mixtapeJSON["users"])
    playlistDict = listToDict(mixtapeJSON["playlists"])

    # apply changes to mixtape_json
    for change in changesJSON:
        changeError = applyChange(change)
        if changeError != "":
            print(changeError)

    # dump data back into output.json 
    mixtapeJSON["playlists"] = playlistDict.values()
    with open("output.json", "w") as outfile:
        json.dump(mixtapeJSON, outfile)

'''
Adds a playlist to the mixtape
'''
def addPlaylist(playlist_id, user_id, song_id):
    # check for duplicate ids
    if playlist_id in playlistDict:
        return "Playlist ID: " + playlist_id + " already exists"
    if user_id not in userDict:
        return "User ID: " + user_id + " not found"
    if song_id not in songDict:
        return "Song ID: " + song_id + " not found"
    
    # new playlist is being added
    newPlayList = {}
    newPlayList["id"] = playlist_id
    newPlayList["user_id"] = user_id
    newPlayList["song_ids"] = [song_id]
    playlistDict[playlist_id] = newPlayList

'''
Adds an existing song to an existing playlist
'''
def addSongToPlaylist(playlist_id, song_id):
    # find playlist and append new song 
    if playlist_id not in playlistDict:
        return "Playlist ID: " + playlist_id + " does not exist"
    if song_id not in songDict:
        return "Song ID: " + song_id + " not found"
    
    playlistDict[playlist_id]["song_ids"].append(song_id)

'''
Removes an existing playlist
'''
def removePlaylist(playlist_id):
    if playlist_id not in playlistDict:
        return "Playlist ID: " + playlist_id + " does not exist"
    
    del playlistDict[playlist_id]

### Helper functions
'''
Consolidates all three functions and calls the correct one per change
'''
def applyChange(change):
    errorMessage = ""
    action = change["action"]
    if action == "addPlaylist":
        errorMessage = addPlaylist(change["playlist_id"], change["user_id"], change["song_id"])
    elif action == "addSong":
        errorMessage = addSongToPlaylist(change["playlist_id"], change["song_id"])
    elif action == "remove":
        errorMessage = removePlaylist(change["playlist_id"])
    if errorMessage is not None:
        return "Change " + change["id"] + " failed. Error: " + errorMessage
    return ""

'''
Helper to create dictionaries for quick access
'''
def listToDict(l):
    d = collections.OrderedDict()
    for el in l:
        d[el["id"]] = el
    return d

if __name__=="__main__":
    main(sys.argv[1:])