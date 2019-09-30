package main

import (
	// "io/ioutil"
	"fmt"
	// "strings"
	"strconv"
	"net"
	"bufio"
)

func serv3() {
	fmt.Println("Start reading")
	read1()
	fmt.Println("Done reading")
	ln, _ := net.Listen("tcp", ":19999")
	conn, _ := ln.Accept()
	fmt.Println("Start listening")
	for {
		// will listen for message to process ending in newline (\n)
		message, _ := bufio.NewReader(conn).ReadString('\n')
		fmt.Println(message)
		ret := "0"
		if exist3(message) {
			ret = "1";
		}
		conn.Write([]byte(ret + "\n"))
	}
}

func exist3(str string) (rt bool) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Program recovered!")
			rt = false
		}
	}()

	h1, _ := strconv.ParseInt(str[0:2], 16, 64)
	h2, _ := strconv.ParseInt(str[2:4], 16, 64)
	h3, _ := strconv.ParseInt(str[4:6], 16, 64)

	rt = exclude[h1][h2][h3]
	return
}