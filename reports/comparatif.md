# Comparatif des approches - projet fraude (TP04)

Date de consultation des documentations : 25/10/2026.

## Tableau comparatif

| Approche | F1 test | Temps humain | Temps machine | Cout estime | Explicabilite | Export / reversibilite |
|---|---|---|---|---|---|---|
| Logistique (reference) | 0.7407 | Faible | 0.09 s | 0 EUR de facturation cloud (poste local) | Tres bonne, coefficients | Totale |
| Random Forest manuel (TP2) | 0.8669 | Eleve, recherche manuelle | 1.46 s pour le modele final | 0 EUR de facturation cloud (poste local) | Bonne, importance des variables | Totale |
| FLAML 60 s | 0.8582 | Faible a moyen | 60.30 s | 0 EUR de facturation cloud (poste local) | Moyenne, depend du modele retenu | Totale, selon les dependances |
| Google Vertex AI AutoML | Non mesure | Faible a moyen | Non mesure | Ressources et services factures selon usage | Importance des variables, explications | Export possible sous conditions |
| Amazon SageMaker Autopilot | Non mesure | Faible a moyen | Non mesure | Instances et stockage factures selon usage | Rapports, importance des variables, notebooks | Artefacts exportables, dependances AWS possibles |
| Azure Automated ML | Non mesure | Faible a moyen | Non mesure | Calcul et services Azure selon usage | Explications et metriques des essais | Modeles exportables sous conditions |

Les temps humains sont des estimations qualitatives, non chronometrees.
Les couts locaux excluent electricite, materiel et temps humain.
Les temps machines locaux sont ceux mesures dans MLflow.
Les couts cloud ne peuvent pas etre chiffres sans region, ressources et duree choisies.

## Commentaire (5 lignes)

1. La regression logistique est recommandee pour obtenir rapidement une reference simple et interpretable.
2. Le reglage manuel convient lorsqu'on connait bien le probleme et qu'on souhaite controler les hyperparametres.
3. FLAML est interessant pour explorer automatiquement plusieurs modeles avec un budget de calcul limite.
4. Vertex AI et SageMaker Autopilot conviennent aux organisations souhaitant integrer AutoML aux services cloud de Google ou AWS.
5. Azure Automated ML convient aux equipes utilisant l'ecosysteme Microsoft ; le choix du cloud depend des couts, de la gouvernance et de la reversibilite.

## Sources officielles

Consultation : 25/10/2026.

Google Vertex AI :
https://cloud.google.com/gemini-enterprise-agent-platform/tabular-workflows-pricing
https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/export/export-model-tabular

Amazon SageMaker Autopilot :
https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html
https://aws.amazon.com/sagemaker/ai/pricing/

Azure Automated ML :
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-define-task-type
https://azure.microsoft.com/en-us/pricing/details/machine-learning/
