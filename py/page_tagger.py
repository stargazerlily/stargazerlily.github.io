import shutil

pageNexus = {
    "floral": {
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
    },

    "blog": {
        "personal": "personal",
        "recipes": "recipes",
        "herbalism": "herbalism",
        "gardening": "gardening"
    },

    "art": {
        "pen": "pen",
        "posca": "posca"
    }
}

for id, tags in pageNexus.items():
    dir = id + "/"
    temp = dir + id + "_template.html"

    for key in tags:
        print("init: " + id + "/" + key)
        shutil.copy(temp, dir + key + ".html")
        with open(dir + key + ".html") as f:
            newText=f.read().replace('#', tags[key])
        with open(dir + key + ".html", "w") as f:
            f.write(newText)
