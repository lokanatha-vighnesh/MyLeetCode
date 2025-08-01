class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> l = new ArrayList<>();
        for(int i =0;i<numRows;i++){
            List<Integer> n = new ArrayList<>();
            for(int j=0;j<=i;j++){
                if(j==0||j==i){
                    n.add(1);
                }else{
                    int a = l.get(i-1).get(j-1);
                    int b = l.get(i-1).get(j);
                    n.add(a+b);
                }
            }
            l.add(n);
        }
        return l;
    }
}
