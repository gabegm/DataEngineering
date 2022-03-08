## Text Wrap

https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

You are given a string `S` and width `w`.

Your task is to wrap the string into a paragraph of width `w`.

## Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

* string string: a long string
* int max_width: the width to wrap to

Returns

* string: a single string with newline characters ('\n') where the breaks should be

## Input Format

The first line contains a string, `string`.
The second line contains the width, `maxwidth`.

## Constraints

```py
0 < len(string) < 1000
0 < maxwidth < len(string)
```

Sample Input 0

```
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```

Sample Output 0

```
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
```

## Solution

```py
import textwrap

def wrap(string, max_width):
    # return ''.join([string[i:i+max_width] + '\n' for i in range(len(string)) if i % 4 == 0])
    return "\n".join(textwrap.wrap(string, width=max_width))

if __name__ == '__main__':
string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4

result = wrap(string, max_width)

print(result)

assert result == "ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ", "incorrect"
```