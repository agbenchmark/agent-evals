import art

ascii_art = art.text2art("Hello!")
with open("ascii_art.txt", "w") as f:
    f.write(ascii_art)
