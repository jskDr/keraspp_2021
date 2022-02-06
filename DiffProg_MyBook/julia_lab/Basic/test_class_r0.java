class Point {
    int x, y;
    public Point(int new_x, int new_y) {
        x = new_x;
        y = new_y;
    } 
    public String toString() {
        return getClass().getSimpleName() + "(" + x + ", " + y + ")";
    }
    public Point add(Point p) {
        return new Point(x + p.x, y + p.y);
    }
}

class test_class {
    public static void test1() {
        Point p1 = new Point(1, 2);
        System.out.println(p1);
    }
    public static void test2() {
        Point p1 = new Point(1, 2);
        Point p2 = new Point(3, 4);
        System.out.println(p1.add(p2)); // java doesn't support operator overloading!
        System.out.println(p1);
    }    
    public static void main(String[] args) {
        test1();
        System.out.println("--------------------");
        test2();
    }
}