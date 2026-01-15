# -*- coding: utf-8 -*-
# =============================================================================
# Project       : Transient
# Module name   : vcf_distortion
# File name     : main.py
# File type     : Python script (Python 3)
# Purpose       : study of nonlinearities in the VCF
# Author        : QuBi (nitrogenium@outlook.fr)
# Creation date : Thursday, 15 January 2026
# -----------------------------------------------------------------------------
# Best viewed with space indentation (2 spaces)
# =============================================================================

# =============================================================================
# EXTERNALS
# =============================================================================
# Project libraries
# None.

# Standard libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from IPython.display import Audio, display



# =============================================================================
# MAIN SCRIPT
# =============================================================================


# Simulation parameters
fs = 44100  # Sample rate (Hz)
T = 1/fs    # Sample period
duration = 2.0  # Duration in seconds (longer to see sweep)
t = np.arange(0, duration, T)

# Filter parameters - linear sweep
fc_start = 10000  # Starting cutoff frequency (Hz)
fc_end = 10       # Ending cutoff frequency (Hz)
fc_sweep = np.linspace(fc_start, fc_end, len(t))  # Linear sweep
Q = 0.707   # Q factor (0.707 for Butterworth response)

# Input signal: square wave at 440Hz
f_input = 440  # Input frequency (Hz)
input_signal = signal.square(2 * np.pi * f_input * t)

# Initialize state variables
BP = np.zeros(len(t))  # Bandpass output
LP = np.zeros(len(t))  # Lowpass output
HP = np.zeros(len(t))  # Highpass output

# Previous sample states for bilinear transform
BP_prev = 0
LP_prev = 0
HP_prev = 0

# Simulate the filter with time-varying cutoff
for n in range(len(t)):
  # Current input
  x = input_signal[n]
  
  # Current cutoff frequency
  fc = fc_sweep[n]
  wc = 2 * np.pi * fc  # Angular frequency
  
  # Highpass calculation (summing junction)
  HP[n] = x - LP_prev - (1/Q) * BP_prev
  
  # First integrator (produces bandpass)
  BP[n] = BP_prev + (wc * T / 2) * (HP[n] + HP_prev)
  
  # Second integrator (produces lowpass)
  LP[n] = LP_prev + (wc * T / 2) * (BP[n] + BP_prev)
  
  # Store previous values for next iteration
  BP_prev = BP[n]
  LP_prev = LP[n]
  HP_prev = HP[n]

# Plot results
fig, axes = plt.subplots(5, 1, figsize=(14, 10))

# Plot cutoff frequency sweep
axes[0].plot(t, fc_sweep, 'k-', linewidth=1.5)
axes[0].set_ylabel('Cutoff (Hz)')
axes[0].set_title(f'State-Variable Filter with Linear Sweep (10kHz→10Hz, Q={Q:.3f}, Square Wave Input={f_input}Hz)')
axes[0].grid(True, alpha=0.3)
axes[0].set_yscale('log')
axes[0].axhline(y=f_input, color='b', linestyle='--', alpha=0.5, label=f'Input freq ({f_input}Hz)')
axes[0].legend()

# Plot input
axes[1].plot(t, input_signal, 'b-', linewidth=0.5, alpha=0.7)
axes[1].set_ylabel('Input')
axes[1].grid(True, alpha=0.3)
axes[1].set_ylim([-1.5, 1.5])

# Plot highpass
axes[2].plot(t, HP, 'r-', linewidth=0.5)
axes[2].set_ylabel('Highpass')
axes[2].grid(True, alpha=0.3)

# Plot bandpass
axes[3].plot(t, BP, 'g-', linewidth=0.5)
axes[3].set_ylabel('Bandpass')
axes[3].grid(True, alpha=0.3)

# Plot lowpass
axes[4].plot(t, LP, 'm-', linewidth=0.5)
axes[4].set_ylabel('Lowpass')
axes[4].set_xlabel('Time (s)')
axes[4].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print some statistics
print(f"Input: Square wave at {f_input} Hz")
print(f"Cutoff sweep: {fc_start} Hz → {fc_end} Hz (linear)")
print(f"Duration: {duration} s")
print(f"Q factor: {Q}")
print(f"\nAt t=0s (fc={fc_start}Hz): Cutoff >> Input frequency")
print(f"At t={duration}s (fc={fc_end}Hz): Cutoff << Input frequency")
print(f"\nNote: The lowpass output starts as a square wave and becomes")
print(f"      progressively more filtered as the cutoff sweeps down.")

# Play the audio outputs
print("\n" + "="*60)
print("AUDIO PLAYBACK")
print("="*60)

# Normalize signals to prevent clipping
def normalize(sig) :
    max_val = np.max(np.abs(sig))
    if max_val > 0:
        return sig / max_val * 0.8
    return sig

print("\nPlaying Input (Square Wave)...")
display(Audio(normalize(input_signal), rate=fs))

print("\nPlaying Highpass Output...")
display(Audio(normalize(HP), rate=fs))

print("\nPlaying Bandpass Output...")
display(Audio(normalize(BP), rate=fs))

print("\nPlaying Lowpass Output (Filter Sweep)...")
display(Audio(normalize(LP), rate=fs))