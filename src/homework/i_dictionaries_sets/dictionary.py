def add_inventory(widgets: dict, widget_name: str, quantity: int) -> None:
    """
    Add or update widget inventory in the dictionary.
    
    Args:
        widgets: Dictionary containing widget names and their quantities
        widget_name: Name of the widget to add or update
        quantity: Quantity to add to the inventory
    """
    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity
def remove_inventory_widget(widgets: dict, widget_name: str) -> str:
    """
    Remove a widget from the inventory dictionary.
            
     Args:
        widgets: Dictionary containing widget names and their quantities
        widget_name: Name of the widget to remove
                
    Returns:
    'Record deleted' if widget was found and removed, 'Item not found' otherwise
    """
    if widget_name in widgets:
        del widgets[widget_name]
        return 'Record deleted'
    else:
        return 'Item not found'