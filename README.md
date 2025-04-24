# ChARM: Cross-Species Prediction of Open Chromatin Regions Using Sequence Features

## 📘 Overview

This repository hosts the scripts, models, and data associated with my M.Tech thesis, which investigates the evolution and sequence determinants of open chromatin regions across vertebrates using human ATAC-seq data. The central goal is to explore whether chromatin accessibility can be inferred from primary DNA sequence alone and how these patterns evolve across species.

---

## 📚 Table of Contents

- [Background](#background)
- [Objective](#objective)
- [Methodology](#methodology)
  - [1. Data Collection](#1-data-collection)
  - [2. Feature Extraction](#2-feature-extraction)
  - [3. Model Development: ChARM](#3-model-development-charm)
  - [4. Cross-Species Prediction](#4-cross-species-prediction)
  - [5. Phylogenetic Analysis](#5-phylogenetic-analysis)
  - [6. Primate-Specific Alu Analysis](#6-primate-specific-alu-analysis)
- [Software and Environment](#software-and-environment)
- [Structure of the Repository](#structure-of-the-repository)

---

## 🧬 Background

ATAC-seq (Assay for Transposase-Accessible Chromatin using sequencing) provides high-resolution data on open chromatin regions. While extensively used in human and model organisms, understanding the **evolutionary conservation** of chromatin accessibility patterns remains an open question.

---

## 🎯 Objective

- Identify sequence-level determinants of chromatin accessibility using ATAC-seq data from humans.
- Develop a predictive model capable of identifying open chromatin from DNA sequence alone.
- Extend these predictions across **105 vertebrate genomes** to explore the evolutionary conservation of chromatin openness.
- Evaluate functional enrichment and evolutionary signals, especially focusing on primate-specific transposons (e.g., **Alu subfamilies**).

---

## 🔍 Methodology

### 1. Data Collection

- **ATAC-seq data** for human samples was obtained and high-confidence open chromatin peaks were selected.
- Corresponding **background regions** (non-accessible chromatin) were also collected for model training.

### 2. Feature Extraction

- Sequence windows around each region were analyzed.
- Extracted features include:
  - k-mer frequencies
  - GC content
  - Sequence entropy
  - Repeat content (if available)
- These were compiled into class 0 (closed chromatin) and class 1 (open chromatin) datasets.

### 3. Model Development: ChARM

- A **Random Forest Classifier** was developed to distinguish between accessible and inaccessible chromatin regions.
- The model was trained using:
  - Stratified cross-validation
  - Feature importance analysis
- Performance was evaluated using confusion matrices, accuracy, precision, and recall scores.

### 4. Cross-Species Prediction

- The trained model (**ChARM**) was applied to **105 vertebrate genomes**.
- Predicted open chromatin regions (`pAERs`: **predicted ATAC-Enriched Regions**) were filtered based on model confidence.

### 5. Phylogenetic Analysis

- All true predictions across species were aligned with a phylogenetic framework to trace:
  - Conserved open regions
  - Divergence in chromatin patterns
  - Gain/loss of accessibility traits through evolution

### 6. Primate-Specific Alu Analysis

- Investigated the presence of **Alu subfamilies** within predicted open chromatin regions in **primates**.
- Assessed the relationship between Alu insertion patterns and predicted chromatin accessibility.
- Early findings suggest a **subfamily-specific contribution** to functional accessibility in primates.

---

## 🛠 Software and Environment

- **Python 3.8**
- `scikit-learn` for model development
- `numpy`, `pandas`, `matplotlib`, `seaborn` for data processing and visualization
- Genomic tools: `BEDTools`, `RepeatMasker` (offline), UCSC utilities
- Custom scripts written in Python and shell

---

# 📂 Scripts and Resources Overview

This section outlines the command-line scripts, Python notebooks, and supporting files used across various stages of the thesis. Each folder corresponds to a chapter in the thesis and is organized by programming environment.

---

## CHAPTER 2 – Data Acquisition, Processing, and Alignment

**Bash Scripts:**
- `data_download.sh`: Script to automate data acquisition.
- `fastqc_command.sh`: Quality check using FASTQC.
- `fastp_command.sh`: Read filtering and trimming using FASTP.
- `bowtie2_command.sh`: Alignment command using Bowtie2.
- `macs3_command.sh`: Peak calling with MACS3.

---

## CHAPTER 3 – Machine Learning Model Development

**Python Scripts:**
- `charm_preprocessing.py`: Sequence preprocessing pipeline (ChARM package).
- `charm_model.py`: ChARM classifier implementation.
- `train_model.py`: Script to train Random Forest model.
- `motif_ids_used.txt`: List of motif IDs used as features.

---

## CHAPTER 4 – ChARM Analysis of hg38

**Python Notebooks:**
- `hicom_regions_processing.ipynb`: Fetch and prepare HiCon regions.
- `stats_analysis.ipynb`: Jupyter notebook for statistical analysis.

---

## CHAPTER 5 – Functional Annotation of pAERs and pAFRs

**Bash Scripts:**
- `repeatmasker_command.sh`: RepeatMasker usage for annotation.

**Python Notebooks:**
- `mutscan_schematic.ipynb`: Visual or analytical workflow for mutation scanning.

---

## CHAPTER 6 – Alu-SINEs and Chromatin Accessibility in Primates

**Bash Scripts:**
- `fimo_command.sh`: Command used with FIMO for motif scanning.

**Python Scripts:**
- `fetch_fimo_sequences.py`: Script to extract sequences for FIMO input.
- `pca_analysis.py`: PCA on motif enrichment, with two types of normalization.

---

## CHAPTER 7 – ChARM-Based Evolutionary Epigenomics

**Files:**
- `species_repeatmasker_list.txt`: List of species and RepeatMasker IDs used.

---

## CHAPTERS 8 & 9 – Methodology and Conclusion

*No scripts provided yet.*

---

### 📎 Note:
You can find all these files under the [`/Scripts/`](./Scripts/) folder of this repository. Each script is commented and organized for reproducibility.

