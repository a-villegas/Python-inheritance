class Restaurant():
    """An obscure example of a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        
    def describe_restaurant(self):
        """Restaurant description""" 
        print(self.name.title() + self.cuisine.title())
        
        
    def open_restaurant(self):
        """ """
        print(self.name.title() + "  is Open for business!")
        
        

ans=Restaurant('Benihanas', 'Japanese')
ans.describe_restaurant()
ans.open_restaurant()