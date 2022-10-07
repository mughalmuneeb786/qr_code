import qrcode
import re 

# this is static string
mynamestring = 'muneeb.pro'

#get input from the user you can comment the above line .
mynamestring = input()

#this line is use to remove special character using regex lib . and store in filename.
file_name = re.sub('[^A-Za-z0-9]+', '', mynamestring)
#select the version and size of the box with borders
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)

#add the our string data and convert into qr .
qr.add_data(mynamestring)
qr.make()

#convert data into qr image with black and white.
img = qr.make_image(fill_color = 'black', back_color = 'white')
#save the file in folder with same variable name of data we get input from a user.
img.save(f'{file_name}.png')