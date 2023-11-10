package main

import "fmt"

func main() {
	var arr [1]int
	arr[0] = 9
	fmt.Println(plusOne(arr[:]))
}

func addFirst(s []int, insertValue int) []int {
	res := make([]int, len(s)+1)
	copy(res[1:], s)
	res[0] = insertValue
	return res
}

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] == 9 {
			digits[i] = 0
		} else {
			digits[i] = digits[i] + 1
			return digits
		}
	}
	return addFirst(digits, 1)
}