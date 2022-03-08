## Absolute Salary Difference

import string
import random
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

def random_char(n: int) -> string:
    return ''.join(random.sample(string.ascii_lowercase, 5))

def percentage_change(col1:Series, col2:Series) -> Series:
    return ((col2 - col1) / col1) * 100

"""
Write a query that calculates the difference between the highest salaries found in the marketing
and engineering departments. Output just the absolute difference in salaries.
"""
def get_abs_salary_difference(df_employee: DataFrame, dept_ids: list) -> DataFrame:
    assert len(dept_ids) == 2, "2 Department IDs required"

    diff = abs(
        df_employees[df_employees["dept_id"] == dept_ids[0]]["salary"].max() -
        df_employees[df_employees["dept_id"] == dept_ids[1]]["salary"].max()
    )

    return diff

def get_departments(n_departments: int) -> DataFrame:
    cols = {"id": np.int64, "department": object}

    id = np.arange(1, n_departments+1, dtype=np.int64).reshape(-1,1)
    department = np.array([random_char(5) for _ in range(n_departments)]).reshape(-1,1)

    a = np.hstack((id, department))

    df = DataFrame(a, columns=list(cols.keys())).astype(cols)

    return df

def get_employees(n_employees:int, n_departments:int) -> DataFrame:
    cols = {"id": np.int64, "fist_name": object, "last_name":object, "salary": np.int64, "dept_id": np.int64}

    id = np.arange(1, n_employees+1, dtype=np.int64).reshape(-1,1)
    first_name = np.array([random_char(5) for _ in range(n_employees)]).reshape(-1,1)
    last_name = np.array([random_char(5) for _ in range(n_employees)]).reshape(-1,1)
    salary = np.array([np.random.randint(26000, 100000) for _ in range(n_employees)], dtype=np.int64).reshape(-1,1)
    dept_id = np.array([np.random.randint(1, n_departments+1) for _ in range(n_employees)], dtype=np.int64).reshape(-1,1)

    a = np.hstack((id, first_name, last_name, salary, dept_id))

    df = DataFrame(a, columns=list(cols.keys())).astype(cols)

    return df

if __name__ == "__main__":
    n_employees = 100
    n_departments = 10

    df_employees = get_employees(n_employees, n_departments)
    df_departments = get_departments(n_departments)

    abs_salary_differenc = get_abs_salary_difference(df_employees, dept_ids=[2, 4])

