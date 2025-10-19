all: ytdl

temp:
	mkdir temp

venv:
	python -m venv venv && source venv/bin/activate && pip install yt_dlp

ytdl: venv temp
	sh scripts/ytdl.sh

update_playlist: venv temp
	sh scripts/update_playlist.sh

clean:
	rm -rf venv
	rm -rf temp

.PHONY: ytdl