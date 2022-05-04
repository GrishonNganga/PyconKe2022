import os, random
from PIL import Image

layers = ['bg', 'outer', 'inner', 'python']
layers_files = {}
selected_image = {}
base_dir = "layers"
files = os.listdir(f'./{base_dir}')
rarity_index = 0

for layer in layers:
    files_for_layer = []
    for file in files:
        if layer in file:
            files_for_layer.append(file)
            layers_files[layer] = files_for_layer

print(layers_files)


for k, v in layers_files.items():
    items_len = len(v)
    rare_weight = (100/ items_len) * (1/10)
    all_else_weight = (100 - rare_weight) / (items_len - 1)
    layer_weights = [rare_weight if str(rarity_index) in i else all_else_weight for i in v]
    selected_image[k] = random.choices(v, weights = layer_weights)

# print(selected_image)