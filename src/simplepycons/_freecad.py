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
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class FreecadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "freecad"

    @property
    def original_file_name(self) -> "str":
        return "freecad.svg"

    @property
    def title(self) -> "str":
        return "FreeCAD"

    @property
    def primary_color(self) -> "str":
        return "#729FCF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FreeCAD</title>
     <path d="M0 0v24h5.6v-9.6h4.8V8.8H5.6V5.6h8V0Zm15.552
 6.4-1.638.086a.4.4 0 0 0-.363.295l-.702 2.576-.714.342L10.9
 9.16v5.74H6.404l.092 1.59a.4.4 0 0 0 .293.363l2.576.7.344.714-1.076
 2.437a.4.4 0 0 0 .097.46l1.225 1.1a.4.4 0 0 0
 .467.052l2.312-1.329.752.268.967 2.488a.4.4 0 0 0
 .394.256l1.65-.092a.4.4 0 0 0 .366-.297l.691-2.578.713-.341 2.446
 1.08a.4.4 0 0 0 .46-.1l1.102-1.225a.4.4 0 0 0
 .049-.466l-1.328-2.315.261-.751 2.487-.967a.4.4 0 0 0
 .256-.393l-.084-1.648a.4.4 0 0 0-.295-.365l-2.578-.692-.344-.714
 1.072-2.45a.4.4 0 0 0-.1-.459l-1.224-1.101a.4.4 0 0
 0-.467-.049l-2.314 1.326-.744-.258-.975-2.49a.4.4 0 0
 0-.395-.253zm2.249 8.801a2.6 2.6 0 0 1-2.6 2.6 2.6 2.6 0 0 1-2.6-2.6
 2.6 2.6 0 0 1 2.6-2.6 2.6 2.6 0 0 1 2.6 2.6" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
