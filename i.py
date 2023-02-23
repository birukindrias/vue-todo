from PIL import Image


def compare_images(image1_path, image2_path):
        image1 = Image.open(image1_path)
        image2 = Image.open(image2_path)
        if image1.mode != image2.mode or image1.size != image2.size:
            return False
           # Compare pixel values
        pixels1 = list(image1.getdata())   
        pixels2 = list(image2.getdata())   
        if pixels1 != pixels2:    
                return False     
        return True 
       # Example usage 
if compare_images('ii.png','io.png'):   
  print("The images are the same")
else:     
  print("The images are not the same")


# compare_images('ii.png','io.png')