from keras.preprocessing.image import ImageDataGenerator
import config

def train_data_generator(batch_size=16):
        train_datagen = ImageDataGenerator(
                        rescale=1./255,
                        shear_range=0.2,
                        zoom_range=0.2,
                        horizontal_flip=True)

        train_generator = train_datagen.flow_from_directory(
                        config.train_dir,  # this is the target directory
                        target_size=(150, 150),  # all images will be resized to 150x150
                        batch_size=batch_size,
                        class_mode='categorical',
                        shuffle=True)  # since we use binary_crossentropy loss, we need binary labels

        print(train_generator.class_indices)

        return train_generator


def val_data_generator(batch_size=16):
        val_datagen = ImageDataGenerator(rescale=1./255)

        val_generator = val_datagen.flow_from_directory(
                        config.val_dir,
                        target_size=(150, 150),
                        batch_size=batch_size,
                        class_mode='categorical',
                        shuffle=True)

        print(val_generator.class_indices)

        return val_generator
