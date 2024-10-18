from manim import *

class ApacheKafka(Scene):
    def construct(self):
        square1 = Rectangle(color=BLUE).shift(LEFT * 4)
        square3 = Rectangle(color=RED).shift(RIGHT * 4)

        text_producer = Tex("Producer").move_to(square1)
        text_consumer = Tex("Consumer").move_to(square3)

        self.play(Create(square1), Write(text_producer))
        self.wait(1)
        self.play(Create(square3), Write(text_consumer))
        self.wait(1)

        arrow1 = Arrow(square1.get_right(), square3.get_left())
        text_message = Tex("Message").move_to(arrow1).move_to(UP * 0.5)

        self.play(Create(arrow1), Write(text_message))
        self.wait(1)

        messages = [
            Text("MessageClass.receive_message()").move_to(arrow1).move_to(UP * 2),
            Text("DataSenderObject.send_message()").move_to(arrow1).move_to(UP * 2),
            Text('ContentObject("Content Object")').move_to(arrow1).move_to(UP * 2)
        ]

        for msg in messages:
            self.play(Write(msg))
            self.wait(1)
            self.play(FadeOut(msg))

        self.wait(2)