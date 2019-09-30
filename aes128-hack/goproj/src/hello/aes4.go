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

func decrypt() {
	key, _ := hex.DecodeString("000000000000001500000000f2000000")
	iv, _ := hex.DecodeString("00000000000000000000000000000000")
	
	ciphertext, _ := hex.DecodeString("e2d9bb8d9b8222bd0c0b7904f3a8db71")
	// ciphertext, _ := hex.DecodeString("6fe1ad578ca4fcd3fcb68e241d0dab57cded9922190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11")

	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err)
	}

	if len(ciphertext) < aes.BlockSize {
		panic("ciphertext too short")
	}
	// fmt.Printf("%x\n", string(iv[:]))

	// CBC mode always works in whole blocks.
	if len(ciphertext)%aes.BlockSize != 0 {
		panic("ciphertext is not a multiple of the block size")
	}

	mode := cipher.NewCBCDecrypter(block, iv)

	mode.CryptBlocks(ciphertext, ciphertext)

	plaintext := string(ciphertext[:])
	fmt.Printf("%s\n", plaintext)
	if (strings.HasPrefix(strings.ToLower(plaintext), "ttm4536{")) {
		fmt.Printf("%s\n", plaintext)
	}

	
}