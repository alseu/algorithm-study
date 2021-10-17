
public class network_dfs {


	public static void main(String[] args) {

		//sample data
		int n = 3;
		int[][] computers = { { 1, 1, 0 }, { 1, 1, 1 }, { 0, 1, 1 } };
		
		int answer = 0;
		boolean[] visited = new boolean[n];	//default::false, start_in_0, size_of_node
		
		//check all nodes where visit is false
		for (int i = 0; i < n; i++) {
			if (visited[i] == false) {
				dfs(visited, i, computers);
				answer++;
			}
		}
		System.out.println(answer);
	}

	//recursive
	public static void dfs(boolean[] visited, int node, int[][] computers) {
		for (int i = 0; i < visited.length; i++) {
			if (visited[i] == false && computers[node][i] == 1) {
				visited[i] = true;
				dfs(visited, i, computers);
			}
		}
	}

}