public class Fact {
    public int Factorial(int n) {
        if (n < 2) { // for n=0, n=1, return 1 for both. 
            return 1;
        }
        else {
            return n * Factorial(n-1);
        }
    }
}