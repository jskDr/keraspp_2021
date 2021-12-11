import java.util.*;

public class Qsort {
    public static int pivot(int[] A, int low, int high) {
        int left = low, right = high, p_item = A[low];
        while (left < right) { // left=0, right=4
            while(A[left] <= p_item && left < high) left++;
            while(A[right] > p_item) right--;
            // while(A[right] > p_item && right > low) right--;
            if(left < right) swap(A, left, right);
        }
        A[low] = A[right];
        A[right] = p_item;
        return right;
    }
    public static void sort(int[] A, int low, int high) {
        int p_pos;
        if (high > low) { // if it is more than one element
            p_pos = pivot(A, low, high); // A, 0, 4
            sort(A, low, p_pos-1);
            sort(A, p_pos+1, high);
        } 
    }
    static void swap(int[] A, int left, int right) {
        int tmp = A[left];
        A[left] = A[right];
        A[right] = tmp;
    }
    public void qsort_test() {
        int[] A = {3, 8, 2, 5, 7};
        sort(A, 0, A.length-1);
        System.out.println(Arrays.toString(A));        
    }
    public static void main(String[] args) {
        System.out.println("Qsort");
        // int[] A = new int[3]; // array size -> 3
        int[] A = {3, 8, 2, 5, 7};
        sort(A, 0, A.length-1);
        System.out.println(Arrays.toString(A));
        // Arrays.stream(A).forEach(System.out::println);
    }
}
