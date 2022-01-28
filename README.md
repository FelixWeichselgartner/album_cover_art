# Album Cover Art

Reads in an image of an album cover and and pulls the lyrics from an API to create an image to create "art", which consists of the colored lyrics to mirror the original. I will add an example soon.


## Usage

* Copy the covers you want use in the `./input/` folder.
* Name the images from `00_foo.png` to `XX_bar.jpg`.
* Create a `songs.txt` file in the `./input/` folder.
* Enter the name of the song (that should be contained by the new image) for `00_foo.png` in the first line, second line is for the next image and so on.
* Install dependencies with: `python3 -m pip install -r requirements.txt`
* Run: `python3 main.py`
* Your ouput is in: `./output/`


## Acknoledgements

Thanks go out to [u/Jkelly515](https://www.reddit.com/user/Jkelly515/) from [here](https://www.reddit.com/r/Eminem/comments/sev4sw/i_made_the_cover_for_recovery_using_lyrics_from/) for the idea.
