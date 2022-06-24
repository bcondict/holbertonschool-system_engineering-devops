# 0x01. Shell, permissions
### what to do the commands _chmod_, _sudo_, _su_, _chgrp_ do
- chmod= change the access permissions of file system object, known as mode
- sudo= allows the ability to run some
- su= switch user
- chown= switch used and/or group ownership of a given file
- chgrp= change group associated with a file system object (file, directory or link)

### linux file permissions
- chmod +rwx _<filename>_ to add permissions
- chmod -rwx _<directoryname>_ to remove permissions
- chmod +x _<filename>_ to allow executable permissions
- chmod -wx _<filename>_ to take out wrte and executable permission

### linux file identities
- u= the user who owns the file 
- g= the group to wuch the user belongs
- o= other (not the owner or the owner's group
- a= everyone or all (u,g and o)

### how to represente each of the three sets of permissions (owner, group, and other) as a single digit
***IDK if this part is right, so sorry 'bout that***
this are examples how to use it
- chwon _<you>_ *some_file*
- chgrp *new_group* *some_file*
- chmod *<permission>* _<filename>_

### how to change permissions, owner and group of a file
- chown
- chgrp
- chmod

### wht can't a normal user _chown_ a file?
 becouse this change the ownership of a file or a directory, so is a root permission

### how to run a command with root privileges?
there are some posibilities
- use "su" and enter the root password when prompted
- put "sudo" in front of the command, and enter your password 
- sudo -i . ...
- sudo -s .

### how to run a command with root privileges
su command

## subgeneral
### how to create a user
useradd _<username>_

### how to create a group
groupadd _<groupname>_


bibliography
- [Ownership and Permissions] (https://mirrors.tripadvisor.com/centos-vault/4.4/docs/html/rhel-sbs-en-4/s1-navigating-ownership.html).