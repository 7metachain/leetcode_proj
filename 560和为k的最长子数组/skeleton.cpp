/*
 * 560. 和为 K 的子数组 —— 关卡化学习骨架 (C++17)
 *
 * 🎯 学习目标：
 *    - 理解前缀和的数学变换
 *    - 掌握"前缀和 + 哈希表"的经典模式
 *    - 最终写出 O(n) 最优解
 *
 * 📌 使用方法：
 *    1. 修改 LEVEL 变量控制当前关卡 (1-6)
 *    2. 在 TODO (Level X) 处填写代码
 *    3. 编译运行：g++ -std=c++17 skeleton.cpp -o skeleton && ./skeleton
 *
 * 📌 输入格式（内置测试 + 交互式）：
 *    - 程序会先运行内置测试
 *    - 然后可输入自定义用例（每组两行：数组 和 k）
 */

#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

// ============================================================
// 🎮 LEVEL 控制器 —— 修改这里切换关卡
// ============================================================
constexpr int LEVEL = 1;

// ============================================================
// 📊 统一测试用例（贯穿所有关卡）
// ============================================================
struct TestCase {
    vector<int> nums;
    int k;
    int expected;
};

const vector<TestCase> TEST_CASES = {
    {{1, 1, 1}, 2, 2},              // 子数组 [1,1] 出现 2 次
    {{1, 2, 3}, 3, 2},              // [1,2] 和 [3]
    {{1, -1, 0}, 0, 3},             // [1,-1], [0], [1,-1,0]
    {{3, 4, 7, 2, -3, 1, 4, 2}, 7, 4},
};


// ============================================================
// Level 1：题意建模 —— 子数组和的计算
// ============================================================
int subarraySumRange(const vector<int>& nums, int l, int r) {
    /*
     * 计算 nums[l..r] 的和（闭区间）
     *
     * TODO (Level 1): 用一个循环累加 nums[l] 到 nums[r] 的元素
     */
    int total = 0;
    // -------- 在此填写 --------
    
    // ----------------------------
    return total;
}


// ============================================================
// Level 2：暴力解 —— 枚举所有子数组 O(n²)
// ============================================================
int bruteForce(const vector<int>& nums, int k) {
    /*
     * 暴力解：双层循环枚举所有 (l, r) 对
     * 复杂度：O(n²)
     *
     * 这是"真值函数"，后续可用于对拍验证
     */
    int n = static_cast<int>(nums.size());
    int ans = 0;
    
    // TODO (Level 2): 枚举左端点 l，对每个 l 枚举右端点 r
    //                 用累加的方式维护 sum，避免重复计算
    // -------- 在此填写 --------
    
    // ----------------------------
    
    return ans;
}


// ============================================================
// Level 3：中间信息暴露 —— 打印前缀和，理解等价变换
// ============================================================
void explainPrefixSum(const vector<int>& nums, int k) {
    /*
     * 打印前缀和数组，帮助理解：
     *   sum(l, r) = pre[r] - pre[l-1]  (当 l > 0)
     *   sum(0, r) = pre[r]             (当 l = 0)
     *
     * 关键洞察：
     *   sum(l, r) = k
     *   => pre[r] - pre[l-1] = k
     *   => pre[l-1] = pre[r] - k
     *
     * 意思是：当右端点固定为 r 时，
     * 满足条件的左端点个数 = 之前出现过多少次前缀和等于 (pre[r] - k)
     */
    int n = static_cast<int>(nums.size());
    
    // 计算前缀和数组（pre[i] = nums[0] + ... + nums[i]）
    vector<long long> pre(n, 0);
    // TODO (Level 3): 填写前缀和的递推公式
    // -------- 在此填写 --------
    
    // ----------------------------
    
    cout << "nums = [";
    for (int i = 0; i < n; i++) {
        cout << nums[i] << (i < n - 1 ? ", " : "");
    }
    cout << "], k = " << k << endl;
    
    cout << "前缀和 pre = [";
    for (int i = 0; i < n; i++) {
        cout << pre[i] << (i < n - 1 ? ", " : "");
    }
    cout << "]" << endl << endl;
    
    // 展示等价变换
    cout << "展示 sum(l,r) = pre[r] - pre[l-1] 的等价性：" << endl;
    for (int l = 0; l < n; l++) {
        for (int r = l; r < n; r++) {
            long long s;
            if (l == 0) {
                s = pre[r];
                if (s == k) {
                    cout << "  ✅ sum(" << l << "," << r << ") = pre[" << r << "] = " 
                         << pre[r] << " = " << k << endl;
                }
            } else {
                s = pre[r] - pre[l - 1];
                if (s == k) {
                    cout << "  ✅ sum(" << l << "," << r << ") = pre[" << r << "] - pre[" 
                         << (l - 1) << "] = " << pre[r] << " - " << pre[l - 1] 
                         << " = " << s << " = " << k << endl;
                }
            }
        }
    }
    cout << endl;
}


// ============================================================
// Level 4-6：目标解函数 —— 前缀和 + 哈希表 O(n)
// ============================================================
int subarraySumOptimal(const vector<int>& nums, int k) {
    /*
     * 最优解：前缀和 + 哈希表
     * 复杂度：O(n) 时间，O(n) 空间
     *
     * 核心思想：
     *   cnt[s] = 前缀和 s 出现的次数
     *   遍历时，对于当前前缀和 prefixSum：
     *     - 需要找的历史前缀和是 prefixSum - k
     *     - ans += cnt[prefixSum - k]
     *     - 然后 cnt[prefixSum] += 1
     */
    
    // Level 4: 引入哈希表 cnt
    unordered_map<long long, int> cnt;
    
    // TODO (Level 6): 为什么需要 cnt[0] = 1？
    //   当 prefixSum == k 时，prefixSum - k == 0
    //   cnt[0] = 1 表示"空前缀"出现 1 次
    //   这样才能正确统计从下标 0 开始的子数组
    // -------- 在此填写 --------
    
    // ----------------------------
    
    long long prefixSum = 0;
    int ans = 0;
    
    for (int x : nums) {
        prefixSum += x;
        
        // TODO (Level 5): 统计之前出现过多少次 prefixSum - k
        // -------- 在此填写 --------
        
        // ----------------------------
        
        // TODO (Level 5): 记录当前前缀和出现次数
        // -------- 在此填写 --------
        
        // ----------------------------
    }
    
    return ans;
}


// ============================================================
// 🧪 测试入口
// ============================================================
vector<int> parseInts(const string& line) {
    string s = line;
    for (char& c : s) {
        if (c == '[' || c == ']' || c == ',') c = ' ';
    }
    vector<int> out;
    stringstream ss(s);
    int x;
    while (ss >> x) out.push_back(x);
    return out;
}

void runTests() {
    cout << string(60, '=') << endl;
    cout << "🎮 当前关卡：Level " << LEVEL << endl;
    cout << string(60, '=') << endl << endl;
    
    if (LEVEL == 1) {
        cout << "📌 Level 1：题意建模 —— 实现 subarraySumRange(nums, l, r)" << endl;
        cout << "   目标：计算 nums[l..r] 的和" << endl << endl;
        
        vector<int> nums = {1, 2, 3, 4, 5};
        cout << "nums = [1, 2, 3, 4, 5]" << endl;
        cout << "subarraySumRange(nums, 0, 2) = " << subarraySumRange(nums, 0, 2) 
             << "  (期望: 6)" << endl;
        cout << "subarraySumRange(nums, 1, 3) = " << subarraySumRange(nums, 1, 3) 
             << "  (期望: 9)" << endl;
        cout << "subarraySumRange(nums, 2, 4) = " << subarraySumRange(nums, 2, 4) 
             << "  (期望: 12)" << endl;
    }
    else if (LEVEL == 2) {
        cout << "📌 Level 2：暴力解 —— 双层循环枚举所有 (l, r) 对" << endl;
        cout << "   目标：实现 O(n²) 的暴力解" << endl << endl;
        
        for (const auto& tc : TEST_CASES) {
            int result = bruteForce(tc.nums, tc.k);
            const char* status = (result == tc.expected) ? "✅" : "❌";
            cout << status << " bruteForce([";
            for (size_t i = 0; i < tc.nums.size(); i++) {
                cout << tc.nums[i] << (i < tc.nums.size() - 1 ? "," : "");
            }
            cout << "], " << tc.k << ") = " << result 
                 << "  (期望: " << tc.expected << ")" << endl;
        }
    }
    else if (LEVEL == 3) {
        cout << "📌 Level 3：中间信息暴露 —— 理解前缀和等价变换" << endl;
        cout << "   目标：实现前缀和递推，观察 sum(l,r) = pre[r] - pre[l-1]" << endl << endl;
        
        explainPrefixSum({1, 1, 1}, 2);
        explainPrefixSum({1, 2, 3}, 3);
    }
    else {  // LEVEL >= 4
        const char* levelDesc[] = {
            "",
            "",
            "",
            "",
            "Level 4：解法结构骨架 —— 引入哈希表 cnt",
            "Level 5：关键思想注入 —— 填写核心逻辑",
            "Level 6：最优解完成 —— 理解 cnt[0] = 1 的必要性"
        };
        int idx = (LEVEL <= 6) ? LEVEL : 6;
        cout << "📌 " << levelDesc[idx] << endl << endl;
        
        bool allPass = true;
        for (const auto& tc : TEST_CASES) {
            int result = subarraySumOptimal(tc.nums, tc.k);
            const char* status = (result == tc.expected) ? "✅" : "❌";
            if (result != tc.expected) allPass = false;
            
            cout << status << " subarraySumOptimal([";
            for (size_t i = 0; i < tc.nums.size(); i++) {
                cout << tc.nums[i] << (i < tc.nums.size() - 1 ? "," : "");
            }
            cout << "], " << tc.k << ") = " << result 
                 << "  (期望: " << tc.expected << ")" << endl;
        }
        
        if (allPass && LEVEL == 6) {
            cout << endl << "🎉 恭喜！所有测试通过，你已完成最优解！" << endl;
            cout << "   现在可以删除 LEVEL 相关代码，骨架即为最终答案。" << endl;
        }
    }
}

void interactiveMode() {
    cout << endl << string(60, '=') << endl;
    cout << "📝 交互模式：输入自定义测试（Ctrl+D 退出）" << endl;
    cout << "   格式：第1行 数组（如 [1,1,1]），第2行 整数 k" << endl;
    cout << string(60, '=') << endl << endl;
    
    string numsLine, kLine;
    while (getline(cin, numsLine) && getline(cin, kLine)) {
        if (numsLine.empty() || kLine.empty()) continue;
        
        auto nums = parseInts(numsLine);
        int k = stoi(kLine);
        
        int result;
        if (LEVEL <= 2) {
            result = bruteForce(nums, k);
            cout << "bruteForce result = " << result << endl;
        } else {
            result = subarraySumOptimal(nums, k);
            cout << "subarraySumOptimal result = " << result << endl;
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    runTests();
    // 如需交互测试，取消下面注释
    // interactiveMode();
    
    return 0;
}

