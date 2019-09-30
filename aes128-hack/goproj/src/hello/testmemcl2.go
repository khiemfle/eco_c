package main

import "net"
import "fmt"
import "bufio"

func cl2() {

  // connect to this socket
  conn, _ := net.Dial("tcp", "127.0.0.1:19999")
  for i := 0; i < 100; i++ { 
    fmt.Fprintf(conn, "aabbcc" + "\n")
    // listen for reply
    message, _ := bufio.NewReader(conn).ReadString('\n')
    if message == "1" {
      fmt.Println("True")
    } else {
      fmt.Println("False")
    }
  }

  for {
    
  }
}