# Project Euler - Problem 52: Permuted Multiples

## Problem Statement

It can be seen that the number 125874, and its double 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer **x** such that **2x, 3x, 4x, 5x, and 6x**
contain the same digits.

## Approach

- Iterate over every positive integer x starting from 1
- For each x, sort its digits and compare with sorted digits of 2x, 3x, 4x, 5x, 6x
- Stop at the first x where all multiples share the same digit set

## Run

```bash
python solution.py
```

## Answer

**x = 142857**

## Verification

| Multiple | Value  | Digits    |
|----------|--------|-----------|
| 1x       | 142857 | 1,2,4,5,7,8 |
| 2x       | 285714 | 1,2,4,5,7,8 |
| 3x       | 428571 | 1,2,4,5,7,8 |
| 4x       | 571428 | 1,2,4,5,7,8 |
| 5x       | 714285 | 1,2,4,5,7,8 |
| 6x       | 857142 | 1,2,4,5,7,8 |

## Requirements

No external libraries — uses Python standard library only.
