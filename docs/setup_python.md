---
layout: spec
title: Python Virtual Environment
sitemapOrder: 40
---

Python/Virtual Environment Tutorial
===================================
{: .primer-spec-toc-ignore }

This document will guide you through installing Python and setting up a Python Virtual Environment.

## Install Python
Install a recent version of Python.

### macOS
{: .primer-spec-toc-ignore }

You might already have Python installed, although your version might be different.
```console
$ python3 --version
Python 3.10.8
```

If you do not have Python or your version of Python is older than 3.6, install a recent version of Python using the [Homebrew package manager](https://brew.sh/).
```console
$ brew install python3
$ python3 --version
Python 3.10.8
```

### WSL or Linux
{: .primer-spec-toc-ignore }
```console
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip python3-venv python3-wheel python3-setuptools
```

<div class="primer-spec-callout warning" markdown="1">
**Pitfall:** On the CAEN Linux servers, the package manager is `yum` insteal of `apt-get`. However, Python should be up-to-date already on these servers, so it shouldn't be an issue.
</div>

## Create a Python virtual environment
Virtual environments are used to create containers with separate installed libraries. They are useful when you want to install different Python programs that have different third party package dependencies. For example, you might have different virtual environments for different course assignments, as different courses or assignments may require different third party packages or different versions of those packages. More on venv and the creation of virtual environments [can be found here](https://docs.python.org/3/library/venv.html).

This section will help you install the Python tools and packages locally, which won't affect Python tools and packages installed elsewhere on the machine.

After finishing this section, you'll have a folder called `env/` that contains all the Python packages you need for this project.

Create a virtual environment in your project's root directory.  ())
```console
$ pwd
/creiglas/eecs298
$ python3 -m venv env
```

Activate virtual environment.  You'll need to do this every time you start a new shell.
```console
$ source env/bin/activate
```

We now have a complete local environment for Python.  Everything lives in one directory.  Environment variables point to this virtual environment.
```console
$ echo $VIRTUAL_ENV
/creiglas/eecs298/env
```

We have a Python interpreter installed inside the virtual environment.  `which python` tells you exactly which python executable file will be used when you type `python`.  Because we're in a virtual environment, there's more than one option!
```console
$ which python3     # Default python exectuable
/creiglas/eecs298/env/bin/python
$ which -a python  # All python executables
/creiglas/eecs298/env/bin/python3
/usr/local/bin/python3
/usr/bin/python3
```

There's a package manager for Python called `pip` installed in the virtual environment.  That will help us install Python packages later.
```console
$ which pip
/creiglas/eecs298/env/bin/pip
$ pip --version
pip 9.0.1 from /creiglas/eecs298/env/lib/python3.7/site-packages (python 3.7)  # Your version may be different
```

<div class="primer-spec-callout warning" markdown="1">
**Pitfall:** You may face an issue where the `python` and/or `pip` commands are not recognized on your machine even after following these steps. In this case, substitute and commands referencing these with `python3` and `pip3` to explicitly reference the executables in your Python 3.x installation.
</div>


Python packages live in the virtual environment.  We can see that Python's own tools are already installed (`pip` and `setuptools`).
```console
$ ls env/lib/python3.7/site-packages/ # Your version may be different
pip
setuptools
...
```

Upgrade the Python tools in your virtual environment
```console
$ pip install --upgrade pip setuptools wheel
```

Install `numpy`. We'll use this tool later.
```console
$ pip install numpy
```

## Understanding Virtual Environments
This section will give more detail about virtual environments and how they work.  Simply put, a virtual environment is a bunch of files (located in `env/` in this tutorial) used by Python.

### Environment
An environment is a collection of *environment variables* that are inputs to your shell and your programs.

Print the names and values of all environment variables using the `env` command.  You'll see key/value pairs used by the shell and used by programs.
```console
$ env
...
PWD=/creiglas/eecs298
HOME=/creiglas
USER=creiglas
PATH=/usr/local/bin:/usr/bin:/bin
...
```

An important example of an environment variable is `PATH`, which tells your shell where to look for commands like `ls`, `cd`, `python` and so on.  It's a colon-separated list (`:`).  You can print the value of one variable using the dollar sign '`$`'.
```console
$ echo $PATH
/usr/local/bin:/usr/bin:/bin
$ printenv PATH  # Alternative
/usr/local/bin:/usr/bin:/bin
$ echo $PATH | tr ':' '\n'
/usr/local/bin
/usr/bin
/bin
```

Notice that each item in the list is a directory that contains executables, for example `/usr/local/bin` usually contains the `python3` executable on macOS with Homebrew (`/opt/homebrew/bin` on Apple Silicon M1).
```console
$ ls /usr/local/bin
...
python3
...
```

### Environment variables inside a Python program
You can set any environment variable you want.
```console
$ export MESSAGE="hello world"
$ echo $MESSAGE
hello world
```

Environment variables are accessible from programs, like this `test.py`.
```python
"""test.py"""
import os
print(os.environ["MESSAGE"])
```

Set an environment variable and run the program.
```console
$ export MESSAGE="hello world"
$ python3 test.py
hello world
```

This example shows that environment variables are simply another way to provide input to a running program.

## Virtual environment
A virtual environment is a self-contained directory that contains a Python installation and a number of additional Python packages.

As you saw earlier, the command to create a virtual environment creates a new directory, `env` in this example.
```console
$ python3 -m venv env  # you ran this earlier
$ ls env/
bin  include  lib  pyvenv.cfg
```

The virtual environment contains a `bin/` directory with executables.  It also contains a `lib/` directory where Python third party packages live.  Your versions might be different.
```console
$ ls env/bin/
...
pip
python
...
$ ls env/lib/python3.7/site-packages/ # Your version may be different
__pycache__      pip-19.2.3.dist-info  setuptools-41.2.0.dist-info
easy_install.py  pkg_resources         pip              setuptools
```

### Activate a virtual environment
In the previous example, we used the virtual environment by calling its Python executable explicitly (e.g., `./env/bin/python`).  As a convenience, we can temporarily make this version the default.

The `bin/activate` script adds `env/bin` to the `PATH` environment variable, making it the first place to look for commands.  Notice that `/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin` is first in the list.
```console
$ source env/bin/activate
$ echo $PATH
/creiglas/eecs298/env/bin:/usr/local/bin:/usr/bin:/bin
$ echo $PATH | tr ':' '\n'
/creiglas/eecs298/env/bin
/usr/local/bin
/usr/bin
/bin
```

Ask the shell where all the `python` executables live, then which one is the default.
```console
$ which -a python
/creiglas/eecs298/env/bin/python
/usr/local/bin/python
/usr/bin/python
$ which python
/creiglas/eecs298/env/bin/python
```

Finally, the `activate` script sets a `$VIRTUAL_ENV` environment variable, which contains the path to the virtual environment directory.
```console
$ echo $VIRTUAL_ENV
/creiglas/eecs298/env
```

### Replicate a virtual environment
In the previous section, we created a Python virtual environment, activated it, and upgraded the Python installer tools (`pip`, `setuptools`, `wheel`).  We have not yet installed any new third party Python packages.
```console
$ pwd
/creiglas/eecs298/
$ echo $VIRTUAL_ENV
/creiglas/eecs298/env
$ pip list
Package    Version
---------- -------
pip        20.1.1
setuptools 47.3.1
wheel      0.34.2
```


### Deactivate a virtual environment
The `deactivate` command simply modifies two environment variables, `PATH` and `VIRTUAL_ENV`.  First, it unsets `VIRTUAL_ENV`.
```console
$ deactivate
$ echo $VIRTUAL_ENV  # Variable not set, output is blank

```

Finally, `deactivate` changes `PATH` to its previous value, before the virtual environment was activated.
```console
$ echo $PATH | tr ':' '\n'
/usr/local/bin
/usr/bin
/bin
```

## Summary
A Python virtual environment helps you manage third party packages.  A pre-configured `python` executable in `./env/bin/` uses the third party packages in `./env/lib/` (the name of `env/` is your choice).

Activate the virtual environment each time you start a new shell.
```console
$ pwd
/creiglas/eecs298/
$ source env/bin/activate
```

The `activate` script changes the `PATH` environment variable, which temporarily changes the default `python` and `pip` executables.
```console
$ which python
/creiglas/eecs298/env/bin/python
$ which pip
/creiglas/eecs298/env/bin/pip
```


## Acknowledgments
Original document written by Andrew DeOrio <awdeorio@umich.edu>.

This document is licensed under a [Creative Commons Attribution-NonCommercial 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/). You're free to copy and share this document, but not to sell it.  You may not share source code provided with this document.
