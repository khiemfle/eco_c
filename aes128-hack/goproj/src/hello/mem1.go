package main

import (
	"io/ioutil"
	// "fmt"
	"strings"
	"strconv"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

var exclude [256][256][256]bool

func read1() {
	
	for i1 := 0; i1 < 256; i1++ {
		for i2 := 0; i2 < 256; i2++ {
			for i3 := 0; i3 < 256; i3++ {
				exclude[i1][i2][i3] = false
			}
		}
	}

	files, err := ioutil.ReadDir("excludes")
    check(err)
    for _, f := range files {
        dat, err := ioutil.ReadFile("excludes/" + f.Name())
		check(err)
		trimed := strings.Trim(string(dat), " |\n")
		spl := strings.Split(trimed, "\n")
		for i := 0; i < len(spl); i++ {
			temp := spl[i]
			h1, _ := strconv.ParseInt(temp[0:2], 16, 64)
			h2, _ := strconv.ParseInt(temp[2:4], 16, 64)
			h3, _ := strconv.ParseInt(temp[4:6], 16, 64)
			
			exclude[h1][h2][h3] = true;
		}
    }
	// for str := range spl {
	// 	fmt.Println(str)
	// }

}

func exist(str string) bool {
	h1, _ := strconv.ParseInt(str[0:2], 16, 64)
	h2, _ := strconv.ParseInt(str[2:4], 16, 64)
	h3, _ := strconv.ParseInt(str[4:6], 16, 64)
	return exclude[h1][h2][h3]
}