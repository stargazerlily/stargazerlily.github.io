import shutil

dir = {

    "master_styles":
        ("body_header_footer",
        "colors",
        "text_styles",
        "text_boxes"),

    "index_master":
        ("style_index",
        "master_styles"),

    "floral_master":
        ("style_floral",
        "master_styles",
        "t_image",
        "tumblrfix"),

    "blog_master":
        ("style_tblog",
        "master_styles",
        "tumblrfix")
}

for key in dir:
    with open("css/" + key + ".css","wb") as write:
        for file in dir[key]:
            with open("css/" + file + ".css","rb") as read:
                shutil.copyfileobj(read, write)
