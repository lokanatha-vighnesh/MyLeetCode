class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        String res = "";
        int l = 0;

        while (true) {
            if (l >= strs[0].length()) break;
            char c = strs[0].charAt(l);

            for (int i = 1; i < strs.length; i++) {
                if (l >= strs[i].length() || strs[i].charAt(l) != c) {
                    return res; 
                }
            }

            res += c;
            l++;
        }
        return res;
    }
}

