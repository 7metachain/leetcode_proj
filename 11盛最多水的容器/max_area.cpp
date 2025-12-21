/*
 * 11. 盛最多水的容器 —— 本地可运行版本 (C++17)
 *
 * 输入格式（每行一组，直到 EOF 退出）：
 *   - [1,8,6,2,5,4,8,3,7]
 *   - 1 8 6 2 5 4 8 3 7
 *   - 1, 8, 6, 2, 5, 4, 8, 3, 7
 *
 * 输出：最大盛水面积
 */

#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
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

static long long maxArea(const std::vector<int>& height) {
    int l = 0, r = static_cast<int>(height.size()) - 1;
    long long ans = 0;

    while (l < r) {
        long long h = std::min(height[l], height[r]);
        long long w = r - l;
        ans = std::max(ans, h * w);

        if (height[l] < height[r]) {
            l++;
        } else {
            r--;
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

        auto height = parseInts(line);
        if (height.size() < 2) {
            std::cout << 0 << '\n';
            continue;
        }
        long long result = maxArea(height);
        std::cout << result << '\n';
    }
    return 0;
}

