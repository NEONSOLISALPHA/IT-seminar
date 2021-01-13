from manimlib.imports import *  # noqa: F403

"""
                    NOTE:
use manim.py in ~/Development/manim-pptx/manim.py
                      OR
     $ cd ~/Development/manim-pptx/manim.py
     $ python -m manim.py $PATH_TO_FILE.PY
"""


class SKCDemo(Scene):
    def construct(self):
        file_scale = 1.1
        text_scale = 0.93
        file_2_text_scale = 0.91
        process_scale = 1.8
        key_down_len = 6
        key_insert_len = 4.2

        file_1 = ImageMobject("animations/assets/file_icon.png")
        file_1.scale(file_scale)
        file_2 = file_1.copy()
        # i don't know why i had to create a duplicate but a very weird bugs caused this  # noqa: E501
        duplicate = file_1.copy().set_opacity(0)
        file_1.to_edge(LEFT, buff=2)
        file_1.save_state()
        file_1_label = TextMobject("Hello").move_to(file_1.get_center())
        file_1_label.add_updater(lambda x: x.move_to(file_1.get_center()))
        file_2_label = (
            TextMobject("IsQ@pq")
            .move_to(file_2.get_center())
            .scale(text_scale)
            .set_opacity(0)
        )

        file_2_label.add_updater(
            lambda label: label.move_to(file_2.get_center()),
        )
        encryption = ImageMobject("animations/assets/Encryption.png")
        encryption.scale(process_scale).move_to(ORIGIN)
        sk = ImageMobject("animations/assets/sk.png").scale(file_2_text_scale)
        sk.move_to(DOWN * key_down_len)
        self.add(sk)
        self.bring_to_back(sk)
        self.play(
            *[
                FadeInFromDown(i)
                for i in [
                    file_1,
                    duplicate,
                    file_1_label,
                    file_2_label,
                    encryption,
                ]
            ]
        )

        ReplacementTransform(duplicate, file_2)
        # file_2 would not disappear so had to do fade in with duplicate

        file_2_label.set_opacity(255)
        self.bring_to_back(file_2)

        self.play(file_1.move_to, ORIGIN)

        sk.save_state()
        self.play(sk.shift, UP * key_insert_len, rate_func=slow_into)
        self.play(Restore(sk))

        self.play(
            ApplyMethod(file_2.to_edge, RIGHT, {"buff": 2}),
            rate_func=exponential_decay,
        )

        faux_label = TextMobject("IsQ@pq")
        faux_label.move_to(file_2.get_center())
        faux_label.scale(text_scale)
        ReplacementTransform(file_2_label, faux_label)

        def text_label(text, file, dir=DOWN, offset=0.5):
            textm = TextMobject(text)
            textm.next_to(
                file,
                dir,
                buff=SMALL_BUFF + offset,
            )
            return textm

        cleartext_label = text_label("Cleartext", file_1.saved_state)
        ciphertext_label = text_label("Ciphertext", file_2)

        sk.generate_target()
        sk.target.shift(UP * 3)

        key_label = text_label("key", sk.target, LEFT, 0.2)

        self.play(Restore(file_1), MoveToTarget(sk))
        self.play(
            *[
                FadeInFromDown(i)
                for i in [
                    key_label,
                    cleartext_label,
                    ciphertext_label,
                ]
            ]
        )

        for i in ["password", r"52*sdf1!9", "1234"]:
            password = text_label(i, sk, LEFT, 0.2)
            self.play(Transform(key_label, password))

        self.remove(file_2_label)
        self.play(
            *[
                FadeOutAndShiftDown(i)
                for i in [
                    file_1,
                    ciphertext_label,
                    cleartext_label,
                    key_label,
                    file_1_label,
                    faux_label,
                    file_2,
                    encryption,
                    sk,
                ]
            ]
        )
