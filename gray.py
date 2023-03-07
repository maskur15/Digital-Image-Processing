def to_grayscale_then_rgb(image):
    image = tf.image.rgb_to_grayscale(image)
    image = tf.image.grayscale_to_rgb(image)
    return image
tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1/255,
    preprocessing_function=to_grayscale_then_rgb
)
