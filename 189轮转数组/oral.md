## 189. 轮转数组（口播稿）

### 中文口播（推荐解法：三次翻转，原地 O(1)）
这题给一个数组 `nums`，要求把它**向右轮转 `k` 位**。核心点是 `k` 可能很大，所以先做 `k %= n`。  
最推荐的原地做法是“三次翻转”：  
1）先把整个数组翻转；  
2）再翻转前 `k` 个；  
3）最后翻转后 `n-k` 个。  
为什么这样就对？可以把原数组看成两段 `[A | B]`，其中 `B` 是最后 `k` 个元素。轮转目标是 `[B | A]`。整体翻转得到 `[reverse(B) | reverse(A)]`，再分别翻转两段，就回到 `[B | A]`。  
复杂度方面，时间 O(n)，空间 O(1)。常见坑：`k==0`、`n==1` 时要直接返回；以及 `k` 必须先取模再做区间翻转。

### English (Recommended: 3-reverse trick, in-place O(1))
We need to rotate an array `nums` to the right by `k` steps. Since `k` can be larger than the array length, we first do `k %= n`.  
The standard in-place solution uses three reversals:  
1) reverse the whole array,  
2) reverse the first `k` elements,  
3) reverse the remaining `n-k` elements.  
Why does it work? Think of the array as `[A | B]`, where `B` is the last `k` elements. The rotated result should be `[B | A]`. After reversing everything, we get `[reverse(B) | reverse(A)]`. Reversing each part again turns them into `[B | A]`.  
Time complexity is O(n) and extra space is O(1). Watch out for edge cases like `k==0` or `n<=1`, and always take modulo before reversing.


