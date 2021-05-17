# mixtape
Basic python application to parse music data JSON files and apply any changes given a changes JSON file

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

Check changes.json to see an example of the formatting

## Scaling the Application
Given a large changes.json file, we could create a stream of changes so that we are not loading all the changes that are needed into memory. Since one change is applied at a time, we only need to load the current change into memory and process that change until we reach the end of the file. If memory is not too much of a constraint, we could also load changes in chunks rather than one at time.

Given a large mixtape.json file, we could continue to use the same approach but it would not be as efficient given the current structure of the file. The changes are only applying to playlists but we have access to a list of users and songs that do not change. We only use the user and song lists to validate that a given song or user exists. It may be better to store the users and songs into a database and have mixtape.json just be a list of playlists. That way, we have less to load into memory and we could even use a similar data stream model used in large changes.json files.