
def calculate_points(*student_points):
    return sum(student_points)


def display_house_points():
    harry_points = 20
    hermione_points = 25
    ron_points = 18
    draco_points = 30

    gryffindor_points = calculate_points(
        harry_points, hermione_points, ron_points
    )
    slytherin_points = calculate_points(draco_points)

    print("Pontos da Grifinória:", gryffindor_points)
    print("Pontos da Sonserina:", slytherin_points)


display_house_points()