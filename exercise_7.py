from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
import unittest

grammar = Grammar(
    '''
    time24 = (time12 postfix) / time12
    time12 = (hr ":" min) / hr
    hr = min / digit
    min = digit digit
    postfix = "am" / "pm"
    digit = ~"[0-9]"
    '''
)


class TimeVisitor(NodeVisitor):
    def visit_time24(self, node, visited_children):
        if isinstance(visited_children[0], int):
            visited_children = [visited_children]
        return sum(visited_children[0])

    def visit_time12(self, node, visited_children):
        if isinstance(visited_children[0], int):
            visited_children = [visited_children]
        return sum(visited_children[0])

    def visit_hr(self, node, visited_children):
        return sum(visited_children) * 60

    def visit_min(self, node, visited_children):
        return visited_children[0] * 10 + visited_children[1]

    def visit_digit(self, node, visited_children):
        return int(node.text)

    def visit_postfix(self, node, visited_children):
        if node.text == 'am':
            return 0
        elif node.text == 'pm':
            return 12 * 60

    def generic_visit(self, node, visited_children):
        if node.text == ":":
            return 0
        else:
            return visited_children or node


class TimeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_cases = {
            '4:15am': 4 * 60 + 15,
            '4:15pm': 4 * 60 + 15 + 12 * 60,
            '4pm': 4 * 60 + 12 * 60,
            '4': 4 * 60,
            '4:15': 4 * 60 + 15,
        }

    def test_times(self):
        for time, minutes in self.test_cases.items():
            with self.subTest(time=time):
                self.assertEqual(TimeVisitor().visit(grammar.parse(time)), minutes)


if __name__ == '__main__':
    unittest.main()
    # TimeVisitor().visit(grammar.parse('4'))
