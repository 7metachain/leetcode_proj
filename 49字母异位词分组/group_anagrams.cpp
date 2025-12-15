/*
 * 49. 字母异位词分组 —— 本地可运行版本 (C++17)
 *
 * 输入格式（每行一组，直到 EOF 退出）：
 *   - ["eat","tea","tan","ate","nat","bat"]
 *   - eat tea tan ate nat bat
 *   - eat, tea, tan, ate, nat, bat
 *
 * 输出：分组后的结果，如 [["eat","tea","ate"],["tan","nat"],["bat"]]
 */

#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

static std::vector<std::string> parseStrs(const std::string& line) {
    // 把 [ ] " ' , 替换为空格，再按空格分割
    std::string s = line;
    for (char& c : s) {
        if (c == '[' || c == ']' || c == '"' || c == '\'' || c == ',') {
            c = ' ';
        }
    }
    std::vector<std::string> out;
    std::stringstream ss(s);
    std::string tok;
    while (ss >> tok) {
        if (!tok.empty()) out.push_back(tok);
    }
    return out;
}

static std::vector<std::vector<std::string>> groupAnagrams(
    const std::vector<std::string>& strs) {
    std::unordered_map<std::string, std::vector<std::string>> mp;
    for (const auto& s : strs) {
        std::string key = s;
        std::sort(key.begin(), key.end());
        mp[key].push_back(s);
    }
    std::vector<std::vector<std::string>> res;
    res.reserve(mp.size());
    for (auto& p : mp) {
        res.push_back(std::move(p.second));
    }
    return res;
}

static void printResult(const std::vector<std::vector<std::string>>& groups) {
    std::cout << "[";
    for (size_t i = 0; i < groups.size(); ++i) {
        if (i) std::cout << ",";
        std::cout << "[";
        for (size_t j = 0; j < groups[i].size(); ++j) {
            if (j) std::cout << ",";
            std::cout << "\"" << groups[i][j] << "\"";
        }
        std::cout << "]";
    }
    std::cout << "]\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string line;
    while (std::getline(std::cin, line)) {
        // 跳过空行
        bool allSpace = true;
        for (char c : line) {
            if (!std::isspace((unsigned char)c)) {
                allSpace = false;
                break;
            }
        }
        if (allSpace) continue;

        auto strs = parseStrs(line);
        auto result = groupAnagrams(strs);
        printResult(result);
    }
    return 0;
}

