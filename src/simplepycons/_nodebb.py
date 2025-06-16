#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class NodebbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nodebb"

    @property
    def original_file_name(self) -> "str":
        return "nodebb.svg"

    @property
    def title(self) -> "str":
        return "NodeBB"

    @property
    def primary_color(self) -> "str":
        return "#1E5EBC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NodeBB</title>
     <path d="M5.908 4.263c-3.439 0-5.4 1.68-5.4 4.156 0 1.525.793
 2.763 2.093 3.316C1.014 12.265 0 13.569 0 15.36c0 2.675 1.984 4.377
 5.6 4.377h6.053c0-1.269.03-2.557.031-4.44V4.263zm6.408 0v11.034c.001
 1.883.031 3.171.031 4.44H18.4c3.616 0 5.6-1.702 5.6-4.377
 0-1.79-1.014-3.095-2.601-3.625 1.3-.553 2.094-1.79 2.094-3.316
 0-2.476-1.962-4.156-5.401-4.156zM6.085 6.74h2.513v3.935H6.085c-1.61
 0-2.447-.73-2.447-1.968S4.475 6.74 6.085 6.74zm9.317 0h2.513c1.61 0
 2.447.73 2.447 1.967 0 1.238-.837 1.968-2.447 1.968h-2.513zm-9.56
 6.366h2.734v1.923c0 1.68-.375 2.233-1.521 2.233H5.622c-1.654
 0-2.492-.707-2.492-2.122 0-1.348.904-2.034 2.712-2.034zm9.582
 0h2.734c1.808 0 2.712.686 2.712 2.034 0 1.415-.838 2.122-2.492
 2.122h-1.433c-1.146 0-1.52-.553-1.52-2.233z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/NodeBB/assets/blob/c59a6d8'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
