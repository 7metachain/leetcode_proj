"""
49. 字母异位词分组 —— 本地可运行版本 (Python3)

输入格式（每行一组，直到 EOF 退出）：
  - ["eat","tea","tan","ate","nat","bat"]
  - eat tea tan ate nat bat
  - eat, tea, tan, ate, nat, bat

输出：分组后的结果，如 [["eat","tea","ate"],["tan","nat"],["bat"]]
"""

from __future__ import annotations

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """排序作为 key，哈希表分组"""
    mp: dict[str, list[str]] = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        mp[key].append(s)
    return list(mp.values())


def _parse_strs(line: str) -> list[str]:
    """解析一行输入为字符串列表，兼容多种格式"""
    # 去掉外层括号、引号，按逗号或空格分割
    cleaned = (
        line.replace("[", " ")
        .replace("]", " ")
        .replace('"', " ")
        .replace("'", " ")
        .replace(",", " ")
    )
    return [tok.strip() for tok in cleaned.split() if tok.strip()]


def _format_output(groups: list[list[str]]) -> str:
    """格式化输出为 LeetCode 风格"""
    inner = ",".join(
        "[" + ",".join(f'"{s}"' for s in g) + "]" for g in groups
    )
    return "[" + inner + "]"


def main() -> None:
    import sys

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        strs = _parse_strs(line)
        result = group_anagrams(strs)
        print(_format_output(result))


if __name__ == "__main__":
    main()

