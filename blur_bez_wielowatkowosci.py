import time
import sys
from PIL import Image,ImageFilter           # biblioteka edycji zdjęć
 
def blur(x):                                # funkcja nakładająca efekt blur
  return x.filter(ImageFilter.BoxBlur(10))  

img  =  Image.open("obraz.jpeg")            # wczytanie obrazu

start = time.time()                         # moment startu mierzenia czasu
complete=blur(img)                          # wywołanie funkcji            
  
end = time.time()                           # moment końca liczenia czasu
complete.show()                             # wyświetlenie zdjęcia z efektem blur
print(end - start)                          # wypisanie czasu trwania skryptu na ekran





