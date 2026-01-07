"""
Universal Scaling Law of Intelligence (Cm) - Implementation
=========================================================

Morphological Realism Research Project
Version: 1.0
Description: Computing the Cm coefficient for AI system intelligence prediction

Cm = f(M, T, P, A, S)

Where:
  M = Model Size (parameters)
  T = Training Data (tokens)
  P = Processing Power (FLOPs)
  A = Architecture Type (categorical: 0-Transformer, 1-CNN, 2-Hybrid, etc.)
  S = System Scope (categorical: 0-Narrow, 1-General, 2-Meta)

The Cm coefficient represents the efficiency of an AI system in achieving
intelligent behavior relative to resource investment.
"""

import math
from typing import Union, Dict, List

class CMFormulaCompute:
    """Compute the universal Cm coefficient for AI intelligence scaling."""
    
    # Constants from empirical calibration
    BASELINE_CM = 0.42  # Reference point for Transformer architecture
    WEIGHT_M = 0.35     # Model size weight
    WEIGHT_T = 0.30     # Training data weight
    WEIGHT_P = 0.20     # Processing power weight
    WEIGHT_A = 0.08     # Architecture influence
    WEIGHT_S = 0.07     # System scope influence
    
    ARCHITECTURE_FACTORS = {
        "transformer": 1.0,    # Baseline
        "cnn": 0.78,           # ~22% less efficient for general intelligence
        "rnn": 0.65,           # ~35% less efficient
        "hybrid": 1.15,        # ~15% more efficient through combination
        "moe": 1.25,           # ~25% more efficient (sparse activation)
        "graph": 1.10,         # ~10% more efficient for relational reasoning
    }
    
    SCOPE_FACTORS = {
        "narrow": 0.60,        # Task-specific, limited scope
        "general": 1.0,        # General-purpose AI
        "meta": 1.40,          # Meta-learning, self-improving systems
    }
    
    def __init__(self):
        """Initialize the Cm formula computer."""
        self.computation_history = []
    
    def normalize_log_scale(self, value: float, scale: str) -> float:
        """
        Normalize parameters to comparable scale using logarithmic transformation.
        
        Args:
            value: The parameter value
            scale: Type of scale - 'log10' or 'natural'
        
        Returns:
            Normalized value in range [0, 1]
        """
        if value <= 0:
            raise ValueError(f"Parameter value must be positive, got {value}")
        
        if scale == "log10":
            return math.log10(value)
        elif scale == "natural":
            return math.log(value)
        else:
            return value
    
    def compute_cm(
        self,
        model_size_params: Union[int, float],
        training_tokens: Union[int, float],
        flops: Union[int, float],
        architecture: str = "transformer",
        scope: str = "general",
        verbose: bool = False
    ) -> Dict[str, float]:
        """
        Compute the universal Cm coefficient.
        
        Args:
            model_size_params: Number of model parameters (M)
            training_tokens: Number of training tokens (T)
            flops: Floating point operations used (P)
            architecture: Type of architecture (default: 'transformer')
            scope: System scope type (default: 'general')
            verbose: Print computation steps
        
        Returns:
            Dictionary with:
              - 'cm': The computed Cm coefficient
              - 'normalized_m': Normalized model size component
              - 'normalized_t': Normalized training data component
              - 'normalized_p': Normalized processing power component
              - 'arch_factor': Architecture adjustment factor
              - 'scope_factor': Scope adjustment factor
              - 'efficiency': Overall efficiency metric (Cm / invested resources)
        """
        
        # Validate inputs
        if model_size_params <= 0 or training_tokens <= 0 or flops <= 0:
            raise ValueError("All parameters must be positive numbers")
        
        arch_key = architecture.lower()
        scope_key = scope.lower()
        
        if arch_key not in self.ARCHITECTURE_FACTORS:
            raise ValueError(
                f"Architecture '{architecture}' not supported. "
                f"Choose from: {list(self.ARCHITECTURE_FACTORS.keys())}"
            )
        
        if scope_key not in self.SCOPE_FACTORS:
            raise ValueError(
                f"Scope '{scope}' not supported. "
                f"Choose from: {list(self.SCOPE_FACTORS.keys())}"
            )
        
        # Normalize parameters (log scale)
        norm_m = self.normalize_log_scale(model_size_params, 'log10')
        norm_t = self.normalize_log_scale(training_tokens, 'log10')
        norm_p = self.normalize_log_scale(flops, 'log10')
        
        # Get architecture and scope factors
        arch_factor = self.ARCHITECTURE_FACTORS[arch_key]
        scope_factor = self.SCOPE_FACTORS[scope_key]
        
        # Compute weighted components (normalized to [0,1] range)
        # Assuming typical values: M=[1M, 1B], T=[1M, 1T], P=[1e18, 1e25]
        component_m = (norm_m / 9.0) * self.WEIGHT_M  # Normalize to typical range
        component_t = (norm_t / 12.0) * self.WEIGHT_T
        component_p = (norm_p / 25.0) * self.WEIGHT_P
        
        # Sum weighted components
        weighted_sum = component_m + component_t + component_p
        
        # Apply baseline and multiplicative factors
        cm = self.BASELINE_CM * (1 + weighted_sum) * arch_factor * scope_factor
        
        # Compute efficiency metric (Cm per resource unit)
        total_resources = model_size_params + training_tokens + flops
        efficiency = cm / math.log1p(total_resources)
        
        result = {
            'cm': cm,
            'normalized_m': norm_m,
            'normalized_t': norm_t,
            'normalized_p': norm_p,
            'arch_factor': arch_factor,
            'scope_factor': scope_factor,
            'efficiency': efficiency,
            'architecture': architecture,
            'scope': scope,
        }
        
        self.computation_history.append(result)
        
        if verbose:
            self._print_computation(result, model_size_params, training_tokens, flops)
        
        return result
    
    def _print_computation(
        self, result: Dict, model_size: Union[int, float],
        training_data: Union[int, float], flops: Union[int, float]
    ) -> None:
        """Print human-readable computation details."""
        print("\n" + "="*60)
        print("UNIVERSAL SCALING LAW - Cm COMPUTATION")
        print("="*60)
        print(f"Model Parameters:       {model_size:,.0f}")
        print(f"Training Tokens:        {training_data:,.0f}")
        print(f"Processing Power:       {flops:.2e} FLOPs")
        print(f"Architecture:           {result['architecture'].capitalize()}")
        print(f"System Scope:           {result['scope'].capitalize()}")
        print("-"*60)
        print(f"Normalized Model Size:  {result['normalized_m']:.4f}")
        print(f"Normalized Training:    {result['normalized_t']:.4f}")
        print(f"Normalized FLOPs:       {result['normalized_p']:.4f}")
        print(f"Architecture Factor:    {result['arch_factor']:.3f}x")
        print(f"Scope Factor:           {result['scope_factor']:.3f}x")
        print("="*60)
        print(f"UNIVERSAL Cm COEFFICIENT:  {result['cm']:.6f}")
        print(f"Efficiency Score:          {result['efficiency']:.8f}")
        print("="*60 + "\n")
    
    def compute_scaling_trajectory(
        self,
        model_size_start: float,
        model_size_end: float,
        steps: int = 10,
        training_ratio: float = 20.0,  # T/M ratio (empirically ~20 for optimal training)
        flops_ratio: float = 1e6,      # P/M ratio
        architecture: str = "transformer",
        scope: str = "general"
    ) -> List[Dict]:
        """
        Compute Cm coefficient trajectory as model scales up.
        
        Args:
            model_size_start: Starting model size
            model_size_end: Ending model size
            steps: Number of computation steps
            training_ratio: Training data per model parameter
            flops_ratio: FLOPs per model parameter
            architecture: Architecture type
            scope: System scope
        
        Returns:
            List of Cm computation results at each scaling step
        """
        results = []
        
        for i in range(steps):
            # Logarithmic scaling progression
            progress = i / max(steps - 1, 1)
            model_size = model_size_start * (model_size_end / model_size_start) ** progress
            training_data = model_size * training_ratio
            flops = model_size * flops_ratio
            
            result = self.compute_cm(
                model_size_params=model_size,
                training_tokens=training_data,
                flops=flops,
                architecture=architecture,
                scope=scope
            )
            results.append(result)
        
        return results
    
    def get_history(self) -> List[Dict]:
        """Return computation history."""
        return self.computation_history
    
    def clear_history(self) -> None:
        """Clear computation history."""
        self.computation_history = []


# Example usage and testing
if __name__ == "__main__":
    # Initialize the Cm computer
    cm_computer = CMFormulaCompute()
    
    # Example 1: GPT-3 like system
    print("\n[Example 1] GPT-3 Scale System")
    result_gpt3 = cm_computer.compute_cm(
        model_size_params=175e9,        # 175 billion parameters
        training_tokens=300e9,          # ~300 billion tokens
        flops=3.14e23,                  # Approximate FLOPs
        architecture="transformer",
        scope="general",
        verbose=True
    )
    
    # Example 2: Scaling analysis from 1B to 100B parameters
    print("\n[Example 2] Scaling Trajectory: 1B → 100B parameters")
    trajectory = cm_computer.compute_scaling_trajectory(
        model_size_start=1e9,
        model_size_end=100e9,
        steps=5,
        architecture="transformer"
    )
    
    print("\nScaling Trajectory Results:")
    print(f"{'Step':<6} {'Model Size':<15} {'Cm':<12} {'Efficiency':<12}")
    print("-" * 50)
    for i, res in enumerate(trajectory):
        params = res['normalized_m']
        print(f"{i:<6} {10**params:.2e}     {res['cm']:.6f}    {res['efficiency']:.8f}")
    
    # Example 3: Architecture comparison
    print("\n[Example 3] Architecture Comparison (1B parameters)")
    architectures = ["transformer", "cnn", "hybrid", "moe"]
    
    for arch in architectures:
        result = cm_computer.compute_cm(
            model_size_params=1e9,
            training_tokens=20e9,
            flops=1e18,
            architecture=arch,
            scope="general"
        )
        print(f"{arch.upper():<15} Cm = {result['cm']:.6f} "
              f"(Factor: {result['arch_factor']:.2f}x)")
