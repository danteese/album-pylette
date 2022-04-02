from colorthief import ColorThief


def rgb_to_hex(r, g, b):
    return '#{:X}{:X}{:X}'.format(r, g, b)


def get_palette(path, color_count, hex=True):
    color_thief = ColorThief(path)
    # get the dominant color
    palette_rgb = color_thief.get_palette(color_count=6)
    if hex is True:
        palette_hex = []
        for color in palette_rgb:
            palette_hex.append(rgb_to_hex(*color))

        return [palette_hex]

    return palette_rgb


if __name__ == "__main__":
    test_albums_path = 'album_examples/'
    albums = [
        'flower_boy.jpg',
        'kids_see_ghosts.jpg',
        'mellon_collie.jpeg',
        'ram.jpg',
        'the_divine.jpeg',
        'yhlqmdlg.jpeg'
    ]
    for album_name in albums:
        print(get_palette(test_albums_path + album_name, 6))
