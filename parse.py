from glob import glob
from collections import defaultdict
from os import makedirs
from os.path import dirname, basename

with open("README.md", "r") as fr:
    readme = [line.strip() for line in fr if line.strip()]

# notes[title][content]
notes = defaultdict(lambda: {'count': 0, 'content': []})

for note in readme:
    note = note.split(" ", 1)

    if len(note) != 2:
        print(f"INCORRECT LENGTH: {note}")
        continue

    title = note[0].lower()
    notes[title]["count"] += 1
    notes[title]["content"].append(note[1])

for title, _ in sorted(notes.items(), key=lambda item: item[1]["count"]):
    count = notes[title]["count"]
    print(f"{title:20} {count:5}")

print(f"\nTotal notes: {len(readme)}\n")

if input("Are you okay with this? [y/n]") == "y":
    for title in notes:
        path = f"notes/{title}.md"
        makedirs(dirname(path), exist_ok=True)
        amount = len(notes[title]["content"])
        out = "\n" + "\n\n".join(notes[title]["content"]) + "\n\n"

        print(f"Writing {amount} notes to {path}...")
        with open(path, "a") as fw:
            fw.write(out)

    print("\nChecking...")
    cum = []
    for f in glob("notes/**/*.md", recursive = True):
        print(f)
        with open(f, "r") as fr:
            cum += [line.strip().lower() for line in fr if line.strip()]
    for linenum, line in enumerate(readme, 1):
        if line.lower().split(' ', 1)[1] not in cum:
            print(f"NOTE {linenum} LOST: {line[:40].lower()}...")
    print("Done.")

else:
    print("Cancelled.")
