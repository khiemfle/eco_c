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
    let ciphertext = hex!("e2d9bb8d9b8222bd0c0b7904f3a8db71");

    let mut decrypter = Crypter::new(
     Cipher::aes_128_cbc(),
     Mode::Decrypt,
     &key,
     Some(&iv)).unwrap();
    
    decrypter.pad(false);

    let mut buf = ciphertext.to_vec();
    let mut plaintext = vec![0; ciphertext.len() + cipher.block_size()];
    let mut count = decrypter.update(&mut buf, &mut plaintext).unwrap();
    count += decrypter.finalize(&mut plaintext[count..]).unwrap();
    plaintext.truncate(count);

    let s = match str::from_utf8(&plaintext) {
            Ok(v) => v,
            Err(_e) => ""
        };

    println!("{}", s);

}