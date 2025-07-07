This is a minimal transformer-based language model built from scratch — a small-scale prototype of an LLM architecture.
It is a lightweight implementation of a transformer based language model, focusing on mathematics and Electrical Engineering content.
It demonstrates the core architecture behind large language models — optimized for domain-specific learning in STEM fields.
This was built by scratch on my Apple M3 Macbook Air, as a 'self-challenge' and what I beleive to be a great learning experience.

Originally based on a character-level GPT-style model, Mezzirak has been repurposed to learn from curated maths and EE resources including:

- University textbooks (PDFs converted to plain text)
- Electrical Engineering formulas, definitions, and problems
- Math Q&A (integration, ODEs, Fourier, linear algebra, etc.)
- Circuit theory, signals and systems, electromagnetics
- Engineering problem-solving techniques

📦 Dataset
Instead of Shakespeare, Mezzirak is trained on a custom dataset:
data/eemath.txt — a large corpus of domain-specific material, extracted from:

Electrical and Computer Engineering textbooks
Math lecture notes and problem banks
Community-contributed technical content
The training is entirely local and open-source, showcasing that you don’t need massive compute to build a focused LLM prototype.

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
- Trained on Shakespeare's text corpus (~1MB)
- Cleaned Git history and environment for reproducibility
- Training logs + sample generations

## 📁 Project Structure

Mezzirak-LLM/
├── data/ # Dataset (tiny Shakespeare)
├── mezzirak.py # Main training script
├── requirements.txt # Python dependencies
├── .gitignore # Files to ignore
└── README.md # This file

## 🧪 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Mezzirak/LLM.git
cd LLM
```
2. Create and activate a virtual environment:

   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:

   pip install -r requirements.txt

4. Train the model:

   python3 mezzirak.py

🌐 What's Next

 - Web interface with Flask or Streamlit to interact with Mezzirak in real time
 - Train on larger corpora (e.g., Wikipedia dumps or GitHub code)
 - Extend to token-level transformer
 - Try quantization/distillation for smaller deployment

📚 Learning References

- The Transformer paper (Attention is All You Need)
- [This git page on building a LLM by rasbt](https://github.com/rasbt/LLMs-from-scratch)
- [nanoGPT by Andrej Karpathy](https://github.com/karpathy/nanoGPT)
