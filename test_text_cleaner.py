#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from tools.text_cleaner import TextCleaner

__author__ = 'NachoCP'


class CleanTest(unittest.TestCase):

    text_cleaner = TextCleaner()

    def test_preprocessor_twitter_test(self):
        texts = [u"Salgo de #VeoTV , que día más 1234 largoooooo...",
                 "RT @FabHddzC: Si amas a alguien, déjalo libre. Si grita ese hombre es mío era @paurubio...",
                 "Desde el escaño. Todo listo para empezar #endiascomohoy en el Congreso http://t.co/Mu2yIgCb",
                 "Be the greatest dancer of your life! practice daily positive habits.  #fun #freedom #habits",
                 "@chrisRWK when u get a chance u should leave that piece out for 10 min then turn the lights out "
                 "surprise",
                 "Obsessed with everything @RugbyRL at the moment. In fact http://t.co/Mu2yIgCb"]
        texts_clean = [u"Salgo de #VeoTV , que día más  largoooooo...",
                       "Si amas a alguien, déjalo libre. Si grita ese hombre es mío era ...",
                       "Desde el escaño. Todo listo para empezar #endiascomohoy en el Congreso",
                       "Be the greatest dancer of your life! practice daily positive habits.  #fun #freedom #habits",
                       "when u get a chance u should leave that piece out for  min then turn the lights out	surprise",
                       "Obsessed with everything  at the moment. In fact"
                       ]
        for i in range(len(texts)):
            self.assertEqual(self.text_cleaner.preprocessor_twitter(texts[i]), texts_clean[i])

    def test_delete_punctuation_marks_test(self):
        texts = ["(H)e_l'l\"\\/-o_", "This method, dont delete! final. sentence? marks;"]
        texts_clean = ["Hello", "This method ,  dont delete !  final .  sentence ?  marks ;"]
        for i in range(len(texts)):
            self.assertEqual(self.text_cleaner.delete_punctuation_marks(texts[i]), texts_clean[i])

    def test_delete_accents_test(self):
        texts = [u"día", u"áíéóúüä"]
        texts_clean = ["dia", "aieouua"]
        for i in range(len(texts)):
            self.assertEqual(self.text_cleaner.delete_accents(texts[i]), texts_clean[i])

    def test_normalize_emoticons_test(self):
        texts = [":))", ":((", "::)", ":)))))"]
        texts_clean = [":)", ":(", ":)", ":)"]
        for i in range(len(texts)):
            self.assertEqual(self.text_cleaner.normalize_emoticons(texts[i]), texts_clean[i])

    def test_clean_pos_test(self):
        pos = ["NNP", "NNP-LOC", "NNS", "JJR", "JJS", "RBR", "RBS", "VBD", "VBN", "VBP", "VBZ"]
        pos_clean = ["NN", "NN", "NN", "JJ", "JJ", "RB", "RB", "VB", "VB", "VB", "VB"]
        for i in range(len(pos)):
            self.assertEqual(self.text_cleaner.clean_pos(pos[i]), pos_clean[i])
