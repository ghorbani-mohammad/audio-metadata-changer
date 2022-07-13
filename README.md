## Audio Metadata Changer

So I needed to change some of my audio files and guess what? I created this python script. It gets a absolute path, and inside that path read all audio files and change their names to their title metadata.

## Usage
```bash
git clone git@github.com:ghorbani-mohammad/audio-metadata-changer.git

cd audio-metadata-changer

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python code.py

# example path would be:
# /mnt/c/Users/Mohammad/Desktop/all-ears-english/english-fluency/
```

## License
[MIT](https://choosealicense.com/licenses/mit/)