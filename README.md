# SMStoTelegram

Aplicativo Android que lê SMS e envia para o Telegram.

## Como subir no GitHub e gerar o APK

### Passo 1 - Criar repositório
1. Acesse github.com e faça login
2. Clique no "+" (canto superior direito) > "New repository"
3. Nome: smstotelegram
4. NÃO marque nenhuma opção (nem README, nem gitignore)
5. Clique "Create repository"

### Passo 2 - Subir os arquivos
1. Extraia o ZIP no seu computador
2. Abra o terminal na pasta extraída
3. Execute os comandos abaixo (troque SEU_USUARIO pelo seu usuário do GitHub):

```
git init
git add .
git commit -m "primeiro commit"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/smstotelegram.git
git push -u origin main
```

### Passo 3 - Baixar o APK
1. No repositório, clique na aba "Actions"
2. Aguarde o build terminar (fica verde quando pronto, ~15 min)
3. Clique no build concluído
4. Baixe o artefato "apk-debug"

## Permissões
- INTERNET: enviar dados ao Telegram
- READ_SMS: ler mensagens recebidas
- RECEIVE_SMS: detectar novas mensagens
