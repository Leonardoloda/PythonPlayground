class Repository:
    def __init__(self, path):
        self.path = path

    def get_file_content(self):
        with open(self.path, 'r') as f:
            return f.read()

    def get_file_content_by_lines(self):
        with open(self.path, 'r') as f:
            return f.readlines()

    def write_file(self, content, filename=""):
        with open(self.path + filename, 'w') as f:
            f.write(content)
