import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory_dictionary = {}
        
        # Test adding Widget1 with quantity of 10
        add_inventory(inventory_dictionary, 'Widget1', 10)
        self.assertEqual(inventory_dictionary['Widget1'], 10)
        
        # Test adding Widget1 with quantity of 25 updates to 35
        add_inventory(inventory_dictionary, 'Widget1', 25)
        self.assertEqual(inventory_dictionary['Widget1'], 35)
        
        # Test adding Widget1 with quantity of -10 updates to 25
        add_inventory(inventory_dictionary, 'Widget1', -10)
        self.assertEqual(inventory_dictionary['Widget1'], 25)

    def test_remove_inventory_widget(self):
        inventory_dictionary = {}
        
        # Add two widgets
        add_inventory(inventory_dictionary, 'Widget1', 10)
        add_inventory(inventory_dictionary, 'Widget2', 20)
        
        # Remove widget1
        remove_inventory_widget(inventory_dictionary, 'Widget1')
        
        # Test that length is 1 and widget2 still exists
        self.assertEqual(len(inventory_dictionary), 1)
        self.assertIn('Widget2', inventory_dictionary)
        self.assertNotIn('Widget1', inventory_dictionary)

if __name__ == '__main__':
    unittest.main()