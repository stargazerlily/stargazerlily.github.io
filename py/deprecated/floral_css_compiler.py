import shutil

css = (
    "css/style_floral.css",
    "css/style_var.css",
    "css/t_image.css",
    "css/tumblrfix.css"
)

# for doc in css:
#     with open("floral/" + doc + ".html") as f:
#         compiled=f.read()
#     with open("floral/" + doc + ".html", "w") as f:
#         f.write(compiled)

with open('css/floral_master.css','wb') as f:
    for doc in css:
        with open(doc,'rb') as fd:
            shutil.copyfileobj(fd, f)
