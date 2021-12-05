public class Fact {
    public static int Factorial(int n) {
        if (n < 2) { // for n=0, n=1, return 1 for both. 
            return 1;
        }
        else {
            return n * Factorial(n-1);
        }
    }
    public static void main(String[] args) {
        System.out.println("Hello, World! -- From Fact"); 
        // out = Factorial(10);
        System.out.println(Factorial(10));
    }
}