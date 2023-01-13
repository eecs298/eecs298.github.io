---
layout: spec
title: Setup VSCode
sitemapOrder: 20
---

Setup up VS Code for Python
==========================
{: .primer-spec-toc-ignore }

[Visual Studio Code](https://code.visualstudio.com/) is a lightweight, easy-to-use, source code editor with debugging support.  It runs on macOS, Windows, and Linux (including CAEN Linux).  Visual Studio Code is not the same program as Visual Studio.

<div class="primer-spec-callout info" markdown="1">
If you already have VS Code installed with the Python extension, skip to the [Create a project](#create-a-project) section.
</div>

## Prerequisites
VS Code relies on external command line tools.  If you haven't installed CLI tools on your machine yet, follow one of these tutorials first.

| [macOS](setup_macos.html)| [Windows](setup_wsl.html) | [Linux](setup_wsl.html#install-cli-tools)

Next, follow our [Command line interface (CLI)](cli.html) tutorial.

## Install
Choose your platform below. Be sure to install the relevant extensions.

### Linux
Install the .deb package at [https://code.visualstudio.com/docs/setup/linux](https://code.visualstudio.com/docs/setup/linux).

### CAEN Linux
VS Code is already installed on CAEN Linux desktop environment.  You can use it while sitting at a CAEN Linux computer, or through a [VNC connection to CAEN Linux](https://teamdynamix.umich.edu/TDClient/76/Portal/KB/ArticleDet?ID=4999).

### macOS
Make sure you have macOS 11.1 or later.
```console
$ sw_vers
ProductName:	macOS
ProductVersion:	11.7
```

Use the homebrew package manager to install VS Code. You can run this command from any directory.
```console
$ brew install --cask visual-studio-code
```

### Windows
Make sure you have updated Windows and WSL installations according to the [WSL tutorial](setup_wsl.html).

Then, Install VS Code from the web [https://code.visualstudio.com/](https://code.visualstudio.com/).

Select "Add to PATH".

<img src="images/vscode005.png" width="480px" />

Reboot.  Open a terminal again (WSL/Ubuntu) and verify your installation.  Your version might be different.

```console
$ code --version
1.74.1
1ad8d514439d5077d2b0b7ee64d2ce82a9308e5a
x64
```

### Extensions
Make sure VS Code is installed correctly by checking the version.  You need version 1.52.1 or higher.
```console
$ code --version
1.52.1
```

Install the VS Code [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
```console
$ code --install-extension ms-vscode.cpptools
```

Verify that the extension is installed.  It's OK if you have other extensions installed.
```console
$ code --list-extensions
ms-python.python
```

## Create a project
<div class="primer-spec-callout info" markdown="1">
If you plan to access course resources from multiple machines this semester, you may wish to do your development work on a remote server rather than a local machine. Learn about how to access U-M servers remotely via VS Code in the [Remote Development](setup_remote.html) tutorial.
</div>

To create a VS Code project, create a folder (directory).  There are many ways to create folders: Finder/File Explorer, the VS Code interface, VS Code integrated terminal, and the system terminal.  We'll use the system terminal and call our example project `p1-stats`.

**macOS:** Open the Terminal application.

**Windows/WSL:** Open the Ubuntu application.

Navigate to the directory where you store your projects, create a new directory, then move into the new directory. Your folder location might be different.  Here's some help with [`cd`](cli.html#cd), the [tilde `~`](cli.html#home-directory-), and [`mkdir`](cli.html#mkdir).
```console
$ mkdir ~/eecs298
$ cd ~/eecs298
$ mkdir lab1
$ cd lab1
```

<div class="primer-spec-callout warning" markdown="1">
**Pitfall:** Avoid paths that contain spaces.  Spaces causes problems with some command line tools.

| Bad Example     | Good Example   |
|-----------------|----------------|
| `EECS 298/` | `eecs298/` |
| `Lab 1/` | `lab1/` |

</div>

Start VS Code and open your project folder by selecting `File` > `Open Folder...` > navigate to your home folder.

<div class="primer-spec-callout info" markdown="1">
**Pro-tip:** Here's a quick way to open VS Code to a specific project folder from the command line.  First make sure you're in the directory that contains your source code.
```console
$ ls
main.py ...
$ code .
```
</div>

### Add new files
Select the add file icon and give it a name, e.g., `lab1.py`.

Alternatively, create your `lab1.py` file from the command line using [`touch`](cli.html#touch).

```console
$ touch main.cpp
```
You can find the built-in VS Code terminal at the bottom of the window. If there if no terminal open, start one by selecting `Terminal` > `New Terminal` and navigating to the correct location via the command line.

## Run
Use the terminal to navigate to the folder containing the Python file you wish to run. Run the file by using `python3`.

```console
$ python3 main.py
```

You can also interface with the Python interpreter interactively within

```console
$ python3
```

This will launch the Python interpreter within your terminal, which you can use to test lines of Python code. To exit the Python interpreter, use

```console
$ exit()
```

## Acknowledgments
Original document written by Andrew DeOrio awdeorio@umich.edu.

This document is licensed under a [Creative Commons Attribution-NonCommercial 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/). You’re free to copy and share this document, but not to sell it. You may not share source code provided with this document.
