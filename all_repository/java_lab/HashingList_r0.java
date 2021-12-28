public class HashingList {
    public class ListNode {
        private int key;
        private int data;
        private ListNode next;
        public int getKey() {
            return key;
        }
        public void setKey(int key) {
            this.key = key;
        }
        public int getData() {
            return data;
        }
        public void setData(int data) {
            this.data = data;
        }
        public ListNode getNext() {
            return next;
        }
        public void setNext(ListNode next) {
            this.next = next;
        }
    }

    public class HashTableNode {
        private ListNode startNode;
        public void setStartNode(ListNode startNode) {
            this.startNode = startNode;
        }
    }

    public class HashTable {
        private int tSize;
        private HashTableNode[] table;
        public int getTSize() {
            return tSize;
        }
        public void setTSize(int tSize) {
            this.tSize = tSize;
            table = new HashTableNode[tSize];
        }
        public HashTableNode[] getTable() {
            return table;
        }
    }

    public class HashTableOperations {
        public final int LOADFACTOR = 20;
        public HashTable createHashTable(int size) {
            HashTable h = new HashTable();
            h.setTSize(size/LOADFACTOR);
            for(int i=0; i < h.getTSize(); i++) {
                HashTableNode[] table = h.getTable();
                table[i].setStartNode(null);
            }
            return h;
        }
        public int hashSearch(HashTable h, int data) {
            return 0;
        }
        public void hashInsert(HashTable h, int data) {
        }
    }

    public void _run() {
        int size = 100;
        HashTableOperations ho = new HashTableOperations();
        HashTable h = ho.createHashTable(size);
        System.out.println("Hash table is created!");
        ho.hashInsert(h, 10);
        int yesno = ho.hashSearch(h, 10);
        System.out.println("Data is inserted and searched!");
    }

    public void run() {
        ListNode startNode;
        startNode = null;
    }

}
