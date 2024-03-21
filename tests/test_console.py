import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_missing_class_name(self, mock_stdout):
        console = HBNBCommand()
        console.do_create('')
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_invalid_class_name(self, mock_stdout):
        console = HBNBCommand()
        console.do_create('InvalidClassName')
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    # Add tests for other methods...
    
    def test_do_quit(self):
        console = HBNBCommand()
        with self.assertRaises(SystemExit):
            console.do_quit('')

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_quit(self, mock_stdout):
        console = HBNBCommand()
        console.help_quit()
        self.assertIn("Exits the program with formatting", mock_stdout.getvalue().strip())

    def test_do_EOF(self):
        console = HBNBCommand()
        with self.assertRaises(SystemExit):
            console.do_EOF('')

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_EOF(self, mock_stdout):
        console = HBNBCommand()
        console.help_EOF()
        self.assertIn("Exits the program without formatting", mock_stdout.getvalue().strip())

    # Add tests for other methods...

if __name__ == '__main__':
    unittest.main()

