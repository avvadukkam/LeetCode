func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	org := x
	rev_num := 0

	for x > 0 {
		rev_num = rev_num*10 + x%10
		x /= 10
	}

	return org == rev_num
}