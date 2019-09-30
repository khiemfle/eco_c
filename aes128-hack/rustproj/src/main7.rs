#[macro_use] extern crate hex_literal;
extern crate base64;
extern crate openssl;

use openssl::symm::*;
use std::str;

fn main() {
    let cipher = Cipher::aes_128_cbc();
    let data = b"TTM4536{afasfas}";
    // let data = b"Some Crypto Text";
    let key = hex!("000000000000001500000000f2000000");
    let iv = hex!("00000000000000000000000000000000");
    let ciphertext = encrypt(
        cipher,
        &key,
        Some(&iv),
        data).unwrap();

    let b = hex::encode(&ciphertext);

    println!("{}", b);

    // let s = match str::from_utf8(&ciphertext) {
    //     Ok(v) => v,
    //     Err(e) => panic!("Invalid UTF-8 sequence: {}", e),
    // };

    // println!("{}", s);

    // assert_eq!(
    //     b"\xB4\xB9\xE7\x30\xD6\xD6\xF7\xDE\x77\x3F\x1C\xFF\xB3\x3E\x44\x5A\x91\xD7\x27\x62\x87\x4D\
    //     \xFB\x3C\x5E\xC4\x59\x72\x4A\xF4\x7C\xA1",
    //     &ciphertext[..]);
}