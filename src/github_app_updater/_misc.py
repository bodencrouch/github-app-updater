"""Vendored misc helpers for standalone updater."""
from __future__ import annotations

import platform
import sys
from enum import Enum
from pathlib import Path


def ensure_directory_exists(path: Path | str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def get_normalized_extension(path: Path | str) -> str:
    return Path(path).suffix.lower()


class ProcessorArchitecture(Enum):
    BIT_32 = 32
    BIT_64 = 64

    @classmethod
    def from_os(cls) -> "ProcessorArchitecture":
        return cls.BIT_64 if sys.maxsize > 2**32 else cls.BIT_32

    @classmethod
    def from_python_interpreter(cls) -> "ProcessorArchitecture":
        return cls.from_os()

    @property
    def machine(self) -> str:
        m = platform.machine().lower()
        return m or ("AMD64" if self is ProcessorArchitecture.BIT_64 else "x86")
