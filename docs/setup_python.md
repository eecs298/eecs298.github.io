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

If you do not have Python or your version of Python is older than 3.8, install a recent version of Python using the [Homebrew package manager](https://brew.sh/). 
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

## Create a Python virtual environment
This section will help you install the Python tools and packages locally, which won't affect Python tools and packages installed elsewhere on your computer.

After finishing this section, you'll have a folder called `env/` that contains all the Python packages you need for this project.

<div class="primer-spec-callout warning" markdown="1">
**Pitfall:** Python 3.8 or later is required.  Your version might be different.
```console
$ python3 --version
Python 3.9.4
```
</div>

<div class="primer-spec-callout warning" markdown="1">
**Pitfall:** Do not use the version of Python provided by Anaconda.
```console
$ which python3
/Users/awdeorio/anaconda/bin/python3
```

**Option 1 (recommended):** Permanently deactivate Anaconda.  After running this command, close your shell and reopen it.
```console
$ conda init --reverse
```

Close your shell and open a new shell.  Your path might be different.
```console
$ which python3
/usr/local/bin/python3  # NOT anaconda
```

**Option 2:** Temporarily deactivate Anaconda.  You'll have to do this every time you start a new shell.  Your path might be different.
```console
$ conda deactivate
$ which python3
/usr/local/bin/python3  # NOT anaconda
```

**Option 3:** Uninstall Anaconda completely ([docs](https://docs.anaconda.com/anaconda/install/uninstall/)).
```console
$ conda install anaconda-clean
$ anaconda-clean --yes
```

Close your shell and open a new shell.  Your path might be different.
```console
$ which python3
/usr/local/bin/python3  # NOT anaconda
```

**Option 4:** Manually deactivate Anaconda.  If none of the above options work, then this one will.

Figure out which hidden shell startup file contains the Anaconda initialization code.
```console
$ pwd
/Users/awdeorio
$ grep -s conda .profile .bashrc .bash_profile .zshrc .zlogin .cshrc .tshrc .login
.bash_profile:# >>> conda initialize >>>
.bash_profile:# !! Contents within this block are managed by 'conda init' !!
...
```

In this case, the file to edit is `.bash_profile`.  Yours might be different.  Use any text editor.  If you're using VS Code, here's a shortcut.  Remember, your filename might be different.
```console
$ code .bash_profile
```

Remove everything you find about Anaconda and save the file.  In this case, we'll delete a chunk that looks like this.
```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/usr/local/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/usr/local/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/usr/local/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/usr/local/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

Close your shell and open a new shell.  Your path might be different.
```console
$ which python3
/usr/local/bin/python3  # NOT anaconda
```
</div>

<div class="primer-spec-callout warning" markdown="1">
**Pitfall:** If the `PYTHONPATH` environment variable is set, it can cause problems.
```console
$ printenv PYTHONPATH  # Output isn't blank, problem!
/Users/awdeorio/local/lib/python3.9/site-packages/
```

**Option 1 (recommended):** Permanently remove the environment variable.  Variables are usually set in your shell initialization file.  Check these files to see if they set the offending variable: `.profile`, `.bashrc`, `.bash_profile`, `.zshrc`, `.zprofile`, `.cshrc`, `.tcshrc`, `.login`.  Delete or comment out any line that contains `PYTHONPATH`.
```bash
$ pwd
/Users/awdeorio
$ grep -s PYTHONPATH .profile .bashrc .bash_profile .zshrc .zlogin .cshrc .tshrc .login
.bashrc: export PYTHONPATH=/Users/awdeorio/local/lib/python3.9/site-packages/

# Edit the file and remove the line.  Ask us if you need help.

# Close your shell and open a new shell

$ printenv PYTHONPATH  # output should be blank
```

**Option 2:** Temporarily unset the `PYTHONPATH` environment variable.  You'll have to do this every time you start a new shell.
```console
$ env --unset PYTHONPATH
$ printenv PYTHONPATH  # output should be blank
```

</div>

Create a virtual environment in your project's root directory.  (More on [venv and the creation of virtual environments](https://docs.python.org/3/library/venv.html))
```console
$ pwd
/Users/awdeorio/src/eecs485/p1-insta485-static
$ python3 -m venv env
```

Activate virtual environment.  You'll need to do this every time you start a new shell.
```console
$ source env/bin/activate
```

We now have a complete local environment for Python.  Everything lives in one directory.  Environment variables point to this virtual environment.
```console
$ echo $VIRTUAL_ENV
/Users/awdeorio/src/eecs485/p1-insta485-static/env
```

We have a Python interpreter installed inside the virtual environment.  `which python` tells you exactly which python executable file will be used when you type `python`.  Because we're in a virtual environment, there's more than one option!
```console
$ which python3     # Default python exectuable
/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin/python
$ which -a python  # All python executables
/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin/python3
/usr/local/bin/python3
/usr/bin/python3
```

There's a package manager for Python installed in the virtual environment.  That will help us install Python packages later.
```console
$ which pip
/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin/pip
$ pip --version
pip 9.0.1 from /Users/awdeorio/src/eecs485/p1-insta485-static/env/lib/python3.7/site-packages (python 3.7)  # Your version may be different
```

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

Install HTML5 Validator. We'll use this tool later.  Your version might be different.
```console
$ pip install html5validator
$ html5validator --version
html5validator 0.3.1
```

## `.gitignore` and Python virtual environment
Do not commit virtual environment files (`env/`) to version control.  This is because `pip` installs binaries inside `env/`.  Those binaries will be different on different operating systems and even different computers running the same OS but using different compilers.

The sample `.gitignore` file you added ignores directories called `env/`.
```console
$ ls
README.md  env
$ git status
On branch main
nothing to commit, working tree clean
```

You made a mistake in your `.gitignore` if you see your Python virtual environment folder as an untracked file.
```console
$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	env/

nothing added to commit but untracked files present (use "git add" to track)
```

<div class="primer-spec-callout info" markdown="1">
**Pro-tip:** Clean your repo, removing all untracked and git-ignored files with `git clean`.
```console
$ git clean -xdi
Would remove the following item:
  env/
*** Commands ***
    1: clean                2: filter by pattern    3: select by numbers    4: ask each
    5: quit                 6: help
What now> 1
Removing env/
```
</div>

## Understanding Virtual Environments
This section will give more detail about virtual environments and how they work.  Simply put, a virtual environment is a bunch of files (located in `env/` in this tutorial) used by Python.

### Environment
An environment is a collection of *environment variables* that are inputs to your shell and your programs.

Print the names and values of all environment variables using the `env` command.  You'll see key/value pairs used by the shell and used by programs.
```console
$ env
...
PWD=/Users/awdeorio/src/eecs485/p1-insta485-static
HOME=/Users/awdeorio
USER=awdeorio
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

A pre-configured `pip` executable installs third party packages to `lib/`.  Your versions of Python and jinja2 may be different.
```console
$ ./env/bin/pip install jinja2
Successfully installed jinja2-2.11.1
$ ls env/lib/python3.7/site-packages/jinja2/ # Your version may be different
__init__.py
...
```

A pre-configured `python` executable in `bin/` uses the third party packages in `lib/`.
```console
$ ./env/bin/python
>>> import jinja2
>>> jinja2.__version__
'2.11.1'
```

### Why virtual environments?
Virtual environments are useful when you want to install different Python programs that have different third party package dependencies.  For example, you might have a virtual environment for a web course's project, and a different one for your machine learning course's homework assignments.  The two assignments have different third party packages and different versions of those packages.

### Activate a virtual environment
In the previous example, we used the virtual environment by calling its Python executable explicitly (e.g., `./env/bin/python`).  As a convenience, we can temporarily make this version the default.

The `bin/activate` script adds `env/bin` to the `PATH` environment variable, making it the first place to look for commands.  Notice that `/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin` is first in the list.
```console
$ source env/bin/activate
$ echo $PATH
/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin:/usr/local/bin:/usr/bin:/bin
$ echo $PATH | tr ':' '\n'
/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin
/usr/local/bin
/usr/bin
/bin
```

Ask the shell where all the `python` executables live, then which one is the default.
```console
$ which -a python
/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin/python
/usr/local/bin/python
/usr/bin/python
$ which python
/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin/python
```

Finally, the `activate` script sets a `$VIRTUAL_ENV` environment variable, which contains the path to the virtual environment directory.
```console
$ echo $VIRTUAL_ENV
/Users/awdeorio/src/eecs485/p1-insta485-static/env
```

### Replicate a virtual environment
In the previous section, we created a Python virtual environment, activated it, and upgraded the Python installer tools (`pip`, `setuptools`, `wheel`).  We have not yet installed any new third party Python packages.
```console
$ pwd
/Users/awdeorio/src/eecs485/p1-insta485-static
$ echo $VIRTUAL_ENV
/Users/awdeorio/src/eecs485/p1-insta485-static/env
$ pip list
Package    Version
---------- -------
pip        20.1.1
setuptools 47.3.1
wheel      0.34.2
```

A `requirements.txt` file lists the exact third party Python packages and their versions needed to replicate another virtual environment.  This is useful for ensuring that developers and production servers have identical packages with identical versions.  It's also useful for ensuring that students and the autograder have identical packages with identical versions.

See the list of package dependencies provided in a `requirements.txt` file. This `requirements.txt` file is bundled with project starter files, so please download the appropriate project starter files before proceeding.  Your output might be different.
```console
$ cat requirements.txt
astroid==2.4.2
...
zipp==3.1.0
```

Install the package dependencies.  Your output might be different.
```console
$ pip install -r requirements.txt
...
Successfully installed astroid-2.4.2 ... zipp-3.1.0
$ pip list
Package            Version
------------------ ---------
astroid            2.4.2
...
zipp               3.1.0
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
/Users/awdeorio/src/eecs485/p1-insta485-static
$ source env/bin/activate
```

The `activate` script changes the `PATH` environment variable, which temporarily changes the default `python` and `pip` executables.
```console
$ which python
/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin/python
$ which pip
/Users/awdeorio/src/eecs485/p1-insta485-static/env/bin/pip
```


## Acknowledgments
Original document written by Andrew DeOrio <awdeorio@umich.edu>.

This document is licensed under a [Creative Commons Attribution-NonCommercial 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/). You're free to copy and share this document, but not to sell it.  You may not share source code provided with this document.
