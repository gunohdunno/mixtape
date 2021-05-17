# mixtape
## Running the Application
Run the program through the terminal with two command-line arguments like so:
```
python apply_changes.py mixtape.json changes.json
```

The changes file is a JSON file and has the following attributes for a single change:
- action: the action to perform (add playlist, remove playlist, add song to a playlist)
- playlist_id: playlist ID
- song_id: song ID
- user_id: user ID

Check changes.json to see an example of the formatting to create your own test cases

## Scaling the Application
Given a large changes.json file, we could create a stream of changes so that we are not loading all the changes that are needed into memory. Since one change is applied at a time, we only need to load the current change into memory and process that change until we reach the end of the file. If memory is not too much of a constraint, we could also load and process changes in chunks rather than one at time.

Given a large mixtape.json file, we could reduce the file size of mixtape.json by not including the users and songs. The changes only apply to playlists so mixtape.json can be a simple list of playlists. The user and song lists are only used to validate if a user or song exists (for this case). The users and songs can be stored in a separate database and they can be validated through database calls. If there are large amounts of playlists, we can use a data stream approach similar to the approach for large changes.json files.