DNA Data Storage — PERFECT PCR
Code repository accompanying the manuscript:
PERFECT PCR: Advancing DNA Data Storage to Near-Maximal Density
Rushant Sabnis, Han Zhang, Bingzhe Li, Arum Han, Paul de Figueiredo, and Qing Sun (2026)
---
Overview
This repository contains Python scripts for encoding digital data into DNA sequences, designing oligonucleotide pools for synthesis, and performing GC content balancing for improved synthesis stability. These scripts were used to generate the DNA sequences described in the manuscript for image, music, and multilingual text storage experiments.
---
Repository Contents
File / Folder	Description
`Oligopool code`	Generates overlapping oligonucleotide pools from an input DNA sequence. Splits the sequence into fragments, adds universal primer binding sites, and outputs forward and reverse oligonucleotides as an Excel file.
`GC converter`	Converts a DNA sequence into a GC-balanced version by uniformly substituting bases to reach a target GC percentage. The transformation is fully reversible using a binary tag stored alongside the sequence.
`Image`	Encodes a digital image into a DNA sequence using delta encoding and decodes retrieved sequences back to an image for visual quality assessment.
`Music file`	Encodes music as note–duration pairs into DNA using a 2-bit per nucleotide scheme and decodes retrieved sequences back to music.
`Golden record`	Encodes multilingual text character by character into DNA using a 4-base codon scheme and decodes retrieved sequences back to text.
`Requirement.txt`	Lists all Python package dependencies.
---
Requirements
Python 3.7 or higher is required. All dependencies can be installed using:
```
pip install -r Requirement.txt
```
All scripts are designed to run in Jupyter Notebook or any Python-supported environment.
---
Usage
Oligopool design
The `Oligopool code` script takes a DNA sequence as input and generates overlapping oligonucleotides for synthesis. Key parameters used in the manuscript:
Fragment size: 720 bp per segment
Oligonucleotide length: 60 bp with 30 bp overlap
Universal forward primer: `TTTGTTTAACTTTAAGAAGGAGATATACAT`
Universal reverse primer: `TTCCTTTCGGGCTTTGTTAGCAGCCGGATC`
To use, set `input_dna_sequence` to your target DNA sequence and run the script. Output is saved as `split_primers_output.xlsx`.
GC content balancing
The `GC converter` script adjusts the GC content of a DNA sequence to a user-defined target percentage. A binary tag is generated alongside the modified sequence, allowing full recovery of the original sequence during decoding. This step is optional and is recommended for sequences with GC content outside the 40–60% range.
To use, set `input_dna` to your target DNA sequence and `target_gc` to the desired GC fraction (e.g. 0.63 for 63%) and run the script.
Image encoding and decoding
The `Image` folder contains scripts for converting a digital image to a DNA sequence and reconstructing the image from a retrieved (potentially error-containing) sequence. Delta encoding is used to represent pixel differences, reducing the total sequence length.
Music encoding and decoding
The `Music file` folder contains scripts for encoding musical note–duration pairs into DNA. Each note is assigned a unique 5-bit binary code and each duration a 3-bit code, yielding 8-bit units per note that are mapped to nucleotides using a 2-bit per base scheme (00 = A, 01 = C, 10 = G, 11 = T).
Multilingual text encoding and decoding
The `Golden record` folder contains scripts for encoding text characters into DNA using a 4-base codon scheme. Homopolymer runs of four or more identical bases are avoided to reduce sequencing errors. The encoded sequence includes greetings in 14 languages sourced from the Voyager Golden Record.
---
Notes
Applying the GC converter reduces effective storage density from 1.88 bits/nucleotide to 1.25 bits/nucleotide. It is recommended only for sequences with challenging GC composition.
The physical redundancy of 1× reported in the manuscript reflects construct-level demonstration across a 100 kb experimental library. Scaling to larger libraries may require additional optimization.
All data storage experiments in the manuscript were performed at an EndoNucS enzyme concentration of 6.25 μM.
---
Citation
Sabnis R, Zhang H, Li B, Han A, de Figueiredo P, Sun Q. PERFECT PCR: Advancing DNA Data Storage to Near-Maximal Density. 2026.
---
Contact
For questions regarding the code, please contact sunqing@tamu.edu or PaulLifeScience@missouri.edu.
