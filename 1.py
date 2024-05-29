# 定义一个产品接口
class Icon:
    def operation(self):
        pass

# 具体产品类
class ConcreteIconA(Icon):
    def operation(self):
        return "结果来自ConcreteProductA"

class ConcreteIconB(Icon):
    def operation(self):
        return "结果来自ConcreteProductB"

# 工厂类
class IconFactory:
    def create_icon(self, product_type):
        if product_type == "intermediate":
            return '☝'
        elif product_type == "leaf":
            return '✌'
        else:
            raise ValueError("不支持的产品类型")

# 客户端代码
if __name__ == "__main__":
    creator = Creator()

    # 根据类型创建产品A
    product_a = creator.create_product('A')
    print(product_a.operation())

    # 根据类型创建产品B
    product_b = creator.create_product('B')
    print(product_b.operation())

    # 尝试创建一个不支持的产品类型
    try:
        product_unknown = creator.create_product('Unknown')
    except ValueError as e:
        print(e)