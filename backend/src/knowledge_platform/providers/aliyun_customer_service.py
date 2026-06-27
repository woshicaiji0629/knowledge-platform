from knowledge_platform.config.settings import Settings
from knowledge_platform.providers.base import (
    CustomerServiceProvider,
    CustomerServiceRequest,
    CustomerServiceResponse,
    ProviderNotConfiguredError,
)


class AliyunCustomerServiceProvider(CustomerServiceProvider):
    provider_name = "aliyun-customer-service"

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def chat(self, request: CustomerServiceRequest) -> CustomerServiceResponse:
        self._ensure_configured()

        return CustomerServiceResponse(
            answer="Aliyun customer service provider is configured, but the API adapter is not implemented yet.",
            provider=self.provider_name,
            session_id=request.session_id,
        )

    def _ensure_configured(self) -> None:
        missing = [
            name
            for name, value in {
                "ALIYUN_CUSTOMER_SERVICE_ENDPOINT": self._settings.aliyun_customer_service_endpoint,
                "ALIYUN_ACCESS_KEY_ID": self._settings.aliyun_access_key_id,
                "ALIYUN_ACCESS_KEY_SECRET": self._settings.aliyun_access_key_secret,
                "ALIYUN_CUSTOMER_SERVICE_INSTANCE_ID": self._settings.aliyun_customer_service_instance_id,
            }.items()
            if not value
        ]
        if missing:
            missing_text = ", ".join(missing)
            raise ProviderNotConfiguredError(f"Aliyun customer service provider is not configured: {missing_text}")
