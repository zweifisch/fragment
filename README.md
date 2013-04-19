# fragment

a static site generator that generate multiple html files from a single
markdown source file devided by the headlines

e.g. `2013-04-19.md`
```markdown
# daily review

what did i enjoy doing today?

# todo

* item
* more item
```

will be splitted into two html files

```
├── daily review
│   ├── index.html
│   └── 2013-04-19.html
└── todo
    ├── index.html
    └── 2013-04-19.html
```

Why? a single file a day with every thing in it and still possible to publish
parts of it. On best to be used with vimwiki.

## usage

install via pip
```sh
pip install fragment
```

```sh
fragment gen --output /var/www/ ~/wiki/diary/
fragment -h
```
