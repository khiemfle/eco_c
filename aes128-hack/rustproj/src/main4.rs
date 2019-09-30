#[macro_use] extern crate hex_literal;
extern crate crypto;
extern crate rand;
extern crate rustc_serialize;

use crypto::aes::{self, KeySize};
use crypto::digest::Digest;
use crypto::hmac::Hmac;
use crypto::mac::Mac;
use crypto::sha2::Sha256;
use crypto::symmetriccipher::SynchronousStreamCipher;
use crypto::blockmodes;
use crypto::buffer;
use crypto::buffer::{ ReadBuffer, WriteBuffer, BufferResult };

use rustc_serialize::base64::{STANDARD, ToBase64};
use rustc_serialize::hex::ToHex;

use std::iter::repeat;
use rand::{OsRng, Rng};
use std::str;

fn main() {
    decrypt2()
}

fn decrypt2() {

    // let mut gen = OsRng::new().expect("Failed to get OS random generator");
    // let mut key: Vec<u8> = repeat(0u8).take(16).collect();
    // gen.fill_bytes(&mut key[..]);
    // let mut nonce: Vec<u8> = repeat(0u8).take(16).collect();
    // gen.fill_bytes(&mut nonce[..]);
    // println!("Key: {}", key.to_base64(STANDARD));
    // println!("Nonce: {}", nonce.to_base64(STANDARD));

    let key = hex!("000000000000001500000000f2000000");
    let iv = hex!("00000000000000000000000000000000");

    let mut cipher = aes::cbc_encryptor(KeySize::KeySize128, &key, &iv, blockmodes::PkcsPadding);
    let secret = b"TTM4536{afasfas}";
    let mut final_result = Vec::<u8>::new();
    let mut read_buffer = buffer::RefReadBuffer::new(secret);
    let mut buffer = [0; 4096];
    let mut write_buffer = buffer::RefWriteBuffer::new(&mut buffer);
    let result = cipher.encrypt(&mut read_buffer, &mut write_buffer, true);
    
    final_result.extend(write_buffer.take_read_buffer().take_remaining().iter().map(|&i| i));

    let s = match str::from_utf8(&final_result) {
        Ok(v) => v,
        Err(e) => panic!("Invalid UTF-8 sequence: {}", e),
    };

    println!("result: {}", s);

}

