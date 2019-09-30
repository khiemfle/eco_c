package main

import (
	// "bytes"
	"crypto/aes"
	"crypto/cipher"
	// "crypto/rand"
	"encoding/hex"
	"fmt"
	// "io"
	"strings"
	"time"
	"strconv"
	"math/rand"
	"os"
	"log"
	"net"
	"bufio"
)

func splitTaskR9(argv []string) {
	s,_ := strconv.Atoi(argv[1])
	e,_ := strconv.Atoi(argv[2])
	var fr [6]int
	for i := 0; i < 6; i++ {
		conv, _ := strconv.ParseInt(argv[i+3], 16, 64)
		fr[i] = int(conv)
	}
	
	decryptR9(s, e, fr, argv[9], argv[10])
}

func newConn(port string) net.Conn {
	conn, _ := net.Dial("tcp", "127.0.0.1:" + port)

	return conn
}

func decryptR9(s int, e int, fr [6]int, port string, destExcludePath string) {
	conn := newConn(port)
	log.SetOutput(new(logWriter))

	logFile, err := os.OpenFile(destExcludePath, os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
	if err != nil {
		panic(err)
	}
	logger := log.New(logFile, "", 0)

	key, _ := hex.DecodeString("000000000000001500000000f2000000")
	temp := "000000000000001500000000f2000000"
	status :="000000"

	iv, _ := hex.DecodeString("00000000000000000000000000000000")
	// ciphertext, _ := hex.DecodeString("e2d9bb8d9b8222bd0c0b7904f3a8db71")
	// ciphertext, _ := hex.DecodeString("6fe1ad578ca4fcd3fcb68e241d0dab57cded9922190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11")
	ciphertext, _ := hex.DecodeString("6fe1ad578ca4fcd3fcb68e241d0dab57")

	plaintext := make([]byte, len(ciphertext))

	start := time.Now()

	for true {
		s1 := rand.NewSource(time.Now().UnixNano())
		r1 := rand.New(s1)
		i1 := r1.Intn(e-fr[0]) + fr[0]

		s2 := rand.NewSource(time.Now().UnixNano())
		r2 := rand.New(s2)
		i2 := r2.Intn(256)
		for i1 == fr[0] && i2 < fr[1] {
			i2 = r2.Intn(256)
		}

		s3 := rand.NewSource(time.Now().UnixNano())
		r3 := rand.New(s3)
		i3 := r3.Intn(256)
		for i1 == fr[0] && i2 == fr[1] && i3 < fr[2] {
			i3 = r3.Intn(256)
		}
		
		fmt.Printf("%s\n", time.Since(start))
		status = hstr(i1)+ hstr(i2)+hstr(i3)
		fmt.Printf("%s\n", status)
		start = time.Now()

		exist := false
		conn, exist = remoteCheck9(conn, status, port)
		if exist {
			continue
		}

		for i5 := 0; i5 < 256; i5++ {
			if i1 == fr[0] && i2 == fr[1] && i3 == fr[2] && i5 < fr[3] {
				continue
			}
			for i8 := 0; i8 < 256; i8++ {
				if i1 == fr[0] && i2 == fr[1] && i3 == fr[2] && i5 == fr[3] && i8 < fr[4] {
					continue
				}
					
				for i13 := 192; i13 < 256; i13++ {
					if i1 == fr[0] && i2 == fr[1] && i3 == fr[2] && i5 == fr[3] && i8 == fr[4] && i13 < fr[5] {
						continue
					}

					temp = hstr(i1)+ hstr(i2)+hstr(i3)+"00"+hstr(i5)+"0000" + hstr(i8) + "00000000"+ hstr(i13)+"000000"
					// fmt.Printf("%s\n", temp)
					key, _ = hex.DecodeString(temp)

					block, err := aes.NewCipher(key)
					if err != nil {
						panic(err)
					}

					if len(ciphertext) < aes.BlockSize {
						panic("ciphertext too short")
					}
					if len(ciphertext)%aes.BlockSize != 0 {
						panic("ciphertext is not a multiple of the block size")
					}

					mode := cipher.NewCBCDecrypter(block, iv)

					mode.CryptBlocks(plaintext, ciphertext)

					// fmt.Printf("%s\n", plaintext)
					if (strings.HasPrefix(strings.ToLower(string(plaintext[:])), "ttm4536{")) {
						fmt.Printf("%s\n", temp)
						fmt.Printf("%s\n", plaintext)

						logFile2, err2 := os.OpenFile("DONE.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
						if err2 != nil {
							panic(err2)
						}
						logger2 := log.New(logFile2, "", 0)
						logger2.Println(fmt.Sprintf("%s", temp))
						logger2.Println(fmt.Sprintf("%s", plaintext))

						panic("DONE")
					}
				}
			}
		}

		logger.Println(fmt.Sprintf("%s", status))
	}	
	
}

func remoteCheck9(conn net.Conn, status string, port string) (nconn net.Conn, rt bool) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recover!")
			rt = false
			nconn = newConn(port)
		}
	}()

	fmt.Fprintf(conn, status + "\n")
	message, _ := bufio.NewReader(conn).ReadString('\n')

	if message == "1" {
		rt = true
	} else {
		rt = false
	}

	nconn = conn

	return
}