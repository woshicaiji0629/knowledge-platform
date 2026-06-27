from knowledge_platform.providers.base import (
    CustomerServiceProvider,
    CustomerServiceRequest,
    CustomerServiceResponse,
)


class CustomerService:
    def __init__(self, provider: CustomerServiceProvider) -> None:
        self._provider = provider

    def chat(self, message: str, session_id: str | None = None) -> CustomerServiceResponse:
        request = CustomerServiceRequest(message=message, session_id=session_id)
        return self._provider.chat(request)
