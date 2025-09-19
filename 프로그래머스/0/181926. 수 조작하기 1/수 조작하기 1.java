import java.util.*;

class Solution {
    public int solution(int n, String control) {
        String[] tmp = control.split("");
        List<String> list = new ArrayList<>(Arrays.asList(tmp));

        for (int i = 0; i < list.size(); i++) {
            String c = list.get(i);

            if (c.equals("w")) {
                n += 1;
            } else if (c.equals("s")) {
                n -= 1;
            } else if (c.equals("d")) {
                n += 10;
            } else if (c.equals("a")) {
                n -= 10;
            }
        }
        return n;
    }
}
