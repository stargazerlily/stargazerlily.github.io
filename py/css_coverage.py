import json
import shutil

with open("css/index_master_minCoverage.css", "wt") as write:
    with open("py/coverage/coverage.json", "rt") as jread:
        data = json.load(jread)
        file = data[0]
        print(file)
        newString = file["text"]
        filedata = "ranges"
        for tuple in file[filedata]:
            print(tuple)
            start = int(tuple["start"])
            end = int(tuple["end"])
            write.write(newString[start:end])
