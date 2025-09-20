class Solution {
    public int solution(String binomial) {
        String[] lst = binomial.split(" ");
        int num1 = Integer.parseInt(lst[0]);
        
        String op = lst[1];
        
        int num2 = Integer.parseInt(lst[2]);
        
        if (op.equals("+")) {
            return num1 + num2;
        }else if (op.equals("-")){
            return num1 - num2;
        }else {
            return num1 * num2;
        }
    }
}