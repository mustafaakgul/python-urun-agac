import qrcode

def qr_olustur(sele):
    string = sele
    code = qrcode.make(string)
    code.save('static/qr/qr.png')