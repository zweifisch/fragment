# fragment

static sites generator that generate multiple html files from single markdown
source file devided by the headlines

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
daily-review
	2013-04-19.html
todo
	2013-04-19.html
```

why? a single file a day with every thing in it and still possible to publish
parts of it. On best to be used with vimwiki.

## usage

```sh
fragment --output /var/www/ ~/wiki/diary/
```
