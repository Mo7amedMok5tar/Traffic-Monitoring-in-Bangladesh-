# Traffic Monitoring in Bangladesh – Object Detection using YOLOv8

This project utilizes YOLOv8 for real-time object detection in traffic footage from Bangladesh. It includes full data preprocessing, model training and fine-tuning, evaluation, and inference on both images and videos. The goal is to detect different types of vehicles and traffic participants to aid in traffic monitoring and analysis.

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Project Structure](#project-structure)  
3. [Data Preparation](#data-preparation)
   * [Dataset Overview](#dataset-overview)
   * [Data Preprocessing](#data-preprocessing)  
4. [Model Training & Fine-Tuning](#model-training--fine-tuning)  
5. [Model Evaluation](#model-evaluation)  
6. [Model Inference](#model-inference)  
7. [How to Run](#how-to-run)  
8. [Results Summary](#results-summary)

---

## Project Overview

This project focuses on **object detection for traffic scenes in Bangladesh** using YOLOv8. The model is trained to recognize 21 different classes of vehicles and traffic participants. The pipeline involves transforming raw data into the YOLO format, training a custom YOLOv8 model, fine-tuning with augmentations, and evaluating on both image and video formats.

---

## Project Structure

The full project is available on [Google Drive](https://drive.google.com/drive/folders/1WXSeespLo6J9ZRcWwHOUYEhPj8ProJQu?usp=sharing). On GitHub, only the `notebooks/` and `src/` folders are uploaded.
```
├── notebooks/
│   ├── 1_data_preparation.ipynb        # Data cleaning, conversion, and organization
│   ├── 2_training_finetuning.ipynb     # Model training and fine-tuning
│   └── 3_testing.ipynb                 # Inference on images and video
│
├── model/                              # YOLOv8 pretrained model files
│
├── src/
│   └── utils/                          # Helper functions for data prep and training
│
├── dataset/                            # Raw dataset before processing
│
├── data_yolo/                          # YOLO-structured dataset (images + labels)
│   ├── images/train, val/
│   └── labels/train, val/
│
├── traffic_monitoring/
│   ├── yolov8_run/                     # First training run results
│   └── yolov8m_run_finetune/          # Fine-tuned model run results
│
├── predict/                            # Inference results
│   ├── results/                        # Image predictions
│   └── video_result/                   # Video predictions
│
├── test_data/                          # Test images
└── test_video/                         # Test video clips
```

---

## Data Preparation

### Dataset Overview

The dataset is sourced from the [DhakaAI Traffic Detection Dataset](https://www.kaggle.com/datasets/rifat963/dhakaai-dhaka-based-traffic-detection-dataset). It contains images of traffic in Bangladesh with XML annotations for 21 classes

### Data Preprocessing

The original dataset was in an unstructured format, with labels in `.xml` (Pascal VOC) and mixed image formats.
Steps taken:
- Converted all images to `.jpeg`
- Transformed `.xml` labels into YOLO text format
- Reorganized into YOLO-compliant structure with `images/train`, `images/val`, `labels/train`, and `labels/val` (80/20 split)
- All conversion and preprocessing were done using custom helper functions implemented in `src/utils/`

---

## Model Training & Fine-Tuning

We trained a YOLOv8 model on the processed dataset.

- **First Run**: 100 epochs on the base dataset  
- **Fine-Tuning**: +50 epochs with added augmentations for robustness  
- Metrics and visualizations were plotted, including:
  - Training & validation loss
  - Precision, Recall, and PR curves
  - Confusion Matrix

---

## Model Evaluation

The model performance was evaluated using:

- **YOLO’s built-in metrics** (Precision, Recall, mAP)
- Comparison between base and fine-tuned runs
- Visualization of performance through graphs and confusion matrix

---

## Model Inference

The trained model was used for inference on both **images** and **video**.

- Image results saved in `predict/results/`
- Video results saved in `predict/video_result/`
- Visual comparison before/after detection shown in the final notebook

### Classes Detected

The model was trained to detect the following classes:

```
["ambulance", "army vehicle", "auto rickshaw", "bicycle", "bus", "car", 
 "garbagevan", "human hauler", "minibus", "minivan", "motorbike", 
 "pickup", "policecar", "rickshaw", "scooter", "suv", "taxi", 
 "three wheelers (CNG)", "truck", "van", "wheelbarrow"]
```

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Mo7amedMok5tar/Traffic-Monitoring-in-Bangladesh.git
   cd traffic-monitoring-yolov8
   ```

2. Run the notebooks in order:
   - `notebooks/0_data_preparation.ipynb`
   - `notebooks/1_training_finetuning.ipynb`
   - `notebooks/2_testing.ipynb`

> **Note**: Ensure you have the YOLOv8 model weights downloaded and available in the `model/` folder.

---

## Results Summary

| Component         | Result / Note                 |
|------------------|-------------------------------|
| Base Training     | 100 epochs, YOLOv8 pretrained |
| Fine-Tuning       | +50 epochs, with augmentations|
| Detection Targets | 21 traffic-related classes    |
| Image Inference   | ✅                            |
| Video Inference   | ✅                            |

---

**Author**: Mohamed Mokhtar  
**Email**: mohamedmokhtar26027@gmail.com  
**LinkedIn**: [linkedin.com/in/mohamed-mokhtar-779b4a254](https://www.linkedin.com/in/mohamed-mokhtar-779b4a254)
