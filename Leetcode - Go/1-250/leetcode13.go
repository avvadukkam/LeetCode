func romanToInt(s string) int {
	romDict := map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	sum := 0

	for i := 0; i < len(s); i++ {
		if i != len(s)-1 && romDict[s[i]] < romDict[s[i+1]] {
			sum -= romDict[s[i]]
		} else {
			sum += romDict[s[i]]
		}
	}

	return sum
}