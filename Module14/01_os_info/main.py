from sklearn.linearmodel import LinearRegression

# Создаем искусственные данные
X = [[1], [2], [3], [4], [5]]  # Независимые переменные
y = [2, 3, 4, 5, 6]  # Зависимая переменная

# Создаем объект модели линейной регрессии
model = LinearRegression()

# Обучаем модель на данных
model.fit(X, y)

# Выводим коэффициенты линейной регрессии
print("Коэффициенты линейной регрессии:")
print("Коэффициент наклона (a):", model.coef[0])
print("Свободный член (b):", model.intercept_)
