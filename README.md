<h1 align="center">tio2-mno2-gqds-cv-ml</h1>

<p align="center">
  Machine-learning analysis of cyclic voltammograms of <b>TiO₂-MnO₂-GQDs</b><br>
  validation schemes · models · figures
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <a href="https://doi.org/10.5281/zenodo.XXXXXXX"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg" alt="DOI"></a>
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#results">Results</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#repository-structure">Structure</a> ·
  <a href="#citation">Citation</a>
</p>

---

## Overview

This repository holds the code, data and results for predicting the current of a TiO₂-MnO₂-GQDs electrode from **potential**, **scan rate** and **sweep direction**, using CV curves recorded at six scan rates (10–60 mV s⁻¹).

The focus is an honest check of how well the models generalise. Five validation schemes are compared, from random splits (optimistic) to purged cross-validation and leave-one-scan-rate-out (demanding).

**Highlights**

- Six CV curves, 12,622 points, one curve per scan rate
- Extra Trees, Random Forest, HistGB and LightGBM compared under five validation schemes
- Feature ablation, split-conformal 90% intervals and SHAP importance
- Everything runs from one notebook and writes a full Excel report plus 300 dpi figures

## Results

| Validation scheme | Extra Trees R² |
|---|---|
| Random splits (holdout, shuffled 5-fold) | ≈ 0.998 |
| Block 5-fold (extrapolation along the curve) | 0.79 |
| Leave-one-scan-rate-out | 0.971 ± 0.043 |
| Purged 5-fold (held-out potential bands) | 0.958 ± 0.036 |

Random-split scores mainly reflect interpolation between neighbouring points and overstate predictive performance. Sweep direction contributed more than scan rate in the feature ablation.

<p align="center">
  <img src="Results/TiO2-MnO2-GQDs_scatter_ET.png" width="85%" alt="Experimental and predicted CV curves">
</p>

<p align="center">
  <img src="Results/validation_schemes_short.png" width="60%" alt="Extra Trees R2 under the validation schemes">
</p>

## Quick start

```bash
git clone https://github.com/comsian-material-lab/tio2-mno2-gqds-cv-ml.git
cd tio2-mno2-gqds-cv-ml
pip install -r requirements.txt
```

The notebook looks for the data files in its own folder. Point it to the `data` folder before starting Jupyter:

```bat
:: Windows (Command Prompt)
set CV_DATA_DIR=data
jupyter notebook
```

```bash
# macOS / Linux
export CV_DATA_DIR=data
jupyter notebook
```

Open `ML_REPORT_TiO2-MnO2-GQDs.ipynb` and choose **Run All**.

<details>
<summary><b>Google Colab and run-time options</b></summary>

- **Colab:** upload the notebook and the six data files, then run all cells. The notebook asks for the files automatically.
- **Run time:** a full run takes about 12 minutes on one CPU, mostly the nested Bayesian tuning. Set `NESTED_TUNING = False` in the settings cell to skip it.
- **Outputs:** written to `RESULTS_TiO2-MnO2-GQDs/` (an Excel report with every table and PNG figures).

</details>

## Repository structure

```
tio2-mno2-gqds-cv-ml/
├── ML_REPORT_TiO2-MnO2-GQDs.ipynb   analysis notebook
├── requirements.txt                  Python packages
├── README.md
├── LICENSE
├── data/                             raw CV files (one per scan rate)
├── Results/                          Excel report and figures
└── Src/                              scripts
```

<details>
<summary><b>Data</b></summary>

Six `.xlsb` files: `10_CV_FINAL`, `20_cv_final`, `30_cv_final`, `40_cv_final`, `50_final1` and `60_cv_final`. Each holds potential (V) and current (A) for one scan rate (10, 20, 30, 40, 50 and 60 mV s⁻¹), potential window about −0.40 to +0.60 V. Other recorded runs (duplicates, outliers and repeats) were not used.

</details>

<details>
<summary><b>Methods in brief</b></summary>

- **Inputs:** potential, scan rate (mV s⁻¹) and sweep direction (1 = increasing potential, 0 = decreasing). The sweep direction is inferred from the data order by smoothing the potential and merging short direction runs, giving two direction changes per curve.
- **Models:** Extra Trees, Random Forest, HistGB and LightGBM (scikit-learn defaults, seed 42); HistGB also tuned by nested Bayesian search.
- **Validation:** (1) random 80:20 holdout, (2) shuffled 5-fold, (3) block 5-fold, (4) leave-one-scan-rate-out, (5) combined model with shuffled and purged 5-fold cross-validation.
- **Extras:** feature ablation, split-conformal 90% intervals, SHAP importance, sweep-direction check.

</details>

## Citation

If you use this code or data, please cite the archived release:

```text
[Authors]. tio2-mno2-gqds-cv-ml (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

## License

Code: MIT License. Data: CC BY 4.0 (if you allow reuse).

## Contact

[Name] · [Institution] · [email]
