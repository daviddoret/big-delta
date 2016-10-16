class NumberWithBase:
    def __init__(self, base):
        self.base = base
        self.value = 0
        self.digits = [0]

    def increment(self):
        self.value += 1
        stop = len(self.digits)
        for pos in range(0, len(self.digits) + 1):
            if self.get_digit(pos) == self.base - 1:
                self.set_digit(pos, 0)
            else:
                new_val = self.get_digit(pos) + 1
                self.set_digit(pos, new_val)
                break

    def get_digit(self, pos):
        while len(self.digits) < pos + 1:
            self.digits.append(0)
        return self.digits[pos]

    def set_digit(self, pos, val):
        while len(self.digits) < pos + 1:
            self.digits.append(0)
        self.digits[pos] = val

    def get_small_delta(self):
        digit_sum = 0
        for i in self.digits:
            digit_sum = digit_sum + i
        return digit_sum

def show_demo_01(max_n):
    numbers_with_base = []
    big_delta = 0

    for n in range(2,max_n):
        numbers_with_base.append(NumberWithBase(n))

    line = "n\tΔ"
    for nb in numbers_with_base:
        line = "{0}\tδ{1}".format(line, nb.base)
    print(line)

    previous_f = 0
    for n in range(0,max_n):
        line = ""
        f = 0
        for nb in numbers_with_base:
            small_delta = nb.get_small_delta()
            if nb.base <= n + 1:
                f += small_delta
                line = "{0}\t{1}".format(line, small_delta)
            else:
                line = "{0}\t".format(line)
            nb.increment()
        diff = f - previous_f
        if diff > big_delta:
            big_delta = diff
        line = "{0}\t{1}{2}".format(n,big_delta,line)
        print(line)
        previous_f = f

show_demo_01(1024)

