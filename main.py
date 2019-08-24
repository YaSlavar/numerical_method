from math import *


class Integral:

    def __init__(self, a, b, eps, step, func):
        """
        Вычисление оперделенных интегралов численными методами
        :param a: левый предел интегрирования (float)
        :param b: правый предел интегрирования (float)
        :param eps: погрешность вычисления (float)
        :param step: шаг сканирования (float)
        :param func: вычисляемая функция (str)
        """
        self.func = func
        self.a = a
        self.b = b
        self.eps = eps
        self.step = step
        eps_str = '{:f}'.format(self.eps)
        eps_str = eps_str.rstrip("0")
        self.after_dicimal = len(eps_str.split(".")[1])

    def function(self, x):
        exec("x={}\nres={}".format(x, self.func))
        return locals()['res']

    def Metod_Levych_Pryamougolnikov(self, a, b, step):
        h = (b - a) / step
        x = a
        summ = 0
        detision = "integral = {}*(".format(step)
        for i in range(int(h)):
            f_x = round(self.function(x), self.after_dicimal)
            summ += f_x
            print("x={} f(x)={}".format(x, f_x))
            if i+1 == h:
                detision += "{})".format(f_x)
            else:
                detision += "{} + ".format(f_x)
            x += step
        summ = summ * step
        print("{} = {}".format(detision, round(summ, self.after_dicimal)))

    def Metod_Srednich_Pryamougolnikov(self, a, b, step):
        h = (b - a) / step
        x = a + (step / 2)
        summ = 0
        detision = "integral = {}*(".format(step)
        for i in range(int(h)):
            f_x = round(self.function(x), self.after_dicimal)
            summ += f_x
            print("x={} f(x)={}".format(x, f_x))
            if i + 1 == h:
                detision += "{})".format(f_x)
            else:
                detision += "{} + ".format(f_x)
            x += step
        summ = summ * step
        print("{} = {}".format(detision, round(summ, self.after_dicimal)))

    def Metod_Pravych_Pryamougolnikov(self, a, b, step):
        h = (b - a) / step
        x = a + step
        summ = 0
        detision = "integral = {}*(".format(step)
        for i in range(int(h)):
            f_x = round(self.function(x), self.after_dicimal)
            summ += f_x
            print("x={} f(x)={}".format(x, f_x))
            if i + 1 == h:
                detision += "{})".format(f_x)
            else:
                detision += "{} + ".format(f_x)
            x += step
        summ = summ * step
        print("{} = {}".format(detision, round(summ, self.after_dicimal)))

    def Metod_Trapeciy(self, a, b, step):
        h = (b - a) / step
        x = a
        summ = 0
        detision = "integral = {}*(f0_fn__2 + (".format(step)
        for i in range(1, int(h)+1):
            x += step
            f_x = round(self.function(x), self.after_dicimal)
            print("x={} f(x)={}".format(x, f_x))
            if i < h - 1:
                summ += f_x
                detision += "{} + ".format(f_x)
            elif i < h:
                summ += f_x
                detision += "{})".format(f_x)
            elif i == h:
                break
        f0_fn__2 = (round(self.function(a), self.after_dicimal) +
                    round(self.function(x), self.after_dicimal)) / 2
        detision = detision.replace("f0_fn__2", "({} + {}) / 2".format(round(self.function(a), self.after_dicimal),
                                                                       round(self.function(x), self.after_dicimal)))
        summ += f0_fn__2
        summ = summ * step
        print("{} = {}".format(detision, round(summ, self.after_dicimal)))

    def Metod_Parabol(self, a, b, step):
        h = (b - a) / step
        step_6 = step / 6
        x = a
        summ = 0
        detision = "integral = {}/6 * (".format(h)
        f_0 = round(self.function(x), self.after_dicimal)
        summ += f_0
        detision += "{} + ".format(f_0)
        print("x={} f(x)={}".format(x, f_0))
        for i in range(1, int(h) * 2):
            x += step / 2
            f_x = round(self.function(x), self.after_dicimal)
            if i % 2 is not 0:
                summ += f_x * 4
                detision += "4*({}) + ".format(f_x)
            else:
                summ += f_x * 2
                detision += "2*({}) + ".format(f_x)
            print("x={} f(x)={}".format(x, f_x))
        x += step / 2
        f_n = round(self.function(x), self.after_dicimal)
        summ += f_n
        summ = summ * step_6
        detision += "{})".format(f_n)
        print("x={} f(x)={}".format(x, f_n))
        print("{} = {}".format(detision, round(summ, self.after_dicimal)))

    def run(self):

        print('ВЫЧИСЛЕНИЕ ОПРЕДЕЛЕННЫХ ИНТЕГРАЛОВ\n\n')

        print('\nМетод левых прямоугольников\n')
        self.Metod_Levych_Pryamougolnikov(self.a, self.b, self.step)
        print('\nМетод средних прямоугольников\n')
        self.Metod_Srednich_Pryamougolnikov(self.a, self.b, self.step)
        print('\nМетод правых прямоугольников\n')
        self.Metod_Pravych_Pryamougolnikov(self.a, self.b, self.step)
        print('\nМетод трапеций\n')
        self.Metod_Trapeciy(self.a, self.b, self.step)
        print('\nМетод парабол\n')
        self.Metod_Parabol(self.a, self.b, self.step)


class Polynome:

    def __init__(self, _fns, _fns1, _fns2, _a_b, _eps):
        """
        Решение нелинейных уравнений
        :param _fns: исходная функция (str)
        :param _fns1: первая производная функции (str)
        :param _fns2: вотрая производная функции (str)
        :param _a_b: отрезок на котором предположительно есть корни (tuple)
        :param _eps: погрешность (float)
        """
        self.fns = _fns
        self.fns_1 = _fns1
        self.fns_2 = _fns2
        self.a = _a_b[0]
        self.b = _a_b[1]
        self.eps = _eps


    @staticmethod
    def func(funcs, x):
        exec("x={}\nres={}".format(x, funcs))
        return locals()['res']

    def run(self):
        after_dicimal = 5
        ab = [self.a, self.b]
        if self.func(self.fns, ab[0]) * self.func(self.fns, ab[1]) < 0:
            # Метод половинного деления

            print("Метод половинного деления")
            print("Дано: \n[{},{}]\n f(a) = {}, f(b) = {}\n"
                  .format(ab[0], ab[1], self.func(self.fns, ab[0]), self.func(self.fns, ab[1])))
            i = 1
            while True:
                c = round(((ab[0] + ab[1]) / 2), after_dicimal)
                print("Итерация {} \nc({}) = ({}+({}))/2  = {}\nf(c{}) = {}\n\n[{},{}][{},{}]"
                      .format(i, i, ab[0], ab[1], c, i,
                              round(self.func(self.fns, c), after_dicimal), ab[0], c, c, ab[1]))

                if self.func(self.fns, ab[0]) * self.func(self.fns, c) < 0:
                    ab[1] = round(c, after_dicimal)
                elif self.func(self.fns, ab[1]) * self.func(self.fns, c) < 0:
                    ab[0] = round(c, after_dicimal)

                i += 1
                if fabs(ab[0] - ab[1]) < 2 * self.eps:
                    c = (ab[0] + ab[1]) / 2
                    f_c = self.func(self.fns, c)
                    print("Значение функции: {} в точке: {}\n\n".format(round(f_c, after_dicimal),
                                                                        round(c, after_dicimal)))
                    break

            # Метод хорд и касательных
            ab = [self.a, self.b]

            print("Метод хорд и касательных")
            f_a = self.func(self.fns, ab[0])
            f_b = self.func(self.fns, ab[1])
            f_2_a = self.func(self.fns_2, ab[0])
            f_2_b = self.func(self.fns_2, ab[1])
            print("Дано: \n[{},{}]\nf(a) = {}, f(b) = {}\nf''(a) = {}, f''(b) = {}\n"
                  .format(ab[0], ab[1], self.func(self.fns, ab[0]), self.func(self.fns, ab[1]),
                          self.func(self.fns_2, ab[0]), self.func(self.fns_2, ab[1])))
            if abs(f_a - f_2_a) < abs(f_b - f_2_b):
                print("Для касательных используем [a.. , т.к. F''(a) ,ближе к краям отрезка")
                kas = self.a
                hord = self.b
            else:
                print("Для касательных используем ..b] , т.к. F''(b) ,ближе к краям отрезка")
                kas = self.b
                hord = self.a
            while True:
                hord_out = "hord = {} - (({} - ({}))*F({})) / (F({}) - F({}))\n"\
                    .format(round(hord, after_dicimal), round(kas, after_dicimal), round(hord, after_dicimal),
                            round(hord, after_dicimal),
                            round(kas, after_dicimal),
                            round(hord, after_dicimal))
                hord_out += " = {} - (({} - ({}))*{}) / ({} - {})"\
                    .format(round(hord, after_dicimal), round(kas, after_dicimal), round(hord, after_dicimal),
                              round(self.func(self.fns, hord), after_dicimal),
                              round(self.func(self.fns, kas), after_dicimal),
                              round(self.func(self.fns, hord), after_dicimal))
                print(hord_out)

                hord = round(hord - ((kas - hord)*self.func(self.fns, hord)) / (self.func(self.fns, kas) - self.func(self.fns, hord)), after_dicimal)
                print(" = {}".format(hord))

                kas_out = "kasat = {} - (F({}) / F'({}))\n"\
                    .format(round(kas, after_dicimal), round(kas, after_dicimal),
                            round(kas, after_dicimal))
                kas_out += " = {} - ({} / {})" \
                    .format(round(kas, after_dicimal), round(self.func(self.fns, kas)),
                            round(self.func(self.fns_1, kas), after_dicimal))
                print(kas_out)

                kas = round(kas - (self.func(self.fns, kas) / self.func(self.fns_1, kas)), after_dicimal)
                print(" = {}".format(kas))
                print("[{},{}]".format(hord, kas))

                if fabs(hord - kas) < 2 * self.eps:
                    answer = (hord + kas) / 2
                    print("Ответ: ", answer)
                    break
        else:
            print("На данном отрезке корня нет")


if __name__ == "__main__":

    fns_type = input("integral or polynome: ")

    if fns_type in ["i", "integral", "интеграл"]:
        fns = input("Введите функцию: ")
        a_b = tuple(map(float, input("Введите предел интегрирования [a b] через пробел: ").split()))
        eps = float(input("Введите погрешность: "))
        step = float(input("Введите шаг: "))
        # fns = "(x*x)/pow((1+x), 3)"
        # a_b = [0, 2.5]
        # eps = 0.00001
        # step = 0.5
        integ = Integral(a_b[0], a_b[1], eps, step, fns)
        integ.run()
    else:
        fns = input("Введите функцию: ")
        fns1 = input("Введите первую производную функции: ")
        fns2 = input("Введите вторую производную функции: ")
        a_b = tuple(map(int, input("Введите отрензок [a b] на котором есть корень: ").split()))
        eps = float(input("Введите погрешность: "))
        # fns = "x*x*x-15*x+6"
        # fns1 = "3*x*x-15"
        # fns2 = "6*x"
        # a_b = [1, 0]
        # eps = 0.001
        pol = Polynome(fns, fns1, fns2, a_b, eps)
        pol.run()
