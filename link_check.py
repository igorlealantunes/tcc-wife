import requests

urls = ["https://www.scielo.br/j/csp/a/YnJk6W34PYN9G5jp39kzCdy/?format=pdf&lang=pt.",
        "https://www.scielo.br/j/reben/a/8PmHNJS7KHKyC8Vfx9JzsXd/?format=pdf&lang=pt.",
        "https://nesprom.unb.br/images/e-books/TICs/hanseniaseavancoes.pdf.",
        "https://ojs.brazilianjournals.com.br/ojs/index.php/BRJD/article/view/59638/43130.",
        "https://www.scielo.br/j/rsbmt/a/335vHvt6zgPfyXb7vnChvQJ/?format=pdf&lang=pt.",
        "https://www.researchgate.net/publication/276395285_Caracteristicas_epidemiologicas_e_espaciais_da_hanseniase_no_Estado_do_Maranhao_Brasil_2001-2012.",
        "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/boletins/epidemiologicos/especiais/2024/be_hansen-2024_19jan_final.pdf.",
        "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/boletins/epidemiologicos/especiais/2021/boletim-hanseniase-_-25-01.pdf.",
        "https://bvsms.saude.gov.br/bvs/publicacoes/manual_prevencao_incapacidades.pdf.",
        "https://bvsms.saude.gov.br/bvs/publicacoes/0118conf_hanseniase.pdf.",
        "https://portal.saude.pe.gov.br/sites/portal.saude.pe.gov.br/files/diretrizes_para_._eliminacao_hanseniase_-_manual_-_3fev16_isbn_nucom_final_2.pdf.",
        "https://bvsms.saude.gov.br/bvs/publicacoes/doencas_infecciosas_parasitaria_guia_bolso.pdf.",
        "https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/h/hanseniase/publicacoes/sei_ms-0020845770-nota-tecnica-16.pdf/view.",
        "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/boletins/epidemiologicos/especiais/2024/be_hansen-2024_19jan_final.pdf.",
        "https://bvsms.saude.gov.br/bvs/publicacoes/estrategia_nacional_enfrentamento_hanseniase_2019.pdf.",
        "https://bvsms.saude.gov.br/bvs/publicacoes/guia_vigilancia_saude_4ed.pdf.",
        "https://bvsms.saude.gov.br/bvs/publicacoes/guia_pratico_hanseniase.pdf.",
        "https://pesquisa.in.gov.br/imprensa/jsp/visualiza/index.jsp?jornal=515&pagina=1&data=27/11/2023.",
        "https://portalsinan.saude.gov.br/images/documentos/Portarias/PORTARIA_DE_CONSOLIDACAO_N4_.pdf.",
        "https://bvsms.saude.gov.br/bvs/publicacoes/protocolo_clinico_diretrizes_terapeuticas_hanseniase.pdf.",
        "http://hansen.bvs.ilsl.br/textoc/producao2009_nao_usar/BRAS%20LEPROLOGIA/1960/PDF/v28n4/v28n4apres.pdf.",
        "https://bvsms.saude.gov.br/bvs/saudelegis/cns/2016/res0510_07_04_2016.html.",
        "https://periodicos.ufpe.br/revistas/index.php/revistaenfermagem/article/view/236224/31296.",
        "https://repositorio.animaeducacao.com.br/items/9937c8d7-3e9b-443d-b4db-e40f3ab1168e.",
        "https://idpjournal.biomedcentral.com/articles/10.1186/s40249-020-00790-4.",
        "https://periodicos.saude.sp.gov.br/hansenologia/article/view/35329/33774.",
        "https://www.scielo.br/j/csp/a/rQC6QzHKh9RCH5C7zLWNMvJ/?format=pdf&lang=pt.",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7946803/.", "https://censo2022.ibge.gov.br/panorama/.",
        "https://periodicos.ufjf.br/index.php/hurevista/article/view/14035/18766.",
        "http://files.bvs.br/upload/S/1413-9979/2012/v17n4/a3329.pdf.",
        "http://scielo.iec.gov.br/pdf/ess/v12n4/v12n4a03.pdf.",
        "https://www.scielo.br/j/rbepid/a/RHnWtVZ9cGSFssFPqkK7jPB/?format=pdf&lang=pt.",
        "https://acervomais.com.br/index.php/medico/article/view/11172/6733.",
        "https://www.scielo.br/j/rsbmt/a/z68X43pYw6hQdSrTj8WqDJm/?format=pdf&lang=pt.",
        "https://www.scielosp.org/pdf/ress/2021.v30n1/e2018126/pt.",
        "https://iris.who.int/bitstream/handle/10665/63060/WHO_LEP_96.5.pdf?sequence=1&isAllowed=y.",
        "https://iris.who.int/bitstream/handle/10665/274127/9789290227076-por.pdf?sequence=47&isAllowed=y.",
        "https://www.who.int/pt/publications/i/item/9789290228509.",
        "https://iris.who.int/bitstream/handle/10665/345048/WER9636-eng-fre.pdf?sequence=1.",
        "https://iris.who.int/bitstream/handle/10665/372812/WER9837-eng-fre.pdf?sequence=1.",
        "https://iris.who.int/bitstream/handle/10665/334562/WER9539-461-468-eng-fre.pdf?sequence=1.",
        "https://iris.who.int/bitstream/handle/10665/345383/WER9638-461-468-eng-fre.pdf?sequence=1.",
        "https://iris.paho.org/bitstream/handle/10665.2/57700/9789275127421_eng.pdf?sequence=1&isAllowed=y.",
        "https://www.arca.fiocruz.br/bitstream/handle/icict/28224/TCC%20J%c3%banior%20-%20Turma%20Caruaru_06-02-11.pdf?sequence=2&isAllowed=y.",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6053250/pdf/pntd.0006622.pdf.",
        "https://periodicos.ufba.br/index.php/enfermagem/article/view/15669/pdf_59.",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7205316/pdf/pntd.0008276.pdf.",
        "https://www.periodicos.unifai.edu.br/index.php/lumen/article/view/60/88.",
        "http://files.bvs.br/upload/S/1679-1010/2012/v10n4/a3046.pdf.",
        "https://iris.paho.org/bitstream/handle/10665.2/34882/v42e422018.pdf?sequence=1&isAllowed=y.",
        "https://www.scielo.br/j/ress/a/SYhPKcN7f8znKV9r93cpF7w/?format=pdf&lang=pt.",
        "https://jidc.org/index.php/journal/article/view/25771459/1260.",
        "https://periodicos.saude.sp.gov.br/hansenologia/article/view/35664/34074.",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6168122/pdf/pntd.0006788.pdf.",
        "https://bvsms.saude.gov.br/bvs/publicacoes/manual_leprologia.pdf.",
        "https://www.historia.uff.br/stricto/teses/Tese-2007_MACIEL_Laurinda_Rosa-S.pdf.",
        "https://iris.who.int/bitstream/handle/10665/333499/WHO-2019-nCoV-neglected_tropical_diseases-2020.1-eng.pdf?sequence=1",
        "http://hansen.bvs.ilsl.br/textoc/livros/OPROMOLLA_DILTOR_nocoes/PDF/apres.pdf."]

for url in urls:
    url = url.rstrip('.')  # Trim the dot at the end of the URL
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Success: {url}")
        else:
            print(f"Failed with status code {response.status_code}: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {url}, Error: {e}")
