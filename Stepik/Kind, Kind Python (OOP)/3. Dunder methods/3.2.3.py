class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions
    
    def __call__(self, value: str):
        *main, extension = value.lower().split('.')  # lower перестраховочный на будущее
        return extension in self.extensions


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
