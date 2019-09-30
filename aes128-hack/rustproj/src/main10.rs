#[macro_use] extern crate hex_literal;
extern crate hex;
extern crate time;

extern crate base64;
extern crate openssl;

use openssl::symm::*;

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
    let cipher = Cipher::aes_128_cbc();
    let iv = hex!("00000000000000000000000000000000");
    // let ciphertext = hex!("e2d9bb8d9b8222bd0c0b7904f3a8db71");
    let ciphertext = hex!("6fe1ad578ca4fcd3fcb68e241d0dab57");
    let mut buf = ciphertext.to_vec();

    let mut start = PreciseTime::now();

    // println!("{} {}", s, e);

    for i1 in (s..e).step_by(1) {
        if i1 < fr[0]{
            continue;
        }
        let i1str = hstr(i1);

        for i2 in (0..256).step_by(1) {
            if i1 == fr[0] && i2 < fr[1] {
                continue;
            }
            let i2str = hstr(i2);

            for i3 in (0..256).step_by(1)  {
                if i1 == fr[0] && i2 == fr[1] && i3 < fr[2] {
                    continue;
                }
                let i3str = hstr(i3);

                let end = PreciseTime::now();
                println!("{} seconds", start.to(end));
                let status = format!("{}{}{}", i1str, i2str, i3str);
                start = PreciseTime::now();

                println!("{}",status);
                for i5 in (0..256).step_by(1)  {
                    let i5str = hstr(i5);

                    for it in (0..256).step_by(1)  {
                        let itstr = hstr(it);

                        for i13 in (192..256).step_by(1)  {
                            let i13str = hstr(i13);

                            let mut plaintext = vec![0; ciphertext.len() + cipher.block_size()];

                            let temp = format!("{}{}{}00{}0000{}00000000{}000000", i1str, i2str, i3str, i5str, itstr, i13str);
                            // println!("{}",temp);
                            let key = hex::decode(temp);

                            let mut decrypter = Crypter::new(
                                cipher,
                                Mode::Decrypt,
                                &key.unwrap(),
                                Some(&iv)).unwrap();
                            decrypter.pad(false);

                            let mut count = decrypter.update(&mut buf, &mut plaintext).unwrap();
                            count += decrypter.finalize(&mut plaintext[count..]).unwrap();
                            plaintext.truncate(count);

                            if plaintext.starts_with(b"ttm4536{") {
                                let s = match str::from_utf8(&plaintext) {
                                    Ok(v) => v,
                                    Err(_e) => continue
                                };

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

