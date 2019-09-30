#[macro_use] extern crate hex_literal;
extern crate aes_soft as aes;
extern crate block_modes;
extern crate hex;

use block_modes::{BlockMode, Cbc};
use block_modes::block_padding::Pkcs7;
use aes::Aes128;
use std::str;

fn main() {
    decrypt2()
}

fn decrypt2() {
    type Aes128Cbc = Cbc<Aes128, Pkcs7>;

    let key = hex!("000000000000001500000000f2000000");
    let iv = hex!("00000000000000000000000000000000");
    let plaintext = "ttm4536{afasfas}".as_bytes();
    
    
    let cipher = Aes128Cbc::new_var(&key, &iv).unwrap();
    let mut buffer = [0u8; 32];
    let pos = plaintext.len();
    buffer[..pos].copy_from_slice(plaintext);
    let ciphertext = cipher.encrypt(&mut buffer, pos).unwrap();
    println!("result: {}", hex::encode(ciphertext));

    // assert_eq!(ciphertext, hex!("1b7a4c403124ae2fb52bedc534d82fa8"));

    let cipher = Aes128Cbc::new_var(&key, &iv).unwrap();
    let mut buf = ciphertext.to_vec();
    let decrypted_ciphertext = cipher.decrypt(&mut buf);

    if let Err(_err) = decrypted_ciphertext {
        println!("Error {}", _err)
    } else {
        let s = match str::from_utf8(decrypted_ciphertext.unwrap()) {
            Ok(v) => v,
            Err(e) => panic!("Invalid UTF-8 sequence: {}", e),
        };

        println!("result: {}", s);
        assert!(decrypted_ciphertext.unwrap().starts_with(b"ttm4536{"));
    }

}

fn decrypt1() {
    // create an alias for convenience
    type Aes128Cbc = Cbc<Aes128, Pkcs7>;

    let key = hex!("000102030405060708090a0b0c0d0e0f");
    let iv = hex!("f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff");
    let plaintext = b"Hello world!";
    let cipher = Aes128Cbc::new_var(&key, &iv).unwrap();

    // buffer must have enough space for message+padding
    let mut buffer = [0u8; 32];
    // copy message to the buffer
    let pos = plaintext.len();
    buffer[..pos].copy_from_slice(plaintext);
    let ciphertext = cipher.encrypt(&mut buffer, pos).unwrap();

    assert_eq!(ciphertext, hex!("1b7a4c403124ae2fb52bedc534d82fa8"));

    // re-create cipher mode instance and decrypt the message
    let cipher = Aes128Cbc::new_var(&key, &iv).unwrap();
    let mut buf = ciphertext.to_vec();
    let decrypted_ciphertext = cipher.decrypt(&mut buf).unwrap();

    assert_eq!(decrypted_ciphertext, plaintext);
    println!("Test");

    // With an enabled std feature (which is enabled by default) you can use encrypt_vec and descrypt_vec methods:

    // let cipher = Aes128Cbc::new_var(&key, &iv).unwrap();
    // let ciphertext = cipher.encrypt_vec(plaintext);

    // assert_eq!(ciphertext, hex!("1b7a4c403124ae2fb52bedc534d82fa8"));

    // let cipher = Aes128Cbc::new_var(&key, &iv).unwrap();
    // let decrypted_ciphertext = cipher.decrypt_vec(&ciphertext).unwrap();

    // assert_eq!(decrypted_ciphertext, plaintext);
}

