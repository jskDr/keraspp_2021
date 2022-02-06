class Point {
    int x, y;
    public Point(int new_x, int new_y) {
        x = new_x;
        y = new_y;
    } 
    public String toString() {
        return getClass().getSimpleName() + "(" + x + ", " + y + ")";
    }
}

class test_class {
    public static void main(String[] args) {
        Point p1 = new Point(1, 2);
        System.out.println(p1);
    }
}