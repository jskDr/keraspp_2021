#include<iostream>
#include<vector>

int sum_vector(int *vector, int size)
{
    int sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += vector[i];
    }
    return sum;
}

// a function to sum all the elements of a vector
int sum_vec(std::vector<int> vector)
{
    int sum = 0;
    for (int i = 0; i < vector.size(); i++)
    {
        sum += vector[i];
    }
    return sum;
}

class sum_vec_class
{
public:
    int sum_vec(std::vector<int> vector)
    {
        int sum = 0;
        for (int i = 0; i < vector.size(); i++)
        {
            sum += vector[i];
        }
        return sum;
    }
    float sum_vec(std::vector<float> vector)
    {
        float sum = 0;
        for (int i = 0; i < vector.size(); i++)
        {
            sum += vector[i];
        }
        return sum;
    }
};

int main() {
    // print hello world
    std::cout << "Hello World!" << std::endl;

    // declare and initialize a vector of size 5
    int vector[5] = {1, 2, 3, 4, 5};
    // print the sum of the vector
    std::cout << sum_vector(vector, 5) << std::endl;

    // declare and initialize a integer vector of size 2
    std::vector<int> vector_int(5);
    vector_int[0] = 100;
    vector_int[1] = 200;
    vector_int[4] = 300;
    // print the sum of the integer vector
    std::cout << sum_vec(vector_int) << std::endl;

    // declare and initialize a integer vector of size 2
    sum_vec_class *myclass = new sum_vec_class();
    std::vector<int> vector_int_2(3);
    vector_int_2[0] = 500;
    vector_int_2[1] = 600;
    vector_int_2[2] = 700;
    // print the sum of the integer vector
    std::cout << myclass->sum_vec(vector_int_2) << std::endl;

    // initialize a float vector of size 2
    std::vector<float> vector_float(2);
    vector_float[0] = 1.2;
    vector_float[1] = 2.5;
    // print the sum of the float vector
    std::cout << myclass->sum_vec(vector_float) << std::endl;

    return 0;
}