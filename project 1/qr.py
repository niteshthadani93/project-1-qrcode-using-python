import qrcode

mygithub = qrcode.make("https://github.com/niteshthadani93")
mygithub.save("mygithub.png", scale=8)

print("QR Generated Successfully ✅")
print("my first project")