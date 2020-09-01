# note-parser

Putting new notes in the correct notepad is time consuming.
If you're with someone or have several ideas at once, it's preferable to put them wherever you can as quickly as possible.
Also, I personally do not trust automatic version control.

I decided that I would just use one notepad and prefix each note with where it should go.
```
todo upload funny video of my dog
```

What if I wanted to create multiple sub-notes?
```
todo upload funny video of my dog
todo/work continue to slave away
video/tutorial recipe for big salad
video/tutorial/linux make tutorial on some linux shit
```

How do we categorize these?
Ideally our script would read these notes and create the following structure, placing the content of the notes in their corresponding files:
```
notes
├── README.md
├── todo
│   └── work.md
└── video
    ├── tutorial
    │   └── linux.md
    └── tutorial.md
```

We could then manually version control our notes with git.

Perhaps if we want to view all *tutorial* notes at once, we could write a simple compilation script and render with pandoc for viewing.
> view.sh
>```bash
>python3 compile.py $1 | pandoc --to=html5 --css github.css --self-contained --metadata title="NOTES" -o tmp.html && firefox tmp.html
>```
```
./view.sh tutorial
```

We could make this faster with a function in our `~/.bashrc`.
```
view(){
	cd ~/note-parser && ./view.sh $1
}
```

If you want to edit notes directly from a web browser and are using github for version control, you can bookmark github's `go to file` option.
```
https://github.com/username/note-parser/find/master
```

## Usage
1. Clone to $HOME, delete .git folder.
1. Add notes to README.md.
1. Run parse.py at your own risk.
1. Run `./view.sh`
