# Leetcode

 每次做动态规划的题，我都觉得自己是个智障。
 ![avatar](https://github.com/UnsupervisedDotey/Leetcode/raw/master/image/cry.jpg)
 
 
# ===========================
 
### 当前进度

|     BABE      | PROGRESS                                  |
| :-----------: | ----------------------------------------- |
|   Yiran Han   |  3/775 Solved - Easy  3 Medium 0  Hard 0  |
| Fangling Liu  | 70/775 Solved - Easy 54 Medium 16 Hard 0  |


# ===========================

## 动态规划 用于解决具有重复可分子问题的场景

先从上到下分解问题，后从下到上遍历解决问题。需要列出 1）初始方程；2）状态转移方程

### 简单

| 题  | 描述 | 初始状态  | 状态转移方程  | 结果 |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| 303 |  给定一个整数数组 nums，求出数组从索引i到j元素的总和，包含i,j两点| dp[0] = 0  | dp[i] = dp[i-1] + nums[i-1] | res = dp[j+1] -dp[i]|
| 121 | 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。  |   | dp[i]=max(0,dp[i−1])|  res=max{前一天最大利润, 今天的价格 - 之前最低价格}|
| 53  | 给定一个整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。  |   |dp[i]=max{nums[i],dp[i−1]+nums[i]}  |  |
| 70 | 假设你正在爬楼梯。需要 _n_ 阶你才能到达楼顶。 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？  |   | dp[i]=dp[i−1]+dp[i−2] |  |
| 746  |数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。 |dp[0] = cost[0], dp[1] = cost[1]| dp[i] = min(dp[i-1],dp[i-2]) + cost[i] |  |
| 198 |你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。|   | dp[i] = max{dp[i-1], dp[i-2]+new_nums[i]}  |  |
|   |   |   |  |  |
|   |   |   |  |  |



### 中等

对不起，我不会，一题都没做出来。。。。。。。

突然开始写sql题