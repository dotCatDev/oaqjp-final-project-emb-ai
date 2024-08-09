from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Test case for positive sentiment
        emotion = 'I am glad this happened'
        result_1 = emotion_detector(emotion)
        print('Statement: ' + emotion + ' domiant emotion: ' + result_1['dominant_emotion'])
       
        emotion_2 = 'I am really mad about this'
        result_2 = emotion_detector(emotion_2)
        print('Statement: ' + emotion_2 + ' domiant emotion: ' + result_2['dominant_emotion'])

        emotion_3 = 'I feel disgusted just hearing about this'
        result_3 = emotion_detector(emotion_3)
        print('Statement: ' + emotion_3 + ' domiant emotion: ' + result_3['dominant_emotion'])

        emotion_4 = 'I am so sad about this'
        result_4 = emotion_detector(emotion_4)
        print('Statement: ' + emotion_4 + ' domiant emotion: ' + result_4['dominant_emotion'])

        emotion_5 = 'I am really afraid that this will happen'
        result_5 = emotion_detector(emotion_5)
        print('Statement: ' + emotion_5 + ' domiant emotion: ' + result_5['dominant_emotion'])
unittest.main()