#!/bin/bash

pip install ipykernel ipywidgets &&
pip install pandas pyarrow &&
conda install cudatoolkit=11.8 &&
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 && 
pip install transformers accelerate
