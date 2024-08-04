
from types import SimpleNamespace
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base_icon import Icon


class IconFactory:
    def __init__(self, factory: type[Icon]) -> None:
        self._factory = factory
        self._prototype = factory()

    @property
    def prototype(self) -> "Icon":
        return self._prototype

    def __call__(self) -> "Icon":
        return self._factory()


class IconCollection(SimpleNamespace):
    def __init__(self, all_icons: dict[str, type[Icon]]) -> None:
        super().__init__()
        self.__dict__.update(IconCollection.__from_all_icons(all_icons))

    @staticmethod
    def __from_all_icons(
            all_icons: "dict[str, type[Icon]]"
    ) -> "dict[str, IconFactory]":
        return {"get_{k}_icon": IconFactory(v) for k, v in all_icons.items()}
