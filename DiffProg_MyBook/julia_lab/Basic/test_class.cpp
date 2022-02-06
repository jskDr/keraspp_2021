#include <iostream>
using namespace std; 

class Vec2D {
    public:
        Vec2D(int, int);
        int getx();
        int gety();
    private:
        int x;
        int y;
};

class Point {
    public:
        Point() {
            x = 0;
            y = 0;
        }
        Point(int, int);
        int getx();
        int gety();
        Point operator+(const Point& p) const {
            return Point(x+p.x, y+p.y);
        };
        Point operator+(Vec2D&) const;
        void operator=(Point& p) {
            x += p.x;
            y += p.y;
        };
    private:
        int x;
        int y;
};

Point Point::operator+(Vec2D& v) const {
    return Point(x + v.getx(), y + v.gety());
}   

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
   return os << "Point(" << p.getx() <<", " << p.gety() << ")";
}

Vec2D::Vec2D(int new_x, int new_y) {
    x = new_x;
    y = new_y;
}

int Vec2D::getx() {
    return x;
}

int Vec2D::gety() {
    return y;
}

ostream &operator<<(ostream &os, Vec2D &v) {
   return os << "Vec2D(" << v.getx() <<", " << v.gety() << ")";
}

void test1() {
    Point p1(1, 2);
    cout << p1 << endl;
}

void test2() {
    Point p1(1, 2);
    Point p2(3, 4);
    // cout << (p1 + p2) << endl;

    Point p3 = p1 + p2; // Point p3() <-- Error, no () is needed
    cout << p3 << endl;

    Vec2D v1(5, 6);
    cout << v1 << endl;
    // cout << v1.getx() << endl;
    Point p4 = p1 + v1;
    cout << p4 << endl;
}

int main() {
    test1();
    cout << "--------------------" << endl;
    test2();
    return 0;
}

