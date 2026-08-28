class Solution {
  public:
    int minCost(vector<vector<int>>& mat) {
        // code here
        int n = mat.size();

        vector<int> dp(3);

        // First row
        for (int j = 0; j < 3; j++) {
            dp[j] = mat[0][j];
        }

        // Remaining rows
        for (int i = 1; i < n; i++) {
            vector<int> ndp(3);

            ndp[0] = mat[i][0] + min(dp[1], dp[2]);
            ndp[1] = mat[i][1] + min(dp[0], dp[2]);
            ndp[2] = mat[i][2] + min(dp[0], dp[1]);

            dp = ndp;
        }

        return min({dp[0], dp[1], dp[2]});
    }
};
