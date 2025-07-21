class Solution {
    public String makeFancyString(String s) {
        int count = 0;
        StringBuilder sta = new StringBuilder();
        sta.append(String.valueOf(s.charAt(0)));
        for(int i = 1;i<s.length();i++){
            if(s.charAt(i-1) == s.charAt(i) && count < 1){
                sta.append(String.valueOf(s.charAt(i)));
                count++;
            }else if(s.charAt(i-1) != s.charAt(i)){
                sta.append(String.valueOf(s.charAt(i)));
                count = 0;
            }else{
                continue;
            }
        }
        return sta.toString();
    }
}
