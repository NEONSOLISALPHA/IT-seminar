from manimlib.imports import *  # noqa: F403

"""
                    NOTE:
use manim.py in ~/Development/manim-pptx/manim.py
                      OR
     $ cd ~/Development/manim-pptx/manim.py
     $ python -m manim.py $PATH_TO_FILE.PY
"""


class TorIntro(Scene):
    def construct(self):
        title = TextMobject("T", "he ", "O", "nion", " R", "outer").scale(2)
        title_Transformed = TextMobject("T", "O", "R", " Protocol").scale(2)
        self.play(Write(title))
        self.play(
            *[
                ReplacementTransform(title[2 * i], title_Transformed[i])
                for i in range(3)
            ],
            *[FadeOut(title[i]) for i in range(6) if i % 2 == 1],
            FadeInFrom(title_Transformed[-1], RIGHT),
        )
        self.play(FadeOutAndShiftDown(title_Transformed))


class Tor(Scene):
    def construct(self):
        client = ImageMobject(r"animations/assets/comp-man.png")
        client.to_edge(LEFT).shift(DOWN * 1.5)

        server_1 = ImageMobject(r"animations/assets/Server.png")
        server_1.move_to(client.get_corner(UR) + UP * 2 + RIGHT * 0.5)  # noqa: E501
        server_2 = server_1.copy().next_to(server_1, RIGHT * 5)
        server_3 = server_1.copy().next_to(server_2, RIGHT * 5)
        servers = [server_1, server_2, server_3]

        website = ImageMobject(r"animations/assets/Website_Server.png")
        website.next_to(server_3, DOWN * 0.7 + RIGHT).shift(DOWN * 0.65)

        website_arrow = Line(
            server_3.get_right(), website.get_edge_center(UP), buff=SMALL_BUFF
        ).add_tip(0.2)
        client_arrow = Line(
            client.get_corner(UR) + LEFT * 1.5,
            server_1.get_left(),
            buff=SMALL_BUFF,
        ).add_tip(0.2)

        public_keys = []
        for index, server in enumerate(servers):
            key = TextMobject(f"k{index+1}")
            key.move_to(server.get_corner(UL) + LEFT * 0.5)
            key.set_color(GREEN)
            public_keys.append(key)

        secret_keys = []
        for index, key in enumerate(public_keys):
            secret_key = TextMobject(f"s{index + 1}")
            secret_key.next_to(key, UP, buff=0.4).set_color(RED)
            secret_keys.append(secret_key)

        arrows = [
            Line(
                servers[i].get_right(),
                servers[i + 1].get_left(),
                buff=SMALL_BUFF,
            ).add_tip(0.2)
            for i in range(len(servers) - 1)
        ]
        self.play(FadeInFrom(client, LEFT))
        self.play(GrowArrow(client_arrow))
        self.play(*[FadeInFrom(servers[i], UP) for i in range(len(servers))])

        client_label = TextMobject("client")
        client_label.next_to(client, DOWN, buff=SMALL_BUFF)
        website_label = TextMobject("WebServer")
        website_label.next_to(website, DOWN, buff=SMALL_BUFF)

        website_label_transformed = TextMobject("www.google.com")
        website_label_transformed.next_to(website, DOWN, buff=SMALL_BUFF)

        server_brace = Brace(Group(*servers), DOWN, buff=SMALL_BUFF)

        tor_label = TextMobject("Tor Servers")
        tor_label.next_to(server_brace, DOWN, buff=SMALL_BUFF)

        server_label = VGroup(server_brace, tor_label)

        self.play(*[GrowArrow(arrows[i]) for i in range(len(arrows))])
        self.play(GrowArrow(website_arrow))
        self.play(FadeInFromDown(website))
        self.play(
            *[
                FadeInFromDown(i)
                for i in [
                    server_label,
                    client_label,
                    website_label,
                ]
            ]
        )
        self.play(
            ReplacementTransform(website_label, website_label_transformed),
        )
        self.play(
            *[FadeInFromDown(i) for i in public_keys],
            FadeOutAndShiftDown(server_label),
        )
        self.play(*[FadeInFromDown(i) for i in secret_keys])

        for i in public_keys:
            i.generate_target()
            i.target.move_to(client.get_center())

        self.play(*[MoveToTarget(i) for i in public_keys])
        self.play(*[FadeOut(i) for i in public_keys])
        onion_full = SVGMobject(r"animations/assets/Onions/onion_Full.svg")
        onion_1 = SVGMobject(r"animations/assets/Onions/Onion_1.svg")
        onion_2 = SVGMobject(r"animations/assets/Onions/Onion_2.svg")
        message = SVGMobject(r"animations/assets/Onions/Message.svg")
        onions = [onion_full, onion_1, onion_2, message]
        onions = [i.set_stroke(BLACK, 2) for i in onions]

        scales = iter([1.5, 1.2, 0.9, 0.6])

        def create_copy(onion):
            onion_ = onion.copy()
            onion_.scale(next(scales))
            onion_.to_edge(DOWN, buff=LARGE_BUFF)
            onion_.shift(DOWN * 0.3)
            return onion_

        onion_copies = [create_copy(i) for i in onions]

        onions[0].next_to(client, RIGHT, buff=SMALL_BUFF).scale(0.4)
        for i in range(1, len(onions)):
            onions[i].next_to(servers[i - 1], DOWN, buff=SMALL_BUFF).scale(0.4)

        onions[0].generate_target()
        onions[0].target.move_to(website.get_center())
        onions[0].target.set_opacity(0)

        words = ["message", "s3", "s2", "s1"]

        def onion_text(onion):
            vg = VGroup(onion)
            for i in range(len(onion) - 1, -1, -1):
                j = len(onion) - i - 1
                text = TextMobject(words[j]).set_color(BLACK)
                if j == 0:
                    text.move_to(onion[i].get_center())
                else:
                    text.move_to(onion[i].get_top() + DOWN * 0.23)
                vg.add(text)
            return vg

        onion_copies = [onion_text(onion_copy) for onion_copy in onion_copies]

        for index, secret_key in enumerate(secret_keys):
            secret_key.generate_target()
            secret_key.target.move_to(onion_copies[index][0].get_center())

        self.play(FadeInFromDown(onion_copies[0]), FadeInFromDown(onion_full))
        for i in range(1, len(onions)):
            self.play(
                Transform(onions[0], onions[i]),
                MoveToTarget(secret_keys[i - 1]),
                Transform(onion_copies[0], onion_copies[i]),
            )
            self.remove(secret_keys[i - 1])

        self.remove(onion_copies[3])
        self.play(
            MoveToTarget(onions[0]),
            FadeOutAndShiftDown(onion_copies[0]),
        )
        self.remove(onions[0])
        self.play(*[Rotate(i) for i in arrows + [client_arrow, website_arrow]])
        self.wait()
        self.play(*[FadeOutAndShiftDown(i) for i in self.mobjects])
