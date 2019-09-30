package main

import (
	// "io/ioutil"
	// "fmt"
	// "strings"
	"strconv"
	"net"
	"bufio"
)

func serv6() {
	read1()
	startPort := 19000
	for i := 0; i < 40; i++ {
		port := startPort + i
		go newConnection(port)
	}

	for {

	}
}

func newConnection(port int) {
	ln, _ := net.Listen("tcp", ":" + strconv.Itoa(port))
	conn, _ := ln.Accept()
	for {
		// will listen for message to process ending in newline (\n)
		message, _ := bufio.NewReader(conn).ReadString('\n')
		if len(message) == 0 {
			conn.Close()
			conn, _ = ln.Accept()
		}
		// fmt.Println(message)
		ret := "0"
		if exist3(message) {
			ret = "1";
		}
		conn.Write([]byte(ret + "\n"))
	}
}
