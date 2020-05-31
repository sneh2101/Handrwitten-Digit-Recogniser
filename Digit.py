from tensorflow import keras
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np
model = keras.models.load_model('mnist.h5')
def predict_digit(img):
        #resize image to 28x28 pixel
        img = img.resize((28,28))
     
        img = img.convert('L')
        img = np.array(img)
        #reshaping to support our model input and normalizing
        img = img.reshape(1,28,28,1)
        img = img/255.0
        #predicting the class
        res = model.predict([img])[0]
        return np.argmax(res), max(res)
    
class Digit(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)
            self.x = self.y = 0
            # Creating elements
            self.canvas = tk.Canvas(self, width=300, height=300, bg = "black", cursor="spider")
            self.label = tk.Label(self, text="Thinking..", font=("Helvetica", 48))
            self.recognise = tk.Button(self, text = "Recognise", command =         self.classify) 
            self.clearbtn = tk.Button(self, text = "Clear", command = self.clear_all)
            # Grid structure
            self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
            self.label.grid(row=0, column=1,pady=2, padx=2)
            self.clearbtn.grid(row=1, column=1, pady=2, padx=2)
            self.recognise.grid(row=1, column=0, pady=2)
           
            self.canvas.bind("<B1-Motion>", self.draw)
        def clear_all(self):
            self.canvas.delete("all")
            self.label.configure(text ="Please Draw a single digit")
       
        def classify(self):
            handle = self.canvas.winfo_id() # get the handle of the canvas
            rect = win32gui.GetWindowRect(handle) # get the coordinate of the canvas
            img = ImageGrab.grab(rect)
            digit, acc = predict_digit(img)
            self.label.configure(text='Digit:' + str(digit)+', Match% :'+ str(int(acc*100))+'%')
        def draw(self, event):
            self.x = event.x
            self.y = event.y
            r=10
            self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='white')
app = Digit()
mainloop()