import java.io.UnsupportedEncodingException;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.IOException;
import java.io.File;

// 
// Decompiled by Procyon v0.5.36
// 

public class MD5
{

    static class MD5$1 {}

    private MD5.MD5State workingState;
    private MD5.MD5State finalState;
    private int[] decodeBuffer;
    private static final byte[] padding;
    
    public MD5() {
        this.workingState = new MD5.MD5State();
        this.finalState = new MD5.MD5State();
        this.decodeBuffer = new int[16];
        this.reset();
    }
    
    public static void main(final String[] array) {
        if (array.length == 0) {
            System.err.println("Please specify a file.");
        }
        else {
            for (final String s : array) {
                try {
                    System.out.println(getHashString(new File(s)) + " " + s);
                }
                catch (IOException ex) {
                    System.err.println(ex.getMessage());
                }
            }
        }
    }
    
    public byte[] getHash() {
        if (!MD5.MD5State.access$000(this.finalState)) {
            MD5.MD5State.access$100(this.finalState, this.workingState);
            final long access$200 = MD5.MD5State.access$200(this.finalState);
            final int n = (int)(access$200 >>> 3 & 0x3FL);
            this.update(this.finalState, MD5.padding, 0, (n < 56) ? (56 - n) : (120 - n));
            this.update(this.finalState, encode(access$200), 0, 8);
            MD5.MD5State.access$002(this.finalState, true);
        }
        return encode(MD5.MD5State.access$300(this.finalState), 16);
    }
    
    public String getHashString() {
        return toHex(this.getHash());
    }
    
    public static byte[] getHash(final byte[] array) {
        final MD5 md5 = new MD5();
        md5.update(array);
        return md5.getHash();
    }
    
    public static String getHashString(final byte[] array) {
        final MD5 md5 = new MD5();
        md5.update(array);
        return md5.getHashString();
    }
    
    public static byte[] getHash(final InputStream inputStream) throws IOException {
        final MD5 md5 = new MD5();
        final byte[] b = new byte[1024];
        int read;
        while ((read = inputStream.read(b)) != -1) {
            md5.update(b, read);
        }
        return md5.getHash();
    }
    
    public static String getHashString(final InputStream inputStream) throws IOException {
        final MD5 md5 = new MD5();
        final byte[] b = new byte[1024];
        int read;
        while ((read = inputStream.read(b)) != -1) {
            md5.update(b, read);
        }
        return md5.getHashString();
    }
    
    public static byte[] getHash(final File file) throws IOException {
        final FileInputStream fileInputStream = new FileInputStream(file);
        final byte[] hash = getHash(fileInputStream);
        fileInputStream.close();
        return hash;
    }
    
    public static String getHashString(final File file) throws IOException {
        final FileInputStream fileInputStream = new FileInputStream(file);
        final String hashString = getHashString(fileInputStream);
        fileInputStream.close();
        return hashString;
    }
    
    public static byte[] getHash(final String s) {
        final MD5 md5 = new MD5();
        md5.update(s);
        return md5.getHash();
    }
    
    public static String getHashString(final String s) {
        final MD5 md5 = new MD5();
        md5.update(s);
        return md5.getHashString();
    }
    
    public static byte[] getHash(final String s, final String s2) throws UnsupportedEncodingException {
        final MD5 md5 = new MD5();
        md5.update(s, s2);
        return md5.getHash();
    }
    
    public static String getHashString(final String s, final String s2) throws UnsupportedEncodingException {
        final MD5 md5 = new MD5();
        md5.update(s, s2);
        return md5.getHashString();
    }
    
    public void reset() {
        MD5.MD5State.access$400(this.workingState);
        MD5.MD5State.access$002(this.finalState, false);
    }
    
    @Override
    public String toString() {
        return this.getHashString();
    }
    
    private void update(final MD5.MD5State md5State, final byte[] array, final int n, int n2) {
        MD5.MD5State.access$002(this.finalState, false);
        if (n2 + n > array.length) {
            n2 = array.length - n;
        }
        int n3 = (int)(MD5.MD5State.access$200(md5State) >>> 3) & 0x3F;
        MD5.MD5State.access$202(md5State, MD5.MD5State.access$200(md5State) + (n2 << 3));
        final int n4 = 64 - n3;
        int i = 0;
        if (n2 >= n4) {
            System.arraycopy(array, n, MD5.MD5State.access$500(md5State), n3, n4);
            transform(md5State, this.decode(MD5.MD5State.access$500(md5State), 64, 0));
            for (i = n4; i + 63 < n2; i += 64) {
                transform(md5State, this.decode(array, 64, i));
            }
            n3 = 0;
        }
        if (i < n2) {
            final int n5 = i;
            while (i < n2) {
                MD5.MD5State.access$500(md5State)[n3 + i - n5] = array[i + n];
                ++i;
            }
        }
    }
    
    public void update(final byte[] array, final int n, final int n2) {
        this.update(this.workingState, array, n, n2);
    }
    
    public void update(final byte[] array, final int n) {
        this.update(array, 0, n);
    }
    
    public void update(final byte[] array) {
        this.update(array, 0, array.length);
    }
    
    public void update(final byte b) {
        this.update(new byte[] { b }, 1);
    }
    
    public void update(final String s) {
        this.update(s.getBytes());
    }
    
    public void update(final String s, final String charsetName) throws UnsupportedEncodingException {
        this.update(s.getBytes(charsetName));
    }
    
    private static String toHex(final byte[] array) {
        final StringBuffer sb = new StringBuffer(array.length * 2);
        for (int length = array.length, i = 0; i < length; ++i) {
            final int j = array[i] & 0xFF;
            if (j < 16) {
                sb.append("0");
            }
            sb.append(Integer.toHexString(j));
        }
        return sb.toString();
    }
    
    private static int FF(int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7) {
        n += ((n2 & n3) | (~n2 & n4));
        n += n5;
        n += n7;
        n = (n << n6 | n >>> 32 - n6);
        return n + n2;
    }
    
    private static int GG(int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7) {
        n += ((n2 & n4) | (n3 & ~n4));
        n += n5;
        n += n7;
        n = (n << n6 | n >>> 32 - n6);
        return n + n2;
    }
    
    private static int HH(int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7) {
        n += (n2 ^ n3 ^ n4);
        n += n5;
        n += n7;
        n = (n << n6 | n >>> 32 - n6);
        return n + n2;
    }
    
    private static int II(int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7) {
        n += (n3 ^ (n2 | ~n4));
        n += n5;
        n += n7;
        n = (n << n6 | n >>> 32 - n6);
        return n + n2;
    }
    
    private static byte[] encode(final long n) {
        return new byte[] { (byte)(n & 0xFFL), (byte)(n >>> 8 & 0xFFL), (byte)(n >>> 16 & 0xFFL), (byte)(n >>> 24 & 0xFFL), (byte)(n >>> 32 & 0xFFL), (byte)(n >>> 40 & 0xFFL), (byte)(n >>> 48 & 0xFFL), (byte)(n >>> 56 & 0xFFL) };
    }
    
    private static byte[] encode(final int[] array, final int n) {
        final byte[] array2 = new byte[n];
        int n2;
        for (int i = n2 = 0; i < n; i += 4) {
            array2[i] = (byte)(array[n2] & 0xFF);
            array2[i + 1] = (byte)(array[n2] >>> 8 & 0xFF);
            array2[i + 2] = (byte)(array[n2] >>> 16 & 0xFF);
            array2[i + 3] = (byte)(array[n2] >>> 24 & 0xFF);
            ++n2;
        }
        return array2;
    }
    
    private int[] decode(final byte[] array, final int n, final int n2) {
        int n3;
        for (int i = n3 = 0; i < n; i += 4) {
            this.decodeBuffer[n3] = ((array[i + n2] & 0xFF) | (array[i + 1 + n2] & 0xFF) << 8 | (array[i + 2 + n2] & 0xFF) << 16 | (array[i + 3 + n2] & 0xFF) << 24);
            ++n3;
        }
        return this.decodeBuffer;
    }
    
    private static void transform(final MD5.MD5State md5State, final int[] array) {
        final int n = MD5.MD5State.access$300(md5State)[0];
        final int n2 = MD5.MD5State.access$300(md5State)[1];
        final int n3 = MD5.MD5State.access$300(md5State)[2];
        final int n4 = MD5.MD5State.access$300(md5State)[3];
        final int ff = FF(n, n2, n3, n4, array[0], 7, -680876936);
        final int ff2 = FF(n4, ff, n2, n3, array[1], 12, -389564586);
        final int ff3 = FF(n3, ff2, ff, n2, array[2], 17, 606105819);
        final int ff4 = FF(n2, ff3, ff2, ff, array[3], 22, -1044525330);
        final int ff5 = FF(ff, ff4, ff3, ff2, array[4], 7, -176418897);
        final int ff6 = FF(ff2, ff5, ff4, ff3, array[5], 12, 1200080426);
        final int ff7 = FF(ff3, ff6, ff5, ff4, array[6], 17, -1473231341);
        final int ff8 = FF(ff4, ff7, ff6, ff5, array[7], 22, -45705983);
        final int ff9 = FF(ff5, ff8, ff7, ff6, array[8], 7, 1770035416);
        final int ff10 = FF(ff6, ff9, ff8, ff7, array[9], 12, -1958414417);
        final int ff11 = FF(ff7, ff10, ff9, ff8, array[10], 17, -42063);
        final int ff12 = FF(ff8, ff11, ff10, ff9, array[11], 22, -1990404162);
        final int ff13 = FF(ff9, ff12, ff11, ff10, array[12], 7, 1804603682);
        final int ff14 = FF(ff10, ff13, ff12, ff11, array[13], 12, -40341101);
        final int ff15 = FF(ff11, ff14, ff13, ff12, array[14], 17, -1502002290);
        final int ff16 = FF(ff12, ff15, ff14, ff13, array[15], 22, 1236535329);
        final int gg = GG(ff13, ff16, ff15, ff14, array[1], 5, -165796510);
        final int gg2 = GG(ff14, gg, ff16, ff15, array[6], 9, -1069501632);
        final int gg3 = GG(ff15, gg2, gg, ff16, array[11], 14, 643717713);
        final int gg4 = GG(ff16, gg3, gg2, gg, array[0], 20, -373897302);
        final int gg5 = GG(gg, gg4, gg3, gg2, array[5], 5, -701558691);
        final int gg6 = GG(gg2, gg5, gg4, gg3, array[10], 9, 38016083);
        final int gg7 = GG(gg3, gg6, gg5, gg4, array[15], 14, -660478335);
        final int gg8 = GG(gg4, gg7, gg6, gg5, array[4], 20, -405537848);
        final int gg9 = GG(gg5, gg8, gg7, gg6, array[9], 5, 568446438);
        final int gg10 = GG(gg6, gg9, gg8, gg7, array[14], 9, -1019803690);
        final int gg11 = GG(gg7, gg10, gg9, gg8, array[3], 14, -187363961);
        final int gg12 = GG(gg8, gg11, gg10, gg9, array[8], 20, 1163531501);
        final int gg13 = GG(gg9, gg12, gg11, gg10, array[13], 5, -1444681467);
        final int gg14 = GG(gg10, gg13, gg12, gg11, array[2], 9, -51403784);
        final int gg15 = GG(gg11, gg14, gg13, gg12, array[7], 14, 1735328473);
        final int gg16 = GG(gg12, gg15, gg14, gg13, array[12], 20, -1926607734);
        final int hh = HH(gg13, gg16, gg15, gg14, array[5], 4, -378558);
        final int hh2 = HH(gg14, hh, gg16, gg15, array[8], 11, -2022574463);
        final int hh3 = HH(gg15, hh2, hh, gg16, array[11], 16, 1839030562);
        final int hh4 = HH(gg16, hh3, hh2, hh, array[14], 23, -35309556);
        final int hh5 = HH(hh, hh4, hh3, hh2, array[1], 4, -1530992060);
        final int hh6 = HH(hh2, hh5, hh4, hh3, array[4], 11, 1272893353);
        final int hh7 = HH(hh3, hh6, hh5, hh4, array[7], 16, -155497632);
        final int hh8 = HH(hh4, hh7, hh6, hh5, array[10], 23, -1094730640);
        final int hh9 = HH(hh5, hh8, hh7, hh6, array[13], 4, 681279174);
        final int hh10 = HH(hh6, hh9, hh8, hh7, array[0], 11, -358537222);
        final int hh11 = HH(hh7, hh10, hh9, hh8, array[3], 16, -722521979);
        final int hh12 = HH(hh8, hh11, hh10, hh9, array[6], 23, 76029189);
        final int hh13 = HH(hh9, hh12, hh11, hh10, array[9], 4, -640364487);
        final int hh14 = HH(hh10, hh13, hh12, hh11, array[12], 11, -421815835);
        final int hh15 = HH(hh11, hh14, hh13, hh12, array[15], 16, 530742520);
        final int hh16 = HH(hh12, hh15, hh14, hh13, array[2], 23, -995338651);
        final int ii = II(hh13, hh16, hh15, hh14, array[0], 6, -198630844);
        final int ii2 = II(hh14, ii, hh16, hh15, array[7], 10, 1126891415);
        final int ii3 = II(hh15, ii2, ii, hh16, array[14], 15, -1416354905);
        final int ii4 = II(hh16, ii3, ii2, ii, array[5], 21, -57434055);
        final int ii5 = II(ii, ii4, ii3, ii2, array[12], 6, 1700485571);
        final int ii6 = II(ii2, ii5, ii4, ii3, array[3], 10, -1894986606);
        final int ii7 = II(ii3, ii6, ii5, ii4, array[10], 15, -1051523);
        final int ii8 = II(ii4, ii7, ii6, ii5, array[1], 21, -2054922799);
        final int ii9 = II(ii5, ii8, ii7, ii6, array[8], 6, 1873313359);
        final int ii10 = II(ii6, ii9, ii8, ii7, array[15], 10, -30611744);
        final int ii11 = II(ii7, ii10, ii9, ii8, array[6], 15, -1560198380);
        final int ii12 = II(ii8, ii11, ii10, ii9, array[13], 21, 1309151649);
        final int ii13 = II(ii9, ii12, ii11, ii10, array[4], 6, -145523070);
        final int ii14 = II(ii10, ii13, ii12, ii11, array[11], 10, -1120210379);
        final int ii15 = II(ii11, ii14, ii13, ii12, array[2], 15, 718787259);
        final int ii16 = II(ii12, ii15, ii14, ii13, array[9], 21, -343485551);
        final int[] access$300 = MD5.MD5State.access$300(md5State);
        final int n5 = 0;
        access$300[n5] += ii13;
        final int[] access$301 = MD5.MD5State.access$300(md5State);
        final int n6 = 1;
        access$301[n6] += ii16;
        final int[] access$302 = MD5.MD5State.access$300(md5State);
        final int n7 = 2;
        access$302[n7] += ii15;
        final int[] access$303 = MD5.MD5State.access$300(md5State);
        final int n8 = 3;
        access$303[n8] += ii14;
    }
    
    static {
        padding = new byte[] { -128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    }
    

    // 
    // Decompiled by Procyon v0.5.36
    // 

    private class MD5State
    {
        private boolean valid;
        private int[] state;
        private long bitCount;
        private byte[] buffer;
        
        
        private void reset() {
            this.state[0] = 1732584193;
            this.state[1] = -271733879;
            this.state[2] = -1732584194;
            this.state[3] = 271733878;
            this.bitCount = 0L;
        }
        
        private MD5State() {
            this.valid = true;
            this.state = new int[4];
            this.buffer = new byte[64];
            this.reset();
        }
        
        private void copy(final MD5State md5State) {
            System.arraycopy(md5State.buffer, 0, this.buffer, 0, this.buffer.length);
            System.arraycopy(md5State.state, 0, this.state, 0, this.state.length);
            this.valid = md5State.valid;
            this.bitCount = md5State.bitCount;
        }
    }
}