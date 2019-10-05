Flag: ttm4536{Banana-limk-shake2019}

Using tshark!?
- https://hackertarget.com/tshark-tutorial-and-filter-examples/

https://stackoverflow.com/questions/13149751/force-gzip-to-decompress-despite-crc-error
    For force decompressing the file that has error checking code!
gzip -dc who.txt.gz > who1.txt
gzip -dc who.txt.gz extract
gzip -dc who.txt.gz 
gzip -d who.txt.gz
??
gzip: who.txt.gz: invalid compressed data--crc error

gzip: who.txt.gz: invalid compressed data--length error

binwalk -D 'GIF image:GIF' http-filter.pcap -e --directory=tmp1

binwalk -D 'GIF image:GIF' communication_bf7e55e0e6f3b0ca3ad60e956907f546.pcap -e --directory=/tmp1

binwalk -D 'GIF image:GIF' communication_bf7e55e0e6f3b0ca3ad60e956907f546.pcap

binwalk -D 'gif image:gif' communication_bf7e55e0e6f3b0ca3ad60e956907f546.pcap

binwalk -D 'GIF out1.GIF' -D 'GIF out2.GIF' -e communication_bf7e55e0e6f3b0ca3ad60e956907f546.pcap

libwebp!?

print(response[:header_length])
header_length = response.find('\r\n\r\n') + 4

response = ''.join(packet[Raw].load for packet in server_packets)

client_packets = PacketList([p for p in packets if p[IP].src == '192.168.56.1' and raw in p])
client_packets = PacketList([p for p in packets if p[IP].src == '192.168.56.1 and Raw in p])
server_packets = PacketList([p for p in packets if p[IP].src == '192.168.56.5' and Raw in p])
    This is for ICMP?

len(packets)
    290 packets

packets2 = PacketList([IP(p[Raw].load) for p in packets])

ip = IP(packets[0][Raw].load)

packets = [p for p in pcap if Raw in p]
    For removing packets with empty content!?

pcap = defragment(pcap)
    <Defragmented http-filter.pcap: TCP:517 UDP:46 ICMP:10 Other:16>

pcap = rdpcap('http-filter.pcap')

Binwalk tool!?

Google tools for decoding the image files!
- dwebp 
- https://developers.google.com/speed/webp/docs/precompiled

Insufficient image data!?

RIFF.X..WEBPVP8X

http://support.moonpoint.com/software/file_formats/riff/webpvp8/

od -H -N 4 fromClientHttp.WebP

od -t x -N 4 fromClientHttp.WebP

Using TCP stream of Wireshark to get a gif file!!
- Select each stream for saving!!
- Save using the RAW format!!