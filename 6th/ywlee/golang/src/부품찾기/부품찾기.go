package 부품찾기

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"

	"../bsearch"
)

func InputNumWithSpace(n int) []int {
	/*
		https://stackoverflow.com/questions/39565055/read-a-set-of-integers-separated-by-space-in-golang
		입력받을 숫자의 개수를 매개변수로 받아서 공백으로 구분된 입력값을 []int 형으로 반환
	*/

	arr := make([]int, n)

	for i := 0; i < n; i++ {
		if _, err := fmt.Scan(&arr[i]); err != nil {
			panic(err)
		}
	}
	return arr
}

func InputNumWithSpace2(n int) string {
	/*
		개행 문자만을 구분자로 사용하여 문자열을 입력받는 방법
		https://edu.goorm.io/qna/2679
		fmt.Scan 계열 함수들은 공백문자도 구분자로 인식하기 때문에 공백이 포함된 문자열을 한 번에 입력받으려면 좀 복잡하게 접근해야 한다.

	*/
	in := bufio.NewReader(os.Stdin)
	line, err := in.ReadString('\n')
	if err != nil {
		panic(err)
	}

	return line
}

func ConvStrToIntArr(s_arr []string, n int) []int {
	/*
		string 슬라이스(s_arr)와 크기(n)을 입력받아 []int 형으로 변환하여 반환
	*/
	i_arr := make([]int, n)
	for i := range s_arr {
		i_arr[i], _ = strconv.Atoi(strings.TrimRight(s_arr[i], "\n")) // 문자열 뒤에 있는 줄바꿈 문자 삭제
	}
	return i_arr
}

func FindParts() {
	var n int
	if _, err := fmt.Scanln(&n); err != nil {
		panic(err)
	}

	own_parts := InputNumWithSpace(n)
	sort.Ints(own_parts)
	fmt.Println(own_parts)

	var m int
	if _, err := fmt.Scanln(&m); err != nil {
		panic(err)
	}

	req_parts := InputNumWithSpace(m)

	var result string
	for _, p := range req_parts {
		fmt.Println(bsearch.BinarySearch(own_parts, p, 0, n-1))
		if bsearch.BinarySearch(own_parts, p, 0, n-1) > 0 {
			result += "yes "
		} else {
			result += "no "
		}
	}
	fmt.Println(result)
}

func FindParts2() {
	var n int
	if _, err := fmt.Scanln(&n); err != nil {
		panic(err)
	}

	s_own_parts := InputNumWithSpace2(n)
	own_parts := ConvStrToIntArr(strings.Split(s_own_parts, " "), n)
	sort.Ints(own_parts)

	var m int
	if _, err := fmt.Scanln(&m); err != nil {
		panic(err)
	}

	s_req_parts := InputNumWithSpace2(m)
	req_parts := ConvStrToIntArr(strings.Split(s_req_parts, " "), m)

	var result string
	for _, p := range req_parts {
		if bsearch.BinarySearch(own_parts, p, 0, n-1) != -1 {
			result += "yes "
		} else {
			result += "no "
		}
	}
	fmt.Println(result)
}
