class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.isEmpty()) {
            return 0;
        }
        if (haystack.equals(needle)) {
            return 0;
        }
        for(int i=0;i<haystack.length()-needle.length()+1;i++){
            int x = 0;
            while(x < needle.length() && haystack.charAt(i+x) == needle.charAt(x)){
                x++;
            }
            if(x == needle.length()){
                return i;
            }
        }
        return -1;
    }
}
