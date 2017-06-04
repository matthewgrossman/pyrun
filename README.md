# pyrun
Command line tool to run quick python scripts in a stream-based context

```bash
bash-3.2$ ls
README.md       main.py         main.pyc        modules.py      modules.pyc     pyrun.py        pyrun.pyc       tags
bash-3.2$ ls | python main.py -ne 'print "COMPILED" if "pyc" in _l else _l'
README.md
main.py
COMPILED
modules.py
COMPILED
pyrun.py
COMPILED
tags
```
