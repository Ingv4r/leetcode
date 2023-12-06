package main

import (
	"fmt"
	"math"
)

func maxProfit(prices []int) int {
    left, right := 0, 1
	var maxProfit float64 = 0.0
	for right < len(prices) {
		var curProfit float64 = float64(prices[right]) - float64(prices[left])
		switch prices[left] < prices[right] {
		case true:
			maxProfit = math.Max(curProfit, maxProfit)
		case false:
			left = right
		}
		right ++
	}
	return int(maxProfit)
}

func main() {
	prices := []int{7,1,5,3,6,4}
	fmt.Println(maxProfit(prices))
}