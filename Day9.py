from sklearn import linear_model
input = raw_input()
number = int(input.split()[0])
size = int(input.split()[1])
X = []
Y = []
queries = []
if 1<=number<=10 and 5<=size<=100:
    for i in range(size):
        values = raw_input()
        temp = []
        temp.append(float(values.split()[0]))
        temp.append(float(values.split()[1]))
        X.append(temp)
        Y.append(float(values.split()[-1]))

    queryNo = int(raw_input())
    if 1<queryNo<=100:
        for i in range(queryNo):
            values = raw_input()
            temp = []
            temp.append(float(values.split()[0]))
            temp.append(float(values.split()[1]))
            queries.append(temp)
    # x = [[0.18, 0.89], [1.0, .26], [.92, .11], [.07, .37], [.85, .16], [.99, .41], [.87, .47]]
    # y = [109.85, 155.72, 137.66, 76.17, 139.75,162.6, 151.77]
    lm = linear_model.LinearRegression()
    lm.fit(X, Y)
    a = lm.intercept_
    b = lm.coef_

    for each in queries:
        print round(a + each[0] * b[0] + each[1] * b[1], 2)