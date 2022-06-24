# 0x04. Loops, conditions and parsing
#### Hoy to create a SSh keys
using command ssh-keygen.
- use the command ``` man ssh-keygen ``` to learn more
#### What is the advantage of using "#!/usr/bin/env bash" over "#!/bin/bash"
The #!/usr/bin/env bash shebang offers more portability because we don’t have to write the absolute path to an interpreter.

| #!/usr/bin/bash | #!/usr/bin/env bash |
--------------------
| Offers more security | Offers more portability |
| More specific, since we have to declare the exact path to an interpreter | Automatically searches for the first occurrence
of an interpreter in the environment |
| Can support extra parameters passed after the declaration of the interpreter | Cannot support extra parameters because the system reads them as a single command |
#### How to use `while`, `until` and `for` loops
- **for**: 
```
for <COINDITION> 
do
	<COMMANDS>
done
```
- **while**:
```
while <COINDITION>
do
	<COMMANDS>
done
```
- **until**:
```
until <COINDITION>
do
	<COMMANDS>
done
```
#### How to use `if`, `else`, `elif` and `case` condition statements
#### How to use the `cut` command
#### what are files and other comparison operators, and how to use them