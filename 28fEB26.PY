class Solution {
  public:
    vector<int> findClosestPair(vector<int> &arr1, vector<int> &arr2, int x) {
        vector<int> res={0,INT_MAX};
        for(auto it : arr1)
        {
            int idx = lower_bound(arr2.begin(),arr2.end(),x-it) - arr2.begin();
            if(abs(it + arr2[idx] - x) < abs(res[0] + res[1] - x))
            res = {it, arr2[idx]};
            if((idx) && (abs(it + arr2[idx-1] - x) < abs(res[0] + res[1] - x)))
            res = {it, arr2[idx-1]};
        }
        return res;
    }
};
