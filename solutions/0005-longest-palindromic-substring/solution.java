class Solution {
    public boolean palindrome(String s){
        int a = 0, b = s.length() - 1;
        while (a < b) {
            if (s.charAt(a) != s.charAt(b)) return false;
            a++;
            b--;
        }
        return true;
    }

    public String longestPalindrome(String s) {
        if (s == null || s.length() < 2) return s;

        String longest = "";
        int n = s.length();

        for (int i = 0; i < n; i++) {
            for (int j = i+1; j <= n; j++) {  // substring(i, j) → j is exclusive
                String sub = s.substring(i, j);
                if (palindrome(sub) && sub.length() > longest.length()) {
                    longest = sub;
                }
            }
        }
        return longest;
    }
}

