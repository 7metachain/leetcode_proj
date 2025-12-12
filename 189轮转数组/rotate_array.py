from __future__ import annotations


def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    if n <= 1:
        return
    k %= n
    if k == 0:
        return

    def rev(l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)


def _parse_ints(line: str) -> list[int]:
    # allow formats like:
    # "1 2 3", "[1,2,3]", "nums = [1, 2, 3]"
    cleaned = (
        line.replace("[", " ")
        .replace("]", " ")
        .replace(",", " ")
        .replace("nums", " ")
        .replace("=", " ")
    )
    out: list[int] = []
    for tok in cleaned.split():
        try:
            out.append(int(tok))
        except ValueError:
            continue
    return out


def _format_list(nums: list[int]) -> str:
    return "[" + ",".join(str(x) for x in nums) + "]"


def main() -> None:
    """
    Interactive stdin mode (until EOF):
    - line1: nums (space-separated, or [..], or "nums = [..]")
    - line2: k
    Output each case as: [rotated_array]
    """
    import sys

    it = iter(sys.stdin.readline, "")
    for line_nums in it:
        line_nums = line_nums.strip()
        if not line_nums:
            continue
        nums = _parse_ints(line_nums)

        line_k = next(it, "")
        if not line_k:
            break
        k_tokens = _parse_ints(line_k)
        if not k_tokens:
            continue
        k = k_tokens[0]

        rotate(nums, k)
        sys.stdout.write(_format_list(nums) + "\n")


if __name__ == "__main__":
    main()

