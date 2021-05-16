import sys
import json

def main(argv):
    # load json data from mixtape and changes files
    global mixtape_json
    global changes_json
    with open(argv[0], "r") as f:
        mixtape_json = json.load(f)

    with open(argv[1], "r") as f:
        changes_json = json.load(f)

    # apply changes to mixtape_json
    for change in changes_json:
        applyChange(change)
    
    # dump data back into output json 
    with open("output.json", "w") as outfile:
        json.dump(mixtape_json, outfile)

# check which type of action is being performed on the mixtape and call proper functions accordingly
def applyChange(change):
    if change["action"] == "addPlaylist":
        addPlaylist(change["playlist_id"], change["user_id"], change["song_id"])
    elif change["action"] == "addSong":
        addSongToPlaylist(change["playlist_id"], change["song_id"])
    elif change["action"] == "remove":
        removePlaylist(change["playlist_id"])

def addPlaylist(playlist_id, user_id, song_id):
    # check for duplicate ids
    for p in mixtape_json["playlists"]:
        if p["id"] == playlist_id:
            return False

    # new playlist is being added
    newPlayList = {}
    newPlayList["id"] = playlist_id
    newPlayList["user_id"] = user_id
    newPlayList["song_ids"] = [song_id]
    mixtape_json["playlists"].append(newPlayList)
    return True

def addSongToPlaylist(playlist_id, song_id):
    # find playlist and append new song 
    for p in mixtape_json["playlists"]:
        if p["id"] == playlist_id:
            p["song_ids"].append(song_id)
            return True
    return False

def removePlaylist(playlist_id):
    for p in mixtape_json["playlists"]:
        if p["id"] == playlist_id:
            mixtape_json["playlists"].remove(p)
            return True
    return False

if __name__=="__main__":
    main(sys.argv[1:])