class Library:
    def __init__(self, books, secret_code):
        # Protected ატრიბუტი: _books, გამოყენებულია წიგნების სიის შესანახად, შეიძლება გამოყენებულ იქნეს კლასის და მის შვილობილი კლასების მიერაც
        self._books = books  

        # Private ატრიბუტი: __secretCode, გამოყენებულია საიდუმლო კოდის დასამალად, რომ კლასის გარეთ წვდომა სიფრთხილეა
        self.__secretCode = secret_code  

    # სტატიკური მეთოდი: არ აქვს წვდომა self ან cls პარამეტრებზე და დამოუკიდებელია კლასის ატრიბუტებისგან
    @staticmethod
    def calculate_late_fee(days_late, fee_per_day):
        return days_late * fee_per_day

    def get_secret_code(self):
        return self.__secretCode

    # კლასის მეთოდი: აქვს წვდომა ობიექტებზე self-ის მეშვეობით
    @classmethod
    def example_class_method(cls):
        print("This is a class method")