#include <iostream>
using namespace std; 

class Point {
    public:
        Point(int, int);
        int getx();
        int gety();
    private:
        int x;
        int y;
};

Point::Point(int new_x, int new_y) {
    x = new_x;
    y = new_y;
}

int Point::getx() {
    return x;
}

int Point::gety() {
    return y;
}

ostream &operator<<(ostream &os, Point &p) {
   return os <<  p.getx() << endl;
}

void test1() {
    Point p1(1, 2);
    // std::cout << p1 << std::endl;
    cout << "(" << p1.getx() << "," << p1.gety() << ")" << endl;
}

int main() {
    test1();
    return 0;
}

