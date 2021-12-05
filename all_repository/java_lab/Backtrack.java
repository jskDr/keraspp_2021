import java.util.Arrays;

public class Backtrack {
    static int N = 2;
    static int A[];
    public static void main(String[] args) {
        System.out.print("Backtrack ");
        // if (args.length > 0) 
        for (int i=0; i<args.length; i++) {
            System.out.print(args[i] + " ");
        }
        System.out.println();
        // System.out.println(Arrays.toString(A));
        if (args.length == 1) {
            int N = Integer.parseInt(args[0]);
            A = new int[N];
            binary_track(N);
        }
        else if (args.length == 2) {
            int N = Integer.parseInt(args[0]);
            int K = Integer.parseInt(args[1]);
            A = new int[N];
            digit_track(N, K);
        }
        else {
            System.out.println("Usage1: Bracktrack N");
            System.out.println("Usage2: Bracktrack N K");
        }
    }

    public static void binary_track(int n) {
        if (n == 0) 
            System.out.println(Arrays.toString(A));
        else {
            A[n-1] = 0;
            binary_track(n-1);
            A[n-1] = 1;
            binary_track(n-1);
        }
    }

    public static void digit_track(int n, int k) {
        if (n == 0) 
            System.out.println(Arrays.toString(A));
        else
            for (int i = 0; i < k; i++) {
                A[n-1] = i;
                digit_track(n-1, k);
            }        
    }
}
