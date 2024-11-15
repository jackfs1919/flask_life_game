##%%
# import pandas as pd
# from sktime.utils.plotting import plot_series
# from scipy.interpolate import lagrange
# import numpy as np

# df = pd.read_csv("Tesla_empty.csv", sep=',', index_col=['Date'], date_format=lambda col: pd.to_datetime(col, format=('%m/%d/%Y')))
# df.sort_index(inplace=True)
# mask = df.isna().any(axis=1)
# rows_with_null_values = df.loc[mask]
# df['Open'].fillna(df['Open'].median())
# df['Open'].interpolate(method='pad', limit=1)
# df['Open'].interpolate(method='nearest', limit=1)
# poly = lagrange(x, y)
# int_value_lag = np.polynominal.Polynominal(poly.coef[::-1])(interpolation_point)
# df['Open'].fillna(int_value_lag)
# rows_with_null_values
# plot_series(df['Open'])
class UserRegistry:
    """Реестр всех пользователей для проверки уникальности логинов."""
    logins = set()  # Множество для хранения уникальных логинов

class UserMail:
    def __init__(self, login, email):
        self._login = None  # Временно храним логин в другом атрибуте
        self.login = login  # Используем свойство для установки логина
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        # Проверяем корректность email
        if isinstance(value, str) and value.count('@') == 1 and '.' in value[(value.find('@') + 1):]:
            self.__email = value
        else:
            print(f'ErrorMail: {value}')

    email = property(fget=get_email, fset=set_email)

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        if not isinstance(value, str):
            raise TypeError(f'{value} не является строкой')
        
        if value in UserRegistry.logins:
            raise ValueError(f'Логин {value} уже имеется в системе')
        
        UserRegistry.logins.add(value)
        self._login = value

jim = UserMail("aka47", 'hello@com.org')
print(isinstance(type(jim).login, property))
print(f'Jim login is {jim.login}')
try:
    bim = UserMail("aka47", 'world@com.org')
except ValueError as e:
    print(e)
jim.login = 'aka48'
print(f'Jim login is {jim.login}')
bim = UserMail("aka47", 'world@com.org')
print(f'Bim login is {bim.login}')