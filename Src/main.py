# ─────────────────────────────────────────────────────────
# EXCEL REPORT
# ─────────────────────────────────────────────────────────
features_info = pd.DataFrame([
    ["Potential (V)",    "Experimental", "Primary driver of current response"],
    ["ScanRate (mV/s)",  "Experimental", "Kinetic effects at different sweep speeds (real value, not an index)"],
    ["Sweep_Direction",  "Experimental", "Anodic (forward) vs cathodic (reverse) branch; inferred from data order"],
], columns=["Feature", "Category", "Justification"])

data_files = pd.concat([
    pd.DataFrame([{"File": f, "ScanRate_mVs": s, "Status": "used", "Note": ""} for s, f in SCAN_FILES.items()]),
    pd.DataFrame([{"File": f, "ScanRate_mVs": "", "Status": "excluded", "Note": n} for f, n in EXCLUDED_FILES.items()]),
], ignore_index=True)

with pd.ExcelWriter(f"{OUT}/ML_REPORT_TiO2-MnO2-GQDs.xlsx") as xw:
    summary_df.to_excel(xw, sheet_name="Validation_Summary", index=False)
    pc_pool.to_excel(xw, sheet_name="Schemes1-3_Pooled_NRMSE", index=False)
    percurve_df.round(4).to_excel(xw, sheet_name="Per_Curve_Detail_Schemes1-3", index=False)
    losro_df.to_excel(xw, sheet_name="Scheme4_Leave1ScanRateOut", index=False)
    purge_df.to_excel(xw, sheet_name="Purged_5Fold_Models", index=False)
    abl_df.to_excel(xw, sheet_name="Feature_Ablation", index=False)
    unc_df.to_excel(xw, sheet_name="Uncertainty", index=False)
    fold_df.to_excel(xw, sheet_name="Fold_Sizes_Pooled", index=False)
    sizes_df.round(1).to_excel(xw, sheet_name="Fold_Sizes_PerCurve", index=False)
    ds_df.to_excel(xw, sheet_name="Dataset_Sizes", index=False)
    sweep_df.to_excel(xw, sheet_name="Sweep_Direction_Check", index=False)
    cp_df.to_excel(xw, sheet_name="Cp_From_Files", index=False)
    extra_df.to_excel(xw, sheet_name="Extra_Checks", index=False)
    data_files.to_excel(xw, sheet_name="Data_Files", index=False)
    if not std_df.empty: std_df.to_excel(xw, sheet_name="Standard_5Fold_Models", index=False)
    if not shap_df.empty: shap_df.to_excel(xw, sheet_name="SHAP_Importance", index=False)
    features_info.to_excel(xw, sheet_name="Feature_List", index=False)

print("\n" + "=" * 70)
print(f"DONE | features: {len(FEATURES)} | seed: {SEED}")
print("\nVALIDATION SUMMARY (R2 mean +/- SD):")
print(summary_df[summary_df.Model.isin(["Extra Trees", "Ridge (baseline)"])].to_string(index=False))
print("\nPurged CV, model comparison:")
print(purge_df.to_string(index=False))
print(f"\nOutputs in {OUT}/")
print("=" * 70)
