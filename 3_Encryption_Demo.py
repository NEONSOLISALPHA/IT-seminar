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


class AKCDemo(Scene):
    def construct(self):
        # scales for all the componenents
        file_scale = 0.8
        key_demo_scale = 1.9
        key_scale = 0.96
        cleartext_scale = 0.8
        ciphertext_scale = 0.63
        process_scale = 1.2
        key_down_pos = 2.9
        key_retrieve_length = 1.7

        title = TextMobject("Symmetric Key Cryptography").scale(1.4)
        title_transformed = TextMobject("Asymmetric Key Cryptography")
        title_transformed.scale(1.4)
        self.play(FadeInFromDown(title))
        self.play(Transform(title, title_transformed))

        title.generate_target()
        title.target.scale(0.7)
        title.target.to_edge(UP, buff=SMALL_BUFF * 2.4)

        pk = ImageMobject(r"animations/assets/pk.png").scale(key_demo_scale)
        sk = ImageMobject(r"animations/assets/sk.png").scale(key_demo_scale)
        keys = Group(pk, sk).arrange(RIGHT, buff=4)
        pk_label = TextMobject("public key").next_to(
            keys[0], DOWN, buff=SMALL_BUFF + 0.2
        )
        sk_label = TextMobject("private key").next_to(
            keys[1], DOWN, buff=SMALL_BUFF + 0.2
        )
        labels = [pk_label, sk_label]
        self.play(MoveToTarget(title), *[FadeInFromDown(i) for i in keys])
        self.play(*[FadeInFromDown(i) for i in labels])

        # clear_text file definition and moving it to the left edge
        file_1 = ImageMobject(r"animations/assets/file_icon.png").scale(
            file_scale,
        )
        file_2 = file_1.copy()
        file_1.to_edge(LEFT, buff=LARGE_BUFF)

        # "Hello" follows around file_1 using file_1.add_updater()
        file_1_label = (
            TextMobject("Hello")
            .move_to(file_1.get_center())
            .scale(cleartext_scale)  # noqa: E501
        )
        file_1_label.add_updater(lambda m: m.move_to(file_1.get_center()))

        """
        ciphertext file label  and moving it
        to the center of decryption image
        """
        file_2_label = TextMobject("IsQ@pq").scale(ciphertext_scale)
        file_2_label.move_to(file_2.get_center())

        file_2_label.add_updater(lambda m: m.move_to(file_2.get_center()))
        encryption = (
            ImageMobject(r"animations/assets/PGP_Encryption.png")
            .shift(LEFT * 2.6)
            .scale(process_scale)
        )
        decryption = (
            ImageMobject(r"animations/assets/PGP_Decryption.png")
            .shift(RIGHT * 2.6)
            .scale(process_scale)
        )

        file_2.move_to(encryption.get_center())

        """
        HACK had to create a duplicate cause file_2
        wouldn't go back to full opacity so, yeah...
        """
        dupli = file_2.copy().set_opacity(0)

        """
        declaring both keys and moving them DOWN below the center of
        processes
        """
        pk = ImageMobject(r"animations/assets/pk.png").scale(key_scale)
        pk.move_to(encryption.get_center() + DOWN * key_down_pos)
        sk = ImageMobject(r"animations/assets/sk.png").scale(key_scale)
        sk.move_to(decryption.get_center() + DOWN * key_down_pos)

        self.play(
            *[FadeOutAndShiftDown(i) for i in labels],
            ReplacementTransform(keys[0], pk),
            ReplacementTransform(keys[1], sk),
            *[
                FadeInFromDown(i)
                for i in [
                    file_1,
                    dupli,
                    file_2_label.set_opacity(0),
                    encryption,
                    decryption,
                    file_1_label,
                ]
            ],
        )

        # bringing mobjects to farthest back layer
        self.bring_to_back(file_2, file_1, file_1_label, file_2_label, pk, sk)

        """
        HACK file_2 didn't want to change opacity back
        to 255 so ended up having to do this...
        """
        ReplacementTransform(dupli, file_2)
        file_2_label.set_opacity(255)
        self.play(file_1.move_to, encryption.get_center())

        def move_key(key):
            key.save_state()
            self.play(
                key.shift,
                UP * key_retrieve_length,
                rate_func=lambda t: exponential_decay(t, 0.22),
            )
            self.play(Restore(key))

        move_key(pk)

        self.play(file_2.move_to, ORIGIN)
        self.play(file_2.move_to, decryption.get_center())
        self.remove(file_2, file_2_label)

        move_key(sk)

        file_1.move_to(decryption.get_center())
        self.play(ApplyMethod(file_1.to_edge, RIGHT, {"buff": LARGE_BUFF}))

        """
        HACK file_2_label refuses to disappear,
        so i had to make a fake one and transform
        """
        label_duplicate = TextMobject("Hello").scale(cleartext_scale)
        label_duplicate.move_to(file_1.get_center())
        ReplacementTransform(file_1_label, label_duplicate)
        self.remove(file_1_label)

        self.play(
            *[
                FadeOutAndShiftDown(i)
                for i in [
                    pk,
                    sk,
                    title,
                    file_1,
                    label_duplicate,
                    encryption,
                    decryption,
                ]
            ]
        )
