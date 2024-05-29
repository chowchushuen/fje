import json
import config


class TreeNode:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []
        self.parent = None
        self.level = 40
        self.icon = None

    def add_child(self, node):
        self.children.append(node)
    def set_icon(self, icon):
        self.icon = icon
    def __rect__(self, level=-1):
        if self.name != "root":
            if self.icon:
                ret = "│   " * level + "├─ " + self.icon + " " + self.name 
            else:
                ret = "│   " * level + "├─ " + self.name 
            if self.value is not None:
                ret += ": " + str(self.value)
            ret = ret + " " + "─"*(self.level-len(ret)) + "┤\n"
        else:
            ret = ""
        for child in self.children:
            ret += child.__rect__(level + 1)
        return ret
    def __tree__(self, level=-1):
        if self.name != "root":
            indent = "│   " * level
            if self.icon:
                ret = indent + "├─ " + self.icon + " " + self.name
            else:
                ret = indent + "├─ " + self.name
            if self.value is not None:
                ret += ": " + str(self.value)
            ret += "\n"
        else:
            ret = ""
        for child in self.children:
            ret += child.__tree__(level + 1)
        return ret

class TreeFactory:
    '''
    def create_node(self, name, value=None):
        return TreeNode(name, value)
    '''
    def create_node(self, name, value=None, icon=None):
        node = TreeNode(name, value)
        if icon:
            node.set_icon(icon)
        return node

class JsonToTree:
    def __init__(self, json_file,icon_factory):
        self.factory = TreeFactory()
        self.icon_factory = icon_factory
        self.root = self.factory.create_node("root")
        self.load_json(json_file)
        

    def load_json(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            self.build_tree(data)

    def build_tree(self, data, parent=None):
        for key, value in data.items():
            icon = self.icon_factory.create_icon("intermediate") if isinstance(value, dict) else self.icon_factory.create_icon("leaf")
            node = self.factory.create_node(key, icon=icon)            
            if parent is not None:
                node.parent = parent
                parent.add_child(node)
            else:
                node.parent = self.root
                self.root.add_child(node)
            if isinstance(value, dict):
                self.build_tree(value, node)
            else:
                node.value = value

    def create_tree(self,product_type):
        if product_type == "tree":
            print(self.root.__tree__())
        elif product_type == "rect":
            print(self.root.__rect__())
        else:
            raise ValueError("不支持的产品类型")
        

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True, help='JSON文件路径')
    parser.add_argument('-s', '--style', type=str, required=True, help='样式')
    parser.add_argument('-i', '--icon', type=str, required=True, help='图标家族')

    # 解析参数
    args = parser.parse_args()
    if(args.icon == 'A'):
        icon_factory = config.IconFactoryA()
    if(args.icon == 'B'):
        icon_factory = config.IconFactoryB()
    json_to_tree = JsonToTree('test.json',icon_factory)
    if(args.style == "tree"):
        json_to_tree.create_tree("tree")
    if(args.style == "rect"):
        json_to_tree.create_tree("rect")

if __name__ == "__main__":
    main()