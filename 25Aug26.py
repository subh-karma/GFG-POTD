class Solution {
  public:
    virtual int minMoves(vector<int>& arr){
      unordered_map<int, int> um;

      int correct=0;
      for(int x: arr){
        um[x]=um[x-1]+1;
        correct=max(correct, um[x]);
      }

      return (arr.size())-correct;
    }
};
