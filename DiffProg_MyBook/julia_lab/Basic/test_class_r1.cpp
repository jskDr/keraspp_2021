#include <iostream>
using namespace std; 

class DrawObj {
    public:
        DrawObj() {
            x = 0;
            y = 0;
        }
        DrawObj(int new_x, int new_y) {
            x = new_x;
            y = new_y;
        };
        DrawObj operator+(DrawObj p) {
            return DrawObj(x+p.x, y+p.y);
        };
        int getx() {return x;};
        int gety() {return y;};
        void setx(int new_x) {x = new_x;}
        void sety(int new_y) {y = new_y;}
        void operator=(DrawObj p){
            setx(p.getx());
            sety(p.gety());
        };
    private:
        int x;
        int y;
};

class Point : public DrawObj {
    public:
        Point(): DrawObj() {
        };
        Point(int new_x, int new_y): DrawObj(new_x, new_y) {
        };
        Point(DrawObj d) {
            setx(d.getx());
            sety(d.gety());
        }
};

class Vec2D : public DrawObj {
    public:
        Vec2D(): DrawObj() {
        };
        Vec2D(int new_x, int new_y): DrawObj(new_x, new_y) {
        };
        Vec2D(DrawObj d) {
            setx(d.getx());
            sety(d.gety());
        }
};


ostream &operator<<(ostream &os, Point &p) {
   return os << "(" << p.getx() <<"," << p.gety() << ")";
}

ostream &operator<<(ostream &os, Vec2D &p) {
   return os << "(" << p.getx() <<"," << p.gety() << ")";
}


void test1() {
    Point p1(1, 2);
    cout << p1 << endl;
}

void test2() {
    Point p1(1, 2), p2(3, 4);
    Point p = p1 + p2;
    cout << p << endl;
    // cout << (p1 + p2) << endl;

    Vec2D v1(5,6);
    cout << v1 << endl;
    p = v1 + p1;
    cout << p << endl;
}

int main() {
    test1();
    cout << "--------------------" << endl;
    test2();
    return 0;
}

