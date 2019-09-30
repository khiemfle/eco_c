#!/bin/bash
# echo 0: e2d9bb8d9b8222bd0c0b7904f3a8db71 | xxd -r | openssl enc -d -aes-128-cbc -nopad -iv 00000000000000000000000000000000 -K 000000000000001500000000f2000000
# echo 0: 6fe1ad578ca4fcd3fcb68e241d0dab57 | xxd -r | openssl enc -d -aes-128-cbc -nopad -iv 00000000000000000000000000000000 -K 000000000000001500000000f2000000


for i1 in {0..255}
do  
    i1Str=`printf "%02x" $i1`
    for i2 in {0..255}
    do
        i2Str=`printf "%02x" $i2`
        for i3 in {0..255}
        do
            i3Str=`printf "%02x" $i3`
            for i5 in {0..255}
            do
                i5Str=`printf "%02x" $i5`
                for i8 in {0..255}
                do
                    i8Str=`printf "%02x" $i8`
                    for i13 in {192..255}
                    do
                        i13Str=`printf "%02x" $i13`
                        key="${i1Str}${i2Str}${i3Str}00${i5Str}0000${i8Str}00000000${i13Str}000000"
                        echo ${key}
                        out=`echo 0: e2d9bb8d9b8222bd0c0b7904f3a8db71 | xxd -r | openssl enc -d -aes-128-cbc -nopad -iv 00000000000000000000000000000000 -K ${key}`
                        # out=`echo 0: e2d9bb8d9b8222bd0c0b7904f3a8db71 | xxd -r | openssl enc -d -aes-128-cbc -nopad -iv 00000000000000000000000000000000 -K 000000000000001500000000f2000000`

                        if [[ $out == TTM4536{* ]]
                        then
                            echo $out
                            echo $key
                            exit 1
                        fi
                    done
                done
            done
        done
    done
done
