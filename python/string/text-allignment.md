# Text Allignment

https://www.hackerrank.com/challenges/text-alignment/problem

In Python, a string of text can be aligned left, right and center.

`.ljust(width)`

This method returns a left aligned string of length width.

```py
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
```

`.center(width)`

This method returns a centered string of length width.

```py
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
```

`.rjust(width)`

This method returns a right aligned string of length width.

```py
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
```

## Task

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

Input Format

A single line containing the thickness value for the logo.

## Constraints

```py
0 < thickness < 50
```

The thickness must be an odd number.

## Output Format

Output the desired logo.

## Sample Input

```
5
```

Sample Output

```
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
```

## Solution

```py
# Replace all ______ with rjust, ljust or center. 
def solve(thickness, c):
    assert 0 < thickness < 50, "must be between 1 and 49"
    assert thickness % 2 != 0, "must be an odd number"

    #Top Cone
    for i in range(thickness):
        print((' '*i).center(thickness-1)+c+(' '*i).center(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).______(thickness*6))    

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))    

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))

if __name__ == "__main__":
    thickness = 5
    c = 'H'

    solve(thickness, c)
```