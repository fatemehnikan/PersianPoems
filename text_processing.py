import os

from tqdm import tqdm

def process_poems(input_folder, output_file):
    start_poem_token = '<start_poem>'
    end_poem_token = '<end_poem>'
    start_beyt_token = '<start_beyt>'
    start_mesra_token = '<srart_mesra>'

    merged_poems = []

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            with open(os.path.join(input_folder, filename), 'r',encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines) <= 1:
                    continue
                poem_body = lines[1:]
                poem_body = [line.strip() for line in poem_body if line.strip()]
                poem = [start_poem_token]
                for i in range(0, len(poem_body), 2):
                    if i + 1 < len(poem_body):
                        beyt = (f"{start_beyt_token}{start_mesra_token}{poem_body[i]}"
                                f"{start_mesra_token}{poem_body[i+1]}")
                    else:
                        beyt = (f"{start_beyt_token}{start_mesra_token}{poem_body[i]}")

                    poem.append(beyt)
                poem.append(end_poem_token)
                merged_poems.append("\n".join(poem))
    with open(output_file, "w", encoding='utf-8') as f:
        f.write("\n\n".join(merged_poems))

input_folder = '/home/nrdc/Downloads/ganjoor-tex-master/txt/abusaeed/robaeeat/'
output_file = '/home/nrdc/Downloads/ganjoor-tex-master/poems.txt'
process_poems(input_folder, output_file)
