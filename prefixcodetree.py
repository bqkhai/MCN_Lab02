class PrefixCodeTree:
    def __init__(self, codebook={}):
        self.codebook = codebook

    def insert(self, codeword, symbol):
        self.codebook[symbol] = ''.join(str(el) for el in codeword)

    def decode(self, encodedData, datalen):
        bytes_as_bits = ''.join(format(byte, '08b') for byte in encodedData)
        bitdata = bytes_as_bits[:datalen]
        print(bitdata)
        res = ''
        while bitdata != '':
            for pre in self.codebook:
                if bitdata.startswith(self.codebook[pre]):
                    res += pre
                    bitdata = bitdata[len(self.codebook[pre]):]
        return res


#test
codebook = {
    'x1':[0],
    'x2':[1,0,0],
    'x3':[1,0,1],
    'x4':[1,1]
}
tree = PrefixCodeTree()
for symbol in codebook:
    tree.insert(codebook[symbol],symbol)

print(tree.decode(b'\xd2\x9f\x20', 21))