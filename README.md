# LSB

Have you ever wanted to send a secret image over the internet without anyone being able to see it?  
Well now you can! With this project you can hide a image inside another and send securely send it without having to think if others will se it.

&nbsp;
## How to use
Download the "hide_image_in_image.py" and run it using python.  
It will print how to use it, but here is also the correct way to use it.

To use it with 1 color pixel (most secure, but can't hold a large image):
```
python hide_image_in_image.py encode1 public.jpg private.jpg
python hide_image_in_image.py decode public.png
```

To use it with 2 color pixels (less secure, but can hold larger image):
```
python hide_image_in_image.py encode2 public.jpg private.jpg
python hide_image_in_image.py decode2 public.png
```

When you encode the image, it will output the public image as secret.png but with the private image inside it.  
When you decode the image, it will output the private image as output.png but.

There are also images in the repository for testing the program. These images have been tested and works.  
Note! The images are not for any commercial use and I don't have any rights over them, they are only for testing.

&nbsp;
## Explanation (Comming soon...)
