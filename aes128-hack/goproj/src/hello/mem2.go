package main

import (
	// "io/ioutil"
	"fmt"
	"strings"
	// "strconv"
	"net"
	"bufio"
)

func serv() {
	ln, _ := net.Listen("tcp", ":19999")
	conn, _ := ln.Accept()
	for {
		// will listen for message to process ending in newline (\n)
		message, _ := bufio.NewReader(conn).ReadString('\n')
		// output message received
		fmt.Print("Message Received:", string(message))
		// sample process for string received
		newmessage := strings.ToUpper(message)
		// send new string back to client
		conn.Write([]byte(newmessage + "\n"))
	}
}
