import java.util.*;
public class RepeatDNA {
    public List<String> findRepeatedDnaSequences(String s) {
        Set seen = new HashSet(), repeated = new HashSet();
        for (int i = 0; i + 9 < s.length(); i++) {
            String ten = s.substring(i, i + 10);
            if (!seen.add(ten))
                repeated.add(ten);
        }
        return new ArrayList(repeated);
    }
    public static void main(String[] args){
        System.out.println(Integer.MIN_VALUE);
        long temp = (long)5 - Integer.MIN_VALUE;
        System.out.println(temp);
    }
    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> result = new ArrayList<int[]>();
        int n = buildings.length;
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
        TreeMap<Integer, Integer> treeMap = new TreeMap<Integer, Integer>();
        int pos = -1, curHeight = -1;
        while (pos+1 < n) {
            do {
                pos++;
                minHeap.add(buildings[pos][1]);
                treeMap.put(buildings[pos][2], buildings[pos][1]);
            } while (pos+1 < n && buildings[pos+1][0] == buildings[pos][0]);
            int curMax = treeMap.lastKey();
            if (curMax != curHeight) {
                result.add(new int[] {buildings[pos][0], curHeight = curMax});
            }
            while (minHeap.size()!=0 && (pos == n-1 || minHeap.peek() < buildings[pos+1][0])) {
                int curpos = minHeap.poll();
                treeMap.values().remove(curpos);
                curMax = treeMap.size() == 0 ? 0 : treeMap.lastKey();
                if (curHeight != curMax ) {
                    result.add(new int[] {curpos, curHeight = curMax});
                }
            }
        }
        return result;
    }
    public List<int[]> getSkylines(int[][] buildings) {
        List<int[]> result = new ArrayList<>();
        List<int[]> height = new ArrayList<>();
        for(int[] b:buildings) {
            height.add(new int[]{b[0], -b[2]});
            height.add(new int[]{b[1], b[2]});
        }
        Collections.sort(height, (a, b) -> {
            if(a[0] != b[0])
                return a[0] - b[0];
            return a[1] - b[1];
        });
        Queue<Integer> pq = new PriorityQueue<>((a, b) -> (b - a));
        pq.offer(0);
        int prev = 0;
        for(int[] h:height) {
            if(h[1] < 0) {
                pq.offer(-h[1]);
            } else {
                pq.remove(h[1]);
            }
            int cur = pq.peek();
            if(prev != cur) {
                result.add(new int[]{h[0], cur});
                prev = cur;
            }
        }
        return result;
    }
}
