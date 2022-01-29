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
        <img src="https://preview.redd.it/89fn3qlbgie81.png?width=960&crop=smart&auto=webp&s=c1aea46ad810398ffd24945a77f7bfe8587549e8" alt="result" width="300">
    </td>
    <td>
        <img src="https://preview.redd.it/m3nji7nhvme81.png?width=640&crop=smart&auto=webp&s=2f58725a66874da3577b0ba41ee6a710a75aa5da" alt="result" width="300">
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
