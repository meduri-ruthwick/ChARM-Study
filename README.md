# 🧬 ChARM – Chromatin Accessibility Retrospective Model

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue.svg">
  <img src="https://img.shields.io/badge/Model-RandomForest-success.svg">
  <img src="https://img.shields.io/badge/License-Available%20on%20Request-lightgrey.svg">
  <img src="https://img.shields.io/badge/Made%20with-PARAM%20Ananta-9cf.svg">
  <img src="https://img.shields.io/badge/Institution-IITGN-blueviolet.svg">
</p>

> A machine learning model for predicting chromatin accessibility from genomic sequence features  
> Developed by **Meduri Ruthwick** & **Dr. Umashankar Singh** | HoMeCell Lab, IIT Gandhinagar  
> Powered by **PARAM Ananta** Supercomputing Cluster 

<p align="center">
  <img src="https://github.com/Sympart/sympart/blob/main/Images/Logos/HoMeCell%20Lab%20Logo-TP.001.png" alt="HoMeCell Lab Logo" height="80"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://github.com/Sympart/sympart/blob/main/Images/Logos/Final_IITGN-Logo-symmetric-White.png" alt="IIT Gandhinagar Logo" height="80"/>
</p>

---

## 📌 Overview

ChARM (Chromatin Accessibility Retrospective Model) is a Random Forest-based machine learning model trained on ATAC-seq data from human HEK293T cells to predict open chromatin regions using **only DNA sequence features**. This approach allows us to explore **chromatin accessibility across 105 vertebrate genomes**, especially for organisms where experimental methods like ATAC-seq are not feasible.

---

## 🎯 Purpose

Understanding open chromatin across all vertebrates is challenging due to experimental constraints. ChARM enables:
- Comparative epigenomic analysis without experimental data
- Insights into chromatin evolution and accessibility landscapes
- In silico prioritization of accessible genomic regions for validation

---

## 🧠 Features Used in Final Model

After experimenting with 80+ feature sets, the final model uses:
- **GC Skew**
- **CpG occurrences**
- **TFBS motif occurrences** (only motifs with >50% GC)

> Trained on ~34,000 sequences (balanced class 0/1)

---

## ⚙️ Model Specifications

- Algorithm: **Random Forest Classifier**
- Library: `scikit-learn`
- Hyperparameter Tuning: `GridSearchCV`
- Parameters searched:
  - `n_estimators`: 100, 200, 300
  - `max_depth`: None, 10, 20, 30
  - `min_samples_split`: 2, 5, 10
  - `min_samples_leaf`: 1, 2, 4
  - `max_features`: sqrt, log2

---

## 📊 Performance

- **ROC AUC**: 0.85  
- **PR AUC**: 0.86  
- Validated across **11 independent human cell lines**
- Key Visualizations:
  - Confusion Matrix
  - Feature Importance
  - Permutation Feature Importance

---

## 🌐 Applications

- Predicted **putative ATAC-like enriched regions (pAERs)** across 105 vertebrate genomes
- In-depth analysis performed for **primate genomes**
- Enables **comparative genomics** and **functional region identification** in species without epigenomic data

---

## 📥 Input & Output

**Input**:  
- BED file of genomic regions (e.g., ATAC peaks, summit regions)

**Output**:  
- Prediction label (open/closed)
- Prediction probability

---

## 📜 License & Access

This repository describes the model and its applications. **Code and models will be available upon request.** [Academic purposes only]

---

## 👤 Authors

- **Meduri Ruthwick**, PhD Scholar, IIT Gandhinagar
- **Dr. Umashankar Singh**, Associate Professor, IIT Gandhinagar

### 🔬 HoMeCell Lab – Department of Biological Sciences and Engineering

Indian Institute of Technology Gandhinagar, Gujarat, India

---

## 📣 Contact

For code access or collaboration inquiries:\
📧 [[meduri.ruthwick@iitgn.ac.in](mailto\:meduri.ruthwick@iitgn.ac.in) | [usingh@iitgn.ac.in](mailto\:usingh@iitgn.ac.in)]\
🔗 [https://github.com/ruthwick](https://github.com/ruthwick)

---

## 📌 Notes

> This model is part of an ongoing thesis project and is yet to be published. Please cite appropriately when referencing ChARM.

---