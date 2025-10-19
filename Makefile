venv:
	python -m venv venv && source venv/bin/activate && pip install yt_dlp

clean:
	rm -rf venv