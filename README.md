# questionsGame

Setup python dev environment:
1. install anaconda, python 2.7: https://www.anaconda.com/download/
2. Install opencv
    a. open Anaconda Prompt
    b. create enviroment(https://chrisconlan.com/installing-python-opencv-3-windows/):
        conda create --name myNewEnv python=2.7.14
         activate myNewEnv
         conda install numpy
         conda install anaconda-client
         conda install --channel https://conda.anaconda.org/menpo opencv3
   c. chack that open cv was installed correctly(https://chrisconlan.com/installing-python-opencv-3-windows/):
        (myNewEnv) C:\Users\adelgad6>python
        >>>import cv2
        >>>cv2.__version__
   d. make spyder run on the newly created enviroment:
        conda install -n myNewEnv spyder
        spyder //to launch spyder 
        

Converting image to text
  I am following this project: https://github.com/schollz/python-ocr
   a. install pytesseract and pillow (https://grimhacker.com/2014/11/23/installing-pytesseract-practically-painless/)
         (myNewEnv) C:\Users\adelgad6>pip install pytesseract
                                     >pip install pillow
         python
         >>> import pytesseract
         >>> from PIL import Image
   b. install tesseract-ocr-setup-4.00.00dev
          article followed:(https://stackoverflow.com/questions/46567157/pytesseract-image-to-string-returns-windows-error-access-denied-error-in-python?rq=1)
           a. download and install tesseract-ocr-setup-4.00.00dev (http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe)
          b. follow article above to setup enviroment variables and set  pytesseract.pytesseract.tesseract_cmd
          c. now this should work:
            import pytesseract
            pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
            from PIL import Image
            print pytesseract.image_to_string(Image.open('C:\\Users\\adelgad6\\Desktop\\text.jpg'));
          
