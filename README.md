# WorkTools 🛠️

## Sobre o Projeto 📖
O WorkTools é uma coleção de ferramentas em Python que desenvolvi para automatizar e facilitar tarefas recorrentes de suporte técnico. Este projeto não só melhora a eficiência do trabalho diário, mas também serve como um campo de estudo para aprofundar conhecimentos em programação Python e familiarização com o GitHub.

## Ferramentas Incluídas 🧰
- **ExcluirAjustes**: Uma ferramenta para remover ajustes desnecessários.
- **ListarAjustes_v2**: Auxilia na listagem e organização de ajustes.
- **OrganizadorJson**: Simplifica a organização de arquivos JSON.
- **OrganizadorJsonPV**: Específico para organizar JSONs de ponto de venda.
- **PesquisarPV_v3**: Facilita a pesquisa de informações de ponto de venda.

### Pré-requisitos 📋
- **Python**: O projeto requer Python para executar as ferramentas. Certifique-se de ter a versão mais recente instalada.

## Contribuições 👐
Me chama na DM

## Licença 📄
Este projeto está sob a licença livre.

### Configuração de credenciais 🔐
As credenciais não são armazenadas no repositório. Antes de executar os scripts,
defina as variáveis de ambiente correspondentes (consulte `.env.example`):

- `OMIE_APP_KEY` e `OMIE_APP_SECRET` para os scripts de ajustes.
- `OMIE_APP_KEY_PV` e `OMIE_APP_SECRET_PV` para `PesquisarPV_v3.py`.

Se alguma variável obrigatória estiver ausente, o script será interrompido com uma
mensagem indicando qual configuração precisa ser definida.
