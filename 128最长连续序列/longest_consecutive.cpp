/*
 * 128. 最长连续序列 —— 本地可运行版本 (C++17)
 *
 * 输入格式（每行一组，直到 EOF 退出）：
 *   - [100,4,200,1,3,2]
 *   - 100 4 200 1 3 2
 *   - 100, 4, 200, 1, 3, 2
 *
 * 输出：最长连续序列的长度
 */

#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

static std::vector<int> parseInts(const std::string& line) {
    // 把 [ ] , 替换为空格，再按空格分割解析整数
    std::string s = line;
    for (char& c : s) {
        if (c == '[' || c == ']' || c == ',') {
            c = ' ';
        }
    }
    std::vector<int> out;
    std::stringstream ss(s);
    int x;
    while (ss >> x) {
        out.push_back(x);
    }
    return out;
}

static int longestConsecutive(const std::vector<int>& nums) {
    std::unordered_set<int> s(nums.begin(), nums.end());
    int ans = 0;

    for (int x : s) {
        // 只从起点开始：x-1 不存在说明 x 是某个连续序列的最左端
        if (s.count(x - 1) == 0) {
            int cur = x;
            while (s.count(cur)) {
                cur++;
            }
            ans = std::max(ans, cur - x);
        }
    }
    return ans;
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

        auto nums = parseInts(line);
        int result = longestConsecutive(nums);
        std::cout << result << '\n';
    }
    return 0;
}

