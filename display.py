# Set up Printing of the results
from PIL import Image, ImageDraw, ImageFont
from IPython.display import Image as Iamge_ipy
from IPython.display import display
from IPython.display import Markdown, display
import sys
def display_images(bs=1):
  filepath = "example_captions.txt"
  with open(filepath, "r") as f:
    sentences = f.read().split('\n')
  for k in range(bs):
    filename0 = '/content/Bird-Image-Generator/netG_epoch_600/example_captions/0_s_%s_g0.png' %k
    filename1 = '/content/Bird-Image-Generator/netG_epoch_600/example_captions/0_s_%s_g1.png' %k
    filename2 = '/content/Bird-Image-Generator/netG_epoch_600/example_captions/0_s_%s_g2.png' %k
    x = Iamge_ipy(filename=filename0) 
    y = Iamge_ipy(filename=filename1) 
    z = Iamge_ipy(filename=filename2) 
    printmd('# **'+sentences[k]+'**')
    display(x, y , z)

def printmd(string):
    display(Markdown(string))


if __name__ == "__main__":
    n = len(sys.argv)
    
    if n == 1 :
        display_images()

    if n == 2:
        bs = int(sys.argv[1])
        display_images(bs)
        
