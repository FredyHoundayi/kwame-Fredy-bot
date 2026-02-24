#!/bin/bash

# Script de déploiement pour Kwame Fredy Bot sur Fly.io

echo "🚀 Déploiement de Kwame Fredy Bot sur Fly.io..."

# Vérifier si Fly CLI est installé
if ! command -v fly &> /dev/null; then
    echo "❌ Fly CLI n'est pas installé. Installation en cours..."
    curl -L https://fly.io/install.sh | sh
    echo "✅ Fly CLI installé. Veuillez recharger votre terminal ou exécuter: source ~/.zshrc"
    exit 1
fi

# Vérifier si l'utilisateur est connecté
if ! fly auth whoami &> /dev/null; then
    echo "❌ Vous n'êtes pas connecté à Fly.io. Veuillez exécuter: fly auth login"
    exit 1
fi

echo "✅ Fly CLI prêt"

# Déployer l'application
echo "📦 Construction et déploiement de l'application..."
fly deploy

if [ $? -eq 0 ]; then
    echo "✅ Déploiement réussi !"
    echo "🌐 Votre application est disponible sur: https://kwame-fredy-bot.fly.dev"
    echo "📊 Vérifiez le statut avec: fly status"
    echo "📝 Voir les logs avec: fly logs"
else
    echo "❌ Échec du déploiement"
    exit 1
fi
