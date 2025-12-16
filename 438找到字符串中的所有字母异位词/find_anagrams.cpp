/*
 * 438. 找到字符串中所有字母异位词 —— 本地可运行版本 (C++17)
 *
 * 输入格式（每组两行，直到 EOF 退出）：
 *   第 1 行：字符串 s
 *   第 2 行：字符串 p
 *
 * 输出：异位词起始索引列表，如 [0,6]
 */

#include <iostream>
#include <string>
#include <vector>

static std::vector<int> findAnagrams(const std::string& s, const std::string& p) {
    std::vector<int> resultIndices;
    const int textLength = static_cast<int>(s.size());
    const int patternLength = static_cast<int>(p.size());

    if (textLength < patternLength) return resultIndices;

    std::vector<int> patternFreq(26, 0);
    std::vector<int> windowFreq(26, 0);

    // 统计 p 的字符频次
    for (char ch : p) {
        patternFreq[ch - 'a']++;
    }

    // 初始化第一个窗口
    for (int i = 0; i < patternLength; i++) {
        windowFreq[s[i] - 'a']++;
    }

    if (windowFreq == patternFreq) {
        resultIndices.push_back(0);
    }

    // 滑动窗口
    for (int right = patternLength; right < textLength; right++) {
        // 加入新字符
        windowFreq[s[right] - 'a']++;
        // 移除旧字符
        windowFreq[s[right - patternLength] - 'a']--;
        // 检查是否匹配
        if (windowFreq == patternFreq) {
            resultIndices.push_back(right - patternLength + 1);
        }
    }

    return resultIndices;
}

static void printResult(const std::vector<int>& indices) {
    std::cout << "[";
    for (size_t i = 0; i < indices.size(); ++i) {
        if (i) std::cout << ",";
        std::cout << indices[i];
    }
    std::cout << "]\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string s, p;
    while (std::getline(std::cin, s) && std::getline(std::cin, p)) {
        // 跳过空行组合
        if (s.empty() || p.empty()) continue;
        auto result = findAnagrams(s, p);
        printResult(result);
    }
    return 0;
}

