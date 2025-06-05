# Entrega 1 - Projeto Final de S202-L1

## Nome: Murilo de Oliveira Domingos Figueiredo

## Bancos de dados utilizados: MongoDB, Neo4J

## Tema do projeto:
O projeto consiste em um sistema de recomendação de filmes. Nele, os usuários podem criar uma conta para escrever resenhas e avaliar os filmes que assistiram. A cada nova avaliação ou resenha publicada, o sistema gera recomendações personalizadas com base nesse conteúdo. A proposta é desenvolver uma versão simplificada de plataformas como o Letterboxd..

## Uso dos bancos de dados:
### MongoDB
O MongoDB será utilizado para armazenar os dados de usuários, filmes e resenhas/avaliações. A flexibilidade de schemas oferecida pelo MongoDB permite que resenhas e avaliações sejam representadas como uma única entidade, sem a necessidade de uma modelagem mais rígida para verificar se o usuário fez apenas uma avaliação ou também escreveu uma resenha..

### Neo4J
O Neo4J será usado para armazenar relações entre usuários e entre usuários e filmes. Com isso, é possível visualizar as conexões entre usuários e os filmes que assistiram. Essa estrutura facilitará a criação de uma lista de recomendações, com base nas interações dos usuários e nas semelhanças entre os filmes avaliados. 