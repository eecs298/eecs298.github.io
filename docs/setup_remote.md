---
layout: spec
title: Setup VSCode
sitemapOrder: 20
---

Set up VS Code for Remote Development
==========================
{: .primer-spec-toc-ignore }

The university hosts remote Linux development servers open to students through CAEN. These servers can be accessed on- and off-campus via ssh. These servers are designed for interactive use, rather than long-running, high resource jobs, though they are sufficient for the work we'll be doing in this course. You can read more about these servers [on the CAEN homepage](https://caen.engin.umich.edu/connect/linux-login-service/).

Accessing them is optional for this course, but these servers may prove useful if you plan on accessing files for the course from multiple machines, such as from your laptop during lab and from your desktop at home.

## Install
VS code provides the ability to seamlessly access a remote server with the [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension.

```console
$ code --install-extension ms-vscode-remote.remote-ssh 	
```

Verify that the extension is installed. It's OK if you have other extensions installed.
```console
$ code --list-extensions
ms-vscode-remote.remote-ssh
```

## Setup
You will see a green icon appear in the bottom-left corner of the VS Code window. If it does not appear upon install, restart VS Code.

Click the green icon to open the remote extension, then select `Connect to Host...`. To access the CAEN Linux server, enter `uniqname@login-course.engin.umich.edu` in the SSH Host box, where `uniqname` is your U-M uniqname. Enter your U-M password when prompted. You will then be prompted to enter a number, 1-3, to indicate your desired 2FA method. Follow the instructions and authenticate. If you do not receive such a prompt, click `details` in the bottom-right window to show the `OUTPUT` tab.

You now have remote access to the CAEN Linux server. To open the VS Code file browser, navigate to `View` > `Explorer`, select `Open Folder`, and navigate to your home directory on the server and press `OK`. You will need to repeat the logon and 2FA process. If there is not a terminal open, navigate to `Terminal` > `New Terminal`.

Any work done on this server will be accessible from any machine equipped with ssh, from both on- and off-campus networks.

You can learn more about using the VS Code Remote - SSH extension [in this tutorial courtesy of Microsoft](https://code.visualstudio.com/docs/remote/ssh#_getting-started).
