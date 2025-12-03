from manim import *


class main_presentation(Scene):
    default_wait_constant = 1.5
    default_animation_time = 1

    # Font sizes
    TITLE_FONT_SIZE = 48
    SUBTITLE_FONT_SIZE = 42
    NORMAL_FONT_SIZE = 36

    # Number to Colours
    num2colour_fill = {0: BLACK, 1:BLUE_E, 2:PURE_RED, 3:PURE_GREEN, 4:YELLOW, 5:GREY, 6:PINK, 7: ORANGE, 8:BLUE_A, 9:PURPLE}
    num2colour_stroke = {0: WHITE, 7: YELLOW}

    def construct(self):
        # Title
        title_first_slide = Text("Google Code Golf Competition", font_size=self.TITLE_FONT_SIZE).to_edge(UP)
        self.play(Write(title_first_slide), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # First slide
        self.presentation_slide(title_first_slide)

        # Second slide
        title_second_slide = Text("Problem xxx", font_size=self.TITLE_FONT_SIZE).to_edge(UP)
        self.play(Transform(title_first_slide, title_second_slide))
        self.wait(self.default_wait_constant)

        input = [[0, 7, 7], [7, 7, 7], [0, 7, 7]]
        output = [
            [0, 0, 0, 0, 7, 7, 0, 7, 7],
            [0, 0, 0, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 7, 7, 0, 7, 7],
            [0, 7, 7, 0, 7, 7, 0, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7],
            [0, 7, 7, 0, 7, 7, 0, 7, 7],
            [0, 0, 0, 0, 7, 7, 0, 7, 7],
            [0, 0, 0, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 7, 7, 0, 7, 7],
        ]
        self.problem_representation(input, output)

        # TODO: test
        matrix = self.power_matrix_init(output)
        self.play(Create(matrix))
        self.wait(self.default_wait_constant)

        self.wait(4)

    #########################################
    # Presentation slide
    #########################################
    def presentation_slide(self, title: Mobject) -> None:

        names = ["Massimiliano", "Alessandro", "Osea", "Alessandro", "Paolo"]
        surnames = ["Ghiotto", "Daldossi", "Fracchia", "Ghiotto", "Bignardi"]

        # Team
        team_name = Text("NeedAJob", font_size=self.SUBTITLE_FONT_SIZE).next_to(title, DOWN)
        self.play(Write(team_name), runtime=self.default_animation_time)
        self.wait(self.default_wait_constant)

        # First line of photos
        photos = VGroup()
        photos_animation = []

        for i in range(3):
            figure = Circle(0.5)

            name = Text(names[i], font_size=self.NORMAL_FONT_SIZE).next_to(figure, DOWN)
            surname = Text(surnames[i], font_size=self.NORMAL_FONT_SIZE).next_to(name, DOWN)

            person = VGroup(figure, name, surname)

            photos.add(person)
            photos_animation += [
                Create(figure),
                Write(name),
                Write(surname),
            ]

        photos.arrange(RIGHT, buff=1.25)
        photos[-1].shift(0.5 * RIGHT)
        # self.play(
        #     Create(photos.scale(0.5), runtime=self.default_animation_time),
        #     runtime=5 * self.default_animation_time,
        # )
        self.play(
            LaggedStart(*photos_animation, lag_ration=0.4),
        )
        self.wait(self.default_animation_time)

        # Second line of photos
        second_photos = VGroup()
        second_photos_animation = []
        for i in range(3, 5):
            figure = Circle(0.5)
            name = Text(names[i], font_size=self.NORMAL_FONT_SIZE).next_to(figure, DOWN)
            surname = Text(surnames[i], font_size=self.NORMAL_FONT_SIZE).next_to(name, DOWN)

            person = VGroup(figure, name, surname)

            second_photos.add(person)

            second_photos_animation += [
                Create(figure),
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
        self.play(LaggedStart(*second_photos_animation, lag_ratio=0.4))
        self.wait(self.default_animation_time)

        # Make all the stuff disappear
        all_mobj = second_photos[::-1] + photos[::-1] + [team_name]
        self.play(LaggedStartMap(Uncreate, all_mobj))
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
            stroke_width=2,
            tip_length=0.15,
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
                    .set_stroke(self.num2colour_stroke[grid[i][j]])
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
