import shutil


# shutil.copy("floral/floral_template.html", "floral.html")
# with open("floral.html") as f:
#     newText=f.read().replace('floral/', "")
#     newText=f.read().replace('../', "")
# with open("floral.html", "w") as f:
#     f.write(newText)

floraltags = {
    "design": "designs",
    "bouquet": "bouquets",
    "wearable": "wearables",
    "corsage": "corsage",
    "boutoinniere": "bout",
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "purple": "purple",
    "pink": "pink",
    "neutral": "neutral",
    "white": "white"
}

for key in floraltags:
    shutil.copy("floral/floral_template.html", "floral/" + key + ".html")
    with open("floral/" + key + ".html") as f:
        newText=f.read().replace('#', floraltags[key])
    with open("floral/" + key + ".html", "w") as f:
        f.write(newText)
