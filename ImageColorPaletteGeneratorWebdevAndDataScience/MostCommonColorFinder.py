import pandas as pd
from PIL import Image

class MostCommonColorFinder:
    def __init__(self):
        self.img_data = []

        self.img = None
        self.columns = ["r", "g", "b"]
        self.most_common_colors = []
        self.img_data = []
        self.filepath = ""
        self.color_values_ready = []
        self.counter = 0

    def find_color(self):
        self.most_common_colors = []

        if not self.filepath == "":
            self.color_values_ready = []
            img = Image.open(self.filepath)
            img.convert("RGB")

            width, height = img.size

            for x in range(0, width):
                for y in range(0, height):
                    r, g, b = img.getpixel((x, y))

                    self.img_data.append((r, g, b))
                    # print(img.getpixel((x, y)))
                    # print(img_data)

            img_df = pd.DataFrame(data=self.img_data, columns=self.columns)

            self.most_common_colors = img_df.value_counts().head()

            # print(most_common_colors)

            for _ in range(0, 5):
                self.color_values_ready.append(list(self.most_common_colors.index[_]))

            print("___________")
            print(self.color_values_ready)
            return self.color_values_ready


