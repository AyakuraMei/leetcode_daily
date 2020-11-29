#include <vector>

class Solution{
    private:
    static constexpr int mod = 1000000007;
    static constexpr int coins[4] = {25, 10, 5, 1};

    public:
    int waysChange(int n){
        std::vector<int> dp(n + 1);
        dp[0] = 1;
        for (int i = 0; i < 4; i++){
            int value = coins[i];
            for (int j = value; j <= n; j++){
                dp[j] = (dp[j] + dp[j - value]) % mod;
            }
        }
        return dp[n];
    }
}