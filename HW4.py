class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        """
        Function __init__ initiates parameters
        :param day: int
        :param month: int
        :param year: int
        """
        self.day = day
        self.month = month
        self.year = year
        Date.isvalid(self)

    def __str__(self) -> str:
        """
        function __str__ gets a parameter self: Date
        return a format string as "day.month.year"
        :param self: Date
        :return: str
        """
        if self.month >= 10 and self.day >= 10:
            return f"{self.day}." + "0%a" % self.month + f".{self.year}"
        else:
            if not self.month >= 10 and self.day >= 10:
                return f"{self.day}." + "0%a" % self.month + f".{self.year}"
            else:
                if not self.month >= 10 and not self.day >= 10:
                    return "0%a" % self.day+"." + "0%a" % self.month + f".{self.year}"
                else:
                    return "0%a" % self.day + f".{self.month}.{self.year}"

    def __eq__(self, other_date) -> bool:
        """
        Function __eq__ gets self : Date, other_eq : Date .
        Function Returns if self == other_eq.
        :param self: Date
        :param other_date: Date
        :return: bool
        """
        flag = (self.year == other_date.year) and (self.month == other_date.month) and (self.day == other_date.day)
        return flag

    def __sub__(self, other_dt) -> int:
        """
        Function __sub__ gets self : Date, other_dt : Date .
        Function returns how many days separates between self and other_dt.
        example .__sub__(Date1(1,1,1999),Date2(5,1,1999)) -> 4
        :return: int
        """
        if self.year > other_dt.year or self.month > other_dt.month and self.day < other_dt.day:
            tempdate = other_dt
            selfsub = self
        else:
            tempdate = self
            selfsub = other_dt
        counter = 0
        flag_sub = True
        while flag_sub:
            if tempdate.year == selfsub.year:
                if tempdate.month == selfsub.month:
                    if tempdate.day == selfsub.day:
                        flag_sub = False
            tempdate = Date.get_next_day(tempdate)
            counter += 1
        return counter

    def __gt__(self, other_greater_than) -> bool:
        """
        Function __gt__ gets self : Date, other_greater_than : Date .
        Function Returns if self > other_less_equal.
        :param self: Date
        :param other_greater_than: Date
        :return: bool
        """
        if self.year > other_greater_than.year or self.month > other_greater_than.month \
           and self.day > other_greater_than.day:
            return True
        else:
            return False

    def __lt__(self, other_date) -> bool:
        """
        Function __lt__ gets self : Date, other_date : Date .
        Function Returns if self < other_less_equal.
        :param self: Date
        :param other_date: Date
        :return: bool
        """
        if self.year < other_date.year or self.month < other_date.month \
         or self.day < other_date.day:
            return True
        else:
            return False

    def __ge__(self, other_greater_equal) -> bool:
        """
        Function __ge__ except 2 parameters
        self : Date, other_greater_equal : Date.
        Returns if self >= other_greater_equal.
        :param self: Date
        :param other_greater_equal: Date
        :return: Bool
        """
        greater_flag = self.year > other_greater_equal.year or self.month > other_greater_equal.month and self.day > other_greater_equal.day
        equal_flag = (self.year == other_greater_equal.year) and (self.month == other_greater_equal.month) and (self.day == other_greater_equal.day)
        if equal_flag or greater_flag:
            return True
        else:
            return False

    def __ne__(self, other_not_equal) -> bool:
        """
        Function __ne__ gets self : Date, other_not_equal : Date .
        Function Returns if self != other_date.
        :param self: Date
        :param other_not_equal: Date
        :return: bool
        """
        equal_flag = (self.year != other_not_equal.year) or (self.month != other_not_equal.month) or (self.day != other_not_equal.day)
        return equal_flag

    def __le__(self, other_less_equal) -> bool:
        """
        Function __le__ gets self : Date, other_less_equal : Date .
        Function Returns if self <= other_less_equal.
        :param self: Date
        :param other_less_equal: Date
        :return: bool
        """
        flag1 = self.year > other_less_equal.year or self.month > other_less_equal.month and self.day > other_less_equal.day
        equal_flag = (self.year == other_less_equal.year) and (self.month == other_less_equal.month) and (self.day == other_less_equal.day)
        if equal_flag or not flag1:
            return True
        else:
            return False

    def get_next_day(self) -> "Date":
        """
        Function get_next_day gets a parameter self: date
        and returns the next day.
        example get_next_day(Date(1,1,1999)) ->  Date(2,1,1999)
        :param self: Date
        :return: Date
        """
        try:
            return Date(self.day+1, self.month, self.year)
        except:
            try:
                return Date(1, self.month+1, self.year)
            except:
                try:
                    return Date(1, 1, self.year+1)
                except:
                    return TypeError(f"Invalid Date")

    def get_next_days(self, days_to_add: int) -> "Date":
        """
        Function get_next_days gets parameters self: date days_to_add: int,
        and returns the future Date after x amount of days.
        example get_next_days(Date(1,1,1999) ,days_to_add = 2) ->  Date(3,1,1999)
        :param self: Date
        :param days_to_add: int
        :return: Date
        """
        tempdate = self
        for i in range(days_to_add):
            try:
                tempdate = Date.get_next_days(tempdate)
            except TypeError:
                return TypeError(f"Invalid Date")
        return tempdate

    def isvalid(self) -> TypeError:
        """
        Function isvalid except parameter self : Date
        and check if isvalid , if invalid raise TypeError
        requirements:
                1) Leap year, february has 29 days else hase 28 days.
                2) months 4,6,9,11 has 30 days during the month
                3) months 1,3,7,8,10,12 has 31 Days during the month
        :param self: Date
        :return: TypeError
        """
        if not isinstance(self.day, int) or not (1 <= self.day <= 31):
            raise TypeError("Day must be between 1 - 31 ")
        if not isinstance(self.month, int) or not (1 <= self.month <= 12):
            raise TypeError("Month must be between 1 - 12 ")
        if not isinstance(self.year, int) or not 1000 <= self.year <= 9999:
            raise TypeError("Year must be between 1000 - 9999 ")
        if self.month == 2:
            if self.year % 4 == 0 or self.year % 4 == 0 \
                    and self.year % 100 == 0 \
                    and self.year % 400 != 0:
                if self.day > 29:
                    raise TypeError(f"Date is invalid - Day: {self.day}, Can't be at Month: {self.month}, on Year: {self.year}.")
                else:
                    if self.day > 28:
                        raise TypeError(f"Date is invalid - Day: {self.day}, Can't be at Month: {self.month}, on Year: {self.year}.")
        if self.month == 4 or self.month == 6 \
                or self.month == 9 or self.month == 11:
            if self.day > 30:
                raise TypeError(f"Date is invalid - Day: {self.day}, Can't be at Month: {self.month}, on Year: {self.year}.")
        if self.month == 1 or self.month == 3 or \
                self.month == 5 or self.month == 7 \
                or self.month == 8 or self.month == 10 \
                or self.month == 12:
            if self.day > 31:
                raise TypeError(f"Date is invalid - Day: {self.day}, Can't be at Month: {self.month}, on Year: {self.year}.")