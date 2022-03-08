# Highest Value Palindrome

https://www.hackerrank.com/challenges/richie-rich/problem

Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider `0`'s left of all higher digits in your tests. For example `0110` is valid, `0011` is not.

Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.

## Example

```py
s = '1231'
k = 3
```

Make `3` replacements to get `'9339'`.

```py
s = '12321'
k = 1
```

Make `1` replacement to get `'12921'`.

## Function Description

Complete the highestValuePalindrome function in the editor below.

highestValuePalindrome has the following parameter(s):

* string s: a string representation of an integer
* int n: the length of the integer string
* int k: the maximum number of changes allowed

## Returns

* string: a string representation of the highest value achievable or -1

## Input Format

The first line contains two space-separated integers, `n` and `k`, the number of digits in the number and the maximum number of changes allowed.

The second line contains an `n`-digit string of numbers.

## Constraints



```
0 < n <= 10^5
0 <= k <= 10^5
Each character i in the number is an integer where 0 <= i <= 0.
```

## Output Format

Sample Input 0

```
STDIN   Function
-----   --------
4 1     n = 4, k = 1
3943    s = '3943'
```

Sample Output 0

```
3993
```

Sample Input 1

```
6 3
092282
```

Sample Output 1

```
992299
```

Sample Input 2

```
4 1
0011
```

Sample Output 2

```
-1
```

## Explanation

Sample 0

There are two ways to make `3943` a palindrome by changing no more than `k = 1` digits:

1. `3943 -> 3443`
2. `3943 -> 3993`

`3993 > 3443`

## Solution

```py
def solve(s, k):
    _s = list(s)

    for i,j in zip(range(((len(_s) // 2)-1), -1, -1), range((len(_s) // 2), len(_s), 1)):
        print("".join(_s))

        # while k > 0:
        if _s[i] != _s[j] and k > 0:
            k -= 1

            if _s[i] > _s[j]:
                _s[j] = _s[i]
            else:
                _s[i] = _s[j]

        if k >= 2 and _s[0] != _s[-1]:
            _s[0], _s[-1] = '9','9'
            k -= 2

    return "".join(_s) if "".join(_s) == "".join(_s)[::-1] else -1

if __name == "__main__":

result = solve('3943', 1)
assert result == '3993', "incorrect"

result = solve('092282', 3)
assert result == '992299', "incorrect"

result = solve('0011', 1)
assert result == -1, "incorrect"
```