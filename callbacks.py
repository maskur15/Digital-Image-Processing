# use early stopping to break the learning process if the model stop learning during 3 epochs

es = tf.keras.callbacks.EarlyStopping(patience=3)
history = model.fit(
  train_x,train_y,
  validation_data=(valid_x, valid_y), callbacks=[es], batch_size=32,
   epochs=30
)
