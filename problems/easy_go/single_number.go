package main

import (
	"fmt"
)


func singleNumber(nums []int) int {
	// Find the element in array, where count of this is 1.
	counter := make(map[int]int)
	for _, c := range nums {
		counter[c] += 1
	}
	for val, key := range counter {
		if key == 1 {
			return val
		}
	}
	return 0
}

func main() {
	// Main function. Print result to terminal.
	numbers := singleNumber([]int{4,4,4,1,1,5,2,2})
	fmt.Println(numbers)
}