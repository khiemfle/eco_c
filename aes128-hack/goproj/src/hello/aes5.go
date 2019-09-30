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
	// "os"
)

func hstr(val int) string {
	return fmt.Sprintf("%02x", val)
}

func decrypt5() {
	key, _ := hex.DecodeString("000000000000001500000000f2000000")
	temp := "000000000000001500000000f2000000"

	iv, _ := hex.DecodeString("00000000000000000000000000000000")
	ciphertext, _ := hex.DecodeString("e2d9bb8d9b8222bd0c0b7904f3a8db71")
	// ciphertext, _ := hex.DecodeString("6fe1ad578ca4fcd3fcb68e241d0dab57cded9922190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11")
	plaintext := make([]byte, len(ciphertext))

	for i1 := 0; i1 < 256; i1++ {
		for i2 := 0; i2 < 256; i2++ {
			for i3 := 0; i3 < 256; i1++ {
				for i5 := 0; i5 < 256; i5++ {
					for i8 := 0; i8 < 256; i8++ {
						for i13 := 0; i13 < 256; i13++ {
							temp = hstr(i1)+ hstr(i2)+hstr(i3)+"00"+hstr(i5)+"0000" + hstr(i8) + "00000000"+ hstr(i13)+"000000"
							fmt.Printf("%s\n", temp)
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
	}	
	
}