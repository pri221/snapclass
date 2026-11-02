from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import io
import librosa
import streamlit as st
import soundfile as sf

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()

def get_voice_embedding(audio_bytes):
    try:
        if not audio_bytes:
            return None
        encoder = load_voice_encoder()

        #audio, sr =librosa.load(io.BytesIO(audio_bytes), sr = 16000)
        # Read directly using SoundFile
        buffer = io.BytesIO(audio_bytes)
        audio, sr = sf.read(buffer)

        # Convert stereo to mono if needed
        if len(audio.shape) > 1:
            audio = np.mean(audio, axis=1)

        # Resample to 16000 Hz if necessary
        if sr != 16000:
            audio = librosa.resample(
                y=audio, orig_sr=sr, target_sr=16000
            )

        wav = preprocess_wav(audio)
        embedding = encoder.embed_utterance(wav)

        return embedding
    except Exception as e:
        st.error('voice recog error')
        return None

def identify_speaker(new_embedding, candidated_dict, threshold=0.65):
    if new_embedding is None or not candidated_dict:
        return None, 0.0

    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidated_dict.items():
        if stored_embedding:
            similarity = np.dot(new_embedding, stored_embedding)
            if similarity>best_score:
                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_sid,best_score

    return None, best_score

def process_bulk_audio(audio_bytes, candidates_dict, threshold = 0.65):
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        segments = librosa.effects.split(audio, top_db=30)

        identify_result ={}

        for start, end in segments:
            if(end-start)<sr*0.5:
                continue
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.embed_utterance(wav)

            sid, score = identify_speaker(embedding, candidates_dict, threshold)

            if sid:
                if sid not in identify_result or score > identify_result[sid]:
                    identify_result[sid] = score

        return identify_result
    except Exception as e:
        st.error('Bilk Process Error')
        return {}
