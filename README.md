This is a minimal transformer-based language model built from scratch — a small-scale prototype of an LLM architecture.
It is a lightweight implementation of a transformer based language model, focusing on mathematics and Electrical Engineering content.
It demonstrates the core architecture behind large language models — optimized for domain-specific learning in STEM fields.
This was built by scratch on my universities desktop and cloud GPU services such as Google Colab and Microsoft Azure as a 'self-challenge' and what I beleive to be a great learning experience.

Mezzirak has been trained to learn from curated maths and EE resources including:

- Hugging face
- Github repositories
- arXiv papers

📦 Dataset
Mezzirak is trained on several  dataset:
data/eemath.txt — a large corpus of domain-specific material, extracted from:

## 🔍 Goals

- Learn, understand and implement a transformer architecture manually
- Build and train a lightweight LLM completely from scratch (no high-level libraries like Hugging Face)
- Run on consumer hardware (MacBook Air M3 with Metal backend)
- Showcase the process and learning journey for not just myself but anyone curious to follow a similar path
- Implenet the LLM on a website for others to try out - like chatGPT, Gemini, Claude etc.

## 🧱 Features

- Implemented in **Python** using **PyTorch**
- Character-level transformer model
- Custom attention block and training loop
- Cleaned Git history and environment for reproducibility
- Training logs + sample generations

## 📂 Project Structure

| File / Folder           | Description |
|-------------------------|-------------|
| `m.py`                  | Loads OpenMathInstruct-1 and saves raw `.txt` |
| `clean_dataset.py`      | Removes metadata, deduplicates lines |
| `train_tokenizer.py`    | Trains a BPE tokenizer using HuggingFace `tokenizers` |
| `encode_to_bin.py`      | Converts cleaned `.txt` into `train.bin` (tokenized) |
| `train_mezzirak.py`     | *(coming soon)* Model training script using `transformers` + PyTorch |
| `tokenizer_model/`      | Stores vocab + merge rules |
| `data/`                 | Raw/cleaned training data and binary file |
| `checkpoints/`          | Will contain model checkpoints during training |


📚 Learning References

- The Transformer paper (Attention is All You Need)
- [This git page on building a LLM by rasbt](https://github.com/rasbt/LLMs-from-scratch)
- [nanoGPT by Andrej Karpathy](https://github.com/karpathy/nanoGPT)
