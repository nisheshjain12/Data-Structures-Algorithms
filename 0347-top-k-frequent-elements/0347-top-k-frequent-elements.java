class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n= nums.length;
        HashMap<Integer,Integer> map = new HashMap<>();
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>( (a,b)->map.get(a)-map.get(b) );  
        
        for(int num:nums){
            map.put(num , map.getOrDefault(num,0)+1) ;
        }
        
        
        int[] ans = new int[k];
        int j=0;
        for(int val:map.keySet()){
            pq.add(val);
            if(pq.size() >k) pq.poll();
        }
       
        for(int i = k - 1; i >= 0; --i) 
         ans[i] = pq.poll();
        
         return ans;
    }
}