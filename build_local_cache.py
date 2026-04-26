#!/usr/bin/env python3
"""
Cirklon Converter - Local Cache Builder

This script builds the local_instrument_data.js file from the pencilresearch/midi repository.

Usage:
    python build_local_cache.py [path_to_midi_directory]
    
    If no path is provided, you'll be prompted to enter one.
"""

import os
import json
import csv
import sys
from pathlib import Path

def build_local_cache():
    print("🎛️ Cirklon Converter - Local Cache Builder")
    print("=" * 50)
    
    # Ask user for the midi-main directory path
    if len(sys.argv) > 1:
        midi_dir = Path(sys.argv[1])
        print(f"📁 Using provided path: {midi_dir}")
    else:
        print("\n📋 Instructions:")
        print("1. Download the latest midi repository from:")
        print("   https://github.com/pencilresearch/midi/archive/refs/heads/main.zip")
        print("2. Extract the ZIP file")
        print("3. Enter the path to the 'midi-main' folder below")
        print()
        
        midi_path = input("Enter path to midi-main directory (or drag & drop): ").strip().strip('"').strip("'")
        if not midi_path:
            print("❌ No path provided. Exiting.")
            return
            
        midi_dir = Path(midi_path)
    
    # Validate directory exists
    if not midi_dir.exists():
        print(f"❌ Error: Directory '{midi_dir}' does not exist!")
        return
    
    if not midi_dir.is_dir():
        print(f"❌ Error: '{midi_dir}' is not a directory!")
        return
        
    print(f"📁 Processing directory: {midi_dir}")
    local_data = {}
    
    # Find all CSV files
    csv_files = list(midi_dir.glob("**/*.csv"))
    
    # Filter out unwanted files
    csv_files = [f for f in csv_files if (
        f.name != "template.csv" and  # Skip template
        not f.name.startswith("._") and  # Skip macOS metadata files
        "__MACOSX" not in str(f)  # Skip macOS metadata directories
    )]
    
    print(f"\n🔄 Processing {len(csv_files)} CSV files...")
    processed_count = 0
    
    for i, csv_file in enumerate(csv_files, 1):
        # Extract brand from parent directory name
        brand = csv_file.parent.name
        
        # Extract model name from filename (remove .csv extension)
        model = csv_file.stem
        
        # Calculate progress
        progress = (i / len(csv_files)) * 100
        
        # Read CSV content
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                csv_content = f.read()
                
            # Initialize brand if not exists
            if brand not in local_data:
                local_data[brand] = {}
                
            # Store the CSV content directly as string (old format for compatibility)
            local_data[brand][model] = csv_content
            processed_count += 1
            
            # Show progress  
            print(f"✓ [{progress:5.1f}%] {brand} / {model}")
            
        except Exception as e:
            print(f"✗ [{progress:5.1f}%] Error reading {csv_file}: {e}")
    
    # Generate JavaScript file with the local data
    js_output = f"""// Local instrument data cache - Generated from pencilresearch/midi repository
// Total: {len([model for brand in local_data.values() for model in brand.keys()])} instruments across {len(local_data)} brands

const LOCAL_INSTRUMENT_DATA = {json.dumps(local_data, indent=2)};

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {{
    module.exports = LOCAL_INSTRUMENT_DATA;
}}
"""
    
    # Write the JavaScript file
    output_file = Path.cwd() / "local_instrument_data.js"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_output)
    
    print(f"\n✅ Local cache generated successfully!")
    print(f"📊 Final Stats:")
    print(f"   - CSV files found: {len(csv_files)}")
    print(f"   - Successfully processed: {processed_count}")
    print(f"   - Failed: {len(csv_files) - processed_count}")
    print(f"   - Brands: {len(local_data)}")
    print(f"   - Total instruments: {sum(len(models) for models in local_data.values())}")
    print(f"   - Output file: {output_file}")
    print(f"   - File size: {output_file.stat().st_size / 1024 / 1024:.1f} MB")
    
    # Print brand summary
    print(f"\n📋 Brand Summary:")
    for brand, models in sorted(local_data.items()):
        print(f"   {brand}: {len(models)} models")

if __name__ == "__main__":
    build_local_cache()