package main

import (
	"fmt"
	"strconv"
)

func binary_search( array []int, target int, start int, end int) int {
	if start > end {
		return (-1)
	}
	var mid int = (start + end) / 2
	if array[mid] == target {
		return mid
	} else if array[mid] > target {
		return binary_search( array, target, start, mid - 1 )
	} else {
		return binary_search( array, target, mid + 1, end )
	}
}

func binary_search_2( array []int, target int, start int, end int) int {
    for ; start <= end; {
        var mid int = (start + end) / 2
        if array[mid] == target {
            return mid
        } else if array[mid] > target {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    return (-1)
}

func main()  {
	array := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	target := 3
	result := binary_search( array, target, 0, array[len(array) - 1])
	fmt.Println("target index = " + strconv.Itoa(result))

	result = binary_search_2( array, target, 0, array[len(array) - 1])
	fmt.Println("target index = " + strconv.Itoa(result))
}