import streamlit as st
import fitz
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

endpoint = "https://ricar-mb7auh0m-eastus2.cognitiveservices.azure.com/"
model_name = "gpt-4o"
deployment = "gpt-4o"

subscription_key = "EeaKfMLIUC2H9MDKn7KAhM5xOzhepHMJwzuRbg5HotC1CZu7kBS3JQQJ99BEACHYHv6XJ3w3AAAAACOGQFF5"
api_version = "2024-12-01-preview"

model = AzureChatOpenAI(
    azure_endpoint=endpoint,
    azure_deployment=model_name,
    openai_api_version=api_version,
    api_key=subscription_key
)

system_template = """
Você é um recrutador especialista na análise de currículos. Abaixo estão as vagas atualmente abertas, com os respectivos requisitos técnicos (hard skills), comportamentais (soft skills) e outros critérios.

Sua tarefa é:

1. Analisar o currículo do candidato.
2. Verificar se ele se encaixa em alguma das vagas listadas.
3. Escolher **a vaga mais compatível** com o perfil do candidato.
4. Classificar o candidato como: **Apto**, **Parcialmente apto** ou **Não apto**.
5. Justificar a escolha com base nos requisitos das vagas.
6. Listar:
   - Quais requisitos o candidato atende (com base no currículo).
   - Quais requisitos estão ausentes (não mencionados ou não demonstrados).
7. Caso o candidato esteja parcialmente apto, sugerir ações para torná-lo apto no futuro.

---

📌 **VAGAS DISPONÍVEIS**

**1. Designer Gráfico**  
💼 *Hard Skills*:
- Microsoft 365  
- Adobe Photoshop  
- Adobe Illustrator  
- Capcut  
- Canva  
- After Effects  
- Adobe Premiere  
- Corel Draw  
- Figma  
- UI/UX  
- Experiência prévia em design  

🌟 *Soft Skills*:
- Criatividade  
- Organização  
- Proatividade  
- Pontualidade  
- Inovação  
- Comunicação  
- Trabalho em equipe  

💰 *Faixa Salarial:* Até R$ 4.000

---

**2. Estagiário Designer Gráfico**  
💼 *Hard Skills*:
- Atendimento ao cliente  
- Gestão de projetos/publicidade  
- Planejamento estratégico  
- Plano de marketing  
- Elaboração de campanhas publicitárias  
- Elaboração de briefings  

🌟 *Soft Skills*:
- Liderança  
- Delegar tarefas  
- Planejamento  
- Organização  
- Comunicação  
- Visão estratégica  
- Engajamento da equipe  
- Trabalho em equipe  

---

**3. Social Media**  
💼 *Hard Skills*:
- Análise de KPIs  
- Domínio de formatos e públicos das redes sociais  
- Formação em Publicidade ou Jornalismo  
- Redação e escrita  
- Experiência anterior na função  

🌟 *Soft Skills*:
- Criatividade  
- Organização  
- Atualização com tendências das redes sociais  
- Trabalho em equipe  

---

**4. Storymaker**  
💼 *Hard Skills*:
- Edição de vídeos curtos  
- Capcut  
- After Effects  
- Conhecimento de formatos para TikTok e Instagram  
- Softwares de edição de vídeo  

🌟 *Soft Skills*:
- Criatividade  
- Organização  
- Atualização com tendências  
- Horário flexível  
- Trabalho em equipe  

---

🧾 **CURRÍCULO DO CANDIDATO**  
{curriculo}

---

📊 **Sua resposta deve seguir exatamente este formato:**

✅ **Vaga mais compatível**: [Nome da vaga]

🧠 **Grau de compatibilidade**: [Apto / Parcialmente apto / Não apto]

✔️ **Requisitos atendidos**:  
- [Liste os principais hard e soft skills que o candidato possui, com base no currículo]

❌ **Requisitos ausentes**:  
- [Liste os requisitos exigidos pela vaga que não estão no currículo ou não foram comprovados]

💡 **Sugestões de desenvolvimento**:  
- [Liste sugestões práticas de aprendizado, capacitação ou experiência para o candidato se tornar apto]

---

🔁 Lembre-se: apenas uma vaga deve ser selecionada como a mais compatível, e todas as seções devem ser respondidas mesmo que o candidato seja considerado não apto.

"""


prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

def extrair_texto_pdf(uploaded_file):
    texto = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            texto += page.get_text()
    return texto

st.title("🔍 Analisador de currículos ")
st.caption("🚀 Seu assistente de IA para escolher os melhores candidatos!")

uploaded_file = st.file_uploader("Envie o currículo!", type=("pdf"))

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Gostaria de analisar um currículo hoje?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if uploaded_file:
        texto = extrair_texto_pdf(uploaded_file)
        response = model.invoke(prompt_template.invoke({"curriculo": texto, "text": prompt}))
        msg = response.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    else:
        st.warning("⚠️ Por favor, envie um currículo em PDF antes de fazer uma pergunta.")