# Breast Cancer Detection

A machine learning project for detecting and classifying breast cancer tumors as malignant or benign using the Wisconsin Diagnostic Breast Cancer (WDBC) dataset.

## 📋 Overview

This project implements a breast cancer detection system that analyzes cell nucleus characteristics from Fine Needle Aspirate (FNA) samples to distinguish between malignant and benign breast masses. The system uses features computed from digitized images of the FNA samples.

## 🎯 Features

The model analyzes 27 different features of cell nuclei, including:

### Mean Measurements
- Radius, texture, perimeter, area
- Smoothness, compactness, concavity
- Concave points, symmetry

### Standard Error Measurements  
- Statistical variability for radius, perimeter, area
- Smoothness, compactness, concavity variations
- Concave points and symmetry errors

### Worst Measurements
- Largest/most severe values for all mean measurements
- Fractal dimension (coastline approximation)

## 🛠️ Technology Stack

- **Python 3.x**
- **Pydantic** - Data validation and modeling
- **Machine Learning Libraries** - scikit-learn, pandas, numpy
- **Visualization** - matplotlib, seaborn

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/abdelrhmanSherpiny/breast_cancer.git
cd breast_cancer

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

### Data Validation with Pydantic

```python
from models import PatientData

# Create a patient data instance
patient = PatientData(
    radius_mean=17.99,
    texture_mean=10.38,
    perimeter_mean=122.8,
    area_mean=1001.0,
    smoothness_mean=0.1184,
    compactness_mean=0.2776,
    concavity_mean=0.3001,
    concave_points_mean=0.1471,
    symmetry_mean=0.2419,
    radius_se=1.095,
    perimeter_se=8.589,
    area_se=153.4,
    smoothness_se=0.006399,
    compactness_se=0.04904,
    concavity_se=0.05373,
    concave_points_se=0.01587,
    symmetry_se=0.03003,
    radius_worst=25.38,
    texture_worst=17.33,
    perimeter_worst=184.6,
    area_worst=2019.0,
    smoothness_worst=0.1622,
    compactness_worst=0.6656,
    concavity_worst=0.7119,
    concave_points_worst=0.2654,
    symmetry_worst=0.4601,
    fractal_dimension_worst=0.1189
)

# Get JSON output
print(patient.model_dump_json(indent=2))
```

## 📊 Dataset

The Wisconsin Diagnostic Breast Cancer (WDBC) dataset contains:
- **569 instances** of breast cancer cases
- **30 features** computed from digitized images
- **2 classes**: Malignant (M) and Benign (B)

### Dataset Source
- University of Wisconsin Hospitals, Madison
- Dr. William H. Wolberg, General Surgery Dept.

## 🔬 Model Performance

The classification model achieves:
- **Accuracy**: ~95-97%
- **Precision**: High precision for both classes
- **Recall**: Effective early detection capability

## 📁 Project Structure

```
breast_cancer/
├── data/
│   └── breast_cancer_data.csv
├── models/
│   └── patient_data.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Abdelrhman Sherpiny**
- GitHub: [@abdelrhmanSherpiny](https://github.com/abdelrhmanSherpiny)

## 🙏 Acknowledgments

- Wisconsin Diagnostic Breast Cancer (WDBC) dataset creators
- UCI Machine Learning Repository
- Dr. William H. Wolberg for the original dataset

## 📚 References

- [Wisconsin Breast Cancer Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))
- Wolberg, W.H., Street, W.N., & Mangasarian, O.L. (1995). "Breast Cancer Wisconsin (Diagnostic) Data Set"

## ⚠️ Disclaimer

This project is for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis. Always consult with qualified healthcare professionals for medical decisions.

---

**Note**: Early detection saves lives. If you or someone you know has concerns about breast cancer, please consult a healthcare professional immediately.