public class FactAlgo {
    // Factorial 
    public int fact( int n) {
        if (n==1) 
            return 1;
        else if (n==0)
            return 1;
        else
            return n * fact(n-1);  
    }
    // Print
    public int Print(int n) {
        if (n == 0)
            return 0;
        else {
            System.out.println(n);
            return Print(n-1);
        }
    }
}
