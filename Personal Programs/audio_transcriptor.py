import os
import whisper

# Cargar modelo (se puede "base", "small", "medium" o "large")
# "base" es rápido y suficiente para audios de WhatsApp
model = whisper.load_model("base")

# Carpeta donde tienes los mp3
carpeta = "audios"

# Crear carpeta si no existe
os.makedirs(carpeta, exist_ok=True)

# Recorre todos los archivos .mp3 en la carpeta
for archivo in os.listdir(carpeta):
    if archivo.endswith(".mp3"):
        ruta = os.path.join(carpeta, archivo)
        print(f"\n🎙 Transcribiendo: {archivo}...")
        resultado = model.transcribe(ruta, language="es")
        texto = resultado["text"]

        # Guardar cada transcripción en un .txt
        with open(ruta.replace(".mp3", ".txt"), "w", encoding="utf-8") as f:
            f.write(texto)

        print(f"✅ Listo. Texto guardado en {archivo.replace('.mp3', '.txt')}")
