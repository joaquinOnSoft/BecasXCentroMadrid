from datetime import date

import requests

from schoolarshipxcenter.reader.DWRClient import DWRClient


class DWRClientMadridCenterDetails(DWRClient):
    URL_BASE = "https://gestiona.comunidad.madrid/wpad_pub/dwr/exec/GraficasDWRAccion.obtenerGrafica.dwr"

    def __init__(self, center_id, url=None):
        self.center_id = center_id
        if url is None:
            super().__init__(self.URL_BASE)
        else:
            super().__init__(url)

    def __extract_data(self, content):
        """
        Extract statistic information from the DWR Ajax call returned by http://gestiona.comunidad.madrid

        :param content: Javascript returned from http://gestiona.comunidad.madrid/. It looks like this js code:
            var s0={};var s1=false;s0.correcto=s1;var s2=230;s0.height=s2;var s3=[];var s4={};var s5=null;s4.color=s5;var s6=false;s4.correcto=s6;var s7="Total";s4.nombreSerie=s7;var s8=[];var s9="2014-2015";s8[0]=s9;var s10="2015-2016";s8[1]=s10;var s11="2016-2017";s8[2]=s11;var s12="2017-2018";s8[3]=s12;var s13="2018-2019";s8[4]=s13;s4.serieX=s8;var s14=[];var s15=643;s14[0]=s15;var s16=623;s14[1]=s16;var s17=657;s14[2]=s17;var s18=684;s14[3]=s18;var s19=728;s14[4]=s19;s4.serieY=s14;
            s3[0]=s4;var s20={};var s21=null;s20.color=s21;var s22=false;s20.correcto=s22;var s23="ESO";s20.nombreSerie=s23;var s24=[];var s25="2014-2015";s24[0]=s25;var s26="2015-2016";s24[1]=s26;var s27="2016-2017";s24[2]=s27;var s28="2017-2018";s24[3]=s28;var s29="2018-2019";s24[4]=s29;s20.serieX=s24;var s30=[];var s31=422;s30[0]=s31;var s32=405;s30[1]=s32;var s33=449;s30[2]=s33;var s34=477;s30[3]=s34;var s35=526;s30[4]=s35;s20.serieY=s30;
            s3[1]=s20;var s36={};var s37=null;s36.color=s37;var s38=false;s36.correcto=s38;var s39="Bachillerato";s36.nombreSerie=s39;var s40=[];var s41="2014-2015";s40[0]=s41;var s42="2015-2016";s40[1]=s42;var s43="2016-2017";s40[2]=s43;var s44="2017-2018";s40[3]=s44;var s45="2018-2019";s40[4]=s45;s36.serieX=s40;var s46=[];var s47=221;s46[0]=s47;var s48=218;s46[1]=s48;var s49=208;s46[2]=s49;var s50=207;s46[3]=s50;var s51=202;s46[4]=s51;s36.serieY=s46;
            s3[2]=s36;s0.listaSeries=s3;var s52="Curso";s0.nombreEjeX=s52;var s53="Alumnos";s0.nombreEjeY=s53;var s54=0;s0.posX=s54;var s55=0;s0.posY=s55;var s56="/usr/aplic_ICM/temp/1580332252623.jpeg";s0.rutaFicheroGrafica=s56;var s57=null;s0.subtitulos=s57;var s58=1;s0.tipoGrafica=s58;
            var s59="N\u00DAMERO DE ALUMNOS";s0.titulo=s59;var s60="../../../ICMdownload/1580332252620.jpeg";s0.urlFicheroGrafica=s60;var s61=460;s0.width=s61;

            DWREngine._handleResponse('8195_1580332252722', s0);

        :return: Dictionary with the statistic information
        """
        data = {}

        if content is not None:
            content = content.replace('var ', '')
            content = content.replace('\n', '')
            content_array = content.split(';')

            temp_data = {}

            for item in content_array:
                param_array = item.split('=')
                if param_array is not None and len(param_array) == 2:
                    temp_data[param_array[0]] = param_array[1]

            data = self.__init_data_columns(data)
            data = self.__extract_students_data(temp_data, data)

        return data

    def __extract_students_data(self, params_array, data):
        for key in params_array:
            if "nombreSerie" in key:
                series_name_ref = params_array[key]
                series_name = params_array[series_name_ref]

                index = int(series_name_ref.replace("s", ""))
                # skip two positions
                index += 2
                init_index = index

                while params_array["s" + str(index)] != "[]":
                    index += 1

                shift = index
                index = init_index
                i = 0

                # Recover column titles
                while params_array["s" + str(index)] != "[]":
                    field_name = series_name + " " + params_array["s" + str(index)]

                    field_name = field_name.replace('"', '')
                    field_name = field_name.replace("\\u00E1", "á")
                    field_name = field_name.replace("\\u00F3", "ó")

                    field_value = params_array["s" + str(shift) + "[" + str(i) + "]"]
                    data[field_name] = params_array[field_value]

                    index += 1
                    i += 1

        return data

    def __init_data_columns(self, data):
        if data is not None:
            fields = ["Total",
                      "Educación Infantil Especial",
                      "Infantil I Ciclo", "Infantil II Ciclo",
                      "Educación Básica Obligatoria", "Primaria",
                      "ESO", "Bachillerato",
                      "FP GM", "FP GS", "FPB",
                      "PCPI: Módulos Voluntarios", "PCPI: Especial",
                      "Programa Formación Transición Vida Adulta",
                      "Programas Profesionales Modalidad Especial"]
            current_year = date.today().year

            for field in fields:
                for year in range(current_year - 5, current_year):
                    field_name = field + " " + str(year - 1) + "-" + str(year)
                    data[field_name] = ''

        return data

    def read(self):
        content = None

        self.add_param("callCount", 1)
        self.set_script_name("GraficasDWRAccion")
        self.set_method_name("obtenerGrafica")
        self.add_param("c0-id", "7176_1673473930106")
        self.add_string_param("c0-e1", self.center_id)
        self.add_string_param("c0-e2", "TODO")
        self.add_string_param("c0-e3", 1)
        self.add_string_param("c0-e4", 1)
        param0 = "{cdCentro:reference:c0-e1, cdnivelEducativo:reference:c0-e2, cdGrafica:reference:c0-e3, " \
                 "tipoGrafica:reference:c0-e4}"
        self.add_object_param("c0-param0", param0)
        self.add_param("xml", "true")

        post_data = super().get_body_params()

        res = requests.post(self.url, data=post_data)

        if res is not None and res.status_code == 200:
            content = self.__extract_data(res.text)

        return content
