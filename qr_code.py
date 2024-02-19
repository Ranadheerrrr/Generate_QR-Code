import qrcode as qr 
img = qr.make("https://www.linkedin.com/in/ranadheer-gajarla-b30228239/")
img.save("Linkedin_QR.png")