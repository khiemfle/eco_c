package main

import (
	// "io/ioutil"
	"fmt"
	// "strings"
	"strconv"
	"net"
	"bufio"
	"time"
)

func serv8() {
	initStorage()
	read2()
	startPort := 19000
	for i := 0; i < 40; i++ {
		port := startPort + i
		go newConnection8(port)
	}

	for {
		time.Sleep(time.Second*3)
		read2()
	}
}

func newConnection8(port int) {
	ln, _ := net.Listen("tcp", ":" + strconv.Itoa(port))
	conn, _ := ln.Accept()
	for {
		// will listen for message to process ending in newline (\n)
		message, _ := bufio.NewReader(conn).ReadString('\n')
		if len(message) == 0 {
			conn.Close()
			conn, _ = ln.Accept()
		}
		ret := "0"
		
		if exist3(message) {
			ret = "1";
		} else {
			fmt.Println(message)
		}
		conn.Write([]byte(ret + "\n"))
	}
}
