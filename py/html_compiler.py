import shutil

dir = {

    "index":
        ("index/head",
        "index/body"
        ),

    "floral":
        ("master_styles",
        "style_index")
}

for key in dir:
    with open(key + ".html","wt") as write:
        for file in dir[key]:
            with open("html/" + file + ".html","rt") as read:
                shutil.copyfileobj(read, write)
    # with open(key + "/" + key + "_template.html","wt") as write:
    #     for file in dir[key]:
    #         with open("html/" + file + ".html","rt") as read:
    #             shutil.copyfileobj(read, write)
