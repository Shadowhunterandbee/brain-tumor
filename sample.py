import h5py

# Path to the HDF5 file
model_path = '/home/shambhavi/Downloads/archive(1)/tumor_model.h5'

# Open the HDF5 file
with h5py.File(model_path, 'r') as file:
    # Print the keys in the file
    print("Keys in the HDF5 file:")
    print(list(file.keys()))

    # Check the structure of the model group
    if 'model_weights' in file:
        print("\nStructure of the 'model_weights' group:")
        print(list(file['model_weights']))

    # Check the attributes of the file
    print("\nAttributes of the HDF5 file:")
    print(dict(file.attrs))
