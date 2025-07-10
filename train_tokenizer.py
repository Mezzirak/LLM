from tokenizers import ByteLevelBPETokenizer

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Train the tokenizer on your text file(s)
tokenizer.train(
    files=["openmathinstruct_train.txt"],  # list of your training files
    vocab_size=30_000,                    # you can tweak vocab size (30k is a good start)
    min_frequency=2,                      # ignore rare tokens appearing less than this
    special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>",
    ],
)

# Save tokenizer files to disk
tokenizer.save_model("tokenizer_model")

print("Tokenizer training complete!")
