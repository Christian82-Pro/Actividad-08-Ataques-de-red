import mlflow


# Indicar la dirección donde está funcionando MLflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")


# Crear o seleccionar el experimento
mlflow.set_experiment(
    "Monitoreo API Ataques de Red"
)


# Función para registrar las métricas del modelo
def registrar_metricas(
    accuracy,
    precision,
    recall,
    f1
):
    """
    Registra las métricas del modelo en MLflow.
    """

    # Iniciar una nueva ejecución
    with mlflow.start_run(
        run_name="Modelo funcionando correctamente"
    ):

        # Registrar las métricas
        mlflow.log_metric(
            "accuracy",
            accuracy
        )

        mlflow.log_metric(
            "precision",
            precision
        )

        mlflow.log_metric(
            "recall",
            recall
        )

        mlflow.log_metric(
            "f1_score",
            f1
        )

        # Registrar información del proyecto
        mlflow.log_param(
            "modelo",
            "Random Forest"
        )

        mlflow.log_param(
            "actividad",
            "Observabilidad"
        )

        mlflow.log_param(
            "estado",
            "Correcto"
        )


# Ejecutar el registro
if __name__ == "__main__":

    print("Registrando métricas en MLflow...")

    registrar_metricas(
        accuracy=0.96,
        precision=0.95,
        recall=0.94,
        f1=0.95
    )

    print("Métricas registradas correctamente.")