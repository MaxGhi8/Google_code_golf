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
            "Problem 286: Medium", font_size=self.SUBTITLE_FONT_SIZE, color=ORANGE
        ).next_to(title_first_slide, DOWN)
        self.play(
            ReplacementTransform(subtitle, subtitle_new),
            runtime=self.default_animation_time,
        )
        self.wait(self.default_wait_constant)
        subtitle = subtitle_new

        input = [
            [8, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 0, 8, 8, 8, 0, 8, 8, 0, 8, 8, 8, 0],
            [0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 8, 0, 8, 0, 0, 8, 0, 8, 0],
            [8, 8, 8, 0, 8, 0, 8, 8, 8, 8, 0, 8, 8, 8, 0, 8, 0, 8, 8, 8, 8, 0, 8, 0],
            [8, 0, 0, 0, 8, 0, 8, 0, 0, 8, 0, 0, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 8, 0],
            [8, 0, 8, 8, 8, 0, 8, 8, 0, 8, 0, 8, 8, 8, 0, 8, 8, 0, 8, 8, 8, 8, 8, 0],
            [8, 0, 8, 0, 0, 0, 0, 8, 0, 8, 0, 8, 0, 0, 0, 0, 8, 0, 8, 0, 0, 0, 0, 0],
            [8, 0, 8, 8, 8, 8, 8, 8, 0, 8, 0, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 3, 2, 3, 0, 0, 0, 8, 0],
            [8, 8, 0, 8, 8, 8, 0, 8, 8, 8, 0, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 0, 8, 0],
            [0, 8, 0, 8, 0, 8, 0, 8, 0, 0, 0, 8, 0, 0, 0, 0, 8, 0, 8, 0, 8, 0, 8, 0],
            [0, 8, 8, 8, 0, 8, 8, 8, 0, 8, 8, 8, 0, 8, 8, 0, 8, 8, 8, 0, 8, 8, 8, 0],
        ]
        output = [
            [8, 3, 2, 3, 2, 3, 8, 8, 8, 8, 8, 8, 0, 8, 8, 8, 2, 8, 8, 0, 8, 8, 8, 0],
            [3, 2, 8, 8, 8, 2, 3, 2, 3, 2, 3, 8, 0, 0, 0, 8, 3, 8, 0, 0, 8, 2, 8, 0],
            [8, 8, 8, 0, 8, 3, 8, 8, 8, 8, 2, 8, 8, 8, 0, 8, 2, 8, 8, 8, 8, 3, 8, 0],
            [8, 0, 0, 0, 8, 2, 8, 0, 0, 8, 3, 2, 3, 8, 0, 8, 3, 2, 3, 2, 3, 2, 8, 0],
            [8, 0, 8, 8, 8, 3, 8, 8, 0, 8, 2, 8, 8, 8, 0, 8, 8, 3, 8, 8, 8, 8, 8, 0],
            [8, 0, 8, 2, 3, 2, 3, 8, 0, 8, 3, 8, 0, 0, 0, 0, 8, 2, 8, 0, 0, 0, 0, 0],
            [8, 0, 8, 8, 8, 8, 8, 8, 0, 8, 2, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 0, 8, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 8, 0],
            [8, 8, 0, 8, 8, 8, 0, 8, 8, 8, 2, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 3, 8, 0],
            [0, 8, 0, 8, 0, 8, 0, 8, 3, 2, 3, 8, 0, 0, 0, 0, 8, 2, 8, 0, 8, 2, 8, 0],
            [0, 8, 8, 8, 0, 8, 8, 8, 2, 8, 8, 8, 0, 8, 8, 0, 8, 8, 8, 0, 8, 8, 8, 0],
        ]
        code = """p=lambda g,n=43:
  g*-n or[*map(lambda*r,x=0:[x:=y or sum({*x%8*sum(g,[-x-8])})for y in r[::-1]],*p(g,n-1))]"""
        self.problem_representation_with_code(
            input, output, code, size_square=0.15, scale_code=0.7
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
        code = """#coding:L1
  import zlib
  exec(zlib.decompress(bytes(
  "�PU^!�Na;�v+^��-e�m{w��'��ש�c-n��	�.L����Fc�l��X�c�Qt����<��S�s�[JC�
  �����fO�i�G����=��V�~OW{ja;ʴd@�e:X.�$s�J�i��O���e��b/�tRE�uG�YM*�[��]�@$5UE
  J�`�HPgɅ��<�Ey�����=�����������m����ə�/0��{�g�E|�ݥ����Xc��I$O","L1"),~9))"""
        self.problem_representation_with_code(
            input, output, code, size_square=0.17, scale_code=0.45
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

        agi_vertical = VGroup(
            Text("A", font_size=70),
            Text("G", font_size=70),
            Text("I", font_size=70),
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN).shift(3*LEFT)
        
        self.play(ReplacementTransform(agi_initial, agi_vertical), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # Expand A -> Artificial
        word1 = Text("Artificial", font_size=70)
        word1.shift(agi_vertical[0].get_center() - word1[0].get_center())
        self.play(
            ReplacementTransform(agi_vertical[0], word1[0]),
            Write(word1[1:]),
            runtime=self.default_animation_time
        )
        self.wait(0.5*self.default_wait_constant)

        # Expand G -> General
        word2 = Text("General", font_size=70)
        word2.shift(agi_vertical[1].get_center() - word2[0].get_center())
        self.play(
            ReplacementTransform(agi_vertical[1], word2[0]),
            Write(word2[1:]),
            runtime=self.default_animation_time
        )
        self.wait(0.5*self.default_wait_constant)

        # Expand I -> Intelligence
        word3 = Text("Intelligence", font_size=70)
        word3.shift(agi_vertical[2].get_center() - word3[0].get_center())
        self.play(
            ReplacementTransform(agi_vertical[2], word3[0]),
            Write(word3[1:]),
            runtime=self.default_animation_time
        )
        self.wait(self.default_wait_constant)

        self.play(FadeOut(word1), FadeOut(word2), FadeOut(word3))
        self.play(FadeOut(subtitle_agi))
        self.wait(self.default_wait_constant)

        # Slide: Problem example 330
        matrix = self.power_matrix_init(output)
        self.play(Create(matrix))
        self.wait(self.default_wait_constant)

        self.wait(4)

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

    def problem_representation(self, input=list[list], output=list[list]) -> None:
        """
        Routine to represent input/output
        """
        # Create objects
        input_matrix = self.draw_matrix(input)
        output_matrix = self.draw_matrix(output).next_to(input_matrix, RIGHT, buff=2)
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

        self.play(LaggedStartMap(Uncreate, all_stuff))
        self.wait(self.default_wait_constant)

        return

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

    def power_matrix_init(self, grid: list[list], gap_const: float = 0.1) -> Mobject:
        """
        Routine that initialize the problem with power of 2 inside the all grid
        """
        n_rows = len(grid)
        n_cols = len(grid[0])

        matrix = VGroup()
        for i in range(n_rows):
            row = VGroup()
            for j in range(n_cols):
                num = MathTex(rf"2^{{{i*n_rows + j}}}", font_size=self.NORMAL_FONT_SIZE)
                row.add(num)
            row.arrange(RIGHT, buff=gap_const)
            matrix.add(row)

        matrix.arrange(DOWN, buff=gap_const)
        return matrix
