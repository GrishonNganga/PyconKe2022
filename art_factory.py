import os, random, json
from PIL import Image

layers = ['bg', 'outer', 'inner', 'python']
layers_files = {}
selected_image = {}
output_file = "generated_nfts.json"
base_dir = "layers"
output_dir = "output/"
files = os.listdir(f'./{base_dir}')
rarity_index = 0

def get_generated_nfts():
    with open(output_file, 'r') as f:
        all_nfts = json.loads(f.read())
        print(all_nfts)
        return all_nfts

def generate_layers():
    for layer in layers:
        files_for_layer = []
        for file in files:
            if layer in file:
                files_for_layer.append(file)
                layers_files[layer] = files_for_layer

    for k, v in layers_files.items():
        items_len = len(v)
        rare_weight = (100/ items_len) * (1/10)
        all_else_weight = (100 - rare_weight) / (items_len - 1)
        layer_weights = [rare_weight if str(rarity_index) in i else all_else_weight for i in v]
        selected_image[k] = random.choices(v, weights = layer_weights)
    
    return selected_image

def merge_layers(layers):
    bg = Image.open(f"{base_dir}/{layers['bg'][0]}")
    outer = Image.open(f"{base_dir}/{layers['outer'][0]}")
    inner = Image.open(f"{base_dir}/{layers['inner'][0]}")
    python = Image.open(f"{base_dir}/{layers['python'][0]}")

    nft_generated = Image.new('RGB', (600,600), (250,250,250))
    nft_generated.paste(bg, (0,0), bg)
    nft_generated.paste(outer, (int(600*0.1), int(600*0.1)), outer)
    nft_generated.paste(inner, (int(600*0.3), int(600*0.265)), inner)
    nft_generated.paste(python, (int(600*0.37), int(600*0.37)), python)
    nft_generated.show()
    return layers['bg'][0].split('.')[0] + layers['outer'][0].split('.')[0] + layers['inner'][0].split('.')[0] + layers['python'][0], nft_generated

def save_image(image_name, image, layers):
    generated_nfts = get_generated_nfts()
    if image_name not in generated_nfts:
        image.save(output_dir + image_name)
        generated_nfts[image_name] = layers
        with open(output_file, "w") as f:
            f.write(json.dumps(generated_nfts))
            f.close()
        return image_name
    else: 
        return None

def generate_unique_nft():
    layers = generate_layers()
    image_name, image = merge_layers(layers)    
    image = save_image(image_name, image, layers)
    if image:
        return image
    else:
        return None
