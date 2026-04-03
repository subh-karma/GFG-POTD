class Solution {
    static ArrayList<Integer> diagView(int mat[][]) {
        // code here
        ArrayList<Integer> ans = new ArrayList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0])
                return a[1] - b[1];
            return a[0] - b[0];
        });
        int n = mat.length;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; j++) 
                pq.offer(new int[] {i + j, i, j});
        }
        
        while (!pq.isEmpty()) {
            int r = pq.peek()[1];
            int c = pq.peek()[2];
            pq.poll();
            ans.add(mat[r][c]);
        }
        return ans;
    }
}

