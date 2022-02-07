
class StringEditting:
    def __init__(self, total_str, old_substr, new_substr):
        self.total_str_ = total_str
        self.old_substr_ = old_substr
        self.new_substr_ = new_substr
        self.new_str = self.total_str_
        result = self.find()
        if result == False:
            print('your substr is not in total str')
        else:
            self.new_str = self.replace(result[0], result[1])


    def find(self):
        index_total, index_old = 0, 0
        start, end = 0, 0
        while index_total < len(self.total_str_):
            if self.total_str_[index_total] == self.old_substr_[index_old]:
                if index_old == 0:
                    start = index_total
                if index_old == len(self.old_substr_)-1:
                    end = index_total
                    return start, end

                index_total += 1
                index_old += 1
            else:
                index_total += 1
                index_old = 0
        return False

    def replace(self, start, end):
        return self.total_str_[:start]+self.new_substr_+self.total_str_[end+1:]

    def get(self):
        return self.new_str

if __name__ == "__main__":
    obj = StringEditting('I love Java!!!', 'Java', 'Python')
    output = obj.get()
    print(output)
