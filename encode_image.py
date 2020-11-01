import base64

################### Incode Image ###################

image_file = open("img1.jpg", "rb") # Here will be read image & convert to Binary && "rb": reBinary

byte_Form = base64.b64encode(image_file.read())

img_after_encode = open("img1_after.bin","wb")
img_after_encode.write(byte_Form)
img_after_encode.close()

################### Decode Image ###################

# image_file = open("img_after.bin", "rb")
# Read_byte = image_file.read()
# image_file.close()
#
# img_after_decode = open("img_after_decode.png","wb")
# img_after_decode.write(base64.b64decode(Read_byte))
# img_after_decode.close()