---
layout: spec
title: macOS Command Line Tools
---

macOS command line tools
========================
{: .primer-spec-toc-ignore }

macOS comes with a Terminal and can run UNIX command-line tools directly.

When you see `$` in this tutorial, you should type into your shell the command that comes after the `$`.

## Open terminal
Open the Terminal application which comes with macOS.

<img src="images/macos010.png" width="480px" />

## Homebrew package manager
Install the [Homebrew package manager](https://brew.sh/).
```console
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

<div class="primer-spec-callout warning" markdown="1">
Apple Silicon users ("M1", "M2", etc.) only - Homebrew installs to a non-standard location, `/opt/homebrew/`. You'll need to run the following to add Homebrew to your path:

```console
$ echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```

Close your terminal and reopen your terminal.
</div>

Check your install.  Your version might be different.
```console
$ brew --version
Homebrew 3.6.14
```

## Install CLI tools
Use the Homebrew package manager to install a few command line programs.
```console
$ brew install wget git tree
```

## Acknowledgments
Original document written by Andrew DeOrio awdeorio@umich.edu.

This document is licensed under a [Creative Commons Attribution-NonCommercial 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/). You’re free to copy and share this document, but not to sell it. You may not share source code provided with this document.
