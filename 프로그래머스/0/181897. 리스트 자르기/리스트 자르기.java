import java.util.*;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        List<Integer> lst = new ArrayList<>();
        for (int i : num_list) {
            lst.add(i);
        }
        
        if (n == 1) {
            lst = lst.subList(0, slicer[1] + 1);
        } else if (n == 2) {
            lst = lst.subList(slicer[0], lst.size());
        } else if (n == 3) {
            lst = lst.subList(slicer[0], slicer[1] + 1);
        } else if (n == 4) {
            List<Integer> tmp = new ArrayList<>();
            for (int i = slicer[0]; i <= slicer[1]; i += slicer[2]) {
                tmp.add(lst.get(i));
            }
            lst = tmp;
        }

        int[] answer = new int[lst.size()];
        for (int i = 0; i < lst.size(); i++) {
            answer[i] = lst.get(i);
        }
        return answer;
    }
}