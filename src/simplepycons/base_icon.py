#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""

from abc import ABC, abstractmethod
from base64 import b64encode
from typing import final, TYPE_CHECKING
from xml.etree import ElementTree

if TYPE_CHECKING:
    from collections.abc import Iterable


ElementTree.register_namespace('', "http://www.w3.org/2000/svg")


class Icon(ABC):
    """"""
    @property
    @abstractmethod
    def name(self) -> "str":
        """"""
        raise NotImplementedError()

    @property
    @abstractmethod
    def original_file_name(self) -> "str":
        """"""
        raise NotImplementedError()

    @property
    @abstractmethod
    def title(self) -> "str":
        """"""
        raise NotImplementedError()

    @property
    @abstractmethod
    def primary_color(self) -> "str":
        """"""
        raise NotImplementedError()

    @property
    @abstractmethod
    def raw_svg(self) -> "str":
        """"""
        raise NotImplementedError()

    @final
    def svg_tree(self) -> "ElementTree.Element":
        """"""
        return ElementTree.fromstring(self.raw_svg)

    @final
    def customize_svg(self, **svg_attrs) -> "ElementTree.Element":
        """"""
        element: ElementTree.Element = self.svg_tree()

        if "fill" not in svg_attrs:
            svg_attrs["fill"] = self.primary_color

        for attribute, value in svg_attrs.items():
            element.set(attribute, value)

        return element

    @final
    def customize_svg_as_bytes(self, **svg_attrs) -> "bytes":
        """"""
        element: ElementTree.Element = self.customize_svg(**svg_attrs)
        return ElementTree.tostring(element)

    @final
    def customize_svg_as_str(
            self,
            text_encoding: str = "utf-8",
            **svg_attrs
    ) -> "str":
        """"""
        data: bytes = self.customize_svg_as_bytes(**svg_attrs)
        return data.decode(text_encoding)

    @final
    def customize_svg_as_data_url(
            self,
            text_encoding: str = "utf-8",
            **svg_attrs
    ) -> "str":
        """"""
        xml: bytes = self.customize_svg_as_bytes(**svg_attrs)
        base64_xml = b64encode(xml).decode(text_encoding)
        return f"data:image/svg+xml;base64, {base64_xml}"

    @property
    def guidelines_url(self) -> "str | None":
        """"""
        return None

    @property
    @abstractmethod
    def source(self) -> "str":
        """"""
        raise NotImplementedError()

    @property
    @abstractmethod
    def license(self) -> "tuple[str | None, str | None]":
        """"""
        raise NotImplementedError()

    @property
    def aliases(self) -> "Iterable[str]":
        """"""
        yield from []
