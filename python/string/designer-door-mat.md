# Designer Door Mat

https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

* Mat size must be `N` X `M`. (`N` is an odd natural number, and is `3` times `N`.)
* The design should have 'WELCOME' written in the center.
* The design pattern should only use |, . and - characters.

## Sample Designs

```
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
```

## Input Format

A single line containing the space separated values of
and `M`.

Constraints

```py
5 < N < 101
15 < M < 303
```

## Output Format

Output the design pattern.

## Sample Input

```
9 27
```

## Sample Output

```
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
```

## Solution

```py
N,M = 9,27

for i in range(N)
    for j in range(M)
        pass
```