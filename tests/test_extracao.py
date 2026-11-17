import re


def test_email():
    texto = "Contato: joao@email.com"

    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        texto
    )

    assert emails == ["joao@email.com"]


def test_telefone():
    texto = "Meu telefone é (12) 99999-8888"

    telefones = re.findall(
        r'(?:\+55\s?)?(?:\(\d{2}\)\s?|\d{2}\s?)?\d{4,5}-?\d{4}',
        texto
    )

    assert telefones == ["(12) 99999-8888"]


def test_url():
    texto = "Acesse https://www.exemplo.com.br"

    urls = re.findall(
        r'https?://[^\s]+|www\.[^\s]+',
        texto
    )

    assert urls == ["https://www.exemplo.com.br"]


def test_sem_resultados():
    texto = "Este texto não possui informações de contato."

    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        texto
    )

    telefones = re.findall(
        r'(?:\+55\s?)?(?:\(\d{2}\)\s?|\d{2}\s?)?\d{4,5}-?\d{4}',
        texto
    )

    urls = re.findall(
        r'https?://[^\s]+|www\.[^\s]+',
        texto
    )

    assert emails == []
    assert telefones == []
    assert urls == []