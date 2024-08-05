def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 0

    for i in range(len(s)):
        count += 1

        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed.append(s[i])
            compressed.append(str(count))
            count = 0

        compressed_string = ''.join(compressed)
        return compressed_string if len(compressed_string) < len(s) else s