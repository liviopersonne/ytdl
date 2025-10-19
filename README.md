# YTDL

Check out the Windows branch if you're on Windows !

This is a small program that I made for personnal use, with it you can download a video or audio from youtube.
You can also download entire playlists in a single command.
There is also a function called "update playlist", which keeps track of the last video you downloaded on a specific playlist, and downloads all of the remaining ones. I use it to keep track of my music playlist on youtube.

## Preparation

### Python virtual env

Make sure you have `python` and `make` installed. Then run `make venv`: this should create your venv.

### Env

There is a `env` folder at the root of your directory containing 2 files:

- `last_id.txt` which should contain a video address like `dE1HftNpDAw`. It should always be the id of the last video downloaded by `update_playlist`. You can initialize it for your first use, and after that it is updated automatically.

- `vars.py` which you can complete with path and playlist info

### Execution rights

Add execution rights with `make exe_rights`

### Menu creation (optionnal)

If you're on kde plasma like me, you can enter the menu editor and setup `ytdl` and `update_music`

Be sure to add the base directory and the option `execute in a terminal`

You can also add an icon if you want !

## Usage

- Run `make` or `make ytdl` for the normal youtube download.
- Run `make update_playlist` to run the playlist updater
