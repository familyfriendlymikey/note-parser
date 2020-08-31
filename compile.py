from glob import glob
from sys import argv
from os.path import basename

query = '' if len(argv) == 1 else argv[1]
paths = [path for path in glob("notes/**/*.md", recursive = True) if query in path]

if paths:
    def depth(path):
        return len(path.split('/'))

    paths.sort(key=lambda path: (path, depth(path)))

    offset = min([depth(path) for path in paths]) - 1

    out = ""
    for path in paths:
        header = "#" * (depth(path) - offset)
        title = basename(path).split(".")[0].title()
        with open(path, "r") as fr:
            out += f"\n{header} {title}\n\n{fr.read()}"
    print(out)
else:
    print("No notes.")
