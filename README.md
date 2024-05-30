# EPC-codon-optimizer
Codon optimizer for Escherichia, Pseudomonas and Caulobacter

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Overview

The EPC codon optimizer is a Python tool that reads protein sequences from a given FASTA or text file, optimizes the corresponding nucleotide sequences for expression in Escherichia coli MG1655, Pseudomonas aeruginosa PA01 and Caulobacter vibrioides NA1000, 
and writes the optimized sequences to an output file. This tool can be useful as a first step in codon optimization for gene synthesis. 
Read the accompanying pdf file 'Rationale for EPC codon optimization' for more details about the project.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/annefrancezcharlot/EPC-codon-optimizer.git
    cd EPC-codon-optimizer
    ```

    or 

    Go to https://github.com/annefrancezcharlot/EPC-codon-optimizer 
    and download the zip file and unzip it

2. **Create a virtual environment:**

    In the folder containing the files:

    ```sh
    python -m venv environment_name
    ```

3. **Activate the virtual environment:**

    - On Windows:

      ```sh
      environment_name\Scripts\activate
      ```

    - On macOS/Linux:

      ```sh
      source environment_name/bin/activate
      ```

4. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare your input FASTA file:** Ensure your input FASTA or text file contains protein sequences with appropriate headers.

2. **Run the script:**

    ```sh
    python epc_opt.py input_sequences.fasta output_sequences.txt
    ```

    - `input_sequences.fasta`: Path to your input FASTA or text file containing protein sequences.
    - `eoutput_sequences.txt`: Path to the output file where optimized nucleotide sequences will be written.

## Example

Here is an example of how to use the script:

```sh
python epc_opt.py example_input.fasta example_output.txt
```

## Contributing

We welcome contributions to the EPC codon optimizer!

## License

This project is licensed under the MIT License. 
