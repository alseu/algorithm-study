package algo1;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class dogTravel_graph {

	public static void main(String[] args) throws IOException {
		int E,V, result;
		int [] parent;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for(int tc = 0;tc < T; tc++) {
			
			//노드의 개수와 간선의 개수 입력받기
			StringTokenizer input = new StringTokenizer(br.readLine());
			E = Integer.parseInt(input.nextToken());
			V = Integer.parseInt(input.nextToken());
			
			parent = new int[E+1];
			result = 0;
			
			//부모 테이블상에서, 부모를 자기 자신으로 초기화
			for(int i=0;i<parent.length;i++) {
				parent[i]=i;
			}
			
			//모든 간선에 대한 정보를 입력받기 + 간선을 하나씩 확인하며
			for(int i=0;i<V;i++) {
				input = new StringTokenizer(br.readLine());
				int s = Integer.parseInt(input.nextToken());
				int e = Integer.parseInt(input.nextToken());
				
				// 싸이클이 발생하지 않는 경우에만 집합에 포함
				if(!isSameParent(parent,s, e)) {
					// 간선을 연결하고 간선 수 +1 (비용이없음)
					result++;
					union(parent, s,e);
				}
								
			}
			
			System.out.println(result);
		}

	}
	// 특정 원소가 속한 집합을 찾기 
	private static int find_parent(int[] parent,int a) {
		if(parent[a] != a) {
			return parent[a] = find_parent(parent,parent[a]);
		}
		return parent[a];
	}
	private static boolean isSameParent(int[] parent, int a, int b) {
		a = find_parent(parent,a);
		b = find_parent(parent,b);
		
		if(a==b) return true;
		else return false;
	}

	// 두 원소가 속한 집합을 합치기
	private static void union(int[] parent, int a, int b) {
		a = find_parent(parent, a);
		b = find_parent(parent, b);
		
		if(a < b) {
			parent[b] = a;
		}else
			parent[a] = b;
	}

}