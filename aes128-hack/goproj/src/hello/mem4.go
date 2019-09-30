package main

import (
	// "io/ioutil"
	"fmt"
	// "strings"
	// "strconv"
	"net"
	"bufio"
)

func serv4() {
	fmt.Println("Start reading")
	read1()
	fmt.Println("Done reading")
	ln, _ := net.Listen("tcp", ":19999")
	conn, _ := ln.Accept()
	fmt.Println("Start listening")
	for {
		// will listen for message to process ending in newline (\n)
		message, _ := bufio.NewReader(conn).ReadString('\n')
		if len(message) == 0 {
			break
		}
		fmt.Println(message)
		ret := "0"
		if exist3(message) {
			ret = "1";
		}
		conn.Write([]byte(ret + "\n"))
	}
}
