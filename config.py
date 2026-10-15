import os


def load_credentials(profile="default"):
    if profile == "pv":
        variable_names = ("OMIE_APP_KEY_PV", "OMIE_APP_SECRET_PV")
    elif profile == "default":
        variable_names = ("OMIE_APP_KEY", "OMIE_APP_SECRET")
    else:
        raise ValueError(f"Perfil de credenciais inválido: {profile}")

    credentials = tuple(os.getenv(name, "").strip() for name in variable_names)
    missing = [name for name, value in zip(variable_names, credentials) if not value]
    if missing:
        raise RuntimeError(
            "Configuração ausente. Defina as variáveis de ambiente: "
            + ", ".join(missing)
        )

    return credentials
