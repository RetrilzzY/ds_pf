from ascii_magic import AsciiArt

my_art = AsciiArt.from_image('dspf.jpg')

my_art.to_html_file('art.html', columns=300, width_ratio=2)