import os
from openai import OpenAI


def transcribe_audio_files(prefix, input_dir, output_dir, response_format="text"):
    """
    Trascrive tutti i file audio che iniziano con un determinato prefisso nella stessa directory,
    in ordine, e salva il risultato in un unico file di testo.

    :param prefix: Prefisso dei file audio (es. "03").
    :param input_dir: Directory contenente i file audio.
    :param output_dir: Directory in cui salvare la trascrizione.
    :param response_format: Formato della risposta (default: "text").
    """
    try:
        # Ottieni API key dall'ambiente o richiedila
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            api_key = input("Enter your OpenAI API key: ")

        # Inizializza il client OpenAI
        client = OpenAI(api_key=api_key)

        # Crea la directory di output se non esiste
        os.makedirs(output_dir, exist_ok=True)

        # Ordina i file che iniziano con il prefisso
        files = sorted(
            [f for f in os.listdir(input_dir) if f.startswith(prefix) and f.endswith(".mp3")],
            key=lambda x: int(x.split('-')[1].split('.')[0])  # Ordina per numero dopo il prefisso
        )

        if not files:
            print(f"Nessun file trovato con prefisso '{prefix}' nella cartella '{input_dir}'.")
            return

        # File di output per la trascrizione
        output_file = os.path.join(output_dir, f"{prefix}.txt")

        # Trascrivi e concatena i risultati
        with open(output_file, "w", encoding="utf-8") as out_file:
            print(f"Inizio trascrizione per i file con prefisso '{prefix}':")
            for file in files:
                file_path = os.path.join(input_dir, file)
                print(f"Trascrizione del file: {file_path}")
                try:
                    with open(file_path, "rb") as audio_file:
                        # Chiamata all'API
                        transcript = client.audio.transcriptions.create(
                            model="whisper-1",
                            file=audio_file,
                            response_format=response_format
                        )

                        # Gestisci se il transcript è un dizionario o una stringa
                        if isinstance(transcript, dict):
                            text = transcript.get("text", "")
                        else:
                            text = str(transcript)  # Usa il transcript direttamente se è stringa

                        # Scrivi il risultato nel file
                        out_file.write(text + " ")
                        print(f"Trascrizione completata per il file: {file_path}")

                except Exception as e:
                    print(f"Errore durante la trascrizione del file {file_path}: {e}")

        print(f"Trascrizione completata. File salvato in: {output_file}")

    except Exception as e:
        print(f"Errore durante la trascrizione: {e}")


def main():
    # Richiedi all'utente il prefisso e le directory
    prefix = input("Enter the prefix of the audio files (e.g., '03'): ")
    input_dir = input("Enter the directory containing the audio files: ").strip('\"')
    output_dir = "./transcripts"

    # Esegui la trascrizione
    transcribe_audio_files(prefix, input_dir, output_dir)


if __name__ == "__main__":
    main()
