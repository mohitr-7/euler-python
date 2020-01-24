problem = """\
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these 
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

print(problem)


def arithmetic_sum(*, initial: int, increment: int, steps: int) -> int:
    result = ((2 * initial) + ((steps - 1) * increment)) * steps // 2
    return result


sums_of_3 = arithmetic_sum(initial=3, increment=3, steps=999 // 3)
sums_of_5 = arithmetic_sum(initial=5, increment=5, steps=999 // 5)
sums_of_15 = arithmetic_sum(initial=15, increment=15, steps=999 // 15)

solution = sums_of_3 + sums_of_5 - sums_of_15

print(solution)
