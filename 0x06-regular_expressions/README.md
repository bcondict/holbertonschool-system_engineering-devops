# 0x06. Regular expression
#### What is a Regular Expression?
Is an Expression used regularly, duh.
| Token | property | RegEx example | test |
| {m, n} | match exact ocurrence of a char/token | a{1,3}h | ah, aah, aaah, aaaah, h, ha, aha |
| ? | match 0 or 1 | a?h | ah, aah, aaah, aaaah, h, ha, aha |
| + | match 1 or more | a+h  | ah, aah, aaah, aaaah, h, ha, aha |
| * | match 0 or more | a*h  | ah, aah, aaah, aaaah, h, ha, aha |
| ^ | match the position at the start of the Line | ^ah  | ah, aah, ha, aha, ha<newline>ah |
| $ | match the position at the end of the Line | ah$  | ah, aah, ha, aha, ah<newline>ha |
| \A | match the position at the start of the String | \Aah | ah, aah, ha, aha, ha<newline>ah |
| \Z | match the position at the end of the String | ah\Z | ah, aah, ha, aha, ah<newline>ha |
| [a-zA-Z0-9] | match one out of several chars | gr[ea]y | grey, gray, greay |
| [a-zA-Z0-9] | match any char which is not one of those in char set | q[^u] | qatar, Iraq |
| [a-zA-Z0-9] | match repeating chars | [0-9]+ | 333, 222, 123 |
| [1st - [2nd]] | match any one char in first list but not in the second list | [0-9[02468]]+ | 1357, 124, 111 |
| \d | match nay digit | \d{1,9} |  1, 123456789, 1234235259 |
| \s | matches any whitespace char | \s+$ | \t, blanck line with spaces |
| \w | matches any word, character i.e. letters, numbers, _. | \w{1,5} | foo_1, $foo_1 |
| \D, \S, \W | matches opposite of avobe char classes | \D+ | Foobar, hello world123 |

#### where to prove it
https://rubular.com/