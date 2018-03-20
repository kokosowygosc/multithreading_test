import time
import sys
from PIL import Image,ImageFilter           # biblioteka edycji zdjęć
from multiprocessing import Process         # biblioteka wielowątkowości

class blur(Process):                        # klasa odpowiedzialna za późniejszą 
  def __init__(self,x):                     # wielowatkowosc z efektem blur
    Process.__init__(self)
    self.x=x.filter(ImageFilter.BoxBlur(10))  

img  =  Image.open("obraz.jpeg")            # wczytanie obrazu
img1 =  img.crop((0, 0, 640, 1080))         # dzielenie obrazu na 3 pionowe cześci
img2 =  img.crop((640, 0, 1280, 1080))
img3 =  img.crop((1280, 0, 1920, 1080))

start = time.time()                         # moment startu mierzenia czasu
if __name__ == '__main__':
  thread1=blur(img1)                        # założenie 3 wątków na procesorze
  thread2=blur(img2)
  thread3=blur(img3)
  images=[thread1.x,thread2.x,thread3.x]    # zebranie WYKONANYCH (blur) danych z wątków

complete = Image.new('RGB', (1920, 1080))   # złożenie obrazu w całość
x_offset = 0
for image in images:
  complete.paste(image, (x_offset,0))
  x_offset += image.size[0]
end = time.time()                           # moment końca liczenia czasu
complete.show()                             # wyświetlenie zdjęcia z efektem blur
print(end - start)                          # wypisanie czasu trwania skryptu na ekran





