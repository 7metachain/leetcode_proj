/*
 * 15. 三数之和 —— 本地可运行版本 (C++17)
 *
 * 输入格式（每行一组，直到 EOF 退出）：
 *   - [-1,0,1,2,-1,-4]
 *   - -1 0 1 2 -1 -4
 *   - -1, 0, 1, 2, -1, -4
 *
 * 输出：所有不重复的三元组，如 [[-1,-1,2],[-1,0,1]]
 */

#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

static std::vector<int> parseInts(const std::string& line) {
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

static std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
    std::vector<std::vector<int>> result;
    std::sort(nums.begin(), nums.end());
    int n = static_cast<int>(nums.size());

    for (int i = 0; i < n - 2; i++) {
        // 剪枝：排序后如果 nums[i] > 0，后面全是正数，不可能凑出 0
        if (nums[i] > 0) break;
        // i 去重
        if (i > 0 && nums[i] == nums[i - 1]) continue;

        int l = i + 1, r = n - 1;
        while (l < r) {
            long long s = static_cast<long long>(nums[i]) + nums[l] + nums[r];
            if (s == 0) {
                result.push_back({nums[i], nums[l], nums[r]});
                l++;
                r--;
                // l 去重
                while (l < r && nums[l] == nums[l - 1]) l++;
                // r 去重
                while (l < r && nums[r] == nums[r + 1]) r--;
            } else if (s < 0) {
                l++;
            } else {
                r--;
            }
        }
    }
    return result;
}

static void printResult(const std::vector<std::vector<int>>& triplets) {
    std::cout << "[";
    for (size_t i = 0; i < triplets.size(); ++i) {
        if (i) std::cout << ",";
        std::cout << "[";
        for (size_t j = 0; j < triplets[i].size(); ++j) {
            if (j) std::cout << ",";
            std::cout << triplets[i][j];
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
        bool allSpace = true;
        for (char c : line) {
            if (!std::isspace(static_cast<unsigned char>(c))) {
                allSpace = false;
                break;
            }
        }
        if (allSpace) continue;

        auto nums = parseInts(line);
        auto result = threeSum(nums);
        printResult(result);
    }
    return 0;
}

