"""Author and run isolated teaching examples; emit the exact captured stdout."""
from pathlib import Path
import html
import json
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROGRAMS = {}


def put(section, programs):
    PROGRAMS[section] = programs


def show(expression, setup=""):
    return (setup + "\n" if setup else "") + f"print({expression})"


put("comments-basic-syntax", [
    '# calculate total\nprint("Ready")',
    'def load():\n    """Load orders."""\nprint(load.__doc__)',
    'a = 1; b = 2\nprint(a, b)',
    'x = 2\nif x > 0:\n    print(x)',
    'active = True\nif active:\n    print("Active")',
    'print("Hello")',
    '# 运行时输入 Rebecca，然后按 Enter\nname = input("Name: ")\nprint(name)',
])
put("variables-assignment", [
    'price = 8500\nprint(price)', 'x = y = 0\nprint(x, y)',
    'x, y = 10, 20\nprint(x, y)', 'a, b = 1, 2\na, b = b, a\nprint(a, b)',
    'item = ["Copper", 8500]\nproduct, price = item\nprint(product, price)',
    'items = [1, 2, 3]\nfirst, *rest = items\nprint(first)\nprint(rest)',
] + [f'{name} = {value}\n{name} {op}= {operand}\nprint({name})' for name, value, op, operand in [
    ('count', 2, '+', 1), ('count', 2, '-', 1), ('price', 100, '*', 2),
    ('total', 10, '/', 2), ('x', 9, '//', 2), ('x', 9, '%', 2), ('x', 3, '**', 2),
]])
put('data-types', [
    'quantity = 10\nprint(type(quantity).__name__)',
    'price = 8.5\nprint(type(price).__name__)',
    'product = "Copper"\nprint(type(product).__name__)',
    'is_active = True\nprint(type(is_active).__name__)',
    'result = None\nprint(result)', 'x = 2 + 3j\nprint(x.real, x.imag)',
    'data = b"ABC"\nprint(data[0])',
    'data = bytearray(b"ABC")\ndata[0] = 97\nprint(data)',
])
put('type-checking-conversion', [show('type(price).__name__', 'price = 8.5'),
    show('isinstance(price, int)', 'price = 8500'), show('int("10")'), show('float("8.5")'),
    show('repr(str(1001))'), show('bool(1)'), show('list((1, 2))'), show('tuple([1, 2])'),
    show('sorted(set([1, 1, 2]))'), show('dict(name="Rebecca")')])
put('boolean-values-truthy-falsy', [
    'is_active = True\nprint(bool(is_active))', 'is_active = False\nprint(bool(is_active))',
    'result = None\nprint(bool(result))',
    'customer = "Rebecca"\nif customer:\n    print("Has customer")',
    'items = []\nif not items:\n    print("Empty")',
])
put('arithmetic-operators', [show(x) for x in ['10 + 5', '10 - 5', '100 * 3', '10 / 4',
    '10 // 3', '10 % 3', '2 ** 3', 'abs(-10)', 'round(8.567, 2)']])
put('comparison-operators', [show(expr, setup) for expr, setup in [
    ('status == "Done"', 'status = "Done"'), ('status != "Rejected"', 'status = "Pending"'),
    ('price > 8000', 'price = 8500'), ('price < 9000', 'price = 8500'),
    ('quantity >= 10', 'quantity = 10'), ('quantity <= 100', 'quantity = 101'),
    ('0 < price < 10000', 'price = 8500')]])
put('logical-operators', [show('active and approved', 'active = True\napproved = False'),
    show('draft or pending', 'draft = False\npending = True'),
    show('not is_completed', 'is_completed = False')])
put('identity-membership', [show('value is None', 'value = None'), show('value is not None', 'value = 0'),
    show('"Copper" in products', 'products = ["Copper", "Nickel"]'),
    show('"Gold" not in products', 'products = ["Copper", "Nickel"]')])
put('strings', ['print("Copper")', "print('Copper')", 'text = """Hello\nWorld"""\nprint(text)',
    'name = "Rebecca"\nprint(f"Hello {name}")', 'print(r"C:\\Users\\Rebecca")',
    'name = "Rebecca"\nprint("Hello " + name)', 'print("-" * 5)', 'product = "Copper"\nprint(len(product))'])
put('string-methods', [show(expr, setup) for expr, setup in [
    ('text.lower()', 'text = "COPPER"'), ('text.upper()', 'text = "copper"'),
    ('name.title()', 'name = "rebecca li"'), ('text.capitalize()', 'text = "cOPPER ORDER"'),
    ('repr(text.strip())', 'text = "  Copper  "'), ('repr(text.lstrip())', 'text = "  Copper  "'),
    ('repr(text.rstrip())', 'text = "  Copper  "'), ('text.replace("A", "B")', 'text = "A-A"'),
    ('text.split(",")', 'text = "Copper,Nickel"'), ('text.rsplit("/", 1)', 'text = "data/2026/orders.csv"'),
    ('text.splitlines()', 'text = "A\\nB\\n"'), ('",".join(items)', 'items = ["Copper", "Nickel"]'),
    ('order_id.startswith("ORD")', 'order_id = "ORD1001"'), ('file.endswith(".csv")', 'file = "orders.csv"'),
    ('text.find("order")', 'text = "new order"'), ('text.index("order")', 'text = "new order"'),
    ('text.count("a")', 'text = "banana"'), ('"123".isdigit()', ''), ('"ABC".isalpha()', ''), ('"A100".isalnum()', ''),
]])
put('escape-characters', ['print("Hello\\nWorld")', 'print("A\\tB")', 'print("C:\\\\data")',
    'print("Say \\"Hi\\"")', "print('It\\'s OK')"])
put('list', ['items = []\nprint(items)', 'items = ["A", "B"]\nprint(items)',
    show('items[0]', 'items = ["A", "B"]'), show('items[-1]', 'items = ["A", "B"]'),
    'items = ["A", "B"]\nitems.append("C")\nprint(items)',
    'items = ["A"]\nother = ["B", "C"]\nitems.extend(other)\nprint(items)',
    'items = ["B"]\nitems.insert(0, "A")\nprint(items)',
    'items = ["A", "B", "A"]\nitems.remove("A")\nprint(items)',
    'items = ["A", "B"]\nprint(items.pop())\nprint(items)',
    'items = ["A", "B"]\nitems.clear()\nprint(items)',
    show('items.index("A")', 'items = ["B", "A"]'), show('items.count("A")', 'items = ["A", "B", "A"]'),
    'items = [3, 1, 2]\nprint(items.sort())\nprint(items)',
    'items = [1, 2, 3]\nitems.reverse()\nprint(items)',
    'items = ["A"]\nnew_items = items.copy()\nnew_items.append("B")\nprint(items)\nprint(new_items)',
])
put('tuple', ['items = ()\nprint(items)', 'point = (10, 20)\nprint(point)',
    'item = ("Copper",)\nprint(item)', 'point = (10, 20)\nx, y = point\nprint(x, y)'])
put('dictionary', ['order = {}\nprint(order)', show('{"id": 1001}'), show('dict(id=1001)'),
    show('order["status"]', 'order = {"status": "Pending"}'),
    'order = {"status": "Pending"}\norder["status"] = "Done"\nprint(order)',
    show('order.get("status")', 'order = {}'), show('order.keys()', 'order = {"id": 1001}'),
    show('order.values()', 'order = {"id": 1001}'), show('order.items()', 'order = {"id": 1001}'),
    'order = {"id": 1}\ndata = {"status": "Done"}\norder.update(data)\nprint(order)',
    'order = {"status": "Done"}\nprint(order.pop("status"))\nprint(order)',
    'order = {}\nprint(order.setdefault("status", "Pending"))\nprint(order)',
    show('"status" in order', 'order = {"status": "Pending"}')])
put('set', [show('set()'), show('sorted({"A", "B", "A"})'),
    'items = {"A"}\nitems.add("C")\nprint(sorted(items))',
    'items = {"A", "B"}\nitems.remove("A")\nprint(items)',
    'items = {"B"}\nitems.discard("A")\nprint(items)',
] + [show(f'sorted(a.{method}(b))', 'a = {1, 2}\nb = {2, 3}') for method in ['union', 'intersection', 'difference']])
put('indexing', [show(f'items[{i}]', 'items = [10, 20, 30]') for i in [0, 1, -1, -2]])
put('slicing', [show('items' + suffix, 'items = [0, 1, 2, 3, 4]') for suffix in ['[1:4]', '[:3]', '[3:]', '[::2]', '[::-1]', '[:]']])
put('conditions', [
    'price = 8500\nif price > 8000:\n    print("High")',
    'price = 7500\nif price > 8000:\n    print("High")\nelif price > 7000:\n    print("Medium")',
    'price = 6000\nif price > 8000:\n    print("High")\nelse:\n    print("Low")',
    'active = True\napproved = True\nif active:\n    if approved:\n        print("Approved")',
    'active = True\nprint("Yes" if active else "No")',
])
put('for-loops', ['items = ["A", "B"]\nfor item in items:\n    print(item)',
    'for i in range(5):\n    print(i)', 'for i in range(1, 5):\n    print(i)',
    'for i in range(0, 10, 2):\n    print(i)',
    'items = ["A", "B"]\nfor index, item in enumerate(items):\n    print(index, item)',
    'items = ["A", "B"]\nfor index, item in enumerate(items, start=1):\n    print(index, item)',
    'names = ["Cu", "Ni"]\nprices = [10, 20]\nfor name, price in zip(names, prices):\n    print(name, price)',
    'data = {"Cu": 10}\nfor key, value in data.items():\n    print(key, value)'])
put('while-loops', ['count = 0\nwhile count < 3:\n    print(count)\n    count += 1',
    'for x in [1, 2, 3]:\n    if x == 2:\n        break\n    print(x)',
    'for x in [1, 2, 3]:\n    if x == 2:\n        continue\n    print(x)',
    'for x in [1, 2]:\n    pass\nprint("Done")',
    'for x in [1, 2]:\n    print(x)\nelse:\n    print("Finished")'])
put('comprehensions', [show(expr, setup) for expr, setup in [
    ('[x * 2 for x in nums]', 'nums = [1, 2, 3]'),
    ('[x for x in nums if x > 10]', 'nums = [5, 15, 20]'),
    ('["High" if x > 10 else "Low" for x in nums]', 'nums = [5, 15]'),
    ('{x: x * 2 for x in nums}', 'nums = [1, 2]'),
    ('sorted({x for x in nums})', 'nums = [1, 1, 2]'),
    ('[x for row in matrix for x in row]', 'matrix = [[1, 2], [3]]')]])
put('functions', [
    'def save():\n    print("Saved")\nsave()',
    'def greet(name):\n    return "Hi " + name\nprint(greet("Rebecca"))',
    'def greet(name):\n    print(name)\ngreet("Rebecca")',
    'def total():\n    return 30\nprint(total())',
    'def order():\n    return 10, 2\nprint(order())',
    'def greet(name="Guest"):\n    print(name)\ngreet()',
    'def greet(name):\n    print(name)\ngreet(name="Rebecca")',
    'def greet(name):\n    print(name)\ngreet("Rebecca")',
    'def show(*items):\n    print(items)\nshow("A", "B")',
    'def show(**data):\n    print(data)\nshow(id=1, status="New")',
    'def f(x, /):\n    return x\nprint(f(10))',
    'def f(*, name):\n    return name\nprint(f(name="Rebecca"))',
    'double = lambda x: x * 2\nprint(double(3))',
])
put('variable-scope', [
    'def f():\n    x = 1\n    print(x)\nf()',
    'x = 1\ndef f():\n    print(x)\nf()',
    'count = 0\ndef increment():\n    global count\n    count += 1\nincrement()\nprint(count)',
    'def outer():\n    count = 0\n    def increment():\n        nonlocal count\n        count += 1\n    increment()\n    print(count)\nouter()',
])
put('built-in-functions', [show(expr, setup) for expr, setup in [
    ('len(items)', 'items = ["A", "B"]'), ('min(prices)', 'prices = [10, 5, 20]'),
    ('max(prices)', 'prices = [10, 5, 20]'), ('sum(amounts)', 'amounts = [10, 20, 30]'),
    ('sorted(items)', 'items = [3, 1, 2]'), ('list(reversed(items))', 'items = [1, 2, 3]'),
    ('any(results)', 'results = [False, True]'), ('all(results)', 'results = [True, True]'),
    ('list(enumerate(items))', 'items = ["A", "B"]'), ('list(zip(a, b))', 'a = [1, 2]\nb = ["A"]'),
    ('list(map(str, values))', 'values = [1, 2]'),
    ('list(filter(is_valid, items))', 'is_valid = lambda x: x > 0\nitems = [-1, 2]'), ('list(range(5))', '')]])
put('sorting', [show('sorted(items)', 'items = [3, 1, 2]'),
    'items = [3, 1, 2]\nprint(items.sort())\nprint(items)',
    show('sorted(items, reverse=True)', 'items = [1, 3, 2]'),
    show('sorted(orders, key=lambda x: x["price"])', 'orders = [{"price": 20}, {"price": 10}]')])
put('modules-imports', [
    'import json\nprint(json.loads("1"))', 'import pandas as pd\nprint(pd.Series([1, 2]).sum())',
    'from pathlib import Path\nprint(Path("orders.csv").suffix)', 'from math import sqrt as root\nprint(root(16))',
    'from math import sqrt, ceil\nprint(sqrt(16), ceil(4.2))',
    '# 创建临时小包，演示相对导入；不会修改你的项目\nimport tempfile, sys\nfrom pathlib import Path\nwith tempfile.TemporaryDirectory() as folder:\n    package = Path(folder) / "demo_package"\n    package.mkdir()\n    (package / "__init__.py").write_text("")\n    (package / "utils.py").write_text("helper = 42")\n    (package / "main.py").write_text("from .utils import helper")\n    sys.path.insert(0, folder)\n    from demo_package.main import helper\n    print(helper)',
    'print(__name__)', 'if __name__ == "__main__":\n    print("Direct run")',
])


def file_program(operation, content='A\\nB'):
    return ('# 只操作临时文件\nimport tempfile\nfrom pathlib import Path\n'
            'with tempfile.TemporaryDirectory() as folder:\n'
            '    path = Path(folder) / "example.txt"\n'
            f'    path.write_text("{content}", encoding="utf-8")\n' +
            '\n'.join('    ' + line if line else '' for line in operation.split('\n')))


put('files', [file_program('with open(path, "r", encoding="utf-8") as f:\n    print(f.read())'),
    file_program('with open(path, "r", encoding="utf-8") as f:\n    print(f.read())'),
    file_program('with open(path, "w", encoding="utf-8") as f:\n    f.write("New")\nprint(path.read_text(encoding="utf-8"))'),
    file_program('with open(path, "a", encoding="utf-8") as f:\n    f.write("C")\nprint(path.read_text(encoding="utf-8"))', 'AB'),
    file_program('with open(path, "rb") as f:\n    print(f.read())', 'ABC'),
    file_program('with open(path, encoding="utf-8") as f:\n    print(f.closed)\nprint(f.closed)'),
    'from io import StringIO\nf = StringIO("A\\nB")\nprint(repr(f.read()))',
    'from io import StringIO\nf = StringIO("A\\nB")\nprint(repr(f.readline()))',
    'from io import StringIO\nf = StringIO("A\\nB")\nprint(f.readlines())',
    'from io import StringIO\nf = StringIO()\nprint(f.write("Hello"))\nprint(f.getvalue())',
    'from io import StringIO\nf = StringIO()\nf.writelines(["A\\n", "B\\n"])\nprint(repr(f.getvalue()))',
    'from io import StringIO\nf = StringIO("Hello")\nf.close()\nprint(f.closed)',
    'from io import StringIO\nf = StringIO("ABC")\nf.read()\nprint(f.seek(0))\nprint(f.read())'])
put('exceptions', [
    'try:\n    print(int("10"))\nexcept ValueError:\n    print("Invalid")',
    'try:\n    int("abc")\nexcept ValueError:\n    print("Caught ValueError")',
    'try:\n    {}["missing"]\nexcept ValueError:\n    print("ValueError")\nexcept KeyError:\n    print("KeyError")',
    'try:\n    int("abc")\nexcept ValueError as e:\n    print(type(e).__name__)',
    'try:\n    int("10")\nexcept ValueError:\n    print("Invalid")\nelse:\n    print("Success")',
    'try:\n    int("abc")\nexcept ValueError:\n    print("Caught")\nfinally:\n    print("Cleanup")',
    'try:\n    raise ValueError("Bad value")\nexcept ValueError as e:\n    print(e)',
    'try:\n    try:\n        int("abc")\n    except ValueError as e:\n        raise RuntimeError("Failed") from e\nexcept RuntimeError as e:\n    print(type(e.__cause__).__name__)',
    'try:\n    10 / 0\nexcept Exception as e:\n    print(type(e).__name__)',
])
exception_exprs = ['int("abc")', '"1" + 1', '{}["missing"]', '[1][99]',
    'open("missing.txt")', '10 / 0', '__import__("example_missing_module_123")',
    'object().missing', 'unknown']
put('common-exceptions', [f'try:\n    {expr}\nexcept Exception as error:\n    print(type(error).__name__)' for expr in exception_exprs])
put('classes', [
    'class Order:\n    pass\nprint(Order.__name__)',
    'class Order:\n    pass\norder = Order()\nprint(type(order).__name__)',
    'class Order:\n    def __init__(self):\n        self.status = "New"\nprint(Order().status)',
    'class Order:\n    def __init__(self):\n        self.status = "New"\n    def show(self):\n        print(self.status)\nOrder().show()',
    'class Order:\n    pass\norder = Order()\norder.status = "Done"\nprint(order.status)',
    'class Order:\n    def save(self):\n        print("Saved")\norder = Order()\norder.save()',
    'class Order:\n    status = "New"\nprint(Order.status)',
    'class Order:\n    status = "New"\nclass SalesOrder(Order):\n    pass\nprint(SalesOrder().status)',
    'class Order:\n    def __init__(self):\n        self.status = "New"\nclass SalesOrder(Order):\n    def __init__(self):\n        super().__init__()\nprint(SalesOrder().status)',
    'class Order:\n    pass\norder = Order()\nprint(isinstance(order, Order))',
    'class Order:\n    pass\nclass SalesOrder(Order):\n    pass\nprint(issubclass(SalesOrder, Order))',
])
put('special-methods', [PROGRAMS['classes'][2],
    'class Order:\n    def __str__(self):\n        return "Order #1"\nprint(str(Order()))',
    'class Order:\n    def __repr__(self):\n        return "Order(id=1)"\nprint(repr(Order()))',
    'class Order:\n    def __len__(self):\n        return 3\nprint(len(Order()))',
    'class Order:\n    def __iter__(self):\n        return iter([1, 2])\nprint(list(Order()))',
    'class Resource:\n    def __enter__(self):\n        return "Ready"\n    def __exit__(self, *args):\n        pass\nwith Resource() as value:\n    print(value)',
    'class Resource:\n    def __enter__(self):\n        return self\n    def __exit__(self, exc_type, exc_value, traceback):\n        print("Closed")\nwith Resource():\n    print("Opened")',
])
put('property-decorators', [
    'def timer(func):\n    def wrapped():\n        print("Before")\n        func()\n    return wrapped\n@timer\ndef save():\n    print("Saved")\nsave()',
    'class Order:\n    @property\n    def total(self):\n        return 20\nprint(Order().total)',
    'class Order:\n    @staticmethod\n    def add(a, b):\n        return a + b\nprint(Order.add(1, 2))',
    'class Order:\n    @classmethod\n    def create(cls):\n        return cls()\nprint(type(Order.create()).__name__)',
    'class Order:\n    @classmethod\n    def name(cls):\n        return cls.__name__\nprint(Order.name())',
])
put('iterables-iterators', ['items = ["A", "B"]\nfor item in items:\n    print(item)',
    'items = [10, 20]\niterator = iter(items)\nprint(next(iterator))',
    'iterator = iter([10, 20])\nprint(next(iterator))\nprint(next(iterator))',
    'iterator = iter([])\ntry:\n    next(iterator)\nexcept StopIteration:\n    print("StopIteration")'])
put('generators', ['def values():\n    yield 10\nprint(next(values()))',
    'def items():\n    yield 1\nprint(list(items()))',
    'nums = [1, 2, 3]\nvalues = (x * 2 for x in nums)\nprint(list(values))',
    'def values():\n    yield from [1, 2]\nprint(list(values()))'])
put('context-managers', [file_program('with open(path, encoding="utf-8") as f:\n    print(f.read())'),
    file_program('with open(path, encoding="utf-8") as file:\n    print(file.read())')])
put('json', [
    'import json\ntext = \'{"id": 1}\'\nprint(json.loads(text))',
    'import json\ndata = {"id": 1}\nprint(json.dumps(data))',
    'import json\nfrom io import StringIO\nfile = StringIO(\'{"id": 1}\')\nprint(json.load(file))',
    'import json\nfrom io import StringIO\nfile = StringIO()\njson.dump({"id": 1}, file)\nprint(file.getvalue())',
    'import json\nprint(json.dumps({"id": 1}, indent=2))',
    'import json\nprint(json.dumps({"name": "铜"}, ensure_ascii=False))',
])
put('csv', [
    'import csv\nfrom io import StringIO\nfile = StringIO("A,B\\n1,2")\nfor row in csv.reader(file):\n    print(row)',
    'import csv\nfrom io import StringIO\nfile = StringIO()\nwriter = csv.writer(file)\nwriter.writerow([1, "Cu"])\nprint(file.getvalue(), end="")',
    'import csv\nfrom io import StringIO\nfile = StringIO("id,name\\n1,Cu")\nprint(next(csv.DictReader(file)))',
    'import csv\nfrom io import StringIO\nfile = StringIO()\nwriter = csv.DictWriter(file, fieldnames=["id", "name"])\nwriter.writerow({"id": 1, "name": "Cu"})\nprint(file.getvalue(), end="")',
    'import csv\nfrom io import StringIO\nfile = StringIO()\nwriter = csv.writer(file)\nwriter.writerow([1, "Cu"])\nprint(file.getvalue(), end="")',
    'import csv\nfrom io import StringIO\nfile = StringIO()\nwriter = csv.writer(file)\nwriter.writerows([[1, "Cu"], [2, "Ni"]])\nprint(file.getvalue(), end="")',
    'import csv\nfrom io import StringIO\nfile = StringIO()\nwriter = csv.DictWriter(file, fieldnames=["id", "name"])\nwriter.writeheader()\nprint(file.getvalue(), end="")',
])


def path_program(operation):
    return ('# 只操作临时目录\nimport tempfile\nfrom pathlib import Path\n'
            'with tempfile.TemporaryDirectory() as folder:\n'
            '    path = Path(folder) / "orders.csv"\n'
            '    path.write_text("Hello", encoding="utf-8")\n' +
            '\n'.join('    ' + line if line else '' for line in operation.split('\n')))


put('pathlib', [show('Path("data/file.csv").as_posix()', 'from pathlib import Path'),
    'from pathlib import Path\n# 路径依运行环境变化\nprint(Path.cwd().is_dir())',
    'from pathlib import Path\n# 主目录依运行环境变化\nprint(Path.home().is_absolute())',
    'from pathlib import Path\nfolder = Path("data")\nprint((folder / "file.csv").as_posix())',
    path_program('print(path.exists())'), path_program('print(path.is_file())'),
    path_program('print(path.parent.is_dir())'),
    path_program('directory = path.parent / "new"\ndirectory.mkdir()\nprint(directory.is_dir())'),
    show('path.name', 'from pathlib import Path\npath = Path("data/orders.csv")'),
    show('path.stem', 'from pathlib import Path\npath = Path("data/orders.csv")'),
    show('path.suffix', 'from pathlib import Path\npath = Path("data/orders.csv")'),
    show('path.parent.as_posix()', 'from pathlib import Path\npath = Path("data/orders.csv")'),
    path_program('print(sorted(p.name for p in path.parent.glob("*.csv")))'),
    path_program('print(sorted(p.name for p in path.parent.rglob("*.csv")))'),
    path_program('print(path.read_text(encoding="utf-8"))'),
    path_program('print(path.write_text("New", encoding="utf-8"))\nprint(path.read_text(encoding="utf-8"))'),
])
put('os', [
    'import os\n# 当前目录依环境变化；这里只显示它是否存在\nprint(os.path.isdir(os.getcwd()))',
    'import os\nos.environ["EXAMPLE_MODE"] = "demo"\nprint(os.getenv("EXAMPLE_MODE"))',
    'import os\nos.environ["EXAMPLE_MODE"] = "demo"\nprint(os.environ["EXAMPLE_MODE"])',
    path_program('import os\nprint(os.path.exists(path))'),
    path_program('import os\nprint(sorted(os.listdir(path.parent)))'),
    path_program('import os\nos.remove(path)\nprint(path.exists())'),
    path_program('import os\nnew = path.parent / "new.csv"\nos.rename(path, new)\nprint(new.name)\nprint(new.exists())'),
])

RESPONSE = ('# 固定的模拟响应，不联网；需要已安装 requests\nimport requests\n'
            'from unittest.mock import patch\n'
            'response = requests.Response()\nresponse.status_code = 200\n'
            'response._content = b\'{"id": 1}\'\nresponse.encoding = "utf-8"\n')
http_programs = []
for method in ['get', 'post', 'put', 'patch', 'delete']:
    extra = ', json={"id": 1}' if method in ['post', 'put', 'patch'] else ''
    http_programs.append(RESPONSE + f'with patch("requests.{method}", return_value=response):\n    result = requests.{method}("https://example.invalid/orders"{extra})\n    print(result.status_code)')
for option, value in [('params', '{"page": 2}'), ('headers', '{"Accept": "application/json"}'),
                      ('json', '{"id": 1}'), ('data', '{"name": "Cu"}'), ('timeout', '10')]:
    method = 'post' if option in ['json', 'data'] else 'get'
    http_programs.append(RESPONSE + f'with patch("requests.{method}", return_value=response) as request:\n    requests.{method}("https://example.invalid/orders", {option}={value})\n    print(request.call_args.kwargs["{option}"])')
http_programs += [RESPONSE + 'print(response.status_code)', RESPONSE + 'print(response.text)',
                 RESPONSE + 'print(response.content)', RESPONSE + 'print(response.json())',
                 RESPONSE + 'print(response.raise_for_status())']
put('api-requests', http_programs)
put('datetime', ['from datetime import datetime\n# 当前时间每次运行可能不同\nprint(datetime.now().isoformat(timespec="seconds"))',
    'from datetime import date\n# 当前日期依运行环境变化\nprint(date.today())',
    'from datetime import date, timedelta\nprint(date(2026, 10, 15) + timedelta(days=1))',
    'from datetime import datetime\nnow = datetime(2026, 10, 15, 9, 30)\nprint(now.strftime("%Y-%m-%d"))',
    'from datetime import datetime\ntext = "2026-10-15"\nprint(datetime.strptime(text, "%Y-%m-%d"))'])
put('math', ['import math\n' + show(expr) for expr in ['math.sqrt(16)', 'math.ceil(4.2)', 'math.floor(4.8)', 'math.pi']])
put('random', ['import random\n# 固定种子，让此教学示例可重复\nrandom.seed(1)\nprint(random.randint(1, 10))',
    'import random\nrandom.seed(1)\nitems = ["Cu", "Ni"]\nprint(random.choice(items))',
    'import random\nrandom.seed(1)\nitems = [1, 2, 3]\nrandom.shuffle(items)\nprint(items)'])
put('regex', ['import re\ntext = "ORD123"\nmatch = re.search(r"\\d+", text)\nprint(match.group())',
    'import re\npattern = r"\\d+"\nprint(re.match(pattern, "123A").group())\nprint(re.match(pattern, "A123"))',
    'import re\nprint(re.findall(r"\\d+", "A12 B34"))',
    'import re\nprint(re.sub(r"\\d+", "#", "ORD123"))',
    'pattern = r"\\d+"\nprint(pattern)'])
put('collections-module', ['from collections import Counter\nitems = ["A", "A", "B"]\nprint(Counter(items))',
    'from collections import defaultdict\ndata = defaultdict(list)\ndata["Cu"].append(1)\nprint(dict(data))',
    'from collections import deque\nitems = deque([1, 2])\nitems.appendleft(0)\nprint(items)'])
put('statistics', ['import statistics\nvalues = [10, 20, 30]\nprint(statistics.mean(values))',
    'import statistics\nvalues = [10, 30, 20]\nprint(statistics.median(values))'])
put('itertools', ['from itertools import chain\na = [1, 2]\nb = [3]\nprint(list(chain(a, b)))',
    'from itertools import repeat\nprint(list(repeat("A", 3)))',
    'from itertools import islice\nitems = iter(range(10))\nprint(list(islice(items, 5)))'])
put('sys', ['import sys\n# 版本随运行环境变化\nprint(sys.version.split()[0])',
    'import sys\nfrom pathlib import Path\nprint(Path(sys.executable).name)',
    'import sys\n# 设定本例的模拟命令行参数\nsys.argv = ["main.py", "orders.csv"]\nprint(sys.argv)',
    'import sys\nsys.path.insert(0, "example_modules")\nprint(sys.path[0])',
    'import sys\ntry:\n    sys.exit(1)\nexcept SystemExit as error:\n    print(error.code)'])
put('time', ['import time\ntime.sleep(0.01)\nprint("Resumed")',
    'import time\n# 时间戳每次运行可能不同\nprint(time.time())'])
log_prefix = 'import logging, sys\nlogging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(levelname)s: %(message)s")\n'
put('logging', [log_prefix + f'logging.{level}("{message}")' for level, message in [('debug','value'), ('info','Started'), ('warning','Slow'), ('error','Failed')]] + [
    '# exception 会附带当前异常信息\nimport logging, sys\nlogging.basicConfig(stream=sys.stdout, format="%(levelname)s: %(message)s")\ntry:\n    int("abc")\nexcept ValueError:\n    logging.exception("Failed")'])

# Package management is terminal syntax. Demonstrate the matching help command;
# do not install, uninstall, or download packages just to author this reference.
pip_options = [['install'], ['install'], ['uninstall'], ['list'], ['show'], ['freeze'], ['install'], ['install']]
put('pip', ['# 用当前解释器查看此命令的帮助；不安装或删除包\nimport subprocess, sys\n'
            f'command = [sys.executable, "-m", "pip", {json.dumps(option[0])}, "--help"]\n'
            'result = subprocess.run(command, capture_output=True, text=True, check=True)\n'
            'print(next(line.strip() for line in result.stdout.splitlines() if line.strip()))' for option in pip_options])
put('virtual-environment', [
    '# 在临时目录创建演示环境，退出时清理\nimport tempfile, venv\nfrom pathlib import Path\nwith tempfile.TemporaryDirectory() as folder:\n    target = Path(folder) / ".venv"\n    venv.EnvBuilder(with_pip=False).create(target)\n    print((target / "pyvenv.cfg").is_file())',
    '# 这是 shell 命令；Python 示例只打印它，不执行\nprint("source .venv/bin/activate")',
    '# 这是 PowerShell 命令；Python 示例只打印它，不执行\nprint(r".venv\\Scripts\\Activate.ps1")',
    '# 这是激活环境后的 shell 命令，不是 Python 函数\nprint("deactivate")',
])
put('type-hints', [
    'name: str = "Rebecca"\nprint(name)', 'quantity: int = 10\nprint(quantity)',
    'price: float = 8500.5\nprint(price)', 'active: bool = True\nprint(active)',
    'def total(qty: int):\n    return qty * 2\nprint(total(3))',
    'def get_name() -> str:\n    return "Rebecca"\nprint(get_name())',
    'def save() -> None:\n    pass\nprint(save())',
    'products: list[str] = ["Cu", "Ni"]\nprint(products)',
    'ids: list[int] = [1, 2]\nprint(ids)',
    'prices: dict[str, int] = {"Cu": 10}\nprint(prices)',
    'point: tuple[int, int] = (10, 20)\nprint(point)',
    'products: set[str] = {"Cu", "Ni"}\nprint(sorted(products))',
    'name: str | None = None\nprint(name)', 'price: int | float = 8500.5\nprint(price)',
    'from typing import Any\nvalue: Any = "Cu"\nprint(value)',
])
put('dataclasses', ['from dataclasses import dataclass\n@dataclass\nclass Order:\n    id: int\nprint(Order(1001))',
    'from dataclasses import dataclass\n@dataclass\nclass Order:\n    order_id: int\nprint(Order(1001).order_id)',
    'from dataclasses import dataclass\n@dataclass\nclass Order:\n    status: str = "Pending"\nprint(Order().status)',
    'from dataclasses import dataclass, field\n@dataclass\nclass Order:\n    items: list = field(default_factory=list)\nprint(Order().items)',
    'from dataclasses import dataclass, field\n@dataclass\nclass Order:\n    items: list = field(default_factory=list)\na = Order()\nb = Order()\na.items.append("Cu")\nprint(a.items)\nprint(b.items)'])

put('match-case', [f'status = "{value}"\nmatch status:\n{body}' for value, body in [
    ('Pending','    case "Pending":\n        print("Wait")'),
    ('Pending','    case "Pending":\n        print("Wait")'),
    ('Unknown','    case "Done":\n        print("Done")\n    case _:\n        print("Other")'),
    ('Processing','    case "Pending" | "Processing":\n        print("Wait")'),
    ('Copper','    case value:\n        print(value)'),
    ('Copper','    case value if len(value) > 3:\n        print("Long")'),
]])
put('walrus-operator', ['items = ["A", "B"]\nif count := len(items):\n    print(count)',
    'def get_value():\n    return 42\nprint(value := get_value())\nprint(value)'])
put('async-python', [
    'import asyncio\nasync def load_data():\n    return 42\nprint(asyncio.run(load_data()))',
    'import asyncio\nasync def fetch_data():\n    return 42\nasync def main():\n    value = await fetch_data()\n    print(value)\nasyncio.run(main())',
    'import asyncio\nasync def stream():\n    yield 1\n    yield 2\nasync def main():\n    async for item in stream():\n        print(item)\nasyncio.run(main())',
    'import asyncio\nclass Session:\n    async def __aenter__(self):\n        print("Opened")\n        return self\n    async def __aexit__(self, *args):\n        print("Closed")\nasync def main():\n    async with Session():\n        print("Working")\nasyncio.run(main())',
    'import asyncio\nasync def load_data():\n    return 42\ncoro = load_data()\nprint(asyncio.iscoroutine(coro))\nprint(asyncio.run(coro))',
])

keywords = {
    'False': PROGRAMS['boolean-values-truthy-falsy'][1], 'None': PROGRAMS['boolean-values-truthy-falsy'][2],
    'True': PROGRAMS['boolean-values-truthy-falsy'][0], 'and': PROGRAMS['logical-operators'][0],
    'as': PROGRAMS['modules-imports'][1], 'assert': 'quantity = 10\nassert quantity >= 0\nprint(quantity)',
    'async': PROGRAMS['async-python'][0], 'await': PROGRAMS['async-python'][1],
    'break': PROGRAMS['while-loops'][1], 'class': PROGRAMS['classes'][0], 'continue': PROGRAMS['while-loops'][2],
    'def': PROGRAMS['functions'][0], 'del': 'order = {"status": "Done"}\ndel order["status"]\nprint(order)',
    'elif': PROGRAMS['conditions'][1], 'else': PROGRAMS['conditions'][2], 'except': PROGRAMS['exceptions'][1],
    'finally': PROGRAMS['exceptions'][5], 'for': PROGRAMS['for-loops'][0], 'from': PROGRAMS['modules-imports'][2],
    'global': PROGRAMS['variable-scope'][2], 'if': PROGRAMS['conditions'][0], 'import': PROGRAMS['modules-imports'][0],
    'in': PROGRAMS['identity-membership'][2], 'is': PROGRAMS['identity-membership'][0],
    'lambda': PROGRAMS['functions'][12], 'nonlocal': PROGRAMS['variable-scope'][3],
    'not': PROGRAMS['logical-operators'][2], 'or': PROGRAMS['logical-operators'][1], 'pass': PROGRAMS['while-loops'][3],
    'raise': PROGRAMS['exceptions'][6], 'return': PROGRAMS['functions'][3], 'try': PROGRAMS['exceptions'][0],
    'while': PROGRAMS['while-loops'][0], 'with': PROGRAMS['context-managers'][0], 'yield': PROGRAMS['generators'][0],
    'match': PROGRAMS['match-case'][0], 'case': PROGRAMS['match-case'][1],
}
symbol_programs = ['print("Hello")', PROGRAMS['list'][2], PROGRAMS['dictionary'][1], PROGRAMS['conditions'][0],
    PROGRAMS['variables-assignment'][2], PROGRAMS['api-requests'][13],
    'for _ in range(3):\n    print("A")', PROGRAMS['functions'][8], PROGRAMS['functions'][9],
    PROGRAMS['dataclasses'][0], PROGRAMS['type-hints'][5], PROGRAMS['walrus-operator'][0],
    PROGRAMS['type-hints'][12], 'def todo():\n    ...\nprint(todo())', '# load orders\nprint("Ready")',
    PROGRAMS['escape-characters'][2]]
put('common-special-symbols', symbol_programs)
put('unpacking-spread-like', [
    'values = [8500, 10]\nprice, quantity = values\nprint(price, quantity)',
    'items = ["Cu", "Ni", "Al"]\nfirst, *rest = items\nprint(first)\nprint(rest)',
    'items = ["Cu", 10]\nprint(*items)',
    'def create_order(product, quantity):\n    print(product, quantity)\ndata = {"product": "Cu", "quantity": 10}\ncreate_order(**data)',
    'a = [1, 2]\nb = [3]\nprint([*a, *b])',
    'a = {"id": 1}\nb = {"id": 2}\nprint({**a, **b})',
    'items = [1, 2]\nprint((*items,))',
    'a = [1, 2]\nb = [2, 3]\nprint(sorted({*a, *b}))'])
put('delete', [
    'result = 10\ndel result\nprint("result" in locals())',
    'items = ["A", "B"]\ndel items[0]\nprint(items)',
    'items = [0, 1, 2, 3]\ndel items[1:3]\nprint(items)', keywords['del'],
    PROGRAMS['dictionary'][10], 'items = ["Copper", "Nickel"]\nitems.remove("Copper")\nprint(items)', PROGRAMS['list'][9]])
put('assert', [keywords['assert'],
    'quantity = -1\ntry:\n    assert quantity >= 0, "Invalid quantity"\nexcept AssertionError as error:\n    print(error)',
    'try:\n    assert False\nexcept AssertionError as error:\n    print(type(error).__name__)'])
put('command-line-script-pattern', ['def main():\n    print("Ready")\nmain()', 'print(__name__)',
    'print(__name__ == "__main__")', 'def main():\n    print("Ready")\nif __name__ == "__main__":\n    main()',
    PROGRAMS['sys'][2]])

# The last section remains a vocabulary reference, but every row gets its own
# short independent program rather than relying on the large end-to-end script.
real_world = [PROGRAMS['modules-imports'][2], PROGRAMS['modules-imports'][0], PROGRAMS['api-requests'][0],
    log_prefix + 'logging.info("Ready")', PROGRAMS['functions'][0], PROGRAMS['functions'][1],
    PROGRAMS['type-hints'][12], 'def load_orders(status=None):\n    print(status)\nload_orders()',
    'def load_orders() -> list[dict]:\n    return [{"id": 1}]\nprint(load_orders())',
    PROGRAMS['type-hints'][6], PROGRAMS['os'][1], 'api_url = None\nif not api_url:\n    print("Missing URL")',
    PROGRAMS['exceptions'][6], PROGRAMS['dictionary'][0], PROGRAMS['identity-membership'][1],
    'params = {}\nstatus = "Completed"\nparams["status"] = status\nprint(params)',
    PROGRAMS['api-requests'][0], PROGRAMS['api-requests'][5], PROGRAMS['api-requests'][9],
    PROGRAMS['api-requests'][14], PROGRAMS['api-requests'][13],
    show('Path("output/orders.json").as_posix()', 'from pathlib import Path'),
    show('Path("output/orders.json").parent.as_posix()', 'from pathlib import Path'),
    path_program('directory = path.parent / "output"\ndirectory.mkdir()\nprint(directory.is_dir())'),
    path_program('directory = path.parent / "a" / "b"\ndirectory.mkdir(parents=True)\nprint(directory.is_dir())'),
    path_program('path.parent.mkdir(exist_ok=True)\nprint(path.parent.is_dir())'),
    PROGRAMS['pathlib'][15], PROGRAMS['json'][1], PROGRAMS['json'][4], PROGRAMS['json'][5],
    path_program('path.write_text("Copper", encoding="utf-8")\nprint(path.read_text(encoding="utf-8"))'),
    PROGRAMS['exceptions'][0], PROGRAMS['exceptions'][1], PROGRAMS['exceptions'][3],
    RESPONSE + 'response.status_code = 500\ntry:\n    response.raise_for_status()\nexcept requests.RequestException as error:\n    print(type(error).__name__)',
    PROGRAMS['exceptions'][8], PROGRAMS['logging'][1], PROGRAMS['logging'][3], PROGRAMS['logging'][4],
    'orders = [{"id": 1}, {"id": 2}]\nprint(len(orders))', PROGRAMS['command-line-script-pattern'][3],
    PROGRAMS['command-line-script-pattern'][0]]
put('common-real-world-pattern', real_world)


def metadata():
    source = (ROOT / 'python-summary.html').read_text(encoding='utf-8')
    sections = {}
    clean = lambda value: html.unescape(re.sub('<[^>]+>', '', value)).strip()
    for match in re.finditer(r'<section id="([^"]+)">(.*?)</section>', source, re.S):
        rows = []
        for row in re.findall(r'<tr>(.*?)</tr>', match[2], re.S):
            cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
            if cells:
                rows.append([clean(cell) for cell in cells])
        sections[match[1]] = rows
    node = '''const fs=require('fs'),vm=require('vm');const s=fs.readFileSync('python-summary.html','utf8');const a=s.indexOf('const D = {')+10,z=s.indexOf('const X =',a);process.stdout.write(JSON.stringify(vm.runInNewContext('('+s.slice(a,z).trim().replace(/;$/,'')+')',{}, {timeout:1000})));'''
    dynamic = json.loads(subprocess.check_output(['node', '-e', node], cwd=ROOT, encoding='utf-8'))
    sections.update(dynamic)
    return sections


def main():
    sections = metadata()
    put('common-python-keywords', [keywords[row[0]] for row in sections['common-python-keywords']])
    output = {}
    count = 0
    for section, rows in sections.items():
        programs = PROGRAMS[section]
        if len(programs) != len(rows):
            raise ValueError(f'{section}: {len(programs)} programs for {len(rows)} rows')
        lessons = []
        for index, (row, program) in enumerate(zip(rows, programs), 1):
            code = f'# {index}. {row[0]} — {row[1]}\n' + program
            # Run only our authored programs, each with an isolated temporary cwd.
            with tempfile.TemporaryDirectory(prefix='python-summary-example-') as folder:
                process = subprocess.run([sys.executable, '-X', 'utf8', '-c', code], input='Rebecca\n',
                    capture_output=True, text=True, encoding='utf-8', cwd=folder, timeout=30)
            if process.returncode or process.stderr.strip():
                raise RuntimeError(f'{section} row {index}:\n{process.stderr}')
            if not process.stdout:
                raise ValueError(f'{section} row {index}: no printed output')
            lessons.append({'code': code, 'output': process.stdout.replace('\r\n', '\n').rstrip('\n')})
            count += 1
        output[section] = lessons
        print(f'{section}: {len(lessons)} outputs captured', flush=True)
    (ROOT / 'python-summary-runnable-data.js').write_text(
        '// Generated by scripts/build_python_summary_runnable.py; stdout from isolated runs.\n'
        + 'window.pythonSummaryRunnable = ' + json.dumps(output, ensure_ascii=False, indent=2) + ';\n', encoding='utf-8')
    print(f'COMPLETE: {len(output)} sections, {count} runnable examples', flush=True)


if __name__ == '__main__':
    main()
