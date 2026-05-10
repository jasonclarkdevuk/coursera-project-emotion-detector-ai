from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection_happy(self):
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")
		
    def test_emotion_detection_anger(self):
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")
		
    def test_emotion_detection_disgust(self):
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "disgust")
		
    def test_emotion_detection_sadness(self):
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")
		
    def test_emotion_detection_fear(self):
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()