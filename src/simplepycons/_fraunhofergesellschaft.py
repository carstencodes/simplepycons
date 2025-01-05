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


class FraunhofergesellschaftIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fraunhofergesellschaft"

    @property
    def original_file_name(self) -> "str":
        return "fraunhofergesellschaft.svg"

    @property
    def title(self) -> "str":
        return "Fraunhofer-Gesellschaft"

    @property
    def primary_color(self) -> "str":
        return "#179C7D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fraunhofer-Gesellschaft</title>
     <path d="M.06 23.99c5.681-2.926 14-7.653
 23.88-14.567v-2.32C15.247 12.792 6.406 17.359.06
 20.38zm0-6.93c6.325-2.575 15.166-6.558 23.88-11.74V4.174C15.751 8.238
 7.24 10.781.06 12.366zM23.94 24V12.332A201.394 201.393 0 0 1 8.596
 24zM5.542 24a166.927 166.926 0 0 0 14.7-9.765 323.136 324.76 0 0 0
 3.698-2.81V9.98C16.257 15.74 8.413 20.542 2.287 24zM.06 10.668C7.044
 9.44 15.589 7.231 23.94 3.262v-1.3C15.526 5.737 7.102 7.338.06
 7.91zM.06 0v6.686c.522-.033 1.054-.07 1.596-.111C7.464 6.126 15.387
 5.1 23.94 1.402V0z" />
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
