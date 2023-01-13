---
layout: spec
title: Command Line Interface (CLI)
excludeFromSitemap: true
---

Command Line Interface (CLI)
============================
{: .primer-spec-toc-ignore }

This is a brief tutorial of command line interface basics.

The *GUI* (Graphic User Interface) is a "point and click" way to interact with a computer.  The Windows File Explorer and macOS Finder are examples of GUIs.

The *CLI* (Command Line Interface) is a text-based way to interact with a computer.  The terminal is another name for the CLI.  On the Windows Subsystem for Linux (WSL) it might be called "Ubuntu".  The CLI is fast, easy to automate, and easy to use remotely.

<img src="images/cli001.png" class="invert-colors-in-dark-mode" width=600px alt="gui vs cli"/>

## Prerequisites
If you're on Windows or macOS and haven't installed CLI tools on your machine yet, follow one of these tutorials first.  Linux users have CLI tools installed by default.

| [macOS](setup_macos.html)| [Windows](setup_wsl.html) |

## Keywords

A *file* stores data like C++ source code (`main.py`) or plain text (`example.txt`).

A *directory* contains files and other directories.  It's also called a folder.

A *path* is the location of a file or directory.  Sometimes we end a directory path with `/`.  For example:
```
/Users/ohjun/Desktop/project/main.py
/Users/ohjun/Desktop/project/stuff/
```
{: data-variant="no-line-numbers" }

## Basic Commands

### `ls`
`ls` prints files and directories in the present working directory.


  <td markdown="1" >

  ```console
  $ ls
  example.txt main.py stuff
  ```

  </td>



<div class="primer-spec-callout info" markdown="1">
**Pro-tip:** Colorize the output of `ls` to tell files and directories apart ([instructions](#colorize-ls-output)).

<img src="images/cli026.png" class="invert-colors-in-dark-mode" width="768px" alt="colorized ls example"/>
</div>

### `tree`
`tree` recursively prints files and directories.  `tree` is useful for comparing your files against a project spec.

```console
$ tree
.
├── example.txt
├── main.py
└── stuff
    └── hello.txt
```

<div class="primer-spec-callout warning" markdown="1">
**Pitfall:** You may need to install `tree`.
```console
$ sudo apt install tree  # WSL, Linux
$ brew install tree      # macOS
```
</div>

### `pwd`
`pwd` prints the path of the present working directory.


  <tr>
  <td markdown="1">

  ```console
  $ pwd
  /Users/creiglas/Desktop/project
  ```

  </td>

  </tr>

### `mkdir`
`mkdir` creates a directory.


  <tr>
  <td markdown="1">

  ```console
  $ mkdir newfolder
  ```

  </td>

  </tr>


### `touch`
`touch` creates an empty file.


  <tr>
  <td markdown="1">

  ```console
  $ touch newfile.py
  ```

  </td>

  </tr>


### `rm`
`rm` removes (deletes) a file.

`rm -rf` removes a directory. The `rm` command deletes files without requiring confirmation and without the option to undo, so be careful!
  <tr>
  <td markdown="1">

  ```console
  $ rm oldfile.py
  $ rm -rf oldfolder/
  ```

  </td>
  </tr>

### `cd`
`cd` changes directory. You can use `cd ~` to return to your home directory and `cd ..` to move up in the file tree. Check out the [Special Paths](#special-paths) section for more.

  <tr>
  <td markdown="1">

  ```console
  $ cd stuff/
  ```

  </td>
  </tr>

### `mv`
`mv` moves a file or directory into a different directory.

  <tr>
  <td markdown="1">

  ```console
  $ mv main.py projects/
  ```

  </td>
  </tr>

`mv` is also the preferred way to rename a file or directory.

  <tr>
  <td markdown="1">

  ```console
  $ mv oldname.txt newname.txt
  ```

  </td>
  </tr>

### `cp`
`cp` copies a file.

  <tr>
  <td markdown="1">

  ```console
  $ cp main.py projects/
  ```

  </td>
  </tr>

### `open` / `wslview`
On macOS, `open` opens a file or directory with the default application, like a double click ([docs](https://ss64.com/osx/open.html)).

On WSL (Windows), `wslview` opens a file or directory with the default application, like a double click ([docs](https://wslutiliti.es/wslu/man/wslview.html)).

<video controls autoplay loop style="width: 100%; max-width: 640px; max-height: 480px;" class="invert-colors-in-dark-mode">
  <source src="images/cli_vid002.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

<div class="primer-spec-callout warning" markdown="1">
**WSL Pitfall:** You may need to install `wslu`, which includes `wslview`.
```console
$ sudo apt install wslu
```
</div>

## Tips and Tricks

### `clear` <kbd>Control</kbd> + <kbd>l</kbd>
`clear` the terminal.  Pro-tip: <kbd>Control</kbd> + <kbd>l</kbd>.  That's a lowercase L.

<video controls autoplay loop style="width: 100%; max-width: 640px; max-height: 480px;" class="invert-colors-in-dark-mode">
  <source src="images/cli_vid003.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tab complete <kbd>TAB</kbd>
<kbd>TAB</kbd> autocompletes a file or directory name.

Type the first part of a filename, then press <kbd>TAB</kbd>.  Press again to show multiple completion options.
```console
$ cd ~/src/eecs2  # Press TAB twice to see options
eecs280/     eecs281/     eecs298/
```

<video controls autoplay loop style="width: 100%; max-width: 640px; max-height: 480px;" class="invert-colors-in-dark-mode">
  <source src="images/cli_vid004.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Previous Command <kbd>⬆</kbd>
<kbd>⬆</kbd> (the up arrow key) cycles through previous commands. The down arrow key can then cycle in the opposite direction.

<video controls autoplay loop style="width: 100%; max-width: 640px; max-height: 480px;" class="invert-colors-in-dark-mode">
  <source src="images/cli_vid005.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Colorize `ls` output
Colorize the output of `ls` so it's easy to tell the difference between files and directories.

<img src="images/cli026.png" class="invert-colors-in-dark-mode" width="768px" alt="colorized ls example"/>

#### Windows/WSL and Linux (Bash shell)
{: .primer-spec-toc-ignore }

Verify you're using the Bash shell, which is typical on WSL Ubuntu Linux.
```console
$ echo $0
-bash
```
{: data-variant="no-line-numbers" }

Edit your shell customization file.
```console
$ touch ~/.bash_profile  # Create file if it doesn't exist
$ wslview ~/.bash_profile
```
{: data-variant="no-line-numbers" }

<div class="primer-spec-callout warning" markdown="1">
**WSL Pitfall:** You may need to install `wslu`, which includes `wslview`.
```console
$ sudo apt install wslu
```
</div>

Add this line.  Whenever you type `ls`, you'll actually get `ls --color`, which adds color.
```bash
alias ls='ls --color'
```
{: data-variant="no-line-numbers" data-title="~/.bash_profile" }

Close your terminal and reopen it.  You should see colorized `ls` output.

<img src="images/cli027.png" class="invert-colors-in-dark-mode" width="512px" alt="colorized ls WSL example"/>

#### macOS (Z shell)
{: .primer-spec-toc-ignore }

Verify you're using the Z shell, which is typical on macOS.
```console
$ echo $0
zsh
```
{: data-variant="no-line-numbers" }

Edit your shell customization file
```console
$ open ~/.zshrc
```
{: data-variant="no-line-numbers" }

Add this line.  Whenever you type `ls`, you'll actually get `ls -G`.
```bash
alias ls='ls -G'
```
{: data-variant="no-line-numbers" data-title="~/.zshrc" }

Close your terminal and reopen it.  You should see colorized `ls` output.

<img src="images/cli028.png" class="invert-colors-in-dark-mode" width="512px" alt="colorized ls macOS example"/>

### Customize prompt
Customize the terminal prompt to be more helpful and look prettier.

First, complete the [Colorize `ls` output](#colorize-ls-output) section. At this point, you should know whether you are using Bash or Z Shell, and you should have a working `.bash_profile` or `.zshrc` file.

#### Windows/WSL and Linux (Bash shell)
{: .primer-spec-toc-ignore }

Add a line to your `.bash_profile` file that sets the `PS1` environment variable.
```bash
export PS1='\[\e[0;32m\][\u] \[\e[0;34m\]\w/ \[\e[01;34m\]$ \[\e[0m\]'
```
{: data-variant="no-line-numbers" data-title="~/.bash_profile" }

Close your terminal and reopen it.  It should look like this.  For more, check out [this guide](https://medium.com/@adamtowers/how-to-customize-your-terminal-and-bash-profile-from-scratch-9ab079256380).

<img src="images/cli029.png" class="invert-colors-in-dark-mode" width="768px" alt="customized bash example"/>

#### macOS (Z shell)
{: .primer-spec-toc-ignore }

Add a line to your `.zshrc` file that sets the `PS1` environment variable.
```zsh
PROMPT='%F{green}[%n] %F{blue}%~%f %B%F{blue}$%f%b '
```
{: data-variant="no-line-numbers" data-title="~/.zshrc" }

Close your terminal and reopen it.  It should look like this.  For more, check out [this guide](https://shah22j.medium.com/how-to-customize-your-zsh-terminal-on-your-own-81f947ca2f12).

<img src="images/cli030.png" class="invert-colors-in-dark-mode" width="768px" alt="customized zsh example"/>

## Special Paths
A *path* is the location of a file or directory.

### Current directory `.`
`.` refers to the current directory.

For example, you might open the current directory in the Finder (File Explorer).
```console
$ open .     # macOS
$ wslview .  # Windows/WSL
```

### Parent directory `..`
`..` refers to the parent directory of the current directory.

```console
$ pwd
/Users/creiglas/Desktop/project/stuff
$ cd ..
$ pwd
/Users/creiglas/Desktop/project
```

### Home directory `~`
`~` refers to your home directory.

```console
$ cd ~
$ pwd
/Users/creiglas
$ ls
Applications Pictures Desktop ...
```

### Root directory `/`
`/` refers to the root directory. This is the top-most directory in your file system, and has no parent.

```console
$ ls /
Applications cores sbin ...
```

### Absolute Path
An *absolute path* starts from the root directory `/`.

For example, sometimes it's useful to make sure the *exact* file is correct.
```console
$ /usr/local/bin/python3  # One version of Python
$ /usr/bin/python3        # Another version of Python
```

### Relative Path
A *relative path* starts from the current directory.

For example, running an executable.
```console
$ python3 ./main.py
```

### Glob `*`
A *glob* is a wildcard path that may match multiple paths.  The `*` symbol matches any string.

```console
$ ls *.py
```

## More commands
This section contains some more useful commands.

### `wget`
`wget` downloads a file from the internet.

```console
$ wget https://tacobell.com/menu.pdf
$ ls
menu.pdf
```

### `tar`
`tar` unpacks an archive ending in `.tar.gz`.

```console
$ tar -xvzf archive.tar.gz
starter-files/
...
$ tree
.
├── archive
│   ├── file1.txt
│   ├── file2.txt
└── archive.tar.gz
```

### `diff`
`diff` compares two files. No output means the files are identical.
```console
$ diff oldfile.py newfile.py
```

### `cat`
`cat` prints the contents of files to the terminal.

```console
$ cat shapes.py
import numpy as np

def get_circumference(radius):
    diameter = 2*radius
    circumference = diameter*np.pi
    return circumference

...
```

### `grep`
`grep` searches inside a file.  It's short for "Globally search for a REgular expression and Print matching lines".

Search for `circumference` in `shapes.py`.
```console
$ grep circumference shapes.py
def get_circumference(radius):
    circumference = diameter*np.pi
    return circumference
```

Search for `circumference` in all `.py` files.  This example also uses a [glob (`*`)](#glob-).
```console
$ grep circumference *.py
shapes.py: def get_circumference(radius):
shapes.py:    circumference = diameter*np.pi
shapes.py:    return circumference
main.py: from shapes import get_circumference
main.py:    circumference = get_circumference(radius)

...
```

## Shell scripting
A *shell script* is a file that contains commands.  Shell scripts are useful for automating things like running test cases. Learn more at the [EECS 485 Shell Scripting Tutorial](https://eecs485staff.github.io/p1-insta485-static/setup_scripting.html).


## Acknowledgments
Original document written by Andrew DeOrio awdeorio@umich.edu and Oh Jun Kweon ohjun@umich.edu.

This document is licensed under a [Creative Commons Attribution-NonCommercial 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/). You’re free to copy and share this document, but not to sell it. You may not share source code provided with this document.
