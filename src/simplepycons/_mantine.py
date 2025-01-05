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


class MantineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mantine"

    @property
    def original_file_name(self) -> "str":
        return "mantine.svg"

    @property
    def title(self) -> "str":
        return "Mantine"

    @property
    def primary_color(self) -> "str":
        return "#339AF0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mantine</title>
     <path d="M12 0C5.377 0 0 5.377 0 12s5.377 12 12 12 12-5.377
 12-12S18.623 0 12 0zm-1.613 6.15a.91.91 0 0 1 .59.176c.43.317.825.68
 1.177 1.082h2.588a.91.91 0 0 1 .912.906.909.909 0 0
 1-.912.907h-1.43c.4.908.604 1.889.602 2.88a7.133 7.133 0 0 1-.601
 2.883h1.427a.91.91 0 0 1 .914.907.91.91 0 0 1-.914.906h-2.588a7.399
 7.399 0 0 1-1.175 1.082.919.919 0 0 1-1.28-.19.904.904 0 0 1
 .191-1.268 5.322 5.322 0 0 0
 2.2-4.32c0-1.715-.801-3.29-2.2-4.32a.906.906 0 0
 1-.191-1.268H9.7a.916.916 0 0 1 .688-.363zm-.778 4.295a1.36 1.36 0 0
 1 1.354 1.354v.033a1.36 1.36 0 0 1-1.354 1.32 1.36 1.36 0 0
 1-1.353-1.32v-.033a1.36 1.36 0 0 1 1.353-1.354z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mantinedev/mantine/blob/f2'''

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
