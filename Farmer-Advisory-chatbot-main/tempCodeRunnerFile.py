@app.route("/api/speech-to-text", methods=["POST"])
def speech_to_text_api():
    try:
        if "audio" in request.files:
            audio_file = request.files["audio"]
            if audio_file.filename:
                audio_path = os.path.join(app.config['AUDIO_FOLDER'], audio_file.filename)
                os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)
                audio_file.save(audio_path)
                transcribed_text = transcribe_audio(audio_path)
                return jsonify({"success": True, "text": transcribed_text})
        return jsonify({"success": False, "error": "No audio file provided"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
