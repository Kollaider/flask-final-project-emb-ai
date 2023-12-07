from flask import Flaske, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


@app.route("/emotionDetector")
def detect_emotion():
    resp =  emotion_detector('I love my life')
    return render_template("indext.html", resp=resp)