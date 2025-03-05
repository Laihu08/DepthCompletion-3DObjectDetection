<h1 align="center">Depth Completion for 3D Object Detection</h1>

![image](https://github.com/user-attachments/assets/269ca28a-7623-4ce6-81b5-43a7b09c23c5)

*A deep learning-based approach for multi-modal 3D object detection using LiDAR and RGB images.*

## 📌 Project Overview
This project implements an advanced **3D object detection framework** leveraging **depth completion** techniques. It is based on the methodology outlined in the master's thesis:

> **"Depth Completion for 3D Object Detection from Sparse Point Cloud and Color Image"** by *Rahul Selvaraj*

The system improves object detection by **densifying sparse LiDAR point clouds** using RGB images, a **self-supervised learning approach**, and **multi-modal fusion techniques**.

---

## 🚀 Features
- **LiDAR & RGB Fusion**: Combines depth information from LiDAR with visual semantics from RGB images.
- **Depth Completion**: Uses **Simple Linear Iterative Clustering (SLIC)** and **deep learning models** to fill in missing depth values.
- **Self-Supervised Learning**: Trains without requiring fully labeled ground-truth depth maps.
- **Improved 3D Object Detection**: Uses denser depth maps to enhance detection accuracy.
- **Multi-Modal Input Handling**: Supports LiDAR, RGB, and depth maps.
- **Benchmarking Against State-of-the-Art**: Compared with leading models on the KITTI dataset.

---

## 📂 Repository Structure
```
DepthCompletion-3DObjectDetection/
│── src/                        # Core source code
│   ├── basic.py
│   ├── CoordConv.py
│   ├── criteria.py
│   ├── Cropping.py
│   ├── generate_lidar_from_depth.py
│   ├── helper.py
│   ├── inverse_warp.py
│   ├── metrics.py
│   ├── model.py
│   ├── RGB_to_SLIC.py
│   ├── vis_utils.py
│── dataloaders/                 # Data loading and processing
│   ├── calib_cam_to_cam.txt      # Camera calibration parameters
│   ├── kitti_loader.py           # KITTI dataset loader
│   ├── transforms.py             # Data transformations
│── scripts/                      # Scripts to run the project
│   ├── main.py                    # Entry point of the project
│── data/                          # Placeholder for dataset files (if needed)
│── notebooks/                     # Jupyter Notebooks for visualization & analysis
│── docs/                          # Documentation (research papers, architecture)
│── tests/                         # Unit tests (to ensure code correctness)
│── README.md                      # Project documentation
│── .gitignore                      # Ignore unnecessary files
│── LICENSE                         # License for usage
```

---

## 📖 Methodology
This project follows the **depth completion pipeline**:
1. **Preprocessing**
   - Convert sparse LiDAR points into depth maps.
   - Apply **SLIC segmentation** on RGB images.
   - Align LiDAR depth with segmented RGB regions.
2. **Depth Completion**
   - Use **self-supervised learning** to train a model for predicting dense depth maps.
   - Incorporate **warping techniques** to refine depth accuracy.
3. **3D Object Detection**
   - Convert dense depth maps back to **point clouds**.
   - Feed the enhanced point clouds into state-of-the-art **3D object detection networks**.
   - Benchmark detection performance against KITTI.

---

## 💻 Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone git@github.com:Laihu08/DepthCompletion-3DObjectDetection.git
cd DepthCompletion-3DObjectDetection
```

### **2️⃣ Create & Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Project**
To process depth completion and run object detection:
```bash
python scripts/main.py
```

---

## 🔬 Example Results
### **Depth Completion Results**
- **(a) RGB Image** → The raw input image from the camera.
- **(b) Sparse Depth Map** → LiDAR depth values, usually incomplete.
- **(c) Predicted Dense Depth Map** → Model-generated dense depth from (b).
- **(d) Ground Truth Dense Depth Map** → The actual full depth map (for evaluation).

[<img width="858" alt="Image" src="https://github.com/user-attachments/assets/e95b6545-c27b-448c-8b40-3abd56243e05" />
](https://private-user-images.githubusercontent.com/55731288/419268331-a1c8c61c-819b-4647-9047-a44c8ccefbf4.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDExNDI1NzYsIm5iZiI6MTc0MTE0MjI3NiwicGF0aCI6Ii81NTczMTI4OC80MTkyNjgzMzEtYTFjOGM2MWMtODE5Yi00NjQ3LTkwNDctYTQ0YzhjY2VmYmY0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA1VDAyMzc1NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTA3NTUyYjYyYTMwY2IxNWEyNDk4NmQxMWNjMTczMDExY2FmNjU1MjFkMmNjNzgwNzNiYzAzOTJhNmZhNDRlZGQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.uKqC-eIxsjkiomlA63E1prymlmmfAxoU3FOXCL7y2h4)

### **3D Object Detection Results**
- **Top row** → RGB images with predicted **3D bounding boxes**.
- **Bottom row** → Corresponding LiDAR **point cloud** with bounding boxes.

[<img width="1214" alt="Image" src="https://github.com/user-attachments/assets/f9fd8e1f-e380-430b-8997-791afa7c2dd8" />](https://private-user-images.githubusercontent.com/55731288/419268351-bd86acd6-323c-4b4d-b7f3-7342dcc18ffd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDExNDI1NzYsIm5iZiI6MTc0MTE0MjI3NiwicGF0aCI6Ii81NTczMTI4OC80MTkyNjgzNTEtYmQ4NmFjZDYtMzIzYy00YjRkLWI3ZjMtNzM0MmRjYzE4ZmZkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA1VDAyMzc1NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM3OTljYmNlNTRhZTdmMTZiMWQ1ZGEzOWZiNTJhNzkyMjQyZTZkZmUxZTQ2Y2E1OTg3MzA4OWE5NzI4N2JmMGUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.1lTYsAqnUsn8-7Y6mZGVNtLiW6qIsTkH07uOB9lzxMQ)

---

## 📊 Performance Benchmarks
| Method | RMSE (mm) ↓ | MAE (mm) ↓ | IRMSE (1/km) ↓ | IMAE (1/km) ↓ |
|--------|------------|-----------|--------------|--------------|
| SparseConvs | 1601.33 | 481.27 | 4.94 | 1.78 |
| Self-supervised | 954.36 | 288.64 | 3.21 | 1.35 |
| CSPN | 1019.64 | 279.46 | 2.93 | 1.15 |
| STD | 814.73 | 249.95 | 2.80 | 1.21 |
| Spade-RGBsD | 917.64 | 279.46 | 2.93 | 1.15 |
| DFuseNet | 1353.65 | 446.64 | 3.78 | 1.80 |
| NLSPN | 761.68 | 299.59 | 2.79 | 1.04 |
| PENet | 730.08 | 210.55 | 2.17 | 0.94 |
| **Ours** | **728.79** | **204.32** | **2.13** | **0.96** |

---

## 📜 Citation
If you use this work in your research, please cite:
```bibtex
@article{selvaraj2021depthcompletion,
  title={Depth Completion for 3D Object Detection from Sparse Point Cloud and Color Image},
  author={Rahul Selvaraj},
  year={2021},
  institution={National Chung Cheng University}
}
```

---

## 📄 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

### 🎯 **Author**
**Rahul Selvaraj**  
🚀 *Senior Software Engineer, R&D at Karma Medical Products*  
🔗 [GitHub](https://github.com/Laihu08) | [LinkedIn](https://www.linkedin.com/in/rahul-selvaraj)  

---

🔥 **If you like this project, give it a star!** ⭐
