from abc import ABC, abstractmethod
class Week(ABC):
    def today(self, date):
        print('Is today {}?'.format(date))
#this function passes in an unknown argument
        @abstractmethod
        def Friday(self, date):
            pass

class Day(Week):

    def Friday(self, date):
        print('Today is {} the 13th.'.format(date))

obj = Day()
obj.today('Friday')
obj.Friday('Friday')

