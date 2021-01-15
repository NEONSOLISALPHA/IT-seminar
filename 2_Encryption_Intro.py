from manimlib.imports import *  # noqa: F403
import math

"""
                    NOTE:
use manim.py in ~/Development/manim-pptx/manim.py
                      OR
     $ cd ~/Development/manim-pptx/manim.py
     $ python -m manim.py $PATH_TO_FILE.PY
"""


class Encryption(Scene):
    def construct(self):
        gibberish = [
            "01ybpqdgtf",
            "5sbf7oplfu",
            "yg5qa1ss18",
            "6itnh51sqg",
            "fvb6egib3s",
            "jzx7lx8j5g",
            "ry32nhbq11",
            "j9ladj2mvd",
            "eaaugrqqo7",
            "oc4cv6gbes",
            "cxtv4fdemr",
            "ntan8hz7jb",
            "3w5zwv7h1c",
            "p8huble8kl",
            "vbnrb2awe6",
            "il5k76g3q6",
            "jc47dmk2yw",
            "aroohgekp3",
            "v78qpy87ey",
            "g6dyxcfj1q",
            "los6h7ylm4",
            "2v1ys2twna",
            "6x55lhhwur",
            "a92pdid5d7",
            "nzklyonwvh",
            "zbdifgpzis",
            "t26crr3m77",
            "jdjqjeeq7l",
            "82xewbgw26",
            "eu65wl5apl",
            "frv3qfplgg",
            "3h7co38b9b",
            "9twu875vvn",
            "4tnjk30rrm",
            "nwfccn92ou",
            "rxsj57txby",
            "mghzbzsksu",
            "zvhabgyg9a",
            "jphkmhpndk",
            "83n7e5251l",
            "kmgdy0q9yf",
            "j4ntryfs4w",
            "sxjyjaffkc",
            "xuxzi4yovz",
            "Ef8hwpoj6i",
            "Eichypoj9n",
            "Ehcyptii0n",
            "Encryption",
        ]
        title_tracker = ValueTracker(0)
        title = TextMobject(gibberish[math.ceil(title_tracker.get_value())])
        title.scale(2)
        title_updater = lambda x: x.become(
            TextMobject(
                gibberish[math.ceil(title_tracker.get_value())],
            ).set_width(x.get_width())
        )
        title.add_updater(title_updater)
        self.add(title)
        self.play(
            title_tracker.increment_value,
            len(gibberish) - 1,
            run_time=1.4,
            rate_func=slow_into,
        )
        points = [
            "In Cryptography, It is the reversible process of converting",
            "cleartext(which can be any data) into an unreadable format",
            "known as ciphertext.",
        ]
        title.remove_updater(title_updater)
        title.generate_target()
        title.target.shift(UP)
        title.target.scale(0.85)
        title.target.set_color(ORANGE)
        points = [TextMobject(i).scale(0.9) for i in points]
        points[0].next_to(title.target, DOWN, buff=LARGE_BUFF * 0.5)
        for i in range(1, len(points)):
            points[i].next_to(points[i - 1], DOWN, buff=SMALL_BUFF)
        self.play(*[FadeInFromDown(i) for i in points], MoveToTarget(title))
        self.play(*[Uncreate(i) for i in points + [title]])


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
