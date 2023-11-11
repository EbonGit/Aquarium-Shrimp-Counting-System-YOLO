# Aquarium Shrimp Counting System

## Overview

This project utilizes computer vision and artificial intelligence to automate the counting of shrimp in an aquarium using a Jetson Nano. The system captures images from a camera placed infront of the aquarium, processes them using deep learning models, and provides the count for automation purposes.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Code Structure](#code-structure)
- [Configuration](#configuration)
- [Integration with Aquarium Automation](#integration-with-aquarium-automation)
- [Demo](#demo)
- [Train](#train)
- [License](#license)

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/aquarium-shrimp-counting.git

# Navigate to the project directory
cd aquarium-shrimp-counting

# Install dependencies
pip install -r requirements.txt

# Install Pycuda
export PATH=/usr/local/cuda-10.2/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH
python3 -m pip install pycuda --user

# Install Seaborn
sudo apt install python3-seaborn
```

## Usage

```bash
# Run the shrimp counting system
python app.py
```

## Hardware Requirements

- NVIDIA Jetson Nano 4GB
- Logitech C270

## Software Requirements

- Ubuntu 20.04.6 [Link](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image)
- Tensorrt [Link](https://github.com/wang-xinyu/tensorrtx)
- Python 3.8
- OpenCV
- YOLOv5

## Code Structure

Explain the organization of your codebase. Highlight key directories and files.

```
/BreadcrumbsAquarium-Shrimp-Counting-System-YOLO
    ├── model.pt
    ├── yolov5
    │   ├── images
    │   ├── build
    │   │   ├── model.engine
    │   │   └── ...
    ├── app.py
    ├── README.md
    ├── requirements.txt
    └── ...
```

## Configuration

```yaml
serial:
  port: /dev/ttyUSB0

engine:
  path: yolov5/build/model.engine

WIDTH:
  resolution: 600x600

model:
  type: YOLOv5
```

## Integration with Aquarium Automation

Explain how the shrimp counting results are integrated into the aquarium automation system.

...

## Demo

[Watch Demo](link-to-demo-video)

## Train

To train your own model, you can follow the example from the YOLOv5 or YOLOv8 notebook and then use TensorRT to convert the .pt model to .engine, making it ready for use. [Link](https://github.com/wang-xinyu/tensorrtx)

...


## License

This project is licensed under the [MIT License](LICENSE).

---
