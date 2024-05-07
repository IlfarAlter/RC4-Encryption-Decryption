class RC4:
    def __init__(self, key):
        self.S = list(range(256))
        self.key = [ord(c) for c in key]
        j = 0
        for i in range(256):
            j = (j + self.S[i] + self.key[i % len(self.key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
        self.i = 0
        self.j = 0

    def encrypt(self, plaintext):
        keystream = self._generate_keystream(len(plaintext))
        ciphertext = [ord(plaintext[i]) ^ keystream[i] for i in range(len(plaintext))]
        return ''.join(chr(c) for c in ciphertext)

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)

    def _generate_keystream(self, length):
        keystream = []
        for _ in range(length):
            self.i = (self.i + 1) % 256
            self.j = (self.j + self.S[self.i]) % 256
            self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
            keystream.append(self.S[(self.S[self.i] + self.S[self.j]) % 256])
        return keystream
