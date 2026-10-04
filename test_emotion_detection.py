from EmotionDetection.emotion_detection import emotion_detector
import unittest

class Test_Emotion_Detection(unittest.TestCase):

    def test_emotion_detection(self):
        result_1 = emotion_detector('Je suis content que cela soit arrivé')
        self.assertEqual(result_1['label'], 'joie')

        result_2 = emotion_detector('Je suis vraiment en colère à ce sujet')
        self.assertEqual(result_2['label'], 'colère')

        result_3 = emotion_detector("Je me sens dégoûté rien qu'en entendant parler de cela")
        self.assertEqual(result_3['label'], 'dégoût')

        result_4 = emotion_detector('Je suis si triste à ce sujet')
        self.assertEqual(result_4['label'], 'tristesse')

        result_5 = emotion_detector("J'ai vraiment peur que cela arrive")
        self.assertEqual(result_5['label'], 'peur')

if __name__ == '__main__':
    unittest.main()   