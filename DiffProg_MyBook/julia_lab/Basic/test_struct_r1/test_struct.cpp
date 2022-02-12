#include <iostream>

struct Point {
    int x;
    int y;
};

void test1() {
    struct Point p1; //= Point(1, 2);
    p1.x = 1;
    p1.y = 2;
    
    std::cout << "(" << p1.x << "," << p1.y << ")" << std::endl;
}

int main() {
    test1();
    return 0;
}

