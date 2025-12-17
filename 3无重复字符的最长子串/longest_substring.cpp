/*
 * 3. 无重复字符的最长子串 —— 本地可运行版本 (C++17)
 *
 * 输入格式（每行一个字符串，直到 EOF 退出）：
 *   - abcabcbb
 *   - pwwkew
 *
 * 输出：最长子串长度 及 子串本身
 */

#include <iostream>
#include <string>
#include <unordered_map>

static std::pair<int, std::string> lengthOfLongestSubstring(const std::string& s) {
    std::unordered_map<char, int> last;
    int left = 0;
    int bestLeft = 0;
    int bestLen = 0;

    for (int right = 0; right < static_cast<int>(s.size()); right++) {
        char c = s[right];

        if (last.count(c)) {
            // left 只能往右，不能往回
            left = std::max(left, last[c] + 1);
        }
        last[c] = right;

        int curLen = right - left + 1;
        if (curLen > bestLen) {
            bestLen = curLen;
            bestLeft = left;
        }
    }

    return {bestLen, s.substr(bestLeft, bestLen)};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string line;
    while (std::getline(std::cin, line)) {
        if (line.empty()) continue;
        auto [length, substring] = lengthOfLongestSubstring(line);
        std::cout << length << " \"" << substring << "\"\n";
    }
    return 0;
}

