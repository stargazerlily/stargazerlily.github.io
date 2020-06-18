import shutil

dir = {

    "master_styles":
        ("body_header_footer",
        "colors",
        "text_styles",
        "text_boxes"),

    "index_master":
        ("master_styles",
        "style_index"),

    "art_master":
        ("master_styles",
        "t_image",
        "tumblrfix",
        "navbar",
        "style_floral"),

    "floral_master":
        ("master_styles",
        "t_image",
        "tumblrfix",
        "navbar",
        "style_floral"),

    "blog_master":
        ("master_styles",
        "tumblrfix",
        "navbar",
        "style_tblog")
}

for key in dir:
    with open("css/" + key + ".css","wt") as write:
        for file in dir[key]:
            with open("css/" + file + ".css","rt") as read:
                shutil.copyfileobj(read, write)
