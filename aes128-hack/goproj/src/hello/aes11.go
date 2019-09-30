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
	"os"
	"log"
)


func splitTask11(argv []string) {
	s,_ := strconv.Atoi(argv[1])
	e,_ := strconv.Atoi(argv[2])
	var fr [6]int
	for i := 0; i < 6; i++ {
		conv, _ := strconv.ParseInt(argv[i+3], 16, 64)
		fr[i] = int(conv)
	}
	
	decrypt11(s, e, fr)
}

func decrypt11(s int, e int, fr [6]int) {
	log.SetOutput(new(logWriter))

	key, _ := hex.DecodeString("000000000000001500000000f2000000")
	temp := "000000000000001500000000f2000000"
	status :="000000"

	iv, _ := hex.DecodeString("00000000000000000000000000000000")
	// ciphertext, _ := hex.DecodeString("e2d9bb8d9b8222bd0c0b7904f3a8db71")
	// ciphertext, _ := hex.DecodeString("6fe1ad578ca4fcd3fcb68e241d0dab57cded9922190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11")
	ciphertext, _ := hex.DecodeString("6fe1ad578ca4fcd3fcb68e241d0dab57")
	// ciphertext, _ := hex.DecodeString("b6f0cfaaa857d60df4012eee2eeffe45")
	
	plaintext := make([]byte, len(ciphertext))

	start := time.Now()

	for i1 := s; i1 < e; i1++ {
		if i1 < fr[0] || i1 >= e {
			continue
		}
		for i2 := 0; i2 < 256; i2++ {
			if i1 == fr[0] && i2 < fr[1] {
				continue
			}
			for i3 := 0; i3 < 256; i3++ {
				if i1 == fr[0] && i2 == fr[1] && i3 < fr[2] {
					continue
				}
				fmt.Printf("%s\n", time.Since(start))
				status = hstr(i1)+ hstr(i2)+hstr(i3)
        		fmt.Printf("%s\n", status)
				start = time.Now()

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

							block, _ := aes.NewCipher(key)

							mode := cipher.NewCBCDecrypter(block, iv)

							mode.CryptBlocks(plaintext, ciphertext)

							// fmt.Printf("%s\n", plaintext)
							if (strings.HasPrefix(strings.ToLower(string(plaintext[:])), "ttm4536{")) {
								logFile2, err2 := os.OpenFile("DONE.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
								if err2 != nil {
									panic(err2)
								}
								logger2 := log.New(logFile2, "", 0)
								logger2.Println(fmt.Sprintf("%s", temp))
								logger2.Println(fmt.Sprintf("%s", plaintext))

								fmt.Printf("%s\n", temp)
								fmt.Printf("%s\n", plaintext)
								panic("DONE")
							}
						}
					}
				}
			}
		}
	}	
	
}