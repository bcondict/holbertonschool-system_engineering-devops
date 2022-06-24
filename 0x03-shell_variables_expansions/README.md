# 0x03. Shell, init files, variables and expansions

### What is the difference between a local and a global variable
a variable is a name to the location to sotre information. global is outside of all the fucions and can be accessed globally in the program; local can be accessed only within fuction or block where they are defined.

### What is a reserved variable
These variables are set or used by Bash, but other shells do not normally treat them specially.

### How to create, update and delete shell variables
- create or defining= Names only contains letter (upper case and lower case), numbers (0 to 9) and underscore character (_). The number never should be before the letters, always after as a letter as a underscore. To define a variable you hace to put * NAME = * *** variable_name ***.

- unset or delete= one you unser a variable you can't access to the stored value in the variable. the syntax is _unset_ ***variable_name***

- access= to access the value stored in a variable prefix its name with the dollar sign ($). for example:
NAME="zarah"
echo $NAME

- read-only variables= using the read-only command the variable value cannot be changed. example:
NAME="zarah"
readonly NAME
NAME="Crist" // the script will show the following result  *this variable is read only.*

### What are the roles of the following reserved variables: HOME, PATH, PS1
- HOME= The current user's home directory; the default for the cd built-in.
- PATH=	A colon-separated list of directories in which the shell looks for commands.
- PS1= The primary prompt string. The default value is "'\s-\v\$ '".

### What are special parameters
These are special shell variables which are set internally by the shell and which are available to the user
### What is the special parameter $??
The exit status of the last command executed.
