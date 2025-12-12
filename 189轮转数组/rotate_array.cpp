#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

static std::vector<long long> parseInts(const std::string& line) {
    // allow: "1 2 3", "[1,2,3]", "nums = [1, 2, 3]"
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

static void rotate(std::vector<long long>& nums, long long k) {
    int n = (int)nums.size();
    if (n <= 1) return;
    k %= n;
    if (k == 0) return;
    std::reverse(nums.begin(), nums.end());
    std::reverse(nums.begin(), nums.begin() + k);
    std::reverse(nums.begin() + k, nums.end());
}

static void printList(const std::vector<long long>& nums) {
    std::cout << "[";
    for (size_t i = 0; i < nums.size(); ++i) {
        if (i) std::cout << ",";
        std::cout << nums[i];
    }
    std::cout << "]\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    // Interactive stdin mode (until EOF):
    // - line1: nums (space-separated, or [..], or "nums = [..]")
    // - line2: k
    // Output each case as: [rotated_array]
    std::string line_nums;
    while (std::getline(std::cin, line_nums)) {
        if (line_nums.find_first_not_of(" \t\r\n") == std::string::npos) continue;
        auto nums_ll = parseInts(line_nums);
        std::vector<long long> nums(nums_ll.begin(), nums_ll.end());

        std::string line_k;
        if (!std::getline(std::cin, line_k)) break;
        auto ks = parseInts(line_k);
        if (ks.empty()) continue;
        long long k = ks[0];

        rotate(nums, k);
        printList(nums);
    }
    return 0;
}


