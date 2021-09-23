import java.util.*;
class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        long answer = (long)times[times.length-1]*(long)n;
        
        long start = times[0];
        long end = answer;

        answer = search(n, times, start, end);
        
        return answer;
    }
    
    public long search(int n, int[] times, long start, long end){
        long mid = (start+end)/2;
        long cnt = 0;    
        
        for(long time : times) { 
            cnt += mid/time;
        }
        if(cnt >= n) { 
            if (start >= mid)
                return mid;
            else
                return search(n, times, start, mid);
        }else{
            if (mid+1 >= end)
                return mid; 
            else
                return search(n, times, mid+1, end); 
        }

    }
        
}