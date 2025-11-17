# Entropic Gradient Flow as Universal Physical Ontology  
## Golden Threshold Discovery — φ⁻¹ = 0.618033...

This repository contains all code used to reproduce the results in the manuscript:

**“Entropic Gradient Flow as Universal Physical Ontology:  
The Golden Threshold Discovery” (2025).**

It demonstrates that the simplest far-from-equilibrium unit governed by:

    dx/dt = (1 - x) - Z(x)

with impedance:

    Z(x) = x^2

converges to the universal, stable equilibrium:

    x* = φ⁻¹ = (√5 − 1) / 2 = 0.618033...

---

## Quick Start (Google Colab)

Paste into a Colab cell:

```python
!git clone https://github.com/logansohm/entropic-gradient-ontology.git
%cd entropic-gradient-ontology
!pip install -r requirements.txt
python run_simulation.py
