import os
import struct
from tokenizers import ByteLevelBPETokenizer
from tqdm import tqdm

def encode_file_to_bin(tokenizer, input_file, output_file):
    # Count total lines for progress bar
    with open(input_file, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)

    with open(input_file, 'r', encoding='utf-8') as f, open(output_file, 'wb') as out_f:
        for line in tqdm(f, total=total_lines, desc="Encoding lines"):
            line = line.strip()
            if not line:
                continue
            try:
                tokens = tokenizer.encode(line).ids
                out_f.write(struct.pack(f'{len(tokens)}I', *tokens))
            except Exception as e:
                print(f"Error encoding line: {line[:50]}... → {e}")

if __name__ == "__main__":
    tokenizer = ByteLevelBPETokenizer(
        "tokenizer_model/vocab.json",
        "tokenizer_model/merges.txt"
    )
    input_file = "openmathinstruct_train_cleaned.txt"
    output_file = "data/train.bin"

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    encode_file_to_bin(tokenizer, input_file, output_file)



