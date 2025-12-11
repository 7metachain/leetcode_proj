from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = float("inf")
    max_profit = 0
    for p in prices:
        if p < min_price:
            min_price = p
        else:
            max_profit = max(max_profit, p - min_price)
    return max_profit


def main() -> None:
    import sys

    data = sys.stdin.read().strip().split()
    prices = list(map(int, data)) if data else []
    print(max_profit(prices))


if __name__ == "__main__":
    main()

