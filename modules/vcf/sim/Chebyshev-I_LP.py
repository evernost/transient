import numpy as np
from scipy import signal
#import sounddevice as sd
import matplotlib.pyplot as plt

# Audio parameters
sample_rate = 48000  # Hz
duration = 8.0  # seconds
square_freq = 440  # Hz (A4 note)

# Filter parameters
cutoff_start = 10000  # Hz
cutoff_end = 50  # Hz
filter_order = 6
ripple_db = 1  # 1 dB ripple

# Generate time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate square wave
square_wave = signal.square(2 * np.pi * square_freq * t)

# Create logarithmic sweep of cutoff frequency
cutoff_freq = np.logspace(np.log10(cutoff_start), np.log10(cutoff_end), len(t))

# Initialize output array
filtered_output = np.zeros_like(square_wave)

# Process in chunks for efficiency (update filter every N samples)
chunk_size = 512
num_chunks = len(t) // chunk_size

# Initialize filter state variables
zi = None

for i in range(num_chunks):
    start_idx = i * chunk_size
    end_idx = min((i + 1) * chunk_size, len(t))
    
    # Use cutoff frequency at the middle of this chunk
    fc = cutoff_freq[start_idx + chunk_size // 2]
    
    # Design Chebyshev Type I filter
    # Normalize cutoff to Nyquist frequency
    normalized_fc = fc / (sample_rate / 2)
    normalized_fc = np.clip(normalized_fc, 0.001, 0.99)  # Ensure valid range
    
    # Create filter coefficients
    sos = signal.cheby1(filter_order, ripple_db, normalized_fc, 
                        btype='low', analog=False, output='sos')
    
    # Apply filter to this chunk
    chunk_input = square_wave[start_idx:end_idx]
    
    if zi is None:
        # Initialize state for first chunk
        zi = signal.sosfilt_zi(sos) * chunk_input[0]
    
    # Filter the chunk with state
    chunk_output, zi = signal.sosfilt(sos, chunk_input, zi=zi)
    
    filtered_output[start_idx:end_idx] = chunk_output

# Normalize to prevent clipping
filtered_output = filtered_output / np.max(np.abs(filtered_output)) * 0.8

# Play the sound
print(f"Playing {duration}s sweep from {cutoff_start}Hz to {cutoff_end}Hz...")
print(f"Square wave fundamental: {square_freq}Hz")
print("Press Ctrl+C to stop playback")

# try:
#     sd.play(filtered_output, sample_rate)
#     sd.wait()
# except KeyboardInterrupt:
#     sd.stop()
#     print("\nPlayback stopped")

# Create visualization
fig, axes = plt.subplots(3, 1, figsize=(12, 8))

# Plot 1: Cutoff frequency over time
axes[0].semilogx(t, cutoff_freq)
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Cutoff Frequency (Hz)')
axes[0].set_title('Cutoff Frequency Sweep (Logarithmic)')
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=square_freq, color='r', linestyle='--', 
                label=f'Square wave freq ({square_freq}Hz)')
axes[0].legend()

# Plot 2: Original square wave (zoomed to first few periods)
time_zoom = 0.01  # Show first 10ms
zoom_samples = int(time_zoom * sample_rate)
axes[1].plot(t[:zoom_samples] * 1000, square_wave[:zoom_samples])
axes[1].set_xlabel('Time (ms)')
axes[1].set_ylabel('Amplitude')
axes[1].set_title(f'Original Square Wave ({square_freq}Hz)')
axes[1].grid(True, alpha=0.3)

# Plot 3: Filtered output waveform (show multiple sections)
section_times = [0.5, 2.0, 4.0, 6.0, 7.5]  # seconds
colors = plt.cm.viridis(np.linspace(0, 1, len(section_times)))

for idx, section_time in enumerate(section_times):
    section_start = int(section_time * sample_rate)
    section_end = section_start + zoom_samples
    if section_end < len(filtered_output):
        fc_at_section = cutoff_freq[section_start]
        axes[2].plot(t[:zoom_samples] * 1000, 
                    filtered_output[section_start:section_end],
                    label=f't={section_time}s, fc={fc_at_section:.0f}Hz',
                    color=colors[idx], alpha=0.7)

axes[2].set_xlabel('Time (ms)')
axes[2].set_ylabel('Amplitude')
axes[2].set_title('Filtered Output at Different Sweep Points')
axes[2].grid(True, alpha=0.3)
axes[2].legend(fontsize=8)

plt.tight_layout()
plt.show()

print("\nVisualization complete!")