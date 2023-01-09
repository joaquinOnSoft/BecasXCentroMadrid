from unittest import TestCase

from ..DWRClientMadridCenterDetails import DWRClientMadridCenterDetails


class TestDWRClientMadridCenterDetails(TestCase):

    @staticmethod
    def getCenter(center_id):
        client = DWRClientMadridCenterDetails(center_id)
        return client.read()

    def testRequestIES(self):
        res = self.getCenter(28041512)

        self.assertIsNotNone(res)
        self.assertEqual(res['Total 2018-2019'], '728')
        self.assertEqual(res['ESO 2018-2019'], '526')
        self.assertEqual(res['Bachillerato 2018-2019'], '202')
        # Check none existing columns have been added
        self.assertEqual(res['Infantil II Ciclo 2018-2019'], '')
        self.assertEqual(res['Educación Infantil Especial 2018-2019'], '')

    def testRequestCP_INF_PRI(self):
        res = self.getCenter(28006275)

        self.assertIsNotNone(res)
        self.assertEqual(res['Total 2018-2019'], '466')
        self.assertEqual(res['Infantil II Ciclo 2018-2019'], '150')
        self.assertEqual(res['Primaria 2018-2019'], '316')

    def testRequestNoData(self):
        res = self.getCenter(28078262)

        self.assertIsNotNone(res)
        self.assertEqual(res['Total 2018-2019'], '')
        self.assertEqual(res['ESO 2018-2019'], '')
        self.assertEqual(res['Bachillerato 2018-2019'], '')

    def testRequestBugEncoding(self):
        res = self.getCenter(28023881)

        self.assertIsNotNone(res)
        self.assertEqual(res['Total 2018-2019'], '156')
        self.assertEqual(res['Infantil II Ciclo 2018-2019'], '40')
        self.assertEqual(res['Primaria 2018-2019'], '99')
        self.assertEqual(res['Educación Básica Obligatoria 2018-2019'], '12')
        self.assertEqual(res['Educación Infantil Especial 2018-2019'], '5')

        self.assertEqual(res['Educación Básica Obligatoria 2014-2015'], '0')
        self.assertEqual(res['Educación Básica Obligatoria 2015-2016'], '4')
        self.assertEqual(res['Educación Básica Obligatoria 2016-2017'], '7')
        self.assertEqual(res['Educación Básica Obligatoria 2017-2018'], '10')
        self.assertEqual(res['Educación Básica Obligatoria 2018-2019'], '12')

    def testRequestFP(self):
        res = self.getCenter(28041354)

        self.assertIsNotNone(res)
        self.assertEqual(res['FP GM 2018-2019'], '71')
        self.assertEqual(res['FP GS 2018-2019'], '0')
        self.assertEqual(res['FPB 2018-2019'], '64')

    def testRequestPCPI(self):
        res = self.getCenter(28041354)

        self.assertIsNotNone(res)
        self.assertEqual(res['PCPI: Módulos Voluntarios 2018-2019'], '0')
        self.assertEqual(res['PCPI: Módulos Voluntarios 2017-2018'], '0')
        self.assertEqual(res['PCPI: Módulos Voluntarios 2016-2017'], '0')
        self.assertEqual(res['PCPI: Módulos Voluntarios 2015-2016'], '0')
        self.assertEqual(res['PCPI: Módulos Voluntarios 2014-2015'], '12')

    def testRequestPCPIEspecial(self):
        res = self.getCenter(28000522)

        self.assertIsNotNone(res)
        self.assertEqual(res['PCPI: Especial 2018-2019'], '0')
        self.assertEqual(res['PCPI: Especial 2017-2018'], '0')
        self.assertEqual(res['PCPI: Especial 2016-2017'], '0')
        self.assertEqual(res['PCPI: Especial 2015-2016'], '0')
        self.assertEqual(res['PCPI: Especial 2014-2015'], '10')
        self.assertEqual(res['Programas Profesionales Modalidad Especial 2018-2019'], '18')
        self.assertEqual(res['Programas Profesionales Modalidad Especial 2017-2018'], '16')
        self.assertEqual(res['Programas Profesionales Modalidad Especial 2016-2017'], '20')
        self.assertEqual(res['Programas Profesionales Modalidad Especial 2015-2016'], '21')
        self.assertEqual(res['Programas Profesionales Modalidad Especial 2014-2015'], '12')

