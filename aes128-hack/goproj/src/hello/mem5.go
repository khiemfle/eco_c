package main

import (
	// "io/ioutil"
	"fmt"
	// "strings"
	// "strconv"
	"net"
	"bufio"
)

func serv5() {
	read1()
	ln, _ := net.Listen("tcp", ":19999")
	conn, _ := ln.Accept()
	for {
		// will listen for message to process ending in newline (\n)
		message, _ := bufio.NewReader(conn).ReadString('\n')
		if len(message) == 0 {
			conn.Close()
			conn, _ = ln.Accept()
		}
		fmt.Println(message)
		ret := "0"
		if exist3(message) {
			ret = "1";
		}
		conn.Write([]byte(ret + "\n"))
	}
	
}
