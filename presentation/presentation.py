from manim import *


class main_presentation(Scene):
    default_wait_constant = 1.5
    default_animation_time = 1

    # Font sizes
    TITLE_FONT_SIZE = 32
    SUBTITLE_FONT_SIZE = 26
    NORMAL_FONT_SIZE = 20

    # Number to Colours
    num2colour_fill = {
        0: BLACK,
        1: BLUE_E,
        2: PURE_RED,
        3: PURE_GREEN,
        4: YELLOW,
        5: GREY,
        6: PINK,
        7: ORANGE,
        8: BLUE_A,
        9: PURPLE,
        10: YELLOW_E,
    }
    num2colour_stroke = {
        0: WHITE,
        1: BLUE_E,
        2: PURE_RED,
        3: PURE_GREEN,
        4: YELLOW,
        5: GREY,
        6: PINK,
        7: ORANGE,
        8: BLUE_A,
        9: PURPLE,
        10: YELLOW_E,
    }

    def construct(self):
        # Slide: title and team presentation
        title_first_slide = Text(
            "Google Code Golf Competition", font_size=self.TITLE_FONT_SIZE
        ).to_edge(UP)
        self.play(Write(title_first_slide), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)
        self.presentation_team(title_first_slide)

        # Slide: challenge presentation
        self.challenge_presentation(title_first_slide)

        # Slide: what we do
        self.what_we_do(title_first_slide)

        # Slide: Example of very easy problem
        subtitle = Text(
            "Problem 116: Easy", font_size=self.SUBTITLE_FONT_SIZE, color=GREEN
        ).next_to(title_first_slide, DOWN)
        self.play(Write(subtitle), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        input = [[4, 1, 1, 4], [1, 1, 1, 1], [4, 4, 4, 1]]
        output = [
            [4, 4, 4, 1],
            [1, 1, 1, 1],
            [4, 1, 1, 4],
            [4, 1, 1, 4],
            [1, 1, 1, 1],
            [4, 4, 4, 1],
        ]
        code = """p=lambda j:j[::-1]+j"""
        self.problem_representation_with_code(input, output, code)

        # Slide: Example of medium problem
        subtitle_new = Text(
            "Problem 190: Medium", font_size=self.SUBTITLE_FONT_SIZE, color=ORANGE
        ).next_to(title_first_slide, DOWN)
        self.play(
            ReplacementTransform(subtitle, subtitle_new),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)
        subtitle = subtitle_new

        input = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        output = [
            [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        code = r"""import re
p=lambda i:exec(r"i[::-1]=zip(*eval(re.sub('.{31}0, ([^0])'*2,r'|\1\g<0>',str(i))));"*20)or i"""
        self.problem_representation_with_code(
            input, output, code, size_square=0.35, scale_code=0.7
        )

        # Slide: Example of very hard problem
        subtitle_new = Text(
            "Problem 18: Hard", font_size=self.SUBTITLE_FONT_SIZE, color=RED
        ).next_to(title_first_slide, DOWN)
        self.play(
            ReplacementTransform(subtitle, subtitle_new),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)
        subtitle = subtitle_new
        input = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 8, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
            [0, 0, 8, 4, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        output = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 4, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 8, 8, 8, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        code = r"""#coding:L1
import zlib
exec(zlib.decompress(bytes(
"�PU^!�Na;�v+^��-e�m{w��'��ש�c-n���.L����Fc�l��X�c�Qt��<��S�s�[JC�
�����fO�i�G����=��V�~OW{ja;ʴd@�e:X.�$s�J�i��O���e��b","L1"),~9))"""
        self.problem_representation_with_code(
            input, output, code, size_square=0.17, scale_code=0.65
        )

        # Slide: definition of AGI
        subtitle_agi = Text(
            "ARC-AGI: The Benchmark", font_size=self.SUBTITLE_FONT_SIZE, color=BLUE
        ).next_to(title_first_slide, DOWN)
        self.play(
            ReplacementTransform(subtitle, subtitle_agi),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)
        subtitle = subtitle_agi

        agi_initial = Text("AGI", font_size=80).move_to(ORIGIN)
        self.play(Write(agi_initial), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(FadeOut(agi_initial), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # Slide: Problem example 330
        subtitle_new = Text(
            "Problem example 330", font_size=self.SUBTITLE_FONT_SIZE, color=BLUE
        ).next_to(title_first_slide, DOWN)
        self.play(
            ReplacementTransform(subtitle, subtitle_new),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)
        subtitle = subtitle_new

        input = [
            [5, 5, 5, 0, 0, 0, 0, 5, 5, 5],
            [0, 5, 5, 0, 5, 5, 0, 5, 0, 0],
            [0, 0, 5, 0, 5, 5, 0, 5, 0, 0],
            [0, 0, 5, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 5, 5, 0, 0, 0, 5],
            [0, 5, 5, 0, 0, 5, 5, 0, 0, 5],
            [0, 0, 0, 0, 0, 5, 5, 0, 0, 5],
            [0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 5, 5, 5, 0, 0, 0, 0, 0],
            [0, 0, 5, 5, 0, 0, 0, 0, 0, 0],
        ]
        output = [
            [1, 1, 1, 0, 0, 0, 0, 2, 2, 2],
            [0, 1, 1, 0, 1, 1, 0, 2, 0, 0],
            [0, 0, 1, 0, 1, 1, 0, 2, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 2, 2, 0, 0, 0, 1],
            [0, 1, 1, 0, 0, 2, 2, 0, 0, 1],
            [0, 0, 0, 0, 0, 2, 2, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        ]
        self.problem_representation(
            input,
            output,
            title=subtitle,
            size_square=0.45,
        )

        # Slide: Classical approach with Dijkstra
        subtitle_new = Text(
            "Problem example 330 - standard approach",
            font_size=self.SUBTITLE_FONT_SIZE,
            color=BLUE,
        ).next_to(title_first_slide, DOWN)
        self.play(
            ReplacementTransform(subtitle, subtitle_new),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)
        subtitle = subtitle_new

        self.classical_approach(input, output, title=subtitle, size_square=0.45)

        # Slide: Code golf approach
        subtitle_new = Text(
            "Problem example 330 - code golf approach",
            font_size=self.SUBTITLE_FONT_SIZE,
            color=BLUE,
        ).next_to(title_first_slide, DOWN)
        self.play(
            ReplacementTransform(subtitle, subtitle_new),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)
        subtitle = subtitle_new

        # Original input
        input_matrix = self.draw_matrix(input, size_square=0.5)
        input_matrix.next_to(subtitle, DOWN)
        self.play(Create(input_matrix), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)
        self.play(Uncreate(input_matrix))

        # Code explanation on simple example
        input = [[5, 5, 0], [0, 5, 0], [0, 0, 5]]
        self.code_golf_approach(input, output, title=subtitle, size_square=1.8)

        # Slide: definition of AGI
        subtitle_agi = Text(
            "ARC-AGI: The Benchmark", font_size=self.SUBTITLE_FONT_SIZE, color=BLUE
        ).next_to(title_first_slide, DOWN)
        self.play(
            ReplacementTransform(subtitle, subtitle_agi),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)
        subtitle = subtitle_agi

        agi_initial = Text("AGI", font_size=80).move_to(ORIGIN)
        self.play(Write(agi_initial), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        agi_vertical = (
            VGroup(
                Text("A", font_size=70),
                Text("G", font_size=70),
                Text("I", font_size=70),
            )
            .arrange(DOWN, buff=0.5)
            .move_to(ORIGIN)
            .shift(5 * LEFT)
        )

        self.play(
            ReplacementTransform(agi_initial, agi_vertical),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)

        # Expand A -> Artificial
        word1 = Text("Artificial", font_size=70)
        word1.shift(agi_vertical[0].get_center() - word1[0].get_center())
        self.play(
            ReplacementTransform(agi_vertical[0], word1[0]),
            Write(word1[1:]),
            runtime=self.default_animation_time,
        )
        self.wait(0.5 * self.default_wait_constant)

        # Expand G -> General
        word2 = Text("General", font_size=70)
        word2.shift(agi_vertical[1].get_center() - word2[0].get_center())
        self.play(
            ReplacementTransform(agi_vertical[1], word2[0]),
            Write(word2[1:]),
            runtime=self.default_animation_time,
        )
        self.wait(0.5 * self.default_wait_constant)

        # Expand I -> Intelligence
        word3 = Text("Intelligence", font_size=70)
        word3.shift(agi_vertical[2].get_center() - word3[0].get_center())
        self.play(
            ReplacementTransform(agi_vertical[2], word3[0]),
            Write(word3[1:]),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)

        # Adjectives
        adjectives = (
            VGroup(
                Text("Knowledge", font_size=40),
                Text("Reasoning", font_size=40),
                Text("Correctness", font_size=40),
                Text("Creativity", font_size=40),
                Text("...", font_size=40),
            )
            .arrange(DOWN, buff=0.5)
            .next_to(word3, RIGHT, buff=1)
        )

        self.play(Write(adjectives), runtime=self.default_animation_time)

        # Arrows
        arrows = VGroup()
        for i in range(len(adjectives) - 1):
            arrow = Arrow(
                word3.get_right(),
                adjectives[i].get_left(),
                buff=0.1,
                stroke_width=2,
                tip_length=0.2,
                color=WHITE,
            )
            arrows.add(arrow)

        self.play(Create(arrows), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        new_adj = Text("Necessity", font_size=40).move_to(adjectives[3].get_center())
        self.play(ApplyWave(adjectives[3]), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant * 0.5)
        self.play(
            ReplacementTransform(adjectives[3], new_adj),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)

        self.play(
            FadeOut(word1),
            FadeOut(word2),
            FadeOut(word3),
            FadeOut(adjectives),
            FadeOut(arrows),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)

        ## Conclusion slide
        self.play(ApplyWave(title_first_slide), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        thanks = Text("Thank you!", font_size=70).move_to(ORIGIN)
        self.play(Write(thanks), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.wait(4 * self.default_wait_constant)

    #########################################
    # Presentation team
    #########################################
    def presentation_team(self, title: Mobject) -> None:
        names = ["Massimiliano", "Alessandro", "Osea", "Alessandro", "Paolo"]
        surnames = ["Ghiotto", "Daldossi", "Fracchia", "Ghiotto", "Bignardi"]
        images_files = ["max.png", "ale_daldox.png", "osea.png", "ale.png", "paolo.png"]

        # Team
        team_name = Text("NeedAJob", font_size=self.SUBTITLE_FONT_SIZE).next_to(
            title, DOWN
        )
        self.play(Write(team_name), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # First line of photos
        photos = Group()
        photos_animation = []

        for i in range(3):
            figure = ImageMobject(f"images/{images_files[i]}").set_height(1.8)

            name = Text(names[i], font_size=self.NORMAL_FONT_SIZE).next_to(figure, DOWN)
            surname = Text(surnames[i], font_size=self.NORMAL_FONT_SIZE).next_to(
                name, DOWN
            )

            person = Group(figure, name, surname)

            photos.add(person)
            photos_animation += [
                FadeIn(figure),
                Write(name),
                Write(surname),
            ]

        photos.arrange(RIGHT, buff=1.25).next_to(team_name, DOWN)
        photos[-1].shift(0.4 * RIGHT)
        # self.play(
        #     Create(photos.scale(0.5), runtime=self.default_animation_time),
        #     runtime=5 * self.default_animation_time,
        # )
        self.play(
            LaggedStart(*photos_animation, lag_ration=0.4),
            runtime=self.default_animation_time * 1.5,
        )

        # Second line of photos
        second_photos = Group()
        second_photos_animation = []
        for i in range(3, 5):
            figure = ImageMobject(f"images/{images_files[i]}").set_height(1.8)
            name = Text(names[i], font_size=self.NORMAL_FONT_SIZE).next_to(figure, DOWN)
            surname = Text(surnames[i], font_size=self.NORMAL_FONT_SIZE).next_to(
                name, DOWN
            )

            person = Group(figure, name, surname)

            second_photos.add(person)

            second_photos_animation += [
                FadeIn(figure),
                Write(name),
                Write(surname),
            ]

        second_photos.arrange(RIGHT, buff=1.35).next_to(photos, DOWN)
        # self.play(
        #     Create(
        #         second_photos,
        #         runtime=self.default_animation_time,
        #     ),
        #     runtime=5 * self.default_animation_time,
        # )
        self.play(
            LaggedStart(*second_photos_animation, lag_ratio=0.4),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_animation_time)

        # Make all the stuff disappear
        all_mobj = list(second_photos)[::-1] + list(photos)[::-1] + [team_name]
        self.play(LaggedStartMap(FadeOut, all_mobj))
        self.wait(self.default_wait_constant)
        return

    #########################################
    # Presentation challenge
    #########################################
    def challenge_presentation(self, title: Mobject) -> None:
        # Subtitle
        subtitle = Text(
            "Challenge: 400 problems", font_size=self.SUBTITLE_FONT_SIZE
        ).next_to(title, DOWN)
        self.play(Write(subtitle), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # Example problem animation
        input = [
            [5] * 10,
            [5, 5] + [4] * 6 + [5, 5],
            [5, 5] + [4] * 6 + [5, 5],
            [5] * 10,
            [5] * 10,
            [5] * 2 + [4] * 5 + [5] * 3,
            [5] * 2 + [4] + [5] * 3 + [4] + [5] * 3,
            [5] * 2 + [4] + [5] * 3 + [4] + [5] * 3,
            [5] * 2 + [4] * 5 + [5] * 3,
            [5] * 10,
        ]
        output = [
            [5] * 10,
            [5, 5] + [4] * 6 + [5, 5],
            [5, 5] + [4] * 6 + [0, 5],
            [5] * 3 + [0] * 6 + [5],
            [5] * 10,
            [5] * 2 + [4] * 5 + [5] * 3,
            [5] * 2 + [4] + [0] * 3 + [4] + [0, 5, 5],
            [5] * 2 + [4] + [0, 5, 5] + [4] + [0, 5, 5],
            [5] * 2 + [4] * 5 + [0] + [5] * 2,
            [5] * 3 + [0] * 5 + [5, 5],
        ]
        input_matrix = self.draw_matrix(input)
        output_matrix = self.draw_matrix(output).next_to(input_matrix, RIGHT, buff=2)
        arrow = Arrow(
            input_matrix.get_edge_center(RIGHT),
            output_matrix.get_edge_center(LEFT),
            buff=0.1,
            stroke_width=2,
            tip_length=0.15,
        )
        all_stuff = VGroup(input_matrix, arrow, output_matrix).next_to(subtitle, DOWN)
        input_matrix, arrow, output_matrix = all_stuff

        self.play(Create(input_matrix), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(GrowArrow(arrow), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(Create(output_matrix), runtime=2 * self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(LaggedStartMap(Uncreate, all_stuff))
        self.wait(self.default_wait_constant)

        # Standard code for solve it
        code = """def p(g):
  for r, row in enumerate(g):
    for c, color in enumerate(row):
      if r and c and color==5 and g[r-1][c-1] not in [0,5]:
        g[r][c]=0
  return g    
"""
        rendered_code = Code(
            code_string=code,
            language="python",
            tab_width=2,
            background="window",
            background_config={"stroke_color": "white"},
        )
        self.play(Write(rendered_code), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # Code Golf code
        golf_code = """p=lambda g,h=[]:g*0!=0and[*map(p,g,g[9:]+h+g)]or(g%6<=h%6)*g"""
        rendered_golf_code = Code(
            code_string=golf_code,
            language="python",
            tab_width=2,
            background="window",
            background_config={"stroke_color": "white"},
        )
        rendered_golf_code.next_to(rendered_code, DOWN)
        self.play(Write(rendered_golf_code), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(
            LaggedStartMap(
                FadeOut, VGroup(rendered_code, rendered_golf_code, subtitle)
            ),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)

        return

    #########################################
    # What we do slide
    #########################################
    def what_we_do(self, title: Mobject) -> None:
        subtitle = Text(
            "What we have done", font_size=self.SUBTITLE_FONT_SIZE, color=BLUE
        ).next_to(title, DOWN)
        self.play(Write(subtitle), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        items = [
            "Learn basic golfing tricks",
            "Automated workflow for golfing with LLMs",
            "Zipping tricks",
            "Study regex",
            "Script for full automation",
        ]

        bullet_list = VGroup()
        for item in items:
            dot = Dot(color=MAIN_COLOR if "MAIN_COLOR" in dir(self) else WHITE)
            text = Text(item, font_size=self.NORMAL_FONT_SIZE)
            if len(item) > 50:
                text = Text(item, font_size=self.NORMAL_FONT_SIZE * 0.7)

            line = VGroup(dot, text).arrange(RIGHT, buff=0.3)
            bullet_list.add(line)

        bullet_list.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        bullet_list.next_to(subtitle, DOWN, buff=0.7)

        self.play(
            LaggedStart(
                *[
                    AnimationGroup(FadeIn(line[0]), Write(line[1]))
                    for line in bullet_list
                ],
                lag_ratio=0.5,
            ),
            runtime=self.default_animation_time * 2,
        )
        self.wait(self.default_wait_constant)

        self.play(FadeOut(subtitle), FadeOut(bullet_list))
        self.wait(self.default_wait_constant)

        return

    #########################################
    # Problem representation
    #########################################
    def problem_representation(
        self, input=list[list], output=list[list], title=None, size_square: float = 1.0
    ) -> None:
        """
        Routine to represent input/output
        """
        # Create objects
        input_matrix = self.draw_matrix(input, size_square=size_square)
        output_matrix = self.draw_matrix(output, size_square=size_square).next_to(
            input_matrix, RIGHT, buff=2
        )

        arrow = Arrow(
            input_matrix.get_edge_center(RIGHT),
            output_matrix.get_edge_center(LEFT),
            buff=0.1,
            stroke_width=4,
            tip_length=0.25,
        )
        all_stuff = VGroup(input_matrix, arrow, output_matrix).move_to(ORIGIN)

        if title:
            all_stuff.next_to(title, DOWN)

        input_matrix, arrow, output_matrix = all_stuff

        # Animate objects
        self.play(Create(input_matrix), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(GrowArrow(arrow), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(Create(output_matrix), runtime=2 * self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(LaggedStartMap(Uncreate, all_stuff))
        self.wait(self.default_wait_constant)

        return

    #########################################
    # Problem representation with code
    #########################################
    def problem_representation_with_code(
        self,
        input=list[list],
        output=list[list],
        code=str,
        size_square: float = 0.5,
        scale_code: float = 1.0,
    ) -> None:
        """
        Routine to represent input/output with code
        """
        # Create objects
        input_matrix = self.draw_matrix(input, size_square=size_square)
        output_matrix = self.draw_matrix(output, size_square=size_square).next_to(
            input_matrix, RIGHT, buff=2
        )
        arrow = Arrow(
            input_matrix.get_edge_center(RIGHT),
            output_matrix.get_edge_center(LEFT),
            buff=0.1,
            stroke_width=4,
            tip_length=0.25,
        )
        all_stuff = VGroup(input_matrix, arrow, output_matrix).move_to(ORIGIN)
        input_matrix, arrow, output_matrix = all_stuff

        # Animate objects
        self.play(Create(input_matrix), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(GrowArrow(arrow), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(Create(output_matrix), runtime=2 * self.default_animation_time)
        self.wait(self.default_wait_constant)

        rendered_code = Code(
            code_string=code,
            language="python",
            tab_width=2,
            background="window",
            background_config={"stroke_color": "white"},
        ).scale(scale_code)
        rendered_code.next_to(output_matrix, DOWN).set_x(0)
        self.play(Write(rendered_code), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(LaggedStartMap(Uncreate, all_stuff))
        self.play(FadeOut(rendered_code))
        self.wait(self.default_wait_constant)

        return

    #########################################
    # Classical approach for problem 330
    #########################################
    def classical_approach(
        self,
        input: list[list],
        output: list[list],
        title: Text,
        size_square: float = 0.5,
    ):
        """
        Routine that represent the classical approach with DFS/BFS
        """
        input_matrix = self.draw_matrix(input, size_square=size_square)

        if title:
            input_matrix.next_to(title, DOWN)

        self.play(Create(input_matrix), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # input_new = input.copy()
        # input_new[0][0] = 10
        # input_matrix_new = self.draw_matrix(input_new, size_square=size_square)
        # if title:
        #     input_matrix.next_to(title, DOWN)
        # self.play(
        #     ReplacementTransform(input_matrix, input_matrix_new),
        #     runtime=self.default_animation_time,
        # )
        # self.wait(self.default_wait_constant)
        # input = input_new
        # input_matrix = input_matrix_new

        # First block
        self.play(
            input_matrix[0][0]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            input_matrix[0][1]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            input_matrix[0][2]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            input_matrix[1][2]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            input_matrix[2][2]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            input_matrix[3][2]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            input_matrix[1][1]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            LaggedStart(
                [
                    input_matrix[0][0]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[0][1]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[1][1]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[0][2]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[1][2]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[2][2]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[3][2]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                ]
            ),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)

        # Second block
        self.play(
            input_matrix[0][7]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.play(
            input_matrix[0][8]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.play(
            input_matrix[0][9]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.play(
            input_matrix[1][7]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.play(
            input_matrix[2][7]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.play(
            input_matrix[3][7]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.5,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            LaggedStart(
                [
                    input_matrix[0][7]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                    input_matrix[0][8]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                    input_matrix[0][9]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                    input_matrix[1][7]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                    input_matrix[2][7]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                    input_matrix[3][7]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                ]
            ),
            runtime=self.default_animation_time,
        )

        # Third block
        self.play(
            input_matrix[1][4]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[1][5]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[2][5]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[2][4]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            LaggedStart(
                [
                    input_matrix[1][4]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[1][5]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[2][4]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[2][5]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                ]
            ),
            runtime=self.default_animation_time,
        )

        # Fourth block
        self.play(
            input_matrix[4][4]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[4][5]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[5][5]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[5][6]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[6][6]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[6][5]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            LaggedStart(
                [
                    input_matrix[4][4]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                    input_matrix[4][5]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                    input_matrix[5][5]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                    input_matrix[5][6]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                    input_matrix[6][5]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                    input_matrix[6][6]
                    .animate.set_fill(self.num2colour_fill[2], opacity=1)
                    .set_stroke(self.num2colour_stroke[2], width=1),
                ]
            ),
            runtime=self.default_animation_time,
        )

        # Fifth block
        self.play(
            input_matrix[4][9]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[5][9]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[6][9]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            LaggedStart(
                [
                    input_matrix[4][9]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[5][9]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[6][9]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                ]
            ),
            runtime=self.default_animation_time,
        )

        # Sixth block
        self.play(
            input_matrix[5][1]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[5][2]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            LaggedStart(
                [
                    input_matrix[5][1]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[5][2]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                ]
            ),
            runtime=self.default_animation_time,
        )

        # Seventh block
        self.play(
            input_matrix[7][2]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[8][2]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[8][3]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[8][4]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[8][1]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[9][2]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.play(
            input_matrix[9][3]
            .animate.set_fill(self.num2colour_fill[10], opacity=1)
            .set_stroke(self.num2colour_stroke[10], width=1),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.5)

        self.play(
            LaggedStart(
                [
                    input_matrix[7][2]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[8][1]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[8][2]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[8][3]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[9][2]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[8][4]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                    input_matrix[9][3]
                    .animate.set_fill(self.num2colour_fill[1], opacity=1)
                    .set_stroke(self.num2colour_stroke[1], width=1),
                ]
            ),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)

        # Remove matrix
        self.play(FadeOut(input_matrix), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # Add code
        code = """def p(g,R=range(10)):
  def f(i,j,m):
  k=1
  for x,y in(1,0),(-1,0),(0,1),(0,-1):
    if 10>(x:=i+x)>-1<(y:=j+y)<10 and m[x][y]>4:
      m[x][y]=-1;k+=f(x,y,m)
  return k
  return[[g[i][j]and(f(i,j,[*map(list,g)])==7)+1
    for j in R]for i in R]
"""
        rendered_code = Code(
            code_string=code,
            language="python",
            tab_width=2,
            background="window",
            background_config={"stroke_color": "white"},
        )
        self.play(Write(rendered_code), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # Add comment
        comment = Text("Lot of code here!").next_to(rendered_code, DOWN)
        self.play(Write(comment), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # Remove all
        self.play(FadeOut(rendered_code), runtime=self.default_animation_time)
        self.play(FadeOut(comment), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        return

    #########################################
    # Code golf approach for problem 330
    #########################################
    def code_golf_approach(
        self, input, output, title: str = "", size_square: float = 0.5
    ):
        input_matrix = self.draw_matrix(input, size_square=size_square)

        if title:
            input_matrix.next_to(title, 2 * DOWN)

        self.play(Create(input_matrix), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # ADD: power of 2s
        n_rows = len(input)
        n_cols = len(input[0])
        nums = VGroup()
        nums_list = []
        for i in range(n_rows):
            row = VGroup()
            row_list = []
            for j in range(n_cols):
                num = MathTex(
                    rf"2^{{{i*n_rows + j}}}",
                    font_size=self.SUBTITLE_FONT_SIZE,
                )
                num.move_to(input_matrix[i][j].get_center())
                row.add(num)
                row_list.append(num)
            nums.add(row)
            nums_list.append(row_list)

        self.play(Write(nums), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        #### Sliding window
        for i in range(n_rows):
            for j in range(n_cols - 1):
                # Select
                self.play(
                    input_matrix[i][j].animate.set_stroke(YELLOW_E, width=3),
                    input_matrix[i][j + 1].animate.set_stroke(YELLOW_E, width=3),
                    runtime=self.default_animation_time * 0.75,
                )
                self.wait(self.default_wait_constant * 0.5)

                # Or
                if input[i][j] == 5 and input[i][j + 1] == 5:
                    num = MathTex(
                        rf"2^{0} | 2^{1}",
                        font_size=self.SUBTITLE_FONT_SIZE,
                    ).move_to(nums[i][j + 1].get_center())
                    self.play(
                        ReplacementTransform(nums[i][j + 1], num),
                        runtime=self.default_animation_time,
                    )
                    self.wait(self.default_wait_constant)

                    num = MathTex(
                        rf"2^{0} + 2^{1}",
                        font_size=self.SUBTITLE_FONT_SIZE,
                    ).move_to(nums[i][j + 1].get_center())
                    self.play(
                        ReplacementTransform(nums[i][j + 1], num),
                        runtime=self.default_animation_time,
                    )
                    self.wait(self.default_wait_constant)
                    nums_list[i][j + 1] = num

                # Deselect
                self.play(
                    input_matrix[i][j].animate.set_stroke(
                        self.num2colour_stroke[input[i][j]], width=1
                    ),
                    input_matrix[i][j + 1].animate.set_stroke(
                        self.num2colour_stroke[input[i][j + 1]], width=1
                    ),
                    runtime=self.default_animation_time * 0.75,
                )
                self.wait(self.default_wait_constant * 0.5)

        #### Rotation
        nums, nums_list, input, input_matrix = self.rotate_matrix(
            input=input,
            nums_list=nums_list,
            input_matrix=input_matrix,
            title=title,
            size_square=size_square,
        )

        #### Sliding window
        for i in range(n_rows):
            for j in range(n_cols - 1):
                # Select
                self.play(
                    input_matrix[i][j].animate.set_stroke(YELLOW_E, width=3),
                    input_matrix[i][j + 1].animate.set_stroke(YELLOW_E, width=3),
                    runtime=self.default_animation_time * 0.35,
                )
                self.wait(self.default_wait_constant * 0.1)

                # Or
                if input[i][j] == 5 and input[i][j + 1] == 5:
                    num = MathTex(
                        rf"2^{0} + 2^{1} + 2^{4}",
                        font_size=self.SUBTITLE_FONT_SIZE,
                    ).move_to(nums[i][j + 1].get_center())
                    self.play(
                        ReplacementTransform(nums[i][j + 1], num),
                        runtime=self.default_animation_time,
                    )
                    self.wait(self.default_wait_constant)
                    nums_list[i][j + 1] = num

                # Deselect
                self.play(
                    input_matrix[i][j].animate.set_stroke(
                        self.num2colour_stroke[input[i][j]], width=1
                    ),
                    input_matrix[i][j + 1].animate.set_stroke(
                        self.num2colour_stroke[input[i][j + 1]], width=1
                    ),
                    runtime=self.default_animation_time * 0.35,
                )
                self.wait(self.default_wait_constant * 0.1)

        #### Rotation
        nums, nums_list, input, input_matrix = self.rotate_matrix(
            input=input,
            nums_list=nums_list,
            input_matrix=input_matrix,
            title=title,
            size_square=size_square,
        )

        #### Change values
        nums_list, nums = self.sliding_window(
            string="2^{0} + 2^{1} + 2^{4}",
            input=input,
            nums=nums,
            nums_list=nums_list,
            input_matrix=input_matrix,
        )

        #### Rotation
        nums, nums_list, input, input_matrix = self.rotate_matrix(
            input=input,
            nums_list=nums_list,
            input_matrix=input_matrix,
            title=title,
            size_square=size_square,
        )

        #### Change values
        nums_list, nums = self.sliding_window(
            string="2^{0} + 2^{1} + 2^{4}",
            input=input,
            nums=nums,
            nums_list=nums_list,
            input_matrix=input_matrix,
        )

        #### Rotation
        nums, nums_list, input, input_matrix = self.rotate_matrix(
            input=input,
            nums_list=nums_list,
            input_matrix=input_matrix,
            title=title,
            size_square=size_square,
        )

        #### Count the bit
        num = MathTex("3", font_size=self.SUBTITLE_FONT_SIZE).move_to(
            nums[0][0].get_center()
        )
        self.play(
            ReplacementTransform(nums[0][0], num),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.3)
        nums_list[0][0] = num

        #
        num = MathTex("3", font_size=self.SUBTITLE_FONT_SIZE).move_to(
            nums[0][1].get_center()
        )
        self.play(
            ReplacementTransform(nums[0][1], num),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.3)
        nums_list[0][1] = num

        #
        num = MathTex("1", font_size=self.SUBTITLE_FONT_SIZE).move_to(
            nums[0][2].get_center()
        )
        self.play(
            ReplacementTransform(nums[0][2], num),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.3)
        nums_list[0][2] = num

        #
        num = MathTex("1", font_size=self.SUBTITLE_FONT_SIZE).move_to(
            nums[1][0].get_center()
        )
        self.play(
            ReplacementTransform(nums[1][0], num),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.3)
        nums_list[1][0] = num

        #
        num = MathTex("3", font_size=self.SUBTITLE_FONT_SIZE).move_to(
            nums[1][1].get_center()
        )
        self.play(
            ReplacementTransform(nums[1][1], num),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.3)
        nums_list[1][1] = num

        #
        num = MathTex("1", font_size=self.SUBTITLE_FONT_SIZE).move_to(
            nums[1][2].get_center()
        )
        self.play(
            ReplacementTransform(nums[1][2], num),
            runtime=self.default_animation_time * 0.3,
        )
        self.wait(self.default_wait_constant * 0.3)
        nums_list[1][2] = num

        #
        for i in range(3):
            num = MathTex("1", font_size=self.SUBTITLE_FONT_SIZE).move_to(
                nums[2][i].get_center()
            )
            self.play(
                ReplacementTransform(nums[2][i], num),
                runtime=self.default_animation_time * 0.3,
            )
            self.wait(self.default_wait_constant * 0.3)
            nums_list[2][i] = num

        #### Recoloring
        for i in range(3):
            for j in range(3):
                self.play(
                    Unwrite(nums_list[i][j]), runtime=self.default_animation_time * 0.3
                )
                self.play(
                    input_matrix[i][j]
                    .animate.set_stroke(
                        self.num2colour_stroke[input[i][j] == 5], width=1
                    )
                    .set_fill(self.num2colour_fill[input[i][j] == 5], opacity=1),
                    runtime=self.default_animation_time * 0.3,
                )
                self.wait(self.default_wait_constant * 0.3)

        self.wait(self.default_wait_constant)

        # Remove grid
        self.play(Unwrite(input_matrix), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # Add code
        code = """p=lambda d,t=23,l=0:-t*d or 
  p([[[[(h:=a>0)*b|a,1<<(l:=l+1)][a%2],h+(a.bit_count()==6)][t<1]
  for a,b in zip(r,[0]+r)]for*r,in zip(*d[::-1])],t-1)"""
        rendered_code = Code(
            code_string=code,
            language="python",
            tab_width=2,
            background="window",
            background_config={"stroke_color": "white"},
        )
        if title:
            rendered_code.next_to(title, 1.5 * DOWN)
        self.play(Write(rendered_code), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # Add more golfed code
        code_2 = """p=lambda g,k=11,l=5:-k*g or 
  p([(b:=1)*[b:=a%~a&[b|a|(l:=l*8),2-a**6%7][k<1]for a in r]
  for r in zip(*g[::-1])],k-1,0)"""
        rendered_code_2 = Code(
            code_string=code_2,
            language="python",
            tab_width=2,
            background="window",
            background_config={"stroke_color": "white"},
        )
        rendered_code_2.next_to(rendered_code, 1.5 * DOWN)
        self.play(Write(rendered_code_2), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        self.play(FadeOut(rendered_code), FadeOut(rendered_code_2))
        self.wait(self.default_wait_constant)

        return

    #########################################
    # Utility for the code golf approach: rotate matrix
    #########################################
    def rotate_matrix(
        self,
        input: list[list],
        nums_list: list[list],
        input_matrix: Mobject,
        title: Mobject = None,
        size_square: float = 0.5,
    ) -> tuple[list[list], Mobject, list[list], Mobject]:
        """
        Animation for the rotation of the matrix and the values, for the code golf approach
        """
        # Matrix
        input = [[*r] for r in zip(*input[::-1])]
        input_matrix_new = self.draw_matrix(input, size_square=size_square)
        if title:
            input_matrix_new.next_to(title, 2 * DOWN)

        # Values
        nums_list = [[*r] for r in zip(*nums_list[::-1])]
        new_nums = VGroup(*[VGroup(*r) for r in nums_list])

        # Animation
        animations = [ReplacementTransform(input_matrix, input_matrix_new)]
        for i in range(len(nums_list)):
            for j in range(len(nums_list[0])):
                animations.append(
                    nums_list[i][j].animate.move_to(input_matrix_new[i][j].get_center())
                )

        self.play(
            *animations,
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)
        nums = new_nums
        input_matrix = input_matrix_new

        return nums, nums_list, input, input_matrix

    #########################################
    # Utility for the code golf approach: sliding window
    #########################################
    def sliding_window(
        self,
        string: str,
        input: Mobject,
        nums: Mobject,
        nums_list: list[list],
        input_matrix: Mobject,
    ) -> tuple[list[list], Mobject]:
        """
        Animation for the change of the values (without sliding window for velocity)
        """
        for i in range(len(nums_list)):
            for j in range(len(nums_list[0]) - 1):
                # Change the value
                if input[i][j] == 5 and input[i][j + 1] == 5:
                    num = MathTex(
                        rf"{string}",
                        font_size=self.SUBTITLE_FONT_SIZE,
                    ).move_to(nums[i][j + 1].get_center())
                    self.play(
                        ReplacementTransform(nums[i][j + 1], num),
                        runtime=self.default_animation_time,
                    )
                    self.wait(self.default_wait_constant)
                    nums_list[i][j + 1] = num

        return nums_list, nums

    #########################################
    # Utility: draw matrix from list of lists
    #########################################
    def draw_matrix(
        self, grid: list[list], size_square: float = 0.5, gap_const: float = 0.1
    ) -> Mobject:
        """
        Routine to represent an input
        """
        n_rows = len(grid)
        n_cols = len(grid[0])

        matrix = VGroup()
        for i in range(n_rows):
            row = VGroup()
            for j in range(n_cols):
                cell = (
                    Square(size_square)
                    .set_fill(self.num2colour_fill[grid[i][j]], opacity=1)
                    .set_stroke(self.num2colour_stroke[grid[i][j]], width=1)
                )
                row.add(cell)
            row.arrange(RIGHT, buff=gap_const)
            matrix.add(row)

        matrix.arrange(DOWN, buff=gap_const)
        return matrix
