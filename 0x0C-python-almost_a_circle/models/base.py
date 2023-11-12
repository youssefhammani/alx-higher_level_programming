#!/usr/bin/python3
"""Module for the Base class."""

import json


class Base:
    """Base class for managing id attribute."""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class."""
        if id is not None:
            # Assign the public instance attribute id with the provided value
            self.id = id
        else:
            # Increment __nb_objects and assign the new value to id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as file:
                data = file.read()
                list_dicts = cls.from_json_string(data)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to CSV format and write to a file."""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if list_objs:
                for obj in list_objs:
                    writer.writerow(obj.to_csv())
            else:
                writer.writerow([])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if row:
                        instances.append(cls.create(*map(int, row)))
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all the Rectangles and Squares."""
        turtle.speed(2)  # Set the turtle drawing speed

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)
            turtle.right(90)
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)
            turtle.right(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.forward(square.size)
            turtle.right(90)
            turtle.forward(square.size)
            turtle.right(90)
            turtle.forward(square.size)
            turtle.right(90)
            turtle.forward(square.size)
            turtle.right(90)

        turtle.done()
