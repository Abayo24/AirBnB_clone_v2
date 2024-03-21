import unittest
from unittest.mock import patch
from console import HBNBCommand

class TestDoCreate(unittest.TestCase):
    
    @patch('builtins.print')
    def test_missing_class_name(self, mock_print):
        console = HBNBCommand()
        console.do_create("")  
        mock_print.assert_called_with("** class name missing **")  

    @patch('builtins.print')
    def test_invalid_class_name(self, mock_print):
        console = HBNBCommand()
        console.do_create("InvalidClassName")  
        mock_print.assert_called_with("** class doesn't exist **")  

    @patch('builtins.print')
    def test_create_instance(self, mock_print):
        console = HBNBCommand()
        with patch('builtins.input', side_effect=['TestObject']):  
            console.do_create("YourClassName")  
        mock_print.assert_called()  

if __name__ == '__main__':
    unittest.main()

