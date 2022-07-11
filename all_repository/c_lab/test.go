package main

import "fmt"

func sum_of_vector(vector []int) int {
	sum := 0
	for i, v := range vector {
		fmt.Println(i, ": ", v)
		sum += v
	}
	return sum
}

func main() {
	fmt.Println("hello world")

	// initialize vector
	vector := []int{10, 20, 30, 40, 50}
	sum := sum_of_vector(vector)
	fmt.Println(sum) // it should be 15.
}
