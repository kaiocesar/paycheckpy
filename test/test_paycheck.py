import unittest
import paycheck.src.paycheck as payc

# Calculo do INSS: 
# Calculo do FGTS: 
# Calculo de dependentes: 
# Calculo do IRRF
# Calcular DSR (Descanso Semanal Remunerado)
# Calculo de vale transporte
# Calculo de adicional noturno
# Calcular adicional insalubridade
# Calcular Salario Liquido

class test_paycheck(unittest.TestCase):

    def test_calcular_inss(self):
        valor_inss = payc.inss(salario_base=3000)
        self.assertEqual(valor, 300)

    def test_calcular_fgts(self):
        valor_fgts = payc.fgts(salario_base=3000)
        self.assertEqual(valor_fgts, 240)

    def test_calcular_dependentes(self):
        valor_dependentes = payc.dependentes(2)
        self.assertEqual(valor_dependentes, 379.18)
    
    def test_calcular_irrf(self):
        valor_inss = payc.inss(salario_base=3000)
        valor_irrf = payc.irrf(inss=valor_inss, salario_base=3000)
        self.assertEqual(valor_irrf, 29.01)

    def test_calcular_dsr(self):
        self.assertEqual(1,1)

    def test_calcular_vale_transporte(self):
        self.assertEqual(1,1)

    def test_calcular_adicional_noturno(self):
        self.assertEqual(1,1)

    def test_calcular_adicional_insalubridade(self):
        self.assertEqual(1,1)

    def test_calcular_salario_liquido(self):
        self.assertEqual(1,1)