package main

import (
	"io/ioutil"
	"fmt"
	"strings"
	"strconv"
	// "net"
	// "bufio"
	"time"
)

var fileMap map[string]time.Time

func serv7() {
	initStorage()
	read2()
	startPort := 19000
	for i := 0; i < 40; i++ {
		port := startPort + i
		go newConnection(port)
	}

	for {
		time.Sleep(time.Second*3)
		read2()
	}
}

func initStorage() {
	fileMap = make(map[string]time.Time)

	for i1 := 0; i1 < 256; i1++ {
		for i2 := 0; i2 < 256; i2++ {
			for i3 := 0; i3 < 256; i3++ {
				exclude[i1][i2][i3] = false
			}
		}
	}
}

func read2() {
	files, err := ioutil.ReadDir("excludes")
    check(err)
    for _, f := range files {
		if f.ModTime() == fileMap[f.Name()] {
			continue
		}
		fmt.Println("Got updated from " + f.Name())
		fileMap[f.Name()] = f.ModTime()

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
}

