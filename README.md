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