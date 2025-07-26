# Solidity .sol to .txt Converter & Zipper 🧰

A simple Python script to convert Solidity `.sol` files into `.txt` format while preserving the directory structure — then zips the result and optionally copies it to a folder (useful for WSL users to copy to Windows). This is ideal to be uploaded to LLMs such as ChatGPT which cannot read .sol files.

## Features

- Recursively walks through `src/` and `test/` folders from Foundry repo (It can be any folders, change the folder names in the `foldernames` list accordingly.
- Converts `.sol` files to `.txt` with mirrored structure
- Zips the output folders
- Copies the zip files to your destination folder (In the code, it copies from a WSL repo to the Windows Downloads folder)

## Prerequisites

- Python 3.6+

## Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/sol-to-txt-converter.git
   cd sol-to-txt-converter
   ```
2. Run the python code:
   ```bash
   python3 soltotxt.py
   ```
