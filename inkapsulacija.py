class Pupil:
    __age=0

    def set_age(self, value:int):
        if value<0:
            print('error')

        else:
            
            #raise ValueError()
            self.__age=value

    def get_age(self):
        return self.__age
pupil=Pupil()
pupil.set_age(1)
print(pupil.get_age())