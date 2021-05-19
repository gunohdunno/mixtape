# mixtape
## Running the Application
Run the program through the terminal with two command-line arguments like so:
```
python apply_changes.py mixtape.json changes.json
```

The changes file is a JSON file and has the following attributes for a single change:
- id: ID of a change so they can be referenced if certain changes fail
- action: the action to perform ("addPlaylist", "addSong", "remove")
- playlist_id: playlist ID
- song_id: song ID
- user_id: user ID

Check changes.json to see an example of the formatting to create your own test cases

## Handling Exceptions
There are a couple ways I thought about handling the exceptions in this application.
1. Have a hard exception when there is an illegal change (e.g. adding a song to a playlist that does not exist)
2. Have the functions return an indicator as to whether it succeeded or not and keep track of which ones failed

I chose to implement the second method since the information provided is more useful for the user. The benefits of this method is that all errors are shown in a single run of the application. This way, the user can save time by fixing all the errors before running it again. The downside to this method is that some errors may occur because a previous change failed. For example, if a playlist failed to add and a song is trying to add to that playlist, it will fail. 

The first method still has its benefits. If the application stops at every error, it will never give you consequential errors that the 2nd method suffers from. The downside is that it is probably slower to debug in the general case since the user will be spending time fixing one change at a time.

## Scaling the Application
Given a large changes.json file, we could create a stream of changes so that we are not loading all the changes that are needed into memory. Since one change is being applied at a time, we only need to load the current change into memory and process that change until we reach the end of the file. If memory is not too much of a constraint, we could also load and process changes in chunks rather than one at time.

Given a large mixtape.json file, we could reduce the file size of mixtape.json. The user and song lists are only used to validate if a user or song exists (for this use-case) so the users and songs can be stored in a separate database or the file could contain just a set of user and song IDs to validate against. This way, we're loading only data that's necessary for the change. 
