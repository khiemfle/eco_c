extern crate base64;
extern crate openssl;

use openssl::symm::*;

const KEY: &'static [u8] = b"1234567890ABCDEF";
const IV: &'static [u8] = b"1234567890ABCDEF";
const CIPHERTEXT: &'static str = "QEVuQwBAEACuPUPByDkk5jyNzQ3Wd3xTy2Isihz62XTLe1M5qKQrvw==";
const HEADER_SIZE: usize = 8;

fn main() {
    let decoded = base64::decode(&CIPHERTEXT).unwrap();
    let ciphertext = &decoded[HEADER_SIZE..];

    let t = Cipher::aes_128_cbc();
    let mut d = Crypter::new(t, Mode::Decrypt, KEY, Some(IV)).unwrap();
    let mut result = vec![0; CIPHERTEXT.len() + t.block_size()];
    d.update(&ciphertext, &mut result).unwrap();
    let len = d.finalize(&mut result).unwrap();
    result.truncate(len);
    println!("{:?}", result);
    println!("{:?}", String::from_utf8_lossy(&result));
}