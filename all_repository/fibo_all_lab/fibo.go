package main

import "fmt"

func fibo(n int) int {
	if n < 2 {
		return n
	}
	return fibo(n-1) + fibo(n-2)
}

func main() {
	fmt.Println(fibo(45))
}
