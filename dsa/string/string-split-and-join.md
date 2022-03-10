# String Split and Join

https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

In Python, a string can be split on a delimiter.

Example:

```py
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
```

Joining a string is simple:

```py
>>> a = "-".join(a)
>>> print a
this-is-a-string 
```

Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

## Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

* string line: a string of space-separated words

Returns

* string: the resulting string

## Input Format

The one line contains a string consisting of space separated words.

Sample Input

`this is a string   `

Sample Output

`this-is-a-string`

## Solution

```py
def split_and_join(line):
    return '-'.join(line.lstrip(' ').rstrip(' ').split(' '))

if __name__ == '__main__':
    line = "this is a string   "

    result = split_and_join(line)

    print(result)

    assert result == "this-is-a-string", "incorrect"
```