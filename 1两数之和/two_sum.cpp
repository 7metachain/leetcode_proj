#include <cctype>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

static std::vector<long long> parseInts(const std::string& line) {
    // allow: "2 7 11 15", "[2,7,11,15]", "nums = [2, 7, 11, 15]", "target = 9"
    std::string s = line;
    for (char& c : s) {
        if (std::isdigit((unsigned char)c) || c == '-') continue;
        c = ' ';
    }
    std::stringstream ss(s);
    std::vector<long long> out;
    long long x;
    while (ss >> x) out.push_back(x);
    return out;
}

static std::vector<int> twoSumOnePass(const std::vector<long long>& nums, long long target) {
    std::unordered_map<long long, int> mp; // value -> index
    for (int i = 0; i < (int)nums.size(); ++i) {
        long long need = target - nums[i];
        auto it = mp.find(need);
        if (it != mp.end()) return {it->second, i};
        mp[nums[i]] = i;
    }
    return {};
}

static std::vector<int> twoSumTwoPass(const std::vector<long long>& nums, long long target) {
    std::unordered_map<long long, int> mp;
    for (int i = 0; i < (int)nums.size(); ++i) mp[nums[i]] = i;
    for (int i = 0; i < (int)nums.size(); ++i) {
        long long need = target - nums[i];
        auto it = mp.find(need);
        if (it != mp.end() && it->second != i) return {i, it->second};
    }
    return {};
}

static void printAns(const std::vector<int>& ans) {
    std::cout << "[";
    for (size_t i = 0; i < ans.size(); ++i) {
        if (i) std::cout << ",";
        std::cout << ans[i];
    }
    std::cout << "]\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    // Interactive stdin mode (until EOF), each case takes 2 lines:
    // - line1: nums (e.g. "2 7 11 15" or "nums = [2,7,11,15]")
    // - line2: target (e.g. "9" or "target = 9")
    //
    // Choose method via env var: TWOSUM_METHOD=one (default) or TWOSUM_METHOD=two
    const char* method = std::getenv("TWOSUM_METHOD");
    bool use_two_pass = method && (std::string(method) == "two" || std::string(method) == "2" ||
                                   std::string(method) == "two_pass");

    std::string line_nums;
    while (std::getline(std::cin, line_nums)) {
        if (line_nums.find_first_not_of(" \t\r\n") == std::string::npos) continue;
        auto nums_ll = parseInts(line_nums);
        std::vector<long long> nums(nums_ll.begin(), nums_ll.end());

        std::string line_target;
        if (!std::getline(std::cin, line_target)) break;
        auto ts = parseInts(line_target);
        if (ts.empty()) continue;
        long long target = ts[0];

        auto ans = use_two_pass ? twoSumTwoPass(nums, target) : twoSumOnePass(nums, target);
        printAns(ans);
    }
    return 0;
}


