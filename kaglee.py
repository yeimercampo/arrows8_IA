import kagglehub

# Download latest version
path = kagglehub.dataset_download("msmart2/arrows8")

print("Path to dataset files:", path)