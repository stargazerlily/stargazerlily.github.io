import shutil

blogtags = {

}

for key in blogtags:
    shutil.copy("blog/blog_template.html", "blog/" + key + ".html")
    with open("blog/" + key + ".html") as f:
        newText=f.read().replace('#', blogtags[key])
    with open("blog/" + key + ".html", "w") as f:
        f.write(newText)
