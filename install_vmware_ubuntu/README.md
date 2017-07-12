# Install vmware and connect to host (June 2017)

Using a virtual machine to run linux within your Windows operating system allows you to run your analyses that require linux, while still allowing you access to useful programs like Microsoft Office. However, convincing your virtual machine (linux) and host (Windows) that they should allow you to see eachother can be challenging. Eleni (elpetrou@uw.edu) searched the interweb to put together a handy tutorial to help get you through this process.

#### 1. Download an ISO (disc image) of the latest version of Ubuntu
[https://www.ubuntu.com/download](https://www.ubuntu.com/download)


#### 2. Download and install VMWARE workstation player for windows operating systems.
[https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/12_0](https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/12_0)

#### 3. Setup new virtual machine
* Open VMWARE workstation player
* Select “Create a New Virtual Machine”
* Select “Installer disc image file” and browse to the Ubuntu iso you downloaded. 
* VMware Player Virtual Machine Wizard -> You should see that it will use Easy Install – this takes care of most of the hard work for you. Click next
* Enter your full name, username and password and hit next 
* Select the maximum disk size and type. Unless you’re planning on some really CPU intensive work inside the VM, select the “Split virtual disk into multiple files” option. Hit next when you’re happy with the settings. 
* This brings you to the confirmation page. Click “Customize Hardware” 
* In the hardware options section select the amount of memory you want the VM to use (Several GB depending on how much data you expect to put on your virtual machine). Leave everything else as it is and click Close. 
* This brings you back to the confirmation page. Click Finish this time 
* You will probably be prompted to download VMware Tools for Linux. Click “Download and Install” to continue 
* Wait for it to install 
* Ubuntu will then start to install, so keep waiting 
* When all is done you’ll be presented with the Ubuntu login screen. So enter your password and you’re on your way.

#### 4. Enable shared drive in vmware workstation player
* Select your virtual machine in VMware Player and click Edit virtual machine settings
* In the Options tab click Shared Folders in the left hand pane
* Click Always enabled in the right and pane and click Add…
* This will take you into the “Add Shared Folder Wizard” 
* Click Next and follow the prompts selecting the folder you created in Step 1
* Also name the share – this is the name that the folder will have in Ubuntu
* Click OK to close the settings
* Play the virtual machine to boot Ubuntu
* Shared folders in Ubuntu appear in the location /mnt/hgfs but you probably won’t be able to see it
* To check to see if Ubuntu is aware that there is a shared folder available run this command in a terminal window:
> vmware-hgfsclient 
* This will output the share name into the terminal window, e.g. 
> vmware-hgfsclient D

#### 5. Upgrade vmware tools
* If you navigate to /mnt/hgfs/ and you do not see the shared folder you specified above, throw a fit. Just kidding. What you need to do is install VMware Tools from within your virtual machine
* Oh, what is that? You thought you did that already? PSYCH! You didn't. 

* How to Install the VMware Tools from the Command Line with the Tar Installer

* The first steps are performed on the host, within Workstation menus:

1. Power on the virtual machine.

2. Look at the bar on top of the screen. Select "Player -> Manage -> Update VMWARE tools"
3. You will notice that ubuntu is now pretending that you loaded a cd-rom into the computer. Take a moment to seethe at this idiotic idea. 
4. Copy and paste all the file in the "cd-rom" (grr) onto the Desktop
5. Open the terminal and navigate to the Desktop (for example: cd ./Desktop)
6. Type the command *ls* to see what files are on the desktop
7. Untar (unzip) the VMware Tools tar file using this unix command
> tar zxpf ./Desktop/filename_of_vmware_tools_here.tar.gz
8. Run the VMware Tools tar installer:
> cd vmware-tools-distrib<br><br>./vmware-install.pl -d

#### 6. Rejoice (or cry)
* Restart the virtual machine
* Navigate to /mnt/hgfs and rejoice when you see your shared folders!!!!!


#### References
* [https://www.vmware.com/support/ws55/doc/ws_newguest_tools_linux.html](https://www.vmware.com/support/ws55/doc/ws_newguest_tools_linux.html)
* [http://theholmesoffice.com/how-to-share-folders-between-windows-and-ubuntu-using-vmware-player/](http://theholmesoffice.com/how-to-share-folders-between-windows-and-ubuntu-using-vmware-player/)


