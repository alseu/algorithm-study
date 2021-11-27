package 개똥벌레

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func InputObs(n int) ([]int, []int) {
	/*
		https://jaewook.me/golang-fast-io-for-competitive-programming	Go Competitive Programming을 위한 빠른 입출력하기
	*/
	j := make([]int, 0, 10)
	s := make([]int, 0, 10)
	reader := bufio.NewReader(os.Stdin)

	for i := 0; i < n; i++ {
		bytes, _, _ := reader.ReadLine()
		num, _ := strconv.Atoi(string(bytes))

		if i%2 == 0 {
			j = append(j, num)
		} else {
			s = append(s, num)
		}
	}

	return j, s
}

func Bugs() {
	var n, h int
	fmt.Scan(&n, &h)

	j, s := InputObs(n)
	sort.Ints(j)
	sort.Ints(s)

	min := n
	count := 0

	// 익명함수 선언
	binarySearch := func(arr []int, target float32, start int, end int) int {
		var mid int
		for start <= end {
			mid = int((start + end) / 2)
			if float32(arr[mid]) < target {
				start = mid + 1
			} else {
				end = mid - 1
			}
		}
		return start
	}

	var j_count, s_count int
	for i := 1; i < h+1; i++ {
		j_count = len(j) - binarySearch(j, float32(i)-0.5, 0, len(j)-1)
		s_count = len(s) - binarySearch(s, float32(h-i)+0.5, 0, len(s)-1)

		if min == j_count+s_count {
			count += 1
		} else if min > j_count+s_count {
			count = 1
			min = j_count + s_count
		}
	}
	fmt.Println(min, count)
}

/*
제출 번호	  아이디	문제	 결과	       메모리	 시간	언어	코드 길이
35831696	lyw1217	3020	맞았습니다!!	7872	116	Go / 수정	1240
*/
