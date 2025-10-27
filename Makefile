all: ytdl

temp:
	mkdir temp

venv:
	python -m venv venv && source venv/bin/activate && python3 -m pip install -U yt-dlp

ytdl: venv temp
	sh scripts/ytdl.sh

update_playlist: venv temp
	sh scripts/update_playlist.sh

exe_rights:
	chmod +x scripts/ytdl.sh scripts/update_playlist.sh

clean:
	rm -rf venv
	rm -rf temp

.PHONY: ytdl
