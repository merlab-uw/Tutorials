# Installing and using Windows Subsystem for Linux: Ubuntu

I have a Windows 10 computer but most of the data file manipulation and pop gen programs that I want to run are better suited to a Linux environment. For that I have often used a virtual machine running Ubuntu, but there are some limitations to using a virtual machine. It is hard to move files between the desktop and the virtual machine and I have had some trouble in the past with maxing out the size of my virtual machine because the data files are so large. I was researching other options and found the Windows Subsystem Linux, which is an Ubuntu terminal that runs on the Windows side of a computer, not inside a virtual machine.

The Windows Subsystem Linux is not appropriate for everything. There are some Unix based graphical programs that don't work with it, and there might be issues with some other Unix programs failing to install or run properly. But I thought it was worth trying out because of the benefit of avoiding a virtual machine.

## **Installing Windows Subsystem for Linux: Ubuntu on Windows 10**
I followed this website to install the subsytem:
https://docs.microsoft.com/en-us/windows/wsl/install-win10

Before installing any Linux distros (short for distribution) for Windows, you must ensure that the "Windows Subsystem for Linux" optional feature is enabled. Open Windows PowerShell as Administrator. You can do this by typing PowerShell into the search bar on the task bar search field near the Windows button on the bottom of the screen, and right clicking on the program PowerShell when it appears. The menu that pops up should give the option to run as an administrator.

Run this command:

`Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`

Restart your computer when prompted.

## **Install your Linux Distribution of Choice**

If you follow the website I listed in the previous section, it has  several options for how to install your Linux distro of choice, but I downloaded Ubuntu v18.04 from the Microsoft store. You can find the Microsoft store if you search for the Microsoft store in your task bar search field.  Otherwise, here is the link to the Microsoft store distribution for [Ubuntu 18.04 LTS](https://www.microsoft.com/store/apps/9N9TNGVNDL3Q). From the store page, click on the button "Get".

The distro will download automatically. When it has finished downloading, you must initialize a new instance before you can use the terminal. Here are the website [instructions] (https://docs.microsoft.com/en-us/windows/wsl/initialize-distro) for how to do that or follow along below.

To complete the initialization, launch a new instance of the Ubuntu terminal. You can do this by clicking the "launch" button in the Microsoft Store page, or launching the distribution from the Start menu by searching for it on the bottom task bar of the desktop.

The first time a newly installed distribution runs, a terminal window will open and you'll be asked to wait for the installation to complete. Once complete, you will be prompted to create a new user account and its password.

This is what that request will look like:

![](../imgs_for_repo/04d681f2da94ec16afe50a8a83f4e5a1.png)

This user account is for the normal non-admin user that you'll be logged-in as by default when launching the Ubuntu terminal on your desktop. You can choose any username and password, they have no bearing on your Windows username. Do not include any spaces in the name.

When you open a new Ubuntu terminal instance, you won't be prompted for your password, but **if you elevate a process using *sudo*, you will need to enter your password**, so make sure you choose a password you can easily remember!

## **Installing Unix programs on Windows 10 with the Ubuntu terminal**

From this [website](https://www.howtogeek.com/265900/everything-you-can-do-with-windows-10s-new-bash-shell/)

The easiest way to install Linux software in your Ubuntu environment is with the *apt-get* or *apt* command. This command downloads and installs software from Ubuntu’s software repositories. You can also compile and install software from the source code just as you would on any Linux distribution.

From [website](https://www.howtogeek.com/261449/how-to-install-linux-software-in-windows-10s-ubuntu-bash-shell/)

*Install Windows 10’s Ubuntu-based Bash shell and you’ll have a complete Ubuntu environment that lets you install and run the same applications you could run on an Ubuntu-based Linux system. Just like on Ubuntu, though, you’ll need the apt-get command to install and update software. Note that Windows 10’s Linux subsystem doesn’t officially support graphical applications or server software (though it is possible to run some graphical applications, unofficially). Officially, it’s intended for Linux terminal applications and other command-line utilities developers might want. Windows 10’s Bash shell only supports 64-bit binaries, so you can’t install and run 32-bit Linux programs.*

First, you’ll want to run the following command to download up-to-date package lists from the software repositories.  Do this before you try to install any package:

```sudo apt-get update```

Then install the programs that you are interested in using this command. Fill in the <> with the name of your program:

```sudo apt-get install <the_program_you_want>```

For instance, I installed vcftools, samtools, and bowtie2, stacks, bwa, python and verified that perl was installed using the above command. If the output to the terminal tells you that you need to install something, or that some package is required, I would recommend just installing it.

If you are not sure what packages are available, or want to browse available packages using a search word, use the following command:

```sudo apt-cache search <your_search_word_here>```

I searched "pop" and "population" and got a fair number of results. Stacks was one of them, along with vcftools.

The following command will update the Ubuntu package catalog and upgrade any installed packages.  It should be done regularly to keep packages up to date:

```sudo apt update && sudo apt-get dist-upgrade```

*apt-get dist-upgrade* will do the same thing as *apt-get upgrade*, plus it will also intelligently handle the dependencies so it might remove obsolete packages or add new ones.  From [website](https://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do)

## **Navigating to your files with the Ubuntu terminal**

The windows subsystem Ubuntu acts as if the hard drives of your computer were mounted like external hard drives (similar to the way your desktop drives are mounted to a virtual machine). To access your hard drive folders you have to navigate to them thoughtfully.

I have the Ubuntu terminal icon pinned to my task bar to make it really easy to run Ubuntu terminal instances. When I open a new instance it looks like this, completely blank with just my user name and the name of the computer:

![](../imgs_for_repo/4d40f262bd50a0bff516a5abc87eaf5e.png)

To navigate to directories on a hard drive of the computer, you have to navigate to */mnt/* first, that is where all the hard drives are "mounted". Here use the *cd* command to get to the *mnt* directory, and then I see what my options are for hard drives:

```cd /mnt
ls```

This is how that looks in the terminal. The letters are the options that I have for hard drives:

 ![](../imgs_for_repo/d418bf1802f7dc0359cb9c00337e6164.png)

If you aren't sure which letter corresponds to which hard drive, look in Windows File Explorer, or you can just try them out one at a time.

```
cd <hard_drive_letter_choice>
ls
```

![](../imgs_for_repo/5207e8f002f01a6b7e8ecd12ebb56c76.png)

Besides navigating through the */mnt/* directory to access your hard drives, the rest of the experience is typical of an Ubuntu/Unix environment.

**Here are some of the websites I found useful:**
-https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/
-https://dev.to/david_j_eddy/run-linux-gui-applications-on-windows-10-3130
-https://devblogs.microsoft.com/commandline/do-not-change-linux-files-using-windows-apps-and-tools/
-https://blogs.msdn.microsoft.com/wsl/2016/04/22/windows-subsystem-for-linux-overview/
-https://docs.microsoft.com/en-us/windows/wsl/initialize-distro
-https://docs.microsoft.com/en-us/windows/wsl/faq
