from abc import ABC, abstractmethod
from dataclasses import dataclass


class ProviderError(Exception):
    """Base provider error."""


class ProviderNotConfiguredError(ProviderError):
    """Raised when provider credentials or endpoint settings are missing."""


@dataclass(frozen=True)
class CustomerServiceRequest:
    message: str
    session_id: str | None = None


@dataclass(frozen=True)
class CustomerServiceResponse:
    answer: str
    provider: str
    session_id: str | None = None


class CustomerServiceProvider(ABC):
    @abstractmethod
    def chat(self, request: CustomerServiceRequest) -> CustomerServiceResponse:
        raise NotImplementedError
