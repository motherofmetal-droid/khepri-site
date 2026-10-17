# Khepri – Projetos BIM em JSON para Revit

**Português** | [English](#english)

O **Khepri** é um aplicativo web de arquitetura, construção e engenharia. Ele gera **planta baixa** e projetos complementares de **incêndio**, **hidrossanitário (hidráulica)**, **elétrica** e **civil (estrutura)** em arquivos **JSON**. Esses arquivos são importados no **Revit** por meio do **pyRevit** ou do **Dynamo**.

[![Abrir o aplicativo](https://img.shields.io/badge/Abrir%20o%20aplicativo-Khepri-164B4B?style=for-the-badge)](https://appkhepri.streamlit.app)
[![Site](https://img.shields.io/badge/Site-Khepri-D98E26?style=for-the-badge)](https://motherofmetal-droid.github.io/khepri-site/)

- 🔗 **Aplicativo:** https://appkhepri.streamlit.app
- 🌐 **Site:** https://motherofmetal-droid.github.io/khepri-site/

## Como funciona

1. Acesse o aplicativo e crie uma conta (há um período de teste gratuito).
2. Escolha o tipo de edificação e a disciplina, ou envie a planta exportada do Revit.
3. Descreva o projeto e clique em **Gerar Projeto Khepri**.
4. Baixe o arquivo **.json** e o memorial técnico (HTML e CSV).
5. No Revit 2026 ou superior, abra o JSON pela aba **Khepri** (extensão pyRevit) ou pelo script do Dynamo.

O guia passo a passo está dentro do próprio aplicativo, na seção "Como abrir o seu projeto".

## O que o Khepri gera

| Disciplina | Conteúdo |
|---|---|
| Arquitetura | Paredes, lajes, aberturas, ambientes, cobertura e mobiliário |
| Civil | Pré-dimensionamento de lajes, vigas, pilares e sapatas (NBR 6118) |
| Elétrica | Quadro, circuitos, luminárias e tomadas (NBR 5410) |
| Hidráulica | Água fria, reservatório e águas pluviais (NBR 5626 e NBR 10844) |
| Incêndio | Saídas, iluminação de emergência e alarme (NBR 9077, 10898 e 17240) |

## Requisitos

- Revit **2026** ou superior
- [pyRevit](https://github.com/pyrevitlabs/pyRevit) (gratuito) ou Dynamo
- Navegador atual. O aplicativo também pode ser instalado como atalho (PWA).

## Aviso importante

O Khepri faz **pré-dimensionamento e modelo de coordenação**. A verificação final, a responsabilidade técnica e a emissão de **ART/RRT** são do profissional habilitado. O Khepri não emite ART/RRT.

## Planos

O aplicativo tem um período de teste gratuito de 3 dias. Depois, o uso continua no plano Khepri Pro, cobrado em reais. Os valores atuais estão dentro do aplicativo.

## Autoria

Idealizado e desenvolvido por **Larissa Moura Nascimento** – Arquiteta, Urbanista e Gestora Ambiental.

**Palavras-chave:** aplicativo de arquitetura, aplicativo de engenharia, aplicativo de construção, projeto de incêndio, engenharia hidrossanitária, planta baixa, BIM, projetos, pyRevit, Dynamo, JSON, Revit, Khepri.

---

## English

**Khepri** is a web app for architecture, construction and engineering. It generates **floor plans** and **fire protection**, **plumbing**, **electrical** and **structural** designs as **JSON** files, which you import into **Revit** with **pyRevit** or **Dynamo**.

- 🔗 **App:** https://appkhepri.streamlit.app
- 🌐 **Website:** https://motherofmetal-droid.github.io/khepri-site/

**How it works:** create an account (free trial available), choose the building type and discipline, describe the project, download the `.json` file, and open it in Revit 2026 or later through the **Khepri** tab (pyRevit extension) or the Dynamo script.

**Requirements:** Revit 2026+, pyRevit or Dynamo, and a modern browser.

**Disclaimer:** Khepri provides pre-sizing and a coordination model. Final verification and professional responsibility belong to the licensed professional. The interface is available in multiple languages. Design documents (technical memorials) are generated in Brazilian Portuguese and follow Brazilian standards (ABNT NBR).

**Keywords:** architecture app, engineering app, construction app, fire protection design, plumbing design, floor plan, BIM, pyRevit, Dynamo, JSON, Revit, Khepri.
