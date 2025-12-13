from __future__ import annotations


def two_sum_one_pass(nums: list[int], target: int) -> list[int]:
    # 单循环：边遍历边查
    mp: dict[int, int] = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in mp:
            return [mp[need], i]
        mp[x] = i
    return []


def two_sum_two_pass(nums: list[int], target: int) -> list[int]:
    # 双循环：先建表再匹配
    mp: dict[int, int] = {}
    for i, x in enumerate(nums):
        mp[x] = i
    for i, x in enumerate(nums):
        need = target - x
        if need in mp and mp[need] != i:
            return [i, mp[need]]
    return []


def _parse_ints(line: str) -> list[int]:
    # allow: "1 2 3", "[1,2,3]", "nums = [1, 2, 3]", "target = 9"
    cleaned = (
        line.replace("[", " ")
        .replace("]", " ")
        .replace(",", " ")
        .replace("nums", " ")
        .replace("target", " ")
        .replace("=", " ")
    )
    out: list[int] = []
    for tok in cleaned.split():
        try:
            out.append(int(tok))
        except ValueError:
            continue
    return out


def main() -> None:
    """
    Interactive stdin mode (until EOF), each case takes 2 lines:
    - line1: nums (e.g. "2 7 11 15" or "nums = [2,7,11,15]")
    - line2: target (e.g. "9" or "target = 9")

    Print indices as: [i,j]
    """
    import os
    import sys

    method = os.environ.get("TWOSUM_METHOD", "one").strip().lower()
    solver = two_sum_two_pass if method in {"two", "two_pass", "2"} else two_sum_one_pass

    it = iter(sys.stdin.readline, "")
    for line_nums in it:
        if not line_nums.strip():
            continue
        nums = _parse_ints(line_nums)
        line_target = next(it, "")
        if not line_target:
            break
        target_tokens = _parse_ints(line_target)
        if not target_tokens:
            continue
        target = target_tokens[0]

        ans = solver(nums, target)
        sys.stdout.write("[" + ",".join(map(str, ans)) + "]\n")


if __name__ == "__main__":
    main()


