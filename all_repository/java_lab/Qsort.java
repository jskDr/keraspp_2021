public class Qsort {
    public int pivot(int[] A, int low, int high) {
        int left = low, right = high, p_item = A[low];
        while (left < right) { // left=0, right=4
            while(A[left] <= p_item && left < high) left++;
            while(A[right] > p_item) right--; // since there is p_item in the most left (low), right can not be lowere than low.
            // while(A[right] > p_item && right > low) right--;
            if(left < right) swap(A, left, right);
        }
        A[low] = A[right];
        A[right] = p_item;
        return right;
    }
    public void sort(int[] A, int low, int high) {
        int p_pos;
        if (high > low) { // if it is more than one element
            p_pos = pivot(A, low, high); // A, 0, 4
            sort(A, low, p_pos-1);
            sort(A, p_pos+1, high);
        } 
    }
    void swap(int[] A, int left, int right) {
        int tmp = A[left];
        A[left] = A[right];
        A[right] = tmp;
    }
    void print_int_array(int[] A) {
        if (A.length > 0) {
            System.out.print("[");
            for (int i=0; i < A.length - 1; i++)
                System.out.print(A[i] + ", ");
            System.out.println(A[A.length-1] +"]");
        }
        else {
            System.out.println("--empty array--");
        }
    }
    public void qsort_test() {
        int[] A = {3, 8, 2, 5, 7};
        System.out.println("Before sorting:");
        print_int_array(A);
        qsort(A);
        System.out.println("After sorting:");
        print_int_array(A);
        // System.out.println(Arrays.toString(A));        
    }
    public void qsort(int[] A) {
        sort(A, 0, A.length-1);        
    }
    public int bin_search(int[] A, int left, int right, int a) {
        if (left <= right) { 
            int mid = left + (right - left) / 2;
            if (A[mid] == a) {
                return mid; 
            } else if (A[mid] > a) {
                return bin_search(A, left, mid-1, a);
            } else {
                return bin_search(A, mid+1, right, a);
            }
        }
        return -1;
    }
    public int bsearch(int[] A, int a) {
        return bin_search(A, 0, A.length-1, a);
    }
    public void binsearch_test() {
        int[] A = {3, 8, 2, 5, 7, 1, 10, 9};       
        print_int_array(A);
        qsort(A); 
        print_int_array(A);
        int a = 9;
        System.out.println("Search for " + a);
        int ix = bsearch(A, a);
        System.out.println(ix);
    }
}
