class Stec:
    def __init__(self):
        self.items = []

    def inc(self, x):
        self.items.append(x)

    def dec(self):
        return self.items.pop()


if __name__ == '__main__':
    st = Stec()
    for i in 'позавчера':
        st.inc(i)

    for i in 'позавчера':
        print(st.dec(), end='')
