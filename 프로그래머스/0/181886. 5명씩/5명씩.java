import java.util.*;

class Solution {
    public String[] solution(String[] names) {
        ArrayList<String> lst = new ArrayList<>();
        
        for (int i = 0; i < names.length; i += 5){
            lst.add(names[i]);        
        }
        
        String[] answer = new String[lst.size()];
        
        for (int j = 0; j < lst.size(); j++){
            answer[j] = lst.get(j);
        }
        return answer;
    }
}