import java.util.*;

class Solution {
    
    public static List<Integer>[] tree;
    public static int[] distance;
    
    public List solution(int n, int[][] roads, int[] sources, int destination) {

        List<Integer> answer = new ArrayList<>();
        tree = new List[n+1];
        for(int i = 0 ; i <= n; ++i){
            tree[i] = new ArrayList();
        }
        
        for(int[] road : roads){
            int node1 = road[0];
            int node2 = road[1];
            // tree[node1][node2] = 1;
            // tree[node2][node1] = 1;
            tree[node1].add(node2);
            tree[node2].add(node1);
        }
        calcuateDistance(n,destination);
        
        
        //System.out.println(distance);
        for(int source : sources){        
            answer.add(distance[source]);

        }
        
        return answer;
    }
    
    public static void calcuateDistance(int n, int destination){
        distance = new int[n+1];
        boolean[] visited = new boolean[n+1];
        Arrays.fill(distance, -1);
        Arrays.fill(visited, false);
        
        distance[destination] = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(destination);
        
        while(!queue.isEmpty()){
            int node = queue.poll();
            visited[node] = true;
            
           // for(int i=1; i<n+1; i++){
                
            for(Integer i : tree[node]){
                //System.out.println(i);
                if(tree[node].contains(i) && !visited[i]){
                    queue.add(i);
                    
                    if(distance[i] == -1){
                        distance[i] = distance[node] + 1;
                    }else{
                        distance[i] = Math.min(distance[node] + 1, distance[i]);
                    }
                    
                }
            }
            

        }
        
        
        
    }
    
}