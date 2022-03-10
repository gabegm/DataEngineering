# Nested List

https://www.hackerrank.com/challenges/nested-list/problem

Given the names and grades for each student in a class of `N` students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

## Example

```py
records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
```

The ordered list of scores is `[20.0, 50.0]`, so the second lowest score is `50.0`. There are two students with that score: `["beta", "alpha"]`. Ordered alphabetically, the names are printed as:

```
alpha
beta
```

## Input Format

The first line contains an integer, `N`, the number of students.

The `2N` subsequent lines describe each student over `2` lines.
* The first line contains a student's name.
* The second line contains their grade.

## Constraints

* `2 <= N <= 5`
* There will always be one or more students having the second lowest grade.

## Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

## Sample Input 0

```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

## Sample Output 0

```
Berry
Harry
```

## Explanation 0

There are `5` students in this class whose names and grades are assembled to build the following list:

```py
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
```

The lowest grade of `37.2` belongs to Tina. The second lowest grade of `37.21` belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

## Solution

```py
def solve(students):
    students = [[l[i], float(l[i+1])] for i in range(0, len(l), 2)]

    s = set()
    [s.add(grade[1]) for grade in students]

    second_lowest =  sorted(list(s))[1]

    return [e[0] for e in students if e[1] == second_lowest]

if __name__ == "__main__":
    l = [
        "Harry",
        "37.21",
        "Berry",
        "37.21",
        "Tina",
        "37.2",
        "Akriti",
        "41",
        "Harsh",
        "39"
    ]

    result = solve(l)

    [print(name) for name in result]
```