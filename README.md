[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18149202.svg)](https://doi.org/10.5281/zenodo.18149202)

# Morphological Realism: Universal Scaling Law of Intelligence (Cm ≈ 0.1)
## Core Idea

Morphological Realism (MR) proposes a universal law for the emergence of stable intelligent structures across scales – from biological organisms and civilizations to artificial neural networks.

The key invariant is the **Morphological Coefficient**:

\[
Cm = \frac{E_{\text{exploration}}}{I_{\text{structure}}} \cdot T_{\text{cycle}}
\]

Empirically, sustainable intelligent systems tend to operate around \( Cm \approx 0.1 \).

## Thermodynamics of Meaning

MR links non-equilibrium thermodynamics and information theory via Landauer's principle:

\[
\Delta S_{\text{env}} \ge k \ln(2) \cdot I_{\text{bits}}
\]

Every bit of stable structure (memory, model weights, cultural form) has an energetic cost, paid as dissipated heat when exploratory motion collides with environmental boundaries (Λ).

## Phases of Double Convergence

1. **Expansion (V)** – high-entropy exploration of the state space.
2. **Boundary (Λ)** – encounter with computational / energetic limits.
3. **Syntax** – selective filtering and compression of useful patterns.
4. **Morphology (C)** – crystallized structure, an attractor of memory.

These phases appear in biology (development → maturity), cognition (explore → exploit), civilizations (expansion → consolidation), and AI training (random init → converged weights).

## Applications

- **MorphScale™** – early stopping and scaling strategy based on Cm, aiming at significant compute reduction for large language models.
- **MorphExplain™** – phase-transition based interpretability, aligning with emerging AI regulation (e.g. EU AI Act) by making learning dynamics inspectable.
- **Universal AGI metric** – using Cm as a scale-invariant indicator of how efficiently a system converts energy into robust, generalizable structure.

---

© 2026 Dimitar Todorinov. All rights reserved for this conceptual framework. 
Research use is welcome with proper citation.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dimitartodorinov/Morphological-Realism.git
   cd Morphological-Realism
Install required dependencies:

bash
pip install numpy scipy matplotlib
Verify installation:

bash
python -c "from cm_formula import calculate_cm; print('✓ Installation successful!')"
Quick Start Example
Calculate the Morphological Coefficient for your system:

python
from cm_formula import calculate_cm

# Example: Neural network training
exploration_energy = 1000.0      # FLOP units or energy (joules)
structural_information = 50.0    # Bits of stable structure
cycle_duration = 100             # Time steps or seconds

# Compute Cm
Cm = calculate_cm(exploration_energy, structural_information, cycle_duration)

print(f"Morphological Coefficient: {Cm:.4f}")

# Check if system is in safe operational range
if 0.08 <= Cm <= 0.12:
    print("✓ System in optimal morphological stability range (Cm ≈ 0.1)")
else:
    print(f"⚠ Warning: Cm = {Cm:.4f} outside safe range [0.08, 0.12]")
    print("  Consider adjusting exploration_energy or structural_information")
Use Cases
1. Neural Networks & Deep Learning
Use MorphScale to detect optimal training termination points:

python
# Monitor training epochs
for epoch in range(100):
    Cm_current = calculate_cm(flops_used, params_learned, epoch)
    if Cm_current > 0.15:  # Approaching danger zone
        print(f"Stop at epoch {epoch} - capability jump detected")
        break
2. Civilizational Modeling
Estimate phase transitions in complexity growth:

python
# Track civilization complexity
time_period = 
for year in time_period:
    Cm = calculate_cm(energy_consumption, tech_complexity, year)
    print(f"Year {year}: Cm = {Cm:.3f}")
3. Biological Systems
Analyze metabolic efficiency via Kleiber's law:

python
# Animal metabolism analysis
species = {"human": 70, "elephant": 4500, "mouse": 0.02}
for animal, mass_kg in species.items():
    basal_metabolic_rate = 70 * (mass_kg ** 0.75)  # Watts
    structural_info = mass_kg * 8.5  # bits per kg
    Cm = calculate_cm(basal_metabolic_rate, structural_info, 1)
    print(f"{animal}: Cm = {Cm:.4f}")
4. AI Safety & Alignment
Monitor Cm to prevent uncontrolled capability jumps:

python
def safe_ai_training(ai_params):
    Cm = calculate_cm(ai_params['compute'], ai_params['parameters'], ai_params['steps'])
    if Cm > 0.12:
        print("🔴 ALERT: AI approaching morphological instability")
        return False  # Halt training
    return True  # Safe to continue
Configuration
The cm_formula.py module accepts three parameters:

Parameter	Type	Description	Example
exploration_energy	float	Energy spent on exploration (FLOP or joules)	1000.0
structural_information	float	Bits of stable structure formed	50.0
cycle_duration	float	Time steps, seconds, or iterations	100
Output: Returns Cm (float) - the Morphological Coefficient

Running Tests
Check if the formula works correctly on your system:

bash
python -m pytest tests/ -v  # If tests are available
# Or manually run examples:
python cm_formula.py
Troubleshooting
Issue: ModuleNotFoundError: No module named 'cm_formula'

Solution: Ensure you're in the repo directory: cd Morphological-Realism

Issue: Cm value is negative

Solution: Check that all input parameters are positive (exploration_energy > 0)

Issue: Formula doesn't match my expectations

Contact: Open an issue on GitHub or email dimitart.todorinov@gmail.com

## License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

### Commercial Licensing
If you wish to use this work in a proprietary or commercial product without open-sourcing your modifications, please contact **dimitar.t.todorinov@gmail.com** for a commercial license.

For the full license text, see [LICENSE](./LICENSE).


## Citation

If you use Morphological Realism in academic work, please cite:

Dimitar Todorinov, *Morphological Realism: Thermodynamics of Meaning and the Topology of Double Convergence*, Zenodo (2026). https://doi.org/10.5281/zenodo.18149202
