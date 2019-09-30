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
	// "os"
)

func splitTaskR1(argv []string) {
	s,_ := strconv.Atoi(argv[1])
	e,_ := strconv.Atoi(argv[2])
	var fr [6]int
	for i := 0; i < 6; i++ {
		conv, _ := strconv.ParseInt(argv[i+3], 16, 64)
		fr[i] = int(conv)
	}
	
	decryptR1(s, e, fr)
}

func decryptR1(s int, e int, fr [6]int) {
	key, _ := hex.DecodeString("000000000000001500000000f2000000")
	temp := "000000000000001500000000f2000000"
	status :="000000"

	iv, _ := hex.DecodeString("00000000000000000000000000000000")
	ciphertext, _ := hex.DecodeString("e2d9bb8d9b8222bd0c0b7904f3a8db71")
	// ciphertext, _ := hex.DecodeString("6fe1ad578ca4fcd3fcb68e241d0dab57cded9922190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11")
	plaintext := make([]byte, len(ciphertext))

	start := time.Now()

	for true {
		s1 := rand.NewSource(time.Now().UnixNano())
		r1 := rand.New(s1)
		i1 := r1.Intn(256)
		for i1 < fr[0] || i1 >= e {
			i1 = r1.Intn(256)
		}
		fmt.Printf("%d\n", i1)

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

		for i5 := 0; i5 < 256; i5++ {
			if i1 == fr[0] && i2 == fr[1] && i3 == fr[2] && i5 < fr[3] {
				continue
			}
			for i8 := 0; i8 < 256; i8++ {
				if i1 == fr[0] && i2 == fr[1] && i3 == fr[2] && i5 == fr[3] && i8 < fr[4] {
					continue
				}
					
				for i13 := 0; i13 < 256; i13++ {
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
						panic("DONE")
					}
				}
			}
		}
	}	
	
}