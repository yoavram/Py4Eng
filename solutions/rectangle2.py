class Rectangle2:
    """Describe a parallel-axes rectangle by storing lower left point, height and width.
    
    Attributes
    ----------
    point : Point
        lower left point
    width : float
        width
    height : float
        height
    """
    def __init__(self, point, height, width):
        assert isinstance(point, Point)
        assert isinstance(height, (int, float))
        assert isinstance(width, (int, float))
        assert height > 0
        assert width > 0        
        self.point = point
        self.height = float(height)
        self.width = float(width)
        
    def __repr__(self):
        representation = "Rectangle with lower left {0} and upper right {1}"
        return representation.format(self.point, Point(self.point.x + self.width, self.point.y + self.height))
    
    def dimensions(self):
        return self.height, self.width

    def area(self):
        area = self.height * self.width
        return area

    def copy(self):
        return Rectangle2(self.point, self.height, self.width)
    
    def transpose(self):
        new_rect = self.copy()
        new_rect.point = Point(new_rect.point.x - new_rect.height , new_rect.point.y - new_rect.width)
        new_rect.height, new_rect.width = new_rect.width, new_rect.height
        return new_rect