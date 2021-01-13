from manimlib.imports import *  # noqa: F403

"""
                    NOTE:
use manim.py in ~/Development/manim-pptx/manim.py
                      OR
     $ cd ~/Development/manim-pptx/manim.py
     $ python -m manim.py $PATH_TO_FILE.PY
"""


class SafelyBrowsingTheWeb(Scene):
    def construct(self):
        title = TextMobject("Safely Browsing the Web")
        title.scale(1.4)
        title.generate_target()
        title.target.to_edge(UP)
        title.target.scale(0.9)

        main_points = [
            "1)  Keep Operating System up to date",
            "2)  Follow Safe Online Behaviour",
            "3)  Oversee online transactions",
        ]

        main_points_vg = VGroup(*[TextMobject(i) for i in main_points])
        main_points_vg.next_to(title.target.get_bottom() + DOWN * 1.3)
        main_points_vg.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.7)
        main_points_vg.to_edge(LEFT)
        main_points_vg.save_state()

        for i in main_points_vg:
            i.generate_target()
            i.target.shift(RIGHT * 1.5)
            i.target.scale(1.3).set_color(ORANGE)

        online_behaviors = [
            ["i)  Use only passwords that contain special charecters"],
            [
                "ii) Think before clicking a link in an",
                "email attachment or a website",
            ],
            [
                "iii)  Only share personal information",
                "with reputable websites which you trust",
            ],
        ]

        online_behaviors_vg_list = []
        for i in online_behaviors:
            vg_list = []
            for j in i:
                vg_list.append(TextMobject(j))
            online_behaviors_vg_list.append(
                VGroup(*vg_list).arrange(DOWN, center=False, aligned_edge=LEFT)
            )
        online_behaviors = VGroup(*online_behaviors_vg_list)
        online_behaviors.arrange(DOWN, center=False, aligned_edge=LEFT)

        for i in online_behaviors:
            if len(i) > 1:
                i[1].shift(RIGHT * 0.6)
            i.generate_target()
            i.target.shift(RIGHT * 3)
            i.target.scale(0.6)

        online_behaviors.move_to(
            online_behaviors[1].target.get_bottom() + DOWN * 0.6,
        )
        self.play(Write(title))
        self.play(MoveToTarget(title))

        self.play(FadeInFrom(main_points_vg, RIGHT))
        self.play(MoveToTarget(main_points_vg[0]))
        self.play(Restore(main_points_vg))

        self.play(
            MoveToTarget(main_points_vg[1]),
            FadeInFrom(online_behaviors, LEFT),
            main_points_vg[2].shift,
            DOWN * 5,
        )

        self.play(
            Restore(main_points_vg),
            FadeOutAndShift(online_behaviors, LEFT),
        )

        main_points_vg[2].generate_target()
        main_points_vg[2].target.shift(RIGHT * 1.5)
        main_points_vg[2].target.scale(1.3).set_color(ORANGE)

        self.play(MoveToTarget(main_points_vg[2]))
        self.play(Restore(main_points_vg))

        self.play(*[Uncreate(i) for i in self.mobjects])
        self.wait()
