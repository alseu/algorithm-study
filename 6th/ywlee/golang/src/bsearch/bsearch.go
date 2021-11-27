package bsearch

func BinarySearch( array []int, target int, start int, end int) int {
	if start > end {
		return (-1)
	}
	var mid int = (start + end) / 2
	if array[mid] == target {
		return mid
	} else if array[mid] > target {
		return BinarySearch( array, target, start, mid - 1 )
	} else {
		return BinarySearch( array, target, mid + 1, end )
	}
}

func BinarySearch2( array []int, target int, start int, end int) int {
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