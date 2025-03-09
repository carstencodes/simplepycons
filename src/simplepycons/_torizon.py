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


class TorizonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "torizon"

    @property
    def original_file_name(self) -> "str":
        return "torizon.svg"

    @property
    def title(self) -> "str":
        return "Torizon"

    @property
    def primary_color(self) -> "str":
        return "#FAAF00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Torizon</title>
     <path d="M11.63.349a.56.56 0 0 0-.304.09L8.719 2.132a.274.274 0 0
 0 0 .457l2.607 1.693a.56.56 0 0 0 .607 0L14.54 2.59a.274.274 0 0 0
 0-.457L11.933.439a.56.56 0 0 0-.303-.09M7.437 3.054a.56.56 0 0
 0-.302.09L4.53 4.837a.274.274 0 0 0 0 .46L7.135 6.99a.56.56 0 0 0
 .604 0l2.606-1.693a.274.274 0 0 0 0-.46L7.74 3.144a.56.56 0 0
 0-.302-.09m8.852.316a.56.56 0 0 0-.302.09l-2.606 1.69a.274.274 0 0 0
 0 .46l2.606 1.693a.56.56 0 0 0 .605 0l2.606-1.693a.274.274 0 0 0
 0-.46l-2.606-1.69a.56.56 0 0 0-.303-.09M3.043 5.924a.56.56 0 0
 0-.303.09L.134 7.707a.274.274 0 0 0 0 .46l2.606 1.69a.56.56 0 0 0
 .605 0l2.606-1.69a.274.274 0 0 0 0-.46L3.345 6.014a.56.56 0 0
 0-.302-.09m9.055.155a.56.56 0 0 0-.301.09l-2.6 1.689a.274.274 0 0 0 0
 .46l2.6 1.693a.56.56 0 0 0 .603.003l2.607-1.692a.274.274 0 0 0
 0-.46L12.4 6.167a.56.56 0 0 0-.302-.089m8.858.309a.56.56 0 0
 0-.304.09L18.045 8.17a.274.274 0 0 0 0 .457l2.607 1.697a.56.56 0 0 0
 .608 0l2.606-1.694a.274.274 0 0 0 0-.46L21.26 6.478a.56.56 0 0
 0-.304-.09M7.702 8.945a.56.56 0 0 0-.303.09l-2.607 1.693a.274.274 0 0
 0 0 .456L7.4 12.877a.56.56 0 0 0 .607 0l2.596-1.685a.274.274 0 0 0
 0-.457l-2.596-1.7a.56.56 0 0 0-.304-.09m9.063.15a.56.56 0 0
 0-.304.09l-2.606 1.694a.274.274 0 0 0 0 .457l2.606 1.692a.56.56 0 0 0
 .608 0l2.606-1.692a.274.274 0 0 0 0-.457L17.07 9.186a.56.56 0 0
 0-.304-.09M24 10.585a1.2 1.2 0 0 1-.351.611L12.973 18.13a1.83 1.83 0
 0 1-1.992 0L.334 11.212a1.15 1.15 0 0 1-.333-.6v1.657a.74.74 0 0 0
 .351.665l10.63 6.913a1.83 1.83 0 0 0 1.991 0l10.676-6.935a.74.74 0 0
 0 .35-.643Zm-11.631 1.379a.56.56 0 0 0-.302.089L9.46 13.745a.274.274
 0 0 0 0 .46l2.607 1.693a.56.56 0 0 0 .604 0l2.607-1.692a.274.274 0 0
 0 0-.46l-2.607-1.694a.56.56 0 0 0-.302-.09m11.63 2.134a1.2 1.2 0 0
 1-.35.607l-10.676 6.92a1.83 1.83 0 0 1-1.992 0L.334 14.722a1.15 1.15
 0 0 1-.333-.597v1.654a.74.74 0 0 0 .351.66l10.63 6.917a1.83 1.83 0 0
 0 1.991 0l10.676-6.934a.74.74 0 0 0 .35-.643z" />
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
