icon_family = {
    'intermediate': '☝',
    'leaf': '✌'
}

class Factory:
    def create_icon(self, product_type):
        pass
class IconFactoryA(Factory):
    def create_icon(self, product_type):
        if product_type == "intermediate":
            return '☝'
        elif product_type == "leaf":
            return '✌'
        else:
            raise ValueError("不支持的产品类型")
class IconFactoryB(Factory):
    def create_icon(self, product_type):
        if product_type == "intermediate":
            return '♢'
        elif product_type == "leaf":
            return '♤'
        else:
            raise ValueError("不支持的产品类型")