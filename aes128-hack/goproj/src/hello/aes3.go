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

func ExampleNewCBCDecrypter() {
	key, _ := hex.DecodeString("6368616e676520746869732070617373")
	iv, _ := hex.DecodeString("00000000000000000000000000000000")
	ciphertext, _ := hex.DecodeString("f42512e1e4039213bd449ba47faa1b74")

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
	if (strings.HasPrefix(plaintext, "example")) {
		fmt.Printf("%s\n", plaintext)
	}

	
}

func ExampleNewCBCEncrypter() {
	// Load your secret key from a safe place and reuse it across multiple
	// NewCipher calls. (Obviously don't use this example key for anything
	// real.) If you want to convert a passphrase to a key, use a suitable
	// package like bcrypt or scrypt.
	key, _ := hex.DecodeString("6368616e676520746869732070617373")
	iv, _ := hex.DecodeString("00000000000000000000000000000000")
	plaintext := []byte("exampleplaintext")

	// CBC mode works on blocks so plaintexts may need to be padded to the
	// next whole block. For an example of such padding, see
	// https://tools.ietf.org/html/rfc5246#section-6.2.3.2. Here we'll
	// assume that the plaintext is already of the correct length.
	if len(plaintext)%aes.BlockSize != 0 {
		panic("plaintext is not a multiple of the block size")
	}

	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err)
	}

	// The IV needs to be unique, but not secure. Therefore it's common to
	// include it at the beginning of the ciphertext.
	ciphertext := make([]byte, len(plaintext))
	// iv := ciphertext[:aes.BlockSize]
	// if _, err := io.ReadFull(rand.Reader, iv); err != nil {
	// 	panic(err)
	// }
	
	fmt.Printf("%x\n", string(iv[:]))
	mode := cipher.NewCBCEncrypter(block, iv)
	mode.CryptBlocks(ciphertext, plaintext)

	// It's important to remember that ciphertexts must be authenticated
	// (i.e. by using crypto/hmac) as well as being encrypted in order to
	// be secure.

	fmt.Printf("%x\n", ciphertext)
}