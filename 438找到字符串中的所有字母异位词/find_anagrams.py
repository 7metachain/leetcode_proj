"""
438. 找到字符串中所有字母异位词 —— 本地可运行版本 (Python3)

输入格式（每组两行，直到 EOF 退出）：
  第 1 行：字符串 s
  第 2 行：字符串 p

输出：异位词起始索引列表，如 [0,6]
"""

from __future__ import annotations


def find_anagrams(s: str, p: str) -> list[int]:
    """频次 + 滑动窗口，O(n) 时间"""
    result: list[int] = []
    n, m = len(s), len(p)
    if n < m:
        return result

    pattern_freq = [0] * 26
    window_freq = [0] * 26

    # 统计 p 的字符频次
    for ch in p:
        pattern_freq[ord(ch) - ord("a")] += 1

    # 初始化第一个窗口
    for i in range(m):
        window_freq[ord(s[i]) - ord("a")] += 1

    if window_freq == pattern_freq:
        result.append(0)

    # 滑动窗口
    for right in range(m, n):
        # 加入新字符
        window_freq[ord(s[right]) - ord("a")] += 1
        # 移除旧字符
        window_freq[ord(s[right - m]) - ord("a")] -= 1
        # 检查是否匹配
        if window_freq == pattern_freq:
            result.append(right - m + 1)

    return result


def _format_output(indices: list[int]) -> str:
    return "[" + ",".join(str(i) for i in indices) + "]"


def main() -> None:
    import sys

    lines = sys.stdin.read().splitlines()
    i = 0
    while i + 1 < len(lines):
        s = lines[i].strip()
        p = lines[i + 1].strip()
        if s and p:
            result = find_anagrams(s, p)
            print(_format_output(result))
        i += 2


if __name__ == "__main__":
    main()

