# YTDL

Check out the Windows branch if you're on Windows !

This is a small program that I made for personnal use, with it you can download a video or audio from youtube.
You can also download entire playlists in a single command.
There is also a function called "update playlist", which keeps track of the last video you downloaded, and downloads all of the remaining ones. I use it to keep track of my music platlist on youtube.

## Preparation

### Dependencies

Make sure you have python with yt_dlp in your PATH environment or in a virtual environment (depending on the case you may want to remove the 1st line of both sh files)

### Env

Create a ```env``` folder at the root of your directory containing 2 files:

- ```last_id.txt``` which should contain a video address like ```dE1HftNpDAw```

- ```vars.py``` which you can complete using ```_vars_model.py```

### Execution rights

Add execution rights with ```chmod +x ytdl.sh update_playlist.sh```

### Menu creation (optionnal)

If you're on kde plasma like me, you can enter the menu editor and setup ```ytdl``` and ```update_music```

Be sure to add the base directory and the option ```execute in a terminal```

You can also add an icon if you want !

## Usage

Execute the sh file or search for them like a normal application if you set up the menu !