from tokenizers import ByteLevelBPETokenizer

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

#training tokenizer on datafile
tokenizer.train(
    files=["openmathinstruct_train.txt"],  
    vocab_size=30_000,                   
    min_frequency=2,                     
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
