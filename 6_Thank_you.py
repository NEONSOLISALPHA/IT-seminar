from manimlib.imports import *  # noqa: F403

"""
                    NOTE:
use manim.py in ~/Development/manim-pptx/manim.py
                      OR
     $ cd ~/Development/manim-pptx/manim.py
     $ python -m manim.py $PATH_TO_FILE.PY
"""


class ThankYou(Scene):
    def construct(self):
        thankyou = TextMobject("Thank You!")
        thankyou.scale(3)
        self.play(Write(thankyou))
        self.play(FadeOutAndShift(thankyou, UP))
