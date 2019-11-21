from Modeling import Model

o_p = Model(78.70833333, 1018.6666666666665, 288.05527916666665, 225.70833333333331, 0.625)
o_n = Model(69.16666667, 1013.3333333333335, 295.47041666666667, 160.0, 1.1666666666666667)

print(o_p.svm_predict(), o_p.lr_predict())
print(o_n.svm_predict(), o_n.lr_predict())
