# Album Cover Art

Reads in an image of an album cover and and pulls the lyrics from an API to create an image to create "art", which consists of the colored lyrics to mirror the original.

<table>
<tr>
    <th>
        Original
    </th>
    <th>
        Without Background
    </th>
    <th>
        With Background
    </th>
</tr>
<tr>
    <td>
        <img src="https://m.media-amazon.com/images/I/815UbQWSslL._SX355_.jpg" alt="original" width="300">
    </td>
    <td>
        <img src="https://i.redd.it/89fn3qlbgie81.png" alt="result" width="300">
    </td>
    <td>
        <img src="https://preview.redd.it/m3nji7nhvme81.png?width=2100&format=png&auto=webp&s=6bedf3bd145c03f7a0ee560bd065b73a99b4a10c" alt="result" width="300">
    </td>
</tr>
</table>


## Usage

* Copy the covers you want use in the `./input/` folder.
* Name the images from `00_foo.png` to `XX_bar.jpg`.
* Create a `songs.txt` file in the `./input/` folder.
* Enter the name of the song (that should be contained by the new image) for `00_foo.png` in the first line, second line is for the next image and so on.
* Install dependencies with: `python3 -m pip install -r requirements.txt`
* Run: `python3 main.py`
* Your ouput is in: `./output/`


## Dependencies

* https://github.com/python-pillow/Pillow
* https://github.com/johnwmillr/LyricsGenius


## Acknoledgements

Thanks go out to [u/Jkelly515](https://www.reddit.com/user/Jkelly515/) from [here](https://www.reddit.com/r/Eminem/comments/sev4sw/i_made_the_cover_for_recovery_using_lyrics_from/) for the idea.
