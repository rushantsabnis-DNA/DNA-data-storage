# 🧬 DNA Data Storage

> Encode, store, and decode digital data (images, audio, files) in synthetic DNA sequences using a GC-content-balanced oligopool encoding pipeline.

---

## Overview

This project implements a pipeline for **DNA-based digital data storage**. It converts binary files (images, music, documents) into DNA nucleotide sequences optimized for synthesis and sequencing reliability.

The pipeline handles:
- **GC content balancing** — ensures sequences are synthesizable
- **Oligopool design** — splits encoded data into fixed-length DNA oligos
- **Golden record encoding** — packages multiple file types for long-term archival

---

 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook (optional, for examples)

### Installation

```bash
git clone https://github.com/rushantsabnis-DNA/DNA-data-storage.git
cd DNA-data-storage
pip install -r requirements.txt
```

### Quick Start

```bash
python src/gc_converter.py --input data/sample_image.png --output outputs/encoded.txt
python src/oligopool.py --input outputs/encoded.txt --output outputs/oligos.csv
```

---

## License

This project is licensed under the Texas A&M University and University of Missouri License 

---

## Contact

**Rushant Sabnis** — [GitHub Profile](https://github.com/rushantsabnis-DNA)

Feel free to open an [issue](https://github.com/rushantsabnis-DNA/DNA-data-storage/issues) for questions or suggestions.
