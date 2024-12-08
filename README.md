# OpenAI Whisper Python Integration

Welcome to the **OpenAI Whisper Python Integration** project! This repository provides an easy-to-use Python interface for OpenAI's Whisper model, enabling high-quality speech-to-text processing.

## Features

- **High-Accuracy Speech Recognition:** Leverage OpenAI's Whisper for precise transcription.
- **Easy Integration:** Streamlined Python implementation for rapid deployment.
- **Audio Processing Utilities:** Useful methods for audio format conversion and splitting files into smaller parts.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.7+
- `openai` Python SDK
- `pydub` (for audio processing)
- `ffmpeg` (required by `pydub`)

## Installation

Clone the repository:
```bash
git clone https://github.com/GBarb0/openai-wisper-python.git
cd openai-wisper-python
```

Install the necessary Python libraries:
```bash
pip install openai pydub
```

Ensure `ffmpeg` is installed on your system. For installation instructions, refer to the [official FFmpeg documentation](https://ffmpeg.org/download.html).

### Audio Processing Utilities

The `prepare.py` script includes additional methods to facilitate audio processing:

- **Convert AAC to MP3:**
  ```python
  from prepare import convert_aac_to_mp3
  
  convert_aac_to_mp3("path/to/input.m4a", "path/to/output.mp3")
  ```
- **Split Large Audio Files:**
  ```python
  from prepare import split_audio
  
  split_audio("path/to/audio.mp3", "output/directory", max_size_mb=20)
  ```

These utilities make it easier to preprocess your audio files before transcription.

### Transcribing Audio Files in Bulk

The `main.py` script can be used to transcribe multiple audio files with a specific prefix:

```bash
python main.py
```

You will be prompted to provide:
- The prefix of the audio files.
- The directory containing the audio files.

Transcriptions will be saved in the `./transcripts` directory.

### Supported Formats

The tool supports various audio formats, including:
- WAV
- MP3
- FLAC

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests. Please adhere to the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- OpenAI for the Whisper model
- The Python community for their support

## Contact

For any inquiries, please reach out via the [Issues](https://github.com/GBarb0/openai-wisper-python/issues) section or email **gianlucabarb0@example.com**.

---

Enjoy using **OpenAI Whisper Python Integration**! 🚀
