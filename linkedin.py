import qrcode

def generate_qr(data,filename="linkedin.png"):
    qr=qrcode.make(data)
    qr.save(filename)
    print("QR code saved as", filename)
generate_qr("https://www.linkedin.com/in/nithish-r-15634239b/")

