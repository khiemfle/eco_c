#[macro_use] extern crate hex_literal;
extern crate aes_soft as aes;
extern crate block_modes;
extern crate hex;
extern crate time;

use block_modes::{BlockMode, Cbc};
use block_modes::block_padding::Pkcs7;
use block_modes::block_padding::ZeroPadding;
use aes::Aes128;
use std::str;
use std::process;
use std::env;
use time::PreciseTime;

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut arr: [i32; 3] = [args[3].parse().unwrap(), args[4].parse().unwrap(), args[5].parse().unwrap()];
    decrypt3(args[1].parse().unwrap(), args[2].parse().unwrap(), &mut arr)
}

fn hstr(val: i32) -> String {
    return format!("{:02x}", val);
}

fn decrypt3(s: i32, e: i32, fr: &mut [i32]) {
    type Aes128Cbc = Cbc<Aes128, ZeroPadding>;
    let iv = hex!("00000000000000000000000000000000");
    // let ciphertext = hex!("e2d9bb8d9b8222bd0c0b7904f3a8db71");
    let ciphertext = hex!("6fe1ad578ca4fcd3fcb68e241d0dab57");

    let mut start = PreciseTime::now();

    println!("{} {}", s, e);

    for i1 in (s..e).step_by(1) {
        if i1 < fr[0]{
            continue;
        }

        for i2 in (0..256).step_by(1) {
            if i1 == fr[0] && i2 < fr[1] {
                continue;
            }
            for i3 in (0..256).step_by(1)  {
                if i1 == fr[0] && i2 == fr[1] && i3 < fr[2] {
                    continue;
                }
                let end = PreciseTime::now();
                println!("{} seconds", start.to(end));
                let status = format!("{}{}{}", hstr(i1), hstr(i2), hstr(i3));
                start = PreciseTime::now();

                println!("{}",status);
                for i5 in (0..256).step_by(1)  {
                    for it in (0..256).step_by(1)  {
                        for i13 in (192..256).step_by(1)  {

                            let temp = format!("{}{}{}00{}0000{}00000000{}000000", hstr(i1), hstr(i2), hstr(i3), hstr(i5), hstr(it),hstr(i13));
                            println!("{}",temp);
                            let key = hex::decode(temp);

                            let cipher = Aes128Cbc::new_var(&key.unwrap(), &iv).unwrap();
                            let mut buf = ciphertext.to_vec();
                            let decrypted_ciphertext = cipher.decrypt(&mut buf);

                            if let Err(_err) = decrypted_ciphertext {
                                println!("Error {}", _err)
                            } else {
                                let s = match str::from_utf8(decrypted_ciphertext.unwrap()) {
                                    Ok(v) => v,
                                    Err(_e) => continue
                                };

                                if decrypted_ciphertext.unwrap().starts_with(b"TTM4536{") {
                                    println!("result: {}", s);
                                    println!("result: {},{},{},{},{},{}", i1, i2, i3, i5, it, i13);
                                    process::exit(1);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

fn decrypt2() {
    type Aes128Cbc = Cbc<Aes128, ZeroPadding>;

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

