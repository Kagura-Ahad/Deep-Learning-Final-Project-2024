# Checking GPU Drivers on Ubuntu

## 1. Check GPU Model and Driver
To display information about your GPU model:
```bash
lspci -nn | grep -E 'VGA|Display'
```
This command shows the GPU model and related details.
## 2. Check Installed Driver
To check the installed driver version:
```bash
sudo lshw -c video
```
This command provides a detailed description of the video card and the driver in use.
## 3. Check NVIDIA GPU Status
For NVIDIA GPUs, to verify driver version and monitor the GPU:
```bash
nvidia-smi
```
This command displays information about the NVIDIA GPU, including driver version and utilization statistics.
## 3. Check if Anaconda is installed
To check if Anaconda is installed:
```bash
conda --version
```
This command checks if Anaconda is installed and displays the version number.
## 4. Install Anaconda
To install Anaconda, download the installer script from the official website:
```bash
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
```
Then run the installer script:
```bash
sha256sum Anaconda3-2022.05-Linux-x86_64.sh
```
```
bash Anaconda3-2022.05-Linux-x86_64.sh
```
## 5. Create a New Conda Environment
To create a new conda environment:
```bash
conda create --name UGEC python=3.11
```
This command creates a new conda environment named UGEC.
## 6. Activate the Conda Environment
To activate the conda environment:
```bash
conda activate UGEC 
```
This command activates the UGEC conda environment.
## 7. Install NVIDIA Toolkit
To install the NVIDIA toolkit:
```bash
conda install -c nvidia cuda-nvcc
```
This command installs the NVIDIA CUDA toolkit in the conda environment.
## 8. Install CUDA Installation
To install CUDA:
```bash
conda install -c "nvidia/label/cuda-11.3.0" cuda-nvcc
```
This command installs the CUDA toolkit version 11.3.0 in the conda environment.
## 9. Verify CUDA Installation
To verify the CUDA installation:
```bash
nvcc --version
```
This command displays the installed CUDA version.
## 10. Install Anaconda Toolkit
To install the Anaconda toolkit:
```bash
conda install -c anaconda cudatoolkit
```
## 10. Install Pytorch and other
To install Pytorch and other libraries:
```bash
conda install pytorch torchvision torchaudio pytorch-cuda -c pytorch -c nvidia
```
This command installs Pytorch and related libraries in the conda environment.
## 11. Test the installations
To test the installations:
```bash
python -c "import torch; print(torch.cuda.is_available())"
```
This command checks if Pytorch is installed correctly and if the GPU is available for computations.

## 12. Print GPU name
To print the GPU name:
```bash
python -c "import torch; print(torch.cuda.get_device_name(0))"
```
This command prints the name of the GPU available for computations.
