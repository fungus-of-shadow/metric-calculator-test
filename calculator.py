"""
我改进的部分：
1. 针对caculate_mean():
    a) 利用assert确保有数据数据
    b) 利用assert确保数据的类型是有效的,数据得是数字类型的
2. 针对calculate_accuracy():
    a) 至少得确保两个序列一样长，通过添加assert避免了案例test_calculate_accuracy_different_lengths失效
    b) 利用assert确保数据的类型是有效的,数据得是数字类型的
3. 针对add_metric():
    a) 至少该确保输入的新的精确率是有效数据

"""


class MetricCalculator:
    def __init__(self):
        self.results = []

    def calculate_mean(self, data):
        assert len(data) > 0, "数据不得为空"  # 确保有数据
        for obj in data:
            assert isinstance(obj, (int, float)), "data中的数据必须为float/int类型"
        return sum(data) / len(data)

    def calculate_accuracy(self, y_true, y_pred):
        assert len(y_true) == len(y_pred), "请确保预测序列长度与真实序列长度一致"  # 确保预测数据和真实数据的数量一直
        assert len(y_true) > 0, "数据不得为空"  # 确保有数据
        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        return correct / len(y_true)

    def add_metric(self, name, value):
        assert isinstance(name, str), "name必须为str类型"
        assert isinstance(value, float), "value必须为float类型"
        assert 0. <= value <= 1., "value必须介于0~1"
        self.results.append((name, value))

    def get_results(self):
        return self.results


if __name__ == '__main__':
    metrical = MetricCalculator()
    print(metrical.get_results)
