class Solution {
    public String reorganizeString(String S) {
        int len = S.length(), num = (len + 1) / 2, max = 0;
        char tc = ' ';
        int[] counts = new int[26];
        char[] sa = S.toCharArray(), res = new char[len];
        // get the count of all chars, and find the most frequent character
        for (int i = 0; i < len; i++) {
            int c = ++counts[sa[i] - 'a'];
            if (c > num) return "";
            if (c > max) {
                max = c;
                tc = sa[i];
            }
        }
        // fill into the array
        for (int i = 0, j = 0; i < len; i += 2) {
            if (max > 0) {
                res[i] = tc;
                counts[tc - 'a']--;
                max--;
            } else {
                for (; j < 26; j++) {
                    if (counts[j] > 0) {
                        res[i] = (char)('a' + j);
                        counts[j]--;
                        break;
                    }
                }
            }
            if (i % 2 == 0 && i + 2 >= len) i = -1;
        }
        return new String(res);
    }
}
