


def load_image(img_path,model_path,show=False):
    from keras.models import load_model
    from keras.preprocessing import image
    import matplotlib.pyplot as plt
    import numpy as np
    import keras
    import os

    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    # load model
    model = keras.models.load_model(model_path)
    # image path
    #img_path = '/media/data/dogscats/test1/19.jpg'      # cat

    # load a single image
    new_image = img_tensor

    # check prediction
    var=model.predict(new_image)
    var=(np.argmax(var, axis=1)[0])

    if(var==2):
      return 'Pneumothorax'
    if(var==1):
      return 'Consolidation'
    if(var==0):
      return 'Cardiomegaly'