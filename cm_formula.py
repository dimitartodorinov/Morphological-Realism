"""
Morphological Coefficient (Cm)
Universal scaling law of stable intelligent systems.

Cm = (E_exploration / I_structure) * T_cycle
"""

def compute_Cm(E_exploration, I_structure, T_cycle):
    """
    E_exploration : float
        Energy spent on exploration / learning.
    I_structure : float
        Information stored as stable structure (bits).
    T_cycle : float
        Duration of one learning / adaptation cycle.

    Returns
    -------
    float
        Morphological Coefficient Cm.
    """
    return (E_exploration / I_structure) * T_cycle


if __name__ == "__main__":
    # Example values (illustrative only)
    cell = compute_Cm(1e-12, 1e6, 1)
    brain = compute_Cm(1e2, 1e12, 1e3)
    llm = compute_Cm(1e15, 1e13, 1e3)

    print("Cell Cm  :", cell)
    print("Brain Cm :", brain)
    print("LLM Cm   :", llm)
