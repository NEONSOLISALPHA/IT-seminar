from manimlib.imports import *  # noqa: F403

"""
                    NOTE:
use manim.py in ~/Development/manim-pptx/manim.py
                      OR
     $ cd ~/Development/manim-pptx/manim.py
     $ python -m manim.py $PATH_TO_FILE.PY
"""


class WaysToTrack(Scene):
    def construct(self):
        main_point_buff = 0.7
        main_point_title_buff = 1.3
        header_scale = 1.3
        header_up_offset = 1.2
        header_points_buff = 0.95
        points_text_scale = 0.85

        title = TextMobject("Ways of Tracking Your Identity")
        title.scale(1.4)
        title.generate_target()
        title.target.to_edge(UP)
        title.target.scale(0.9)

        main_points = [
            ["1)  ", "IP Address"],
            ["2)  ", "Cookies and Tracking Scripts"],
            ["3)  ", "HTTP Referrer"],
            ["4) ", "Super Cookies"],
            ["5) ", "User Agent"],
        ]

        main_points = VGroup(*[TextMobject(*i) for i in main_points])
        main_points.next_to(
            title.target.get_bottom() + DOWN * main_point_title_buff,
        )
        main_points.arrange(
            DOWN,
            center=False,
            aligned_edge=LEFT,
            buff=main_point_buff,
        )
        main_points.to_edge(LEFT)
        main_points.save_state()

        self.play(FadeInFromDown(title))  # Write and move title
        self.play(MoveToTarget(title))
        self.play(FadeInFrom(main_points, RIGHT))

        def gen_target_and_move(header, points):
            main_points.generate_target()
            main_points.target.shift(LEFT).set_opacity(0)
            header.generate_target()
            header.target.move_to(ORIGIN + UP * header_up_offset)
            header.target.scale(header_scale).set_color(ORANGE)
            points.next_to(
                header.target,
                DOWN,
                buff=LARGE_BUFF * header_points_buff,
            )
            self.play(
                MoveToTarget(main_points),
                MoveToTarget(header),
                FadeInFromDown(points),
            )
            self.play(Restore(main_points), FadeOutAndShiftDown(points))

        def get_vg_from_para_list(para_list):
            vg = VGroup(*[TextMobject(i) for i in para_list])
            vg.arrange(
                DOWN,
                center=True,
                aligned_edge=LEFT,
                buff=SMALL_BUFF * 2,
            )
            return vg.scale(points_text_scale)

        IP_Address_point = get_vg_from_para_list(
            [
                "IP(Internet Protocol) Address is a unique address of your network",  # noqa: E501
                "on the internet all devices in the same network have the same ",  # noqa: E501
                "IP address. It can be used to get your geographical location.",  # noqa: E501
            ]
        )

        cookies_points = [
            [
                [
                    r"1) First Party Cookies: ",
                    r"$\hspace{1em}$Cookies made and used by a website you",
                ],
                [
                    r"$\hspace{1em}$frequently visit, that contain data such as login information."  # noqa: E501
                ],
            ],
            [
                [
                    r"2) Third Party Cookies: ",
                    r"$\hspace{1em}$Cookies used by other websites that collect",  # noqa: E501
                ],
                [
                    r"$\hspace{1em}$information such as search history to serve you personalized ads."  # noqa: E501
                ],
            ],
        ]
        outer_vg_list = []
        for i in cookies_points:
            inner_vg_list = []
            for j in i:
                text = TextMobject(*j).scale(points_text_scale)
                if len(j) > 1:
                    text[0].scale(1.1).set_color(YELLOW)
                inner_vg_list.append(text)
            outer_vg_list.append(
                VGroup(*inner_vg_list).arrange(
                    DOWN,
                    center=False,
                    aligned_edge=LEFT,
                    buff=SMALL_BUFF * 2,
                )
            )
        cookies_points = VGroup(*outer_vg_list).arrange(
            DOWN,
            center=False,
            aligned_edge=LEFT,
            buff=LARGE_BUFF,
        )

        HTTP_Referrer_points = get_vg_from_para_list(
            [
                "It is an HTTP header field which links to the URL of the website",  # noqa: E501
                "the user is coming from. By checking the HTTP referrer the website ",  # noqa: E501
                "can know where the request originated form and the IP Address",  # noqa: E501
                "of the user. a website can pass login information to a linked site ",  # noqa: E501
                "using the HTTP referrer.",
            ]
        )
        Super_Cookie_points = get_vg_from_para_list(
            [
                "These are a variety of cookies that back even after being deleted",  # noqa: E501
                "they might be stored in many different places such as in the flash",  # noqa: E501
                "cookies (RIP Flash Player 1995-2020), HTML5 storage,",
                "Browsing history etc",
            ]
        )
        UserAgent_points = get_vg_from_para_list(
            [
                "When a user connects to a website, the browser sends a User Agent",  # noqa: E501
                "to the website. this contains information about the user's Operating",  # noqa: E501
                "System, and information about the browser. This can also be used to",  # noqa: E501
                "track a user and serve him personalised ads.",
            ]
        )
        for index, points in enumerate(
            [
                IP_Address_point,
                cookies_points,
                HTTP_Referrer_points,
                Super_Cookie_points,
                UserAgent_points,
            ]
        ):
            gen_target_and_move(main_points[index][1], points)

        self.play(
            *[FadeOutAndShiftDown(i) for i in main_points],
            FadeOutAndShiftDown(title),
        )
