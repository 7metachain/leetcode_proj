/*
 * 560. 和为 K 的子数组 —— 本地可运行版本 (C++17)
 *
 * 输入格式（每组两行，直到 EOF 退出）：
 *   第 1 行：数组 nums（如 [1,1,1] 或 1 1 1）
 *   第 2 行：整数 k
 *
 * 输出：和为 k 的连续子数组个数
 */

#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
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

static int subarraySum(const std::vector<int>& nums, int k) {
    std::unordered_map<long long, int> cnt;
    cnt[0] = 1;  // 空前缀：前缀和为 0 出现 1 次

    long long prefixSum = 0;
    int ans = 0;

    for (int x : nums) {
        prefixSum += x;
        // 统计之前出现过多少次 prefixSum - k
        if (cnt.count(prefixSum - k)) {
            ans += cnt[prefixSum - k];
        }
        // 记录当前前缀和
        cnt[prefixSum]++;
    }

    return ans;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string numsLine, kLine;
    while (std::getline(std::cin, numsLine) && std::getline(std::cin, kLine)) {
        if (numsLine.empty() || kLine.empty()) continue;
        auto nums = parseInts(numsLine);
        int k = std::stoi(kLine);
        int result = subarraySum(nums, k);
        std::cout << result << '\n';
    }
    return 0;
}

