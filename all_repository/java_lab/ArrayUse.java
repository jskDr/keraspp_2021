import java.util.*;

import java.util.Arrays;

public class ArrayUse {
    public void run() {
        System.out.println("Hello Java");
        
        int[] A = new int[10];
        A[5] = 37;
        System.out.format("A[5] = %d\n", A[5]);

        ListNode node = new ListNode(); // ListNode() is needed.
        node.setData(37);
        System.out.format("node.data = %d\n", node.getData());
        
        ListNode[] node_array = new ListNode[10];
        // Arrays.fill(node_array, new ListNode());
        Arrays.setAll(node_array, p -> new ListNode(p,null));
        System.out.format("node_array[3].data = %d\n", node_array[3].getData());
        node_array[5].setData(37);
        System.out.format("node_array[5].data = %d\n", node_array[5].getData());

        int[] X = {1,2,3};
        for(int x: X) System.out.println(x);
        System.out.println(Arrays.toString(X));
        Arrays.stream(X).forEach(System.out::println);  
    }
}
