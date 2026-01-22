# tests/test_h2_premixed_pipeline.py
import os
import numpy as np
import pytest

import aPriori as ap


@pytest.mark.slow
@pytest.mark.integration
def test_h2_premixed_end_to_end(apriori_test_cache_dir: str):
    """
    End-to-end smoke/integration test:
      - download dataset if needed
      - load Field3D
      - compute reaction rates
      - Favre filter
      - compute a subset of derived quantities

    Assertions focus on:
      - attributes exist
      - shapes are consistent
      - values are finite
      - a couple of basic physical / numerical sanity checks
    """
    dns_data_folder = os.path.join(apriori_test_cache_dir, "h2_premixed_dns")

    os.makedirs(dns_data_folder, exist_ok=True)

    # Download only if needed
    if not os.path.exists(os.path.join(dns_data_folder, "data")):
        ap.download(dataset="h2_premixed", dest_folder=dns_data_folder)

    dns_field = ap.Field3D(dns_data_folder)

    # --- DNS reaction rates (should create RH2_DNS etc.)
    dns_field.compute_reaction_rates(exist_ok=True)

    # Check a couple of key variables exist and are readable
    assert hasattr(dns_field, "YH2"), "Dataset should expose YH2"
    assert hasattr(dns_field, "RH2_DNS"), "Reaction-rate computation should expose RH2_DNS"

    yh2_dns = dns_field.YH2.value
    rh2_dns = dns_field.RH2_DNS.value

    assert yh2_dns.shape == dns_field.shape
    assert rh2_dns.shape == dns_field.shape
    assert np.isfinite(yh2_dns).all()
    assert np.isfinite(rh2_dns).all()

    # Basic sanity: mass fraction should be within [0, 1] up to tiny tolerance
    assert yh2_dns.min() >= -1e-8
    assert yh2_dns.max() <= 1.0 + 1e-8

    # --- Favre filter
    filter_size = 6
    filtered_path = dns_field.filter_favre(filter_size, exist_ok=True)
    filtered_field = ap.Field3D(filtered_path)

    # Filtered reaction rates
    filtered_field.compute_reaction_rates(exist_ok=True)

    # Check filtered variables exist
    assert hasattr(filtered_field, "YH2")
    assert hasattr(filtered_field, "RH2_DNS")
    assert hasattr(filtered_field, "RH2_LFR"), "LFR rates should be computed by compute_reaction_rates"

    yh2_f = filtered_field.YH2.value
    rh2_dns_f = filtered_field.RH2_DNS.value
    rh2_lfr_f = filtered_field.RH2_LFR.value

    assert yh2_f.shape == filtered_field.shape
    assert np.isfinite(yh2_f).all()
    assert np.isfinite(rh2_dns_f).all()
    assert np.isfinite(rh2_lfr_f).all()

    # Filtering should not explode the range
    assert yh2_f.min() >= -1e-6
    assert yh2_f.max() <= 1.0 + 1e-6

    # --- Derived quantities on filtered field (subset of your script)
    filtered_field.compute_strain_rate(save_tensor=True)
    assert hasattr(filtered_field, "S_LES") or hasattr(filtered_field, "S_DNS"), "strain-rate outputs should exist"

    filtered_field.compute_residual_dissipation_rate(mode="Smag")
    assert hasattr(filtered_field, "Epsilon_r_Smag"), "Smag model output should exist"
    eps = filtered_field.Epsilon_r_Smag.value
    assert eps.shape == filtered_field.shape
    assert np.isfinite(eps).all()

    filtered_field.compute_residual_kinetic_energy()
    assert hasattr(filtered_field, "K_r")  (
        "Residual kinetic energy output attribute 'K_r' should exist "
    )

    # Timescales
    filtered_field.compute_chemical_timescale(mode="SFR", replace_nonreacting="max")
    assert hasattr(filtered_field, "Tau_c_SFR"), "Chemical timescale should exist"
    tau_c = filtered_field.Tau_c_SFR.value
    assert np.isfinite(tau_c).all()

    filtered_field.fuel = "H2"
    filtered_field.ox = "O2"
    filtered_field.compute_chemical_timescale(mode="Ch")
    assert hasattr(filtered_field, "Tau_c_Ch"), "Chomiak timescale should exist"

    filtered_field.compute_mixing_timescale(mode="Kolmo")
    assert hasattr(filtered_field, "Tau_m_Kolmo"), "Mixing timescale should exist"

    # Progress variable + gradient + laplacian
    filtered_field.compute_progress_variable("H2O")
    assert hasattr(filtered_field, "C"), "Progress variable should exist"

    filtered_field.compute_gradient_C()
    assert hasattr(filtered_field, "C_grad"), "Progress-variable gradient should exist"

    filtered_field.compute_laplacian_C()
    assert hasattr(filtered_field, "C_laplacian"), "Progress-variable laplacian should exist"

    # --- Optional: midplane cut smoke test (fast check it doesn't crash)
    cut_field = ap.Field3D(filtered_field.cut([0, 0, 100], exist_ok=True))
    assert cut_field.shape[2] == 1 or cut_field.shape[2] < filtered_field.shape[2], "Cut should reduce domain"


