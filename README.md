# poet-jupyter
An initial directory setup for jupyter notebook integration with django

Setting needed in vscode:
```
"jupyter.runStartupCommands": [
    "%load_ext autoreload\n%autoreload 2",
    "import os,sys;sys.path.insert(0, os.environ.get('POET_PROJECT_PATH'))",
    "from py_local.django import jupyter_setup"
]
```
