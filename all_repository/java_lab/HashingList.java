public class HashingList {
    public int Hash(int data, int tSize) {
        return data % tSize;
    }

    public class HashTableNode {
        private int blockCount;
        private KeyListNode startNode;
        public int getBlockCount() {
            return blockCount;
        }
        public void setBlockCount(int blockCount) {
            this.blockCount = blockCount;
        }
        public void setStartNode(KeyListNode startNode) {
            this.startNode = startNode;
        }
        public KeyListNode getStartNode() {
            return startNode;
        }
        public KeyListNode getLastNode() {
            KeyListNode curNode = startNode, prevNode = startNode;
            while(curNode != null) {
                prevNode = curNode;
                curNode = curNode.getNext();
            }
            return prevNode;
        }
    }

    public class HashTable {
        private int tSize;
        private int count;
        private HashTableNode[] table;
        public int getTSize() {
            return tSize;
        }
        public void setTSize(int tSize) {
            this.tSize = tSize;
            table = new HashTableNode[tSize];
            for(int i=0; i < table.length; i++) {
                table[i] = new HashTableNode();
            }
        }
        public int getCount() {
            return count;
        }
        public void setCount(int count) {
            this.count = count;
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
        public boolean hashSearch(HashTable h, int data) {
            int index = Hash(data, h.getTSize());
            KeyListNode node = h.getTable()[index].getStartNode();
            while(node != null) {
                if(node.getData() == data) 
                    return true;
                node = node.getNext();
            }
            return false;
        }
        public int hashInsert(HashTable h, int data) {
            int index;
            KeyListNode newNode, lastNode;
            if(!hashSearch(h, data)) {
                index = Hash(data, h.getTSize()); 
                // temp = node.getNext();
                newNode = new KeyListNode();
                if(newNode == null) {
                    System.out.println("Memory Error!");
                    return -1;
                }      
                newNode.setKey(index);
                newNode.setData(data);

                // System.out.println(h.getTable().length);
                // System.out.println(index);
                HashTableNode table_index = h.getTable()[index];
                // System.out.println(table_index.getStartNode());

                lastNode = table_index.getLastNode();
                if(lastNode != null) {
                    newNode.setNext(lastNode.getNext()); // <-null
                    lastNode.setNext(newNode);
                }
                else {
                    table_index.setStartNode(newNode);
                }
                table_index.setBlockCount(table_index.getBlockCount()+1);
                h.setCount(h.getCount()+1);
                if(h.getCount() / h.getTSize() > LOADFACTOR)
                    rehash(h);
                return 1;
            }
            return 0;
        }
        public boolean hashDelete(HashTable h, int data) {
            int index = Hash(data, h.getTSize());
            KeyListNode node = h.getTable()[index].getStartNode();
            KeyListNode prevNode = null;
            while(node != null) {
                if(node.getData() == data) {
                    if(prevNode == null) {
                        h.getTable()[index].setStartNode(null);
                        node = null;    
                    }
                    else {
                        prevNode.setNext(node.getNext());
                        node = null;
                    }
                    return true; // delete success
                }
                prevNode = node;
                node = node.getNext();
            }
            return false;
        }
        public void hashList(HashTable h) {
            HashTableNode[] table = h.getTable();
            KeyListNode startNode;
            for(int i=0; i < table.length; i++) {
                startNode = table[i].getStartNode();
                if(startNode != null) {
                    while(startNode != null) {
                        System.out.println(i + ": Data = " + startNode.getData());
                        startNode = startNode.getNext();
                    }
                }
                else 
                    System.out.println(i + ": node = <null>");
                System.out.println();
            }
        }
        public HashTable rehash(HashTable h){
            int size = h.getTSize() * LOADFACTOR;
            HashTableNode[] table = h.getTable();
            HashTable new_h = createHashTable(size * 2);
 
            HashTableNode[] new_h_table = new_h.getTable();
            for(int i=0; i < h.getTSize(); i++) {
                for(KeyListNode node = table[i].getStartNode();
                    node != null; node = node.getNext()) {
                    hashInsert(new_h, node.getData());
                }
            }            
            return new_h;
        }
    }

    public void run() {
        int size = 100;
        HashTableOperations ho = new HashTableOperations();
        HashTable h = ho.createHashTable(size);
        System.out.println("Hash table is created!");

        ho.hashInsert(h, 2);
        System.out.println("Data is inserted!"); 
        ho.hashInsert(h, 7);
        System.out.println("Data is inserted!");
        ho.hashInsert(h, 5);
        System.out.println("Data is inserted!");
        ho.hashInsert(h, 10);
        System.out.println("Data is inserted!");        

        ho.hashList(h);

        boolean yesno;
        yesno = ho.hashSearch(h, 2);
        System.out.println("Data is searched: " + yesno);
        yesno = ho.hashSearch(h, 7);
        System.out.println("Data is searched: " + yesno);       
        yesno = ho.hashSearch(h, 8);
        System.out.println("Data is searched: " + yesno);   
        yesno = ho.hashSearch(h, 10);
        System.out.println("Data is searched: " + yesno);   
        yesno = ho.hashSearch(h, 15);
        System.out.println("Data is searched: " + yesno);         
        yesno = ho.hashSearch(h, 5);
        System.out.println("Data is searched: " + yesno);   
        
        yesno = ho.hashDelete(h, 2);
        if(yesno)
            System.out.println("Data is deleted");
        else 
            System.out.println("No such data exist");
        
        yesno = ho.hashDelete(h, 2);
        if(yesno)
            System.out.println("Data is deleted");
        else 
            System.out.println("No such data exist");    
        
        ho.hashInsert(h, 9);
        ho.hashList(h);
        HashTable new_h = ho.rehash(h);
        System.out.println("New Hash table");
        ho.hashList(new_h);
        // System.out.format("TSize: %d\n", new_h.getTSize());
    }
}
