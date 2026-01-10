# Projet 10 – Infrastructure & Services

## 1. Présentation
Ce projet met en place une infrastructure complète autour d’un service web sécurisé,
déployé sur une VM Ubuntu Server, avec conteneurisation Docker.

## 2. Architecture
- VM Ubuntu Server
- DNS interne (Bind9)
- DHCP
- Reverse Proxy Nginx (HTTPS)
- API FastAPI
- Base de données MySQL
- Docker & Docker Compose

## 3. Réseau
- Domaine interne : intra.local
- Résolution DNS interne via Bind9
- Attribution IP via DHCP

## 4. Sécurité
- HTTPS avec certificat autosigné
- Isolation des services via Docker networks
- Aucun port base de données exposé

## 5. Services Docker
- api : service FastAPI (CRUD utilisateurs)
- db : MySQL 8
- nginx : reverse proxy HTTPS

## 6. Exploitation
### Démarrage
docker compose up -d

### Vérification
docker ps  
curl https://web.intra.local/health

### Arrêt
docker compose down

## 7. Maintenance
- Logs accessibles via docker logs
- Mise à jour via rebuild des images
- Sauvegarde des volumes MySQL
