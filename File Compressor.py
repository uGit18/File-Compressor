import zlib, base64

file1 = open('1.txt','r')
text = file1.read()
file1.close()

code = base64.b64encode(zlib.compress(text.encode('utf-8'),9))
code = code.decode('utf-8')

f = open('compressed.txt','w')
f.write(code)
f.close()
