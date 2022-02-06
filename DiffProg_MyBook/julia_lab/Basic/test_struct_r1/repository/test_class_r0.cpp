/*
[2022-2-2]
Class with public member variables
*/
#include <iostream>

class Point {
    public: 
        int x;
        int y;
};

void test1() {
    class Point p1; //= Point(1, 2);
    p1.x = 1;
    p1.y = 2;
    
    std::cout << "(" << p1.x << "," << p1.y << ")" << std::endl;
}

int main() {
    test1();
    return 0;
}

