# Project Euler - Problem 52: Permuted Multiples
#
# Find the smallest positive integer x such that
# 2x, 3x, 4x, 5x, and 6x contain the same digits as x.


def same_digits(a, b):
    """Check if two numbers contain exactly the same digits."""
    return sorted(str(a)) == sorted(str(b))


def find_permuted_multiple():
    """
    Find the smallest x where x, 2x, 3x, 4x, 5x, 6x all have the same digits.
    """
    x = 1
    while True:
        digits_x = sorted(str(x))

        if all(sorted(str(x * i)) == digits_x for i in range(2, 7)):
            return x

        x += 1


def main():
    print("=" * 50)
    print("  Project Euler - Problem 52: Permuted Multiples")
    print("=" * 50)
    print()
    print("Finding smallest x where 2x, 3x, 4x, 5x, 6x")
    print("all contain the same digits as x...")
    print()

    result = find_permuted_multiple()

    print(f"Answer: x = {result}")
    print()
    print("Verification:")
    print("-" * 30)
    for i in range(1, 7):
        multiple = result * i
        print(f"  {i}x = {i} × {result} = {multiple}  →  digits: {''.join(sorted(str(multiple)))}")

    print()
    print(f"✓ All multiples contain the same digits: {''.join(sorted(str(result)))}")
    print("=" * 50)


if __name__ == "__main__":
    main()
