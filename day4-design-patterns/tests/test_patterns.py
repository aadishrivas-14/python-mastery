import sys
sys.path.insert(0, '../src')
from patterns import *

def test_singleton():
    s1 = Singleton()
    s2 = Singleton()
    assert s1 is s2

def test_factory():
    factory = ShapeFactory()
    circle = factory.create_shape("circle")
    assert circle.draw() == "Drawing Circle"
    square = factory.create_shape("square")
    assert square.draw() == "Drawing Square"

def test_builder():
    pizza = PizzaBuilder().add_cheese().add_pepperoni().build()
    assert "cheese" in pizza.ingredients
    assert "pepperoni" in pizza.ingredients

def test_prototype():
    original = Prototype({"name": "Original", "data": [1, 2, 3]})
    clone = original.clone()
    assert clone.data["name"] == "Original"
    clone.data["data"].append(4)
    assert len(original.data["data"]) == 3

def test_adapter():
    class OldSystem:
        def old_method(self):
            return "old"
    adapter = Adapter(OldSystem())
    assert adapter.new_method() == "old"

def test_decorator():
    class Component:
        def operation(self):
            return "Component"
    decorated = LoggerDecorator(Component())
    result = decorated.operation()
    assert "Component" in result

def test_facade():
    computer = ComputerFacade()
    result = computer.start()
    assert "started" in result.lower()

def test_proxy():
    proxy = ImageProxy("photo.jpg")
    assert proxy.loaded == False
    proxy.display()
    assert proxy.loaded == True

def test_observer():
    subject = Subject()
    observer1 = Observer("O1")
    observer2 = Observer("O2")
    subject.attach(observer1)
    subject.attach(observer2)
    subject.notify("event")
    assert observer1.received == "event"
    assert observer2.received == "event"

def test_strategy():
    context = PaymentContext()
    context.set_strategy(CreditCardStrategy())
    assert "credit card" in context.pay(100).lower()
    context.set_strategy(PayPalStrategy())
    assert "paypal" in context.pay(100).lower()

def test_command():
    receiver = Receiver()
    cmd = ConcreteCommand(receiver, "action")
    cmd.execute()
    assert receiver.state == "action"
    cmd.undo()
    assert receiver.state == ""

def test_state():
    context = StateContext()
    assert context.state.name() == "StateA"
    context.request()
    assert context.state.name() == "StateB"

def test_iterator():
    collection = CustomIterator([1, 2, 3, 4, 5])
    result = [x for x in collection]
    assert result == [1, 2, 3, 4, 5]

def test_template():
    processor = CSVProcessor()
    result = processor.process()
    assert "CSV" in result

def test_chain():
    h1 = ConcreteHandler1()
    h2 = ConcreteHandler2()
    h3 = ConcreteHandler3()
    h1.set_next(h2).set_next(h3)
    assert h1.handle(1) == "Handler1"
    assert h1.handle(2) == "Handler2"
    assert h1.handle(3) == "Handler3"

class Observer:
    def __init__(self, name):
        self.name = name
        self.received = None
    def update(self, data):
        self.received = data

class PaymentContext:
    def __init__(self):
        self.strategy = None
    def set_strategy(self, strategy):
        self.strategy = strategy
    def pay(self, amount):
        return self.strategy.pay(amount)

class CreditCardStrategy:
    def pay(self, amount):
        return f"Paid {amount} with Credit Card"

class PayPalStrategy:
    def pay(self, amount):
        return f"Paid {amount} with PayPal"

class Receiver:
    def __init__(self):
        self.state = ""
    def action(self, cmd):
        self.state = cmd
    def undo_action(self):
        self.state = ""

class ConcreteCommand:
    def __init__(self, receiver, action):
        self.receiver = receiver
        self.action = action
    def execute(self):
        self.receiver.action(self.action)
    def undo(self):
        self.receiver.undo_action()

class StateContext:
    def __init__(self):
        self.state = StateA(self)
    def request(self):
        self.state.handle()

class StateA:
    def __init__(self, context):
        self.context = context
    def name(self):
        return "StateA"
    def handle(self):
        self.context.state = StateB(self.context)

class StateB:
    def __init__(self, context):
        self.context = context
    def name(self):
        return "StateB"
    def handle(self):
        self.context.state = StateA(self.context)

class CSVProcessor(DataProcessor):
    def read(self):
        return "CSV"

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request == 1:
            return "Handler1"
        return super().handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request == 2:
            return "Handler2"
        return super().handle(request)

class ConcreteHandler3(Handler):
    def handle(self, request):
        if request == 3:
            return "Handler3"
        return super().handle(request)
