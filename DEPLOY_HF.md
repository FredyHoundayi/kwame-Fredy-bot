# Hugging Face Spaces deployment guide

## Étapes pour déployer sur Hugging Face Spaces

### 1. Créer un nouveau Space
1. Allez sur [huggingface.co/new-space](https://huggingface.co/new-space)
2. Choisissez un nom : `kwame-fredy-bot`
3. Sélectionnez `Docker` comme SDK
4. Choisissez `Free` (CPU Basic) pour commencer
5. Rendez-le `Public` ou `Private` selon votre préférence
6. Cliquez sur `Create Space`

### 2. Configurer les secrets
Dans votre Space, allez dans `Settings` > `Repository secrets` et ajoutez :

```
GROQ_API_KEY=votre_clé_groq
TAVILY_API_KEY=votre_clé_tavily
GETWEATHER_API_KEY=votre_clé_weather
```

### 3. Pousser le code
```bash
git remote add space https://huggingface.co/spaces/VOTRE_USERNAME/kwame-fredy-bot
git add .
git commit -m "Deploy to Hugging Face Spaces"
git push space main
```

### 4. Attendre le build
Hugging Face va automatiquement :
- Construire l'image Docker
- Installer les dépendances
- Lancer l'application

Votre app sera disponible sur : `https://huggingface.co/spaces/VOTRE_USERNAME/kwame-fredy-bot`

## Avantages de Hugging Face Spaces

✅ **Gratuit** pour les projets personnels
✅ **Déploiement automatique** avec Git
✅ **HTTPS inclus** 
✅ **Domaine personnalisé** gratuit
✅ **Support GPU** disponible (payant)
✅ **Interface simple** et intuitive

## Alternative : Interface Web

Vous pouvez aussi utiliser l'interface web pour uploader les fichiers :
1. Créez votre Space
2. Utilisez l'éditeur de fichiers web
3. Uploadez tous vos fichiers
4. Ajoutez les secrets dans Settings
