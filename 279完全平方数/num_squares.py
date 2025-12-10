def num_squares(n: int) -> int:
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1

    dp = [0] + [float("inf")] * n

    for i in range(1, n + 1):
        for sq in squares:
            if sq > i:
                break
            dp[i] = min(dp[i], dp[i - sq] + 1)

    return dp[n]


def main() -> None:
    import sys

    for line in sys.stdin:
        tokens = line.strip().split()
        for token in tokens:
            try:
                n = int(token)
            except ValueError:
                continue
            print(num_squares(n))


if __name__ == "__main__":
    main()

