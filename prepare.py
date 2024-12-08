from pydub import AudioSegment
import os


def convert_aac_to_mp3(input_file, output_file):
    """
    Converte un file audio da .aac (o .m4a) a .mp3.

    :param input_file: Percorso al file .aac.
    :param output_file: Percorso al file di output .mp3.
    """
    try:
        print("Conversione da .m4a a .mp3 in corso...")
        audio = AudioSegment.from_file(input_file, format="m4a")
        audio.export(output_file, format="mp3")
        print("Conversione completata.")
    except Exception as e:
        print(f"Errore durante la conversione: {e}")
        raise


def split_audio(file_path, output_dir, max_size_mb=20):
    """
    Divide un file audio in blocchi di massimo `max_size_mb` megabyte.

    :param file_path: Percorso al file audio da dividere.
    :param output_dir: Cartella di output per i blocchi.
    :param max_size_mb: Dimensione massima di ogni blocco in megabyte.
    """
    try:
        print(f"Caricamento del file audio: {file_path}")
        audio = AudioSegment.from_file(file_path)
        max_size_bytes = max_size_mb * 1024 * 1024  # Converti MB in byte
        duration_ms = len(audio)  # Durata totale in millisecondi
        chunk_duration_ms = max_size_bytes / (audio.frame_rate * audio.frame_width) * 1000

        # Dividi il file in blocchi
        os.makedirs(output_dir, exist_ok=True)
        start = 0
        part = 1

        while start < duration_ms:
            end = min(start + chunk_duration_ms, duration_ms)
            chunk = audio[start:end]
            output_file = os.path.join(output_dir, f"{os.path.basename(file_path).split('.')[0]}-{part}.mp3")
            chunk.export(output_file, format="mp3")
            print(f"Creato blocco: {output_file}")
            start = end
            part += 1

        print("Divisione completata.")
    except Exception as e:
        print(f"Errore durante la divisione: {e}")
        raise


def main():
    input_aac_file = "./data/10.m4a"  # Sostituisci con il percorso del tuo file .m4a
    output_mp3_file = "./out/10.mp3"  # Specifica il nome del file .mp3
    output_dir = "./out/split"  # Cartella per i file divisi

    try:
        # Step 1: Conversione da AAC a MP3
        convert_aac_to_mp3(input_aac_file, output_mp3_file)

        # Step 2: Divisione del file MP3 in blocchi da 20 MB
        split_audio(output_mp3_file, output_dir, max_size_mb=20)
        print("Elaborazione completata.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")


if __name__ == "__main__":
    main()