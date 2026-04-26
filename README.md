# MIDI to Cirklon .cki Converter

This web tool converts MIDI CC definitions from the [pencilresearch/midi](https://github.com/pencilresearch/midi) repository into Sequentix Cirklon .cki instrument definition files.

## Features

- **Offline-First Database**: Includes 279 instruments from 88 brands cached locally for instant access
- **Brand and Model Selection**: Browse through all available synthesizer brands and models from the pencilresearch/midi database
- **Real-time Preview**: See exactly what your .cki file will look like before downloading
- **Automatic Conversion**: Converts CSV data including:
  - MIDI Control Change (CC) definitions
  - NRPN (Non-Registered Parameter Numbers) where available
  - Parameter names, descriptions, and value ranges
  - Section organization
- **Character Limit Handling**: Automatically respects Cirklon's strict limits:
  - Instrument names: 9 characters maximum
  - CC parameter labels: 6 characters maximum  
  - Smart shortening priority: 1) Remove spaces first, 2) Remove lowercase vowels
  - Always preserves capital letters (A-Z) and consonants
  - Only uses Cirklon-allowed characters: `[-A-Za-z0-9()#. $@!&+{}*]`
- **Name Review & Customization**: Optional checkbox to review all automatic shortenings
  - Shows original names, auto-shortened names, and editable custom name fields
  - Real-time character counting with length validation
  - Applies custom names to final .cki output
  - Perfect for creating more intuitive parameter abbreviations
- **Modern Web Interface**: Clean, responsive design that works on desktop and mobile
- **Direct Download**: Generate and download .cki files with proper naming

## How to Use

1. **Open the Tool**: Open `cirklon-converter.html` in any modern web browser
2. **Select Brand**: Choose from the dropdown list of available synthesizer brands
3. **Select Model**: After selecting a brand, choose the specific model from the available CSV files
4. **Review Names (Optional)**: Check "Review and customize parameter names" to customize automatic shortenings
5. **Preview (Optional)**: Click "Preview" to see the generated .cki content before downloading
6. **Generate File**: Click "Generate .cki File" to create and download your instrument definition

### Name Review Workflow

When "Review and customize parameter names" is checked:
1. The tool analyzes all parameter names that will be shortened
2. A modal displays each name with: original → auto-shortened → custom name field
3. Edit any names you want to customize (respects character limits)
4. Click "Apply Changes & Generate" to create the .cki file with your custom names

## Generated .cki Format

The tool creates .cki files in the correct Cirklon JSON format:

```json
{
  "instrument_data": {
    "[Brand] [Model]": {
      "CC_defs": {
        "CC_1": {
          "label": "Parameter Name",
          "min_val": 0,
          "max_val": 127,
          "start_val": 64
        }
      },
      "track_values": {
        "slot_1": {
          "MIDI_CC": 1,
          "label": "Parameter Name"
        }
      },
      "midi_port": "1",
      "midi_chan": 1,
      "multi": false,
      "presend_pgm": false,
      "default_note": "C 3",
      "default_patt": "P3",
      "poly_spread": "off",
      "no_bankL": false,
      "no_bankM": false,
      "no_xpose": false,
      "no_fts": false,
      "show_note_nums": false,
      "no_thru": false
    }
  }
}
```

## Technical Details

- **Offline-First**: Uses local cache of 279 instruments (1.6MB) for instant access
- **Optional Online Updates**: "Fetch Latest from GitHub" button for getting newest data
- **CSV Parsing**: Handles quoted fields and various CSV formats
- **Correct Format**: Generates .cki files in the proper JSON format used by the [Cirklon Organizer](https://cirklon-community.gitlab.io/cirklon-organizer/)
- **Error Handling**: Graceful error handling with user-friendly messages
- **Browser Compatibility**: Works with all modern browsers
- **No Dependencies**: Pure HTML, CSS, and JavaScript - no external libraries

## Supported Data

The tool processes the following CSV columns from the pencilresearch/midi database:

- `manufacturer` - Brand name
- `device` - Model name
- `section` - Parameter grouping
- `parameter_name` - Control name
- `parameter_description` - Detailed description
- `cc_msb` - MIDI CC number
- `cc_min_value`, `cc_max_value`, `cc_default_value` - Value ranges
- `nrpn_msb`, `nrpn_lsb` - NRPN definitions
- `nrpn_min_value`, `nrpn_max_value`, `nrpn_default_value` - NRPN ranges

## Local Database

The tool includes a comprehensive local database with **279 instruments from 88 brands**:

**Popular Brands Include:**
- Elektron (15 instruments): Analog Rytm, Digitakt, Model Cycles, Syntakt, etc.
- KORG (21 instruments): minilogue, prologue, volca series, Wavestate, etc.  
- Roland (35 instruments): Jupiter-X, TR-8S, System-8, JU-06A, etc.
- Moog (12 instruments): Mother-32, Matriarch, Subsequent series, etc.
- Chase Bliss (24 instruments): MOOD, blooper, Brothers, Generation Loss, etc.
- Sequential (6 instruments): Prophet Rev2, Prophet-6, Take 5, etc.
- Arturia (4 instruments): MicroFreak, Polybrute, MatrixBrute, etc.
- And 81 more brands including Behringer, Novation, Waldorf, Dreadbox, etc.

## Using with Cirklon

1. Save the generated .cki file to your Cirklon's SD card in the appropriate directory
2. Load the instrument definition on your Cirklon sequencer
3. Assign the instrument to tracks in your songs
4. The parameter names and controls will be available for real-time manipulation

## Format Compatibility

The generated .cki files are fully compatible with:
- **Sequentix Cirklon** hardware sequencer (all firmware versions)
- **[Cirklon Organizer](https://cirklon-community.gitlab.io/cirklon-organizer/)** - Official web-based instrument editor
- Other Cirklon community tools that work with .cki files

The files use the official JSON format structure as defined by the Cirklon community tools.

## Contributing

The underlying data comes from the community-maintained [pencilresearch/midi](https://github.com/pencilresearch/midi) repository. To add support for new instruments or improve existing definitions, contribute to that project.

## License

This converter tool is provided as-is for the Cirklon community. The MIDI data is from the pencilresearch/midi project and follows their licensing terms.