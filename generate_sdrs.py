import json

# List of SDRs Define start and end freq along with sample rate
sdr_list = [
    {
        "name": "RTL-SDR",
        "type": "rtl_sdr",
        "always-on": False,
        "device": "00000001",
        "direct_sampling": 0,
        "rf_gain": "auto",
        "bias_tee": True,
        "device_start_freq": 65e6,  # 65 MHz
        "device_end_freq": 2300e6,  # 2300 MHz
        "device_samp_rate": 2.4e6,  # 2.4 MHz
        "device_min_samp_rate": 2e6  # 2 MHz
    }
    # ... add more SDR entries as needed
]

# Your existing JSON data
json_data = '''
{
    "version": 8,
    "sdrs": {}
}
'''

# Load JSON data
data = json.loads(json_data)

# Iterate through the list of SDRs and add them to the JSON data
for i, sdr in enumerate(sdr_list, start=1):
    sdr_id = f"sdr_id_{i}"
    data["sdrs"][sdr_id] = {
        **sdr,
        "profiles": {}  # You can add profiles here if needed
    }

# Custom profiles
# available decoders=ft8,ft4,jt65,jt9,wspr,fst4,fst4w,q65,msk144,js8,packet,ais,page,sstv,fax,ism,hfdl,vdl2,acars,adsb
custom_profiles = {
    # Short Name : (Start Frequency, End Freqncy, Decoder), Notes
    "VLF": (3e3, 20e3, "wspr"),  # 3 kHz – 20 kHz
    "Standard Frequency and Time Signal": (20e3, 30e3, "time"),  # 20 kHz – 30 kHz
    "Longwave AM Radio": (30e3, 300e3, "acars"),  # 30 kHz – 300 kHz
    "Medium Frequency": (300e3, 530e3, "wspr"),  # 300 kHz – 530 kHz
    "AM Broadcast": (530e3, 1700e3, "am"),  # 530 kHz – 1700 kHz
    "Top Band": (1.8e6, 2e6, "jt65"),  # 1.8 MHz – 2 MHz
    "80 Meters": (3.5e6, 4e6, "jt9"),  # 3.5 MHz – 4 MHz
    "Shortwave AM Radio": (4e6, 5.3e6, "am"),  # 4 MHz – 5.3 MHz
    "60 Meters": (5.3e6, 5.4e6, "wspr"),  # 5.3 MHz – 5.4 MHz
    "40 Meters": (7e6, 7.3e6, "fst4"),  # 7 MHz – 7.3 MHz
    "30 Meters": (10.1e6, 10.15e6, "fst4w"),  # 10.1 MHz – 10.15 MHz
    "20 Meters": (14e6, 14.35e6, "q65"),  # 14 MHz – 14.35 MHz
    "17 Meters": (18.068e6, 18.168e6, "msk144"),  # 18.068 MHz – 18.168 MHz
    "15 Meters": (21e6, 21.45e6, "js8"),  # 21 MHz – 21.45 MHz
    "12 Meters": (24.89e6, 24.99e6, "packet"),  # 24.89 MHz – 24.99 MHz
    "Citizens Band Radio": (26.965e6, 27.405e6, "am"),  # 26.965 MHz – 27.405 MHz
    "Free Band CB Radio": (27.405e6, 28e6, "ais"),  # 27.405 MHz – 28 MHz
    "10 Meters": (28e6, 29.7e6, "ais"),  # 28 MHz – 29.7 MHz
    "VHF Low Band": (29.7e6, 50e6, "am"),  # 29.7 MHz – 50 MHz
    "6 Meters": (50e6, 54e6, "page"),  # 50 MHz – 54 MHz
    "VHF Low Band": (54e6, 88e6, "am"),  # 54 MHz – 88 MHz
    "FM Broadcast": (88e6, 108e6, "wfm"),  # 88 MHz – 108 MHz
    "VHF": (108e6, 148e6, "ft4"),  # 108 MHz – 148 MHz
    "VHF High Band": (148e6, 156.025e6, "am"),  # 148 MHz - 156.025 MHz
    "Marine VHF Radio": (156.025e6, 157.425e6, "fm"),  # 156.025 MHz – 157.425 MHz
    "VHF Marine Band": (157.425e6, 162.4e6, "fm"),  # 157.425 MHz - 162.4 MHz
    "Weather Radio": (162.4e6, 162.55e6, "fm"),  # 162.4 MHz – 162.55 MHz
    "VHF High Band": (162.55e6, 216e6, "am"),  # 162.55 MHz - 216 MHz
    "218-219 MHz Service": (216e6, 219e6, "fm"),  # 216 MHz - 219 MHz
    "1.25 Meters": (219e6, 225e6, "fax"),  # 219 MHz – 225 MHz    
    "VHF Range": (225e6, 420e6, "am"),  # 225 MHz - 420 MHz
    "70 Centimeters": (420e6, 450e6, "ism"),  # 420 MHz – 450 MHz
    "UHF": (450e6, 462.5625e6, "ft8"),  # 450 MHz – 462.5625 MHz
    "Family Radio Service": (462.5625e6, 467.7125e6, "fm"),  # 462.5625 MHz – 467.7125 MHz
    "UHF": (467.7125e6, 470e6, "ft8"),  # 467.7125 MHz – 470 MHz
    "General Mobile Radio Service": (467e6, 470e6, "fm"),  # 467 MHz – 470 MHz
    "UHF": (470e6, 902e6, "am"),  # 470 MHz - 902 MHz
    "33 Centimeters": (902e6, 928e6, "hfdl"),  # 902 MHz – 928 MHz
    "ADS-B 978 MHz": (976.8e6, 979.2e6, "adsb"),  # 978 MHz ADS-B frequency
    "ADS-B": (1088.8e6, 1091.2e6, "adsb"),  # 1088.8 MHz – 1091.2 MHz
    "23 Centimeters": (1240e6, 1300e6, "vdl2"),  # 1240 MHz – 1300 MHz
    "L Band": (1.3e9, 3000e9, "ft8"),  # 1.3 GHz – 3 GHz
    "S Band": (3000e9, 5.925e9, "ft4"),  # 3 GHz – 5.925 GHz
    "C Band": (5.925e9, 6.875e9, "ft8"),  # 5.925 GHz – 6.875 GHz
    "X Band": (6.875e9, 30e9, "q65"),  # 6.875 GHz – 30 GHz
    "Ka Band": (30e9, 300e9, "msk144")  # 30 GHz – 300 GHz
}


sorted_custom_profiles = dict(sorted(custom_profiles.items(), key=lambda x: x[1][0]))

# Function Calculate Sample Rate
def calc_sample_rate(start_freq, end_freq, device_samp_rate, device_min_samp_rate, device_start_freq, device_end_freq):
    result = end_freq - start_freq
    if device_min_samp_rate < result < device_samp_rate:
        return result
    elif result <= device_min_samp_rate:
        return device_min_samp_rate
    else:
        return device_samp_rate

# Function to calculate center frequency
def calculate_center_freq(start_freq, end_freq):
    return (start_freq + end_freq) / 2

# Function to generate profiles for a given frequency range
def generate_profiles(profiles, calc_sample_rate_func, device_samp_rate, device_min_samp_rate, device_start_freq, device_end_freq):
    generated_profiles = {}
    
    for profile_name, (start_freq, end_freq, decoder) in profiles.items():
        center_freq = calculate_center_freq(start_freq, end_freq)
        
        # Ensure that the profile frequency range is within the device limits
        if end_freq <= device_start_freq or start_freq >= device_end_freq:
            continue
        
        # Calculate the starting point of the loop based on the device's start frequency
        loop_start_freq = max(start_freq, device_start_freq)
        
        # Calculate the number of profiles needed to cover the specified bandwidth
        num_profiles = int((min(end_freq, device_end_freq) - loop_start_freq) / calc_sample_rate_func(start_freq, end_freq, device_samp_rate, device_min_samp_rate, device_start_freq, device_end_freq))
        
        # Ensure that at least one profile is generated
        num_profiles = max(num_profiles, 1)
        
        # Create profiles with overlapping ranges
        for i in range(num_profiles):
            profile_start_freq = loop_start_freq + i * calc_sample_rate_func(start_freq, end_freq, device_samp_rate, device_min_samp_rate, device_start_freq, device_end_freq)
            profile_end_freq = profile_start_freq + calc_sample_rate_func(start_freq, end_freq, device_samp_rate, device_min_samp_rate, device_start_freq, device_end_freq)
            
            part_suffix = f" - Part {i+1}" if num_profiles > 1 else ""
            
            profile_data = {
                "name": f"{profile_name}{part_suffix}",
                "center_freq": calculate_center_freq(profile_start_freq, profile_end_freq),
                "rf_gain": "auto",
                "samp_rate": calc_sample_rate_func(start_freq, end_freq, device_samp_rate, device_min_samp_rate, device_start_freq, device_end_freq),
                "start_freq": calculate_center_freq(profile_start_freq, profile_end_freq),
                "start_mod": decoder,
                "initial_squelch_level": -45,
                "waterfall_auto_level_default_mode": "true",
                "eibi_bookmarks_range": 25,
                "repeater_range": 25
            }
            
            # Check if the generated profile falls within the specified frequency range
            if profile_start_freq >= device_start_freq and profile_end_freq <= device_end_freq:
                generated_profiles[f"{profile_name}{part_suffix}"] = profile_data
    
    return generated_profiles

# Update the profiles in the JSON data for all SDRs
for sdr_id, sdr_data in data["sdrs"].items():
    sdr_data["profiles"] = generate_profiles(
        sorted_custom_profiles, calc_sample_rate, sdr_data["device_samp_rate"], sdr_data["device_min_samp_rate"], sdr_data["device_start_freq"], sdr_data["device_end_freq"]
    )

# Print the updated JSON
print(json.dumps(data, indent=4))
