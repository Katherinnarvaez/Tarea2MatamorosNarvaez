import tarea2


def test_Calculos():
    A = 25
    B = 10
    try:
        A = int(A)
        try:
            B = int(B)
            resta, suma, multiplicacion = tarea2.Calculos(A, B)
            assert resta >= 0, -10
        except ValueError:
            tipoB = type(B)
            assert tipoB == int, -10
    except ValueError:
        tipoA = type(A)
        assert tipoA == int, -10
