import java.util.*;

/*BFS Solution (TLE -- Still very interesting)
https://leetcode.com/problems/jump-game/
*/

class JumpGame {
	public static void main (String[] args) {
		int[] nums = {2,0,0};
	    Queue<Integer> q = new LinkedList<>();
		q.add(0);

		Set<Integer> visited = new HashSet<Integer>();
		int cur;
		boolean a = true;

		while (q.size() > 0) {
			cur = q.peek();
			q.remove();
			System.out.println(cur);
			if (cur==nums.length-1) {
				System.out.println("True");
				a = false;

				break;
			} else {
				for (int i=1; i<nums[cur]+1; i++) {
					if (visited.contains((cur+i))==false) {
						System.out.println("cur " + (cur+i));
						q.add(cur+i);
						visited.add(cur+i);

					}
				}

			}

		}

		if (a==true) {
			System.out.println("false");
		}

	}
}
